"""Validate catalog metadata, generated index, and local Markdown destinations."""

from datetime import date
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from catalog import CATEGORIES, ROOT, read_catalog, render

SKIP = {".git", ".venv", "outputs", "node_modules", "__pycache__"}
LINK = re.compile(r"!?\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)")
FIELDS = {"id", "title", "url", "category", "topics", "level", "kind", "why", "access", "caveat"}


def markdown_files() -> list[Path]:
    return sorted(path for path in ROOT.rglob("*.md") if not path.name.startswith("._") and not any(part in SKIP for part in path.relative_to(ROOT).parts))


def without_code(text: str) -> str:
    return re.sub(r"^```[^\n]*\n.*?^```\s*$", "", text, flags=re.MULTILINE | re.DOTALL)


def anchors(path: Path) -> set[str]:
    text = without_code(path.read_text(encoding="utf-8"))
    found = set(re.findall(r'<(?:a|h[1-6])\s+[^>]*id=[\"\']([^\"\']+)', text))
    seen = {}
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, flags=re.MULTILINE):
        heading = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", heading)
        slug = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        found.add(f"{slug}-{count}" if count else slug)
    return found


def validate_catalog(data: dict) -> list[str]:
    errors = []
    seen_ids, seen_urls = set(), set()
    if not isinstance(data, dict) or not isinstance(data.get("resources"), list):
        return ["Catalog must be an object containing a resources list."]
    try:
        date.fromisoformat(data["updated"])
    except (KeyError, TypeError, ValueError):
        errors.append("Catalog updated must be an ISO date.")
    for index, row in enumerate(data["resources"]):
        label = f"catalog row {index + 1}"
        if not isinstance(row, dict) or set(row) != FIELDS:
            errors.append(f"{label}: expected fields {sorted(FIELDS)}")
            continue
        if any(not isinstance(value, str) for key, value in row.items() if key != "topics"):
            errors.append(f"{label}: all fields except topics must be strings")
            continue
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", row["id"]):
            errors.append(f"{label}: invalid id")
        if row["id"] in seen_ids:
            errors.append(f"{label}: duplicate id {row['id']}")
        canonical = row["url"].rstrip("/").casefold()
        if canonical in seen_urls:
            errors.append(f"{label}: duplicate URL {row['url']}")
        seen_ids.add(row["id"])
        seen_urls.add(canonical)
        url = urlsplit(row["url"])
        if url.scheme != "https" or not url.netloc or url.username or url.password:
            errors.append(f"{label}: expected a public HTTPS URL")
        for key in ("title", "why"):
            if not row[key].strip():
                errors.append(f"{label}: empty {key}")
        enums = {
            "category": CATEGORIES,
            "level": ["beginner", "intermediate", "advanced", "all"],
            "kind": ["course", "book", "paper", "repository", "documentation", "dataset", "benchmark", "portal"],
            "access": ["free", "registration", "mixed"],
        }
        for key, allowed in enums.items():
            if row[key] not in allowed:
                errors.append(f"{label}: invalid {key} {row[key]!r}")
        topics = row["topics"]
        if not isinstance(topics, list) or not topics or any(not isinstance(t, str) or not t.strip() for t in topics):
            errors.append(f"{label}: topics must be a nonempty list of strings")
    return errors


def validate_links() -> list[str]:
    errors = []
    for source in markdown_files():
        for match in LINK.finditer(without_code(source.read_text(encoding="utf-8"))):
            href = match.group(1).strip("<>")
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc:
                continue
            target = (source.parent / unquote(parsed.path)).resolve() if parsed.path else source
            if not target.is_relative_to(ROOT):
                errors.append(f"{source.relative_to(ROOT)}: link escapes repository: {href}")
            elif not target.exists():
                errors.append(f"{source.relative_to(ROOT)}: missing {href}")
            elif parsed.fragment and target.suffix == ".md" and unquote(parsed.fragment) not in anchors(target):
                errors.append(f"{source.relative_to(ROOT)}: missing anchor {href}")
    return errors


def main() -> None:
    try:
        data = read_catalog()
    except (OSError, json.JSONDecodeError) as exc:
        sys.exit(f"Cannot read catalog: {exc}")
    errors = validate_catalog(data)
    if not errors:
        index = ROOT / "resources/README.md"
        if not index.exists() or index.read_text(encoding="utf-8") != render(data):
            errors.append("Resource index is stale: run python3 scripts/catalog.py render")
    errors.extend(validate_links())
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    print(f"Checked {len(data['resources'])} resources and links in {len(markdown_files())} Markdown files.")


if __name__ == "__main__":
    main()
