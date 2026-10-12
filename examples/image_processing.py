"""Explore image gradients on a synthetic scene or a local image."""

import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps


def synthetic_scene(size: int = 256) -> Image.Image:
    image = Image.new("RGB", (size, size), (22, 29, 45))
    draw = ImageDraw.Draw(image)
    draw.rectangle((24, 32, 132, 148), fill=(244, 183, 72))
    draw.ellipse((100, 100, 232, 232), fill=(72, 198, 180))
    draw.line((16, 236, 238, 18), fill=(245, 245, 245), width=4)
    return image


def sobel_magnitude(gray: np.ndarray) -> np.ndarray:
    """Return unnormalized Sobel magnitude, using edge padding."""
    if gray.ndim != 2 or min(gray.shape) < 1:
        raise ValueError("Expected a nonempty grayscale image.")
    padded = np.pad(gray.astype(np.float32), 1, mode="edge")
    windows = np.lib.stride_tricks.sliding_window_view(padded, (3, 3))
    kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
    gx = np.einsum("ijkl,kl->ij", windows, kernel)
    gy = np.einsum("ijkl,kl->ij", windows, kernel.T)
    return np.hypot(gx, gy)


def process(image: Image.Image, output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    image = ImageOps.exif_transpose(image).convert("RGB")
    image.thumbnail((1024, 1024))
    gray = ImageOps.grayscale(image)
    blurred = gray.filter(ImageFilter.GaussianBlur(radius=1.2))
    magnitude = sobel_magnitude(np.asarray(blurred))
    scale = float(magnitude.max())
    normalized = magnitude * (255.0 / scale) if scale else magnitude
    edges = Image.fromarray(np.clip(normalized, 0, 255).astype(np.uint8))
    panels = [("input", image), ("gray", gray), ("blurred", blurred), ("sobel", edges)]
    board = Image.new("RGB", (4 * 256, 284), "#111827")
    draw = ImageDraw.Draw(board)
    for index, (label, panel) in enumerate(panels):
        panel.save(output / f"{label}.png")
        preview = ImageOps.contain(panel.convert("RGB"), (256, 256))
        board.paste(preview, (index * 256, 28))
        draw.text((index * 256 + 10, 8), label, fill="white")
    board.save(output / "comparison.png")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", type=Path, help="Optional local image; default is a drawn scene.")
    parser.add_argument("--output", type=Path, default=Path("outputs/image-processing"))
    args = parser.parse_args()
    if args.image:
        with Image.open(args.image) as image:
            process(image, args.output)
    else:
        process(synthetic_scene(), args.output)
    print(f"Saved input, grayscale, blur, gradients and comparison to {args.output}")


if __name__ == "__main__":
    main()
