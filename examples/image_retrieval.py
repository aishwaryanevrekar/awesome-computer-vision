"""Rank local images by color histograms; use --demo for an offline gallery."""

import argparse
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageOps, UnidentifiedImageError

EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff"}


def descriptor(path: Path, bins: int = 16) -> np.ndarray:
    with Image.open(path) as image:
        image = ImageOps.exif_transpose(image).convert("RGB")
        image.thumbnail((256, 256))
        pixels = np.asarray(image)
    hist = np.concatenate([np.histogram(pixels[:, :, channel], bins=bins, range=(0, 256))[0] for channel in range(3)]).astype(np.float64)
    return hist / np.linalg.norm(hist)


def rank_images(query: Path, gallery: Path, top_k: int = 5) -> tuple[list[dict], list[dict]]:
    if top_k < 1:
        raise ValueError("top_k must be positive.")
    if not gallery.is_dir():
        raise ValueError(f"Gallery directory does not exist: {gallery}")
    query_vector = descriptor(query)
    ranked, skipped = [], []
    for path in sorted(gallery.rglob("*")):
        if path.name.startswith("._") or not path.is_file() or path.suffix.lower() not in EXTENSIONS or path.resolve() == query.resolve():
            continue
        try:
            score = float(np.clip(query_vector @ descriptor(path), -1.0, 1.0))
            ranked.append({"path": str(path), "cosine_similarity": score})
        except (OSError, UnidentifiedImageError, Image.DecompressionBombError) as exc:
            skipped.append({"path": str(path), "reason": str(exc)})
    ranked.sort(key=lambda row: (-row["cosine_similarity"], row["path"]))
    return ranked[:top_k], skipped


def create_demo(output: Path) -> tuple[Path, Path]:
    gallery = output / "demo-gallery"
    gallery.mkdir(parents=True, exist_ok=True)
    for color, rgb in {"orange": (238, 155, 45), "green": (49, 185, 125), "blue": (60, 110, 220)}.items():
        for shape in ("circle", "square"):
            image = Image.new("RGB", (128, 128), (25, 25, 35))
            draw = ImageDraw.Draw(image)
            if shape == "circle":
                draw.ellipse((24, 24, 104, 104), fill=rgb)
            else:
                draw.rectangle((28, 28, 100, 100), fill=rgb)
            image.save(gallery / f"{color}-{shape}.png")
    query = output / "query.png"
    image = Image.new("RGB", (128, 128), (25, 25, 35))
    ImageDraw.Draw(image).ellipse((15, 24, 95, 104), fill=(238, 155, 45))
    image.save(query)
    return query, gallery


def save_contact_sheet(query: Path, rows: list[dict], output: Path) -> None:
    tiles = [("query", query)] + [(f"{row['cosine_similarity']:.3f}", Path(row["path"])) for row in rows]
    # Limit the preview; the JSON retains every requested result.
    tiles = tiles[:11]
    board = Image.new("RGB", (len(tiles) * 144, 170), "#111827")
    draw = ImageDraw.Draw(board)
    for i, (label, path) in enumerate(tiles):
        with Image.open(path) as image:
            image = ImageOps.exif_transpose(image).convert("RGB")
            tile = ImageOps.contain(image, (128, 128))
        board.paste(tile, (i * 144 + 8, 32))
        draw.text((i * 144 + 8, 10), label, fill="white")
    board.save(output / "matches.png")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--query", type=Path)
    parser.add_argument("--gallery", type=Path)
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--output", type=Path, default=Path("outputs/retrieval"))
    args = parser.parse_args()
    if args.top_k < 1:
        parser.error("--top-k must be at least 1")
    if args.demo and (args.query or args.gallery):
        parser.error("Use --demo or --query with --gallery, not both.")
    args.output.mkdir(parents=True, exist_ok=True)
    if args.demo:
        query, gallery = create_demo(args.output)
    elif args.query and args.gallery:
        query, gallery = args.query, args.gallery
    else:
        parser.error("Provide --demo or both --query and --gallery.")
    try:
        rows, skipped = rank_images(query, gallery, args.top_k)
    except (ValueError, OSError, Image.DecompressionBombError) as exc:
        parser.error(str(exc))
    report = {"query": str(query), "method": "16-bin per-channel RGB histograms + cosine", "matches": rows, "skipped": skipped}
    (args.output / "results.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    save_contact_sheet(query, rows, args.output)
    print(f"Saved {len(rows)} matches, {len(skipped)} skipped files: {args.output}")


if __name__ == "__main__":
    main()
