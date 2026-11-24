#!/usr/bin/env python3
"""Raster previews of the original Swiss Sales SVG artwork; no logo redesign."""
from io import BytesIO
from pathlib import Path
from PIL import Image
import cairosvg

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

def render_svg(path, output_width):
    data = cairosvg.svg2png(url=str(path), output_width=output_width)
    return Image.open(BytesIO(data)).convert("RGBA")

def save_optimized(image, path):
    image = image.convert("RGB")
    image.save(path, "PNG", optimize=True)

# Square favicon: the existing emblem intact, scaled to fit with whitespace.
crest = render_svg(ASSETS / "crest-mark.svg", 320)
square = Image.new("RGBA", (512, 512), "#FAF9F6")
square.alpha_composite(crest, ((512 - crest.width) // 2, (512 - crest.height) // 2))
save_optimized(square, ASSETS / "favicon-512.png")

# Social card: the existing, complete logo lockup, unchanged on a cream canvas.
lockup = render_svg(ASSETS / "logo-lockup.svg", 960)
card = Image.new("RGBA", (1200, 630), "#FAF9F6")
card.alpha_composite(lockup, ((1200 - lockup.width) // 2, (630 - lockup.height) // 2))
save_optimized(card, ASSETS / "social-preview.png")
print("Generated original-artwork favicon and social preview.")
