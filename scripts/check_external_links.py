"""Check public HTTP destinations. This does not verify resource content."""

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import json
import re
from urllib.error import HTTPError, URLError
from urllib.parse import urldefrag
from urllib.request import Request, urlopen

from check_repository import LINK, ROOT, markdown_files, without_code
from catalog import read_catalog


def collect_urls() -> list[str]:
    urls = {row["url"] for row in read_catalog()["resources"]}
    for path in markdown_files():
        text = without_code(path.read_text(encoding="utf-8"))
        urls.update(match.group(1).strip("<>") for match in LINK.finditer(text) if match.group(1).startswith(("https://", "http://")))
        urls.update(re.findall(r"<(https?://[^>]+)>", text))
    return sorted({urldefrag(url)[0] for url in urls})


def check(url: str, timeout: float = 15) -> dict:
    headers = {"User-Agent": "computer-vision-resource-link-check/1.0"}
    last_error = ""
    for method in ("HEAD", "GET"):
        try:
            request = Request(url, headers=headers, method=method)
            with urlopen(request, timeout=timeout) as response:
                return {"url": url, "status": response.status, "result": "ok", "destination": response.url}
        except HTTPError as exc:
            # HEAD is sometimes unsupported or denied; verify with a small GET.
            if method == "HEAD":
                continue
            result = "broken" if exc.code in (404, 410) else "needs-review"
            return {"url": url, "status": exc.code, "result": result, "detail": str(exc)}
        except (URLError, OSError, ValueError) as exc:
            last_error = str(exc)
    return {"url": url, "status": None, "result": "needs-review", "detail": last_error}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--timeout", type=float, default=15)
    parser.add_argument("--output", default="outputs/link-report.json")
    args = parser.parse_args()
    if not 1 <= args.workers <= 16 or args.timeout <= 0:
        parser.error("Use 1–16 workers and a positive timeout.")
    urls = collect_urls()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        rows = list(pool.map(lambda url: check(url, args.timeout), urls))
    output = ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    summary = dict(Counter(row["result"] for row in rows))
    output.write_text(json.dumps({"summary": summary, "links": rows}, indent=2) + "\n", encoding="utf-8")
    print(f"Checked {len(rows)} unique URLs: {summary}. Report: {output}")
    for row in rows:
        if row["result"] != "ok":
            print(f"{row['result']}: {row['status']} {row['url']}")
    raise SystemExit(1 if any(row["result"] == "broken" for row in rows) else 0)


if __name__ == "__main__":
    main()
