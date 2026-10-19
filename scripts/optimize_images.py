"""Generate the site's responsive WebP assets without changing the originals.

Requires Pillow: python -m pip install Pillow
Run from any directory: python scripts/optimize_images.py
"""

from pathlib import Path

from PIL import Image, ImageOps


IMAGE_ROOT = Path(__file__).resolve().parents[1] / "assets" / "images"
OUTPUT_ROOT = IMAGE_ROOT / "optimized"
PROFILES = {
    "graduation": ((480, 960, 1440), 82),
    "bio-photo": ((110, 220), 85),
    **{
        name: ((320, 640, 1920), 90)
        for name in ("Vision", "OCC", "Kuwait", "SDSW", "PM", "IAQ")
    },
}


def main():
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    for name, (widths, quality) in PROFILES.items():
        source = IMAGE_ROOT / f"{name}.jpg"
        with Image.open(source) as image:
            image = ImageOps.exif_transpose(image).convert("RGB")
            for width in widths:
                if width > image.width:
                    raise ValueError(f"Refusing to upscale {source.name} to {width}px")
                height = round(image.height * width / image.width)
                resized = image.resize((width, height), Image.Resampling.LANCZOS)
                target = OUTPUT_ROOT / f"{name}-{width}.webp"
                resized.save(target, "WEBP", quality=quality, method=6)
                print(f"{target.name}: {width}x{height}, {target.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
