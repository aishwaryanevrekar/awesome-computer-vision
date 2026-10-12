"""Search the catalog, or render its Markdown index (standard library only)."""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = ["foundations", "courses", "papers", "models", "tools", "datasets", "evaluation", "deployment", "communities"]


def read_catalog() -> dict:
    return json.loads((ROOT / "resources/catalog.json").read_text(encoding="utf-8"))


BLURBS = {
    "foundations": "Math, NumPy, and the books that make everything else easier.",
    "courses": "Structured lectures and hands-on courses. Pick one, finish it.",
    "papers": "The papers worth reading in full, from ResNet to 2026.",
    "models": "Checkpoints and reference code you can actually run.",
    "tools": "Libraries and platforms for data, labeling, tracking, and 3D.",
    "datasets": "Where the data lives, and what you are allowed to do with it.",
    "evaluation": "Evaluators and benchmarks, so your numbers mean something.",
    "deployment": "Getting a model off your laptop and onto a device or server.",
    "communities": "Where the field publishes and where to ask for help.",
}
START = ["cs231n", "dive-into-deep-learning", "pytorch-tutorials", "opencv", "resnet-paper", "vit-paper", "timm", "coco-api", "onnx-runtime"]


def render(data: dict) -> str:
    rows = data["resources"]
    by_id = {row["id"]: row for row in rows}
    lines = [
        "# Resource catalog", "",
        f"**{len(rows)} hand-picked resources** across {len({r['category'] for r in rows})} categories. Updated {data['updated']}.", "",
        "[Home](../README.md) · [Roadmaps](../roadmaps/README.md) · [Projects](../projects/README.md) · [Paper guide](../research/paper-reading.md)", "",
        "> You do not need all of this. Pick what fits your current milestone and ignore the rest.", "",
        "## If you read nothing else", "",
        "Nine entries that cover most of what a newcomer needs:", "",
    ]
    for key in START:
        if key in by_id:
            row = by_id[key]
            lines.append(f"- **[{row['title']}]({row['url']})** · {row['why']}")
    lines += [
        "", "## Search from your terminal", "",
        "```bash",
        "python3 scripts/catalog.py search segmentation",
        "python3 scripts/catalog.py search --level beginner",
        "python3 scripts/catalog.py search --category datasets --json",
        "```", "",
        "Levels are beginner, intermediate, advanced, or all. Access is free, registration, or mixed. Free to read does not mean free to reuse or free to run, so check the license and the caveat.", "",
        "Missing something? Edit [catalog.json](catalog.json), run `make render`, and see [CONTRIBUTING](../CONTRIBUTING.md).", "",
        "## Browse", "",
    ]
    for category in CATEGORIES:
        count = sum(row["category"] == category for row in rows)
        if count:
            lines.append(f"- [{category.title()}](#{category}) ({count}): {BLURBS[category]}")
    for category in CATEGORIES:
        entries = [row for row in rows if row["category"] == category]
        if not entries:
            continue
        lines += ["", f"## {category.title()}", "", f"_{BLURBS[category]}_", ""]
        for row in entries:
            meta = f"{row['level']} · {row['kind']}" + ("" if row["access"] == "free" else f" · {row['access']} access")
            lines.append(f"- **[{row['title']}]({row['url']})** `{meta}`")
            lines.append(f"  {row['why']}")
            if row["caveat"]:
                lines.append(f"  _Heads up: {row['caveat']}_")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    search = commands.add_parser("search")
    search.add_argument("query", nargs="?", default="")
    search.add_argument("--level", choices=["beginner", "intermediate", "advanced", "all"])
    search.add_argument("--category", choices=CATEGORIES)
    search.add_argument("--json", action="store_true", dest="as_json")
    commands.add_parser("render")
    args = parser.parse_args()
    data = read_catalog()
    if args.command == "render":
        (ROOT / "resources/README.md").write_text(render(data), encoding="utf-8")
        print(f"Rendered {len(data['resources'])} resources.")
        return
    matches = [
        row for row in data["resources"]
        if args.query.casefold() in " ".join([row["title"], row["why"], *row["topics"]]).casefold()
        and (not args.level or row["level"] in {args.level, "all"})
        and (not args.category or row["category"] == args.category)
    ]
    if args.as_json:
        print(json.dumps(matches, indent=2, ensure_ascii=False))
    else:
        for row in matches:
            print(f"{row['title']} [{row['level']} / {row['category']}]\n  {row['why']}\n  {row['url']}")
        print(f"\n{len(matches)} matching resources.")


if __name__ == "__main__":
    main()
