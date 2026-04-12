#!/usr/bin/env python3
"""Generate per-park OG images for crowd calendar pages.

Usage: python3 tools/generate_og_images.py
Output: images/og/og-crowd-calendar-{slug}.png (2400x1260, retina-ready)
"""

import os
from PIL import Image, ImageDraw, ImageFont

WIDTH = 2400
HEIGHT = 1260

FONTS = {
    "bold": "/Library/Fonts/SF-Pro-Display-Bold.otf",
    "semibold": "/Library/Fonts/SF-Pro-Display-Semibold.otf",
    "medium": "/Library/Fonts/SF-Pro-Display-Medium.otf",
    "regular": "/Library/Fonts/SF-Pro-Display-Regular.otf",
}

PARKS = [
    {"slug": "epic-universe", "name": "Epic Universe", "region": "Orlando, FL", "tagline": "The newest Universal park"},
    {"slug": "universal-studios-florida", "name": "Universal Studios Florida", "region": "Orlando, FL", "tagline": "The original Universal park"},
    {"slug": "islands-of-adventure", "name": "Islands of Adventure", "region": "Orlando, FL", "tagline": "Wizarding World + coasters"},
    {"slug": "seaworld-orlando", "name": "SeaWorld Orlando", "region": "Orlando, FL", "tagline": "Marine life + thrill rides"},
    {"slug": "busch-gardens-tampa", "name": "Busch Gardens Tampa", "region": "Tampa, FL", "tagline": "World-class coasters + wildlife"},
    {"slug": "busch-gardens-williamsburg", "name": "Busch Gardens Williamsburg", "region": "Williamsburg, VA", "tagline": "European-themed thrill park"},
    {"slug": "cedar-point", "name": "Cedar Point", "region": "Sandusky, OH", "tagline": "Roller coaster capital of the world"},
    {"slug": "kings-island", "name": "Kings Island", "region": "Mason, OH", "tagline": "World-class coasters near Cincinnati"},
    {"slug": "kings-dominion", "name": "Kings Dominion", "region": "Doswell, VA", "tagline": "Virginia's premier thrill park"},
    {"slug": "carowinds", "name": "Carowinds", "region": "Charlotte, NC", "tagline": "Straddling the NC/SC border"},
    {"slug": "canadas-wonderland", "name": "Canada's Wonderland", "region": "Vaughan, ON", "tagline": "Canada's premier theme park"},
    {"slug": "six-flags-over-georgia", "name": "Six Flags Over Georgia", "region": "Austell, GA", "tagline": "Atlanta's thrill destination"},
    {"slug": "six-flags-great-adventure", "name": "Six Flags Great Adventure", "region": "Jackson, NJ", "tagline": "East Coast's biggest thrill park"},
    {"slug": "six-flags-great-america", "name": "Six Flags Great America", "region": "Gurnee, IL", "tagline": "Chicago-area thrills"},
]


def load_font(weight, size):
    path = FONTS.get(weight)
    if path and os.path.exists(path):
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def crowd_color(level):
    if level <= 3:
        return "#22c55e"
    if level <= 6:
        return "#f59e0b"
    if level <= 8:
        return "#ef4444"
    return "#991b1b"


def draw_gradient_bg(img):
    """Draw dark background with subtle brand gradient."""
    draw = ImageDraw.Draw(img)
    # Base dark
    draw.rectangle([0, 0, WIDTH, HEIGHT], fill="#000000")

    # Subtle orange radial glow (top-left)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            dx = (x - WIDTH * 0.15) / WIDTH
            dy = (y - HEIGHT * 0.25) / HEIGHT
            dist = (dx * dx + dy * dy) ** 0.5
            alpha = max(0, 0.14 - dist * 0.12)
            r = int(249 * alpha)
            g = int(115 * alpha)
            b = int(22 * alpha)
            px = img.getpixel((x, y))
            img.putpixel((x, y), (min(255, px[0] + r), min(255, px[1] + g), min(255, px[2] + b)))

    # Subtle pink radial glow (bottom-right)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            dx = (x - WIDTH * 0.85) / WIDTH
            dy = (y - HEIGHT * 0.75) / HEIGHT
            dist = (dx * dx + dy * dy) ** 0.5
            alpha = max(0, 0.08 - dist * 0.10)
            r = int(255 * alpha)
            g = int(65 * alpha)
            b = int(108 * alpha)
            px = img.getpixel((x, y))
            img.putpixel((x, y), (min(255, px[0] + r), min(255, px[1] + g), min(255, px[2] + b)))


def draw_crowd_dots(draw, x, y, size=28, gap=10):
    """Draw a 1-10 crowd level meter with sample levels."""
    sample_levels = [3, 5, 7, 9, 4, 2, 6, 8, 5, 3]
    for i, level in enumerate(sample_levels):
        dot_x = x + i * (size + gap)
        color = crowd_color(level)
        draw.rounded_rectangle(
            [dot_x, y, dot_x + size, y + size],
            radius=6,
            fill=color,
        )
        # Draw the number inside
        num_font = load_font("bold", 16)
        draw.text(
            (dot_x + size // 2, y + size // 2),
            str(level),
            font=num_font,
            fill="#FFFFFF",
            anchor="mm",
        )


def generate_park_og(park, output_dir):
    """Generate a single park OG image."""
    img = Image.new("RGB", (WIDTH, HEIGHT), "#000000")
    draw_gradient_bg(img)
    draw = ImageDraw.Draw(img)

    # Fonts
    font_label = load_font("semibold", 32)
    font_park = load_font("bold", 96)
    font_tagline = load_font("medium", 42)
    font_region = load_font("regular", 38)
    font_cta = load_font("semibold", 36)
    font_url = load_font("medium", 34)

    left_x = 120
    y = 140

    # "CROWD CALENDAR" label
    draw.text((left_x, y), "CROWD CALENDAR", font=font_label, fill="#F97316")
    y += 60

    # Park name (may need to wrap if long)
    name = park["name"]
    # Check if name fits
    bbox = draw.textbbox((0, 0), name, font=font_park)
    max_width = WIDTH - 240
    if bbox[2] - bbox[0] > max_width:
        # Use smaller font for long names
        font_park_small = load_font("bold", 76)
        draw.text((left_x, y), name, font=font_park_small, fill="#FFFFFF")
        y += 100
    else:
        draw.text((left_x, y), name, font=font_park, fill="#FFFFFF")
        y += 120

    # "Know When to Go" in accent green
    font_italic = load_font("semibold", 56)
    draw.text((left_x, y), "Know When to Go", font=font_italic, fill="#34D399")
    y += 80

    # Region
    draw.text((left_x, y), park["region"], font=font_region, fill="#999999")
    y += 60

    # Tagline
    draw.text((left_x, y), park["tagline"], font=font_tagline, fill="#BBBBBB")
    y += 80

    # Sample crowd dots row
    draw_crowd_dots(draw, left_x, y, size=44, gap=14)
    y += 70

    # Legend below dots
    font_legend = load_font("regular", 24)
    legend_items = [
        ("#22c55e", "Low"),
        ("#f59e0b", "Moderate"),
        ("#ef4444", "High"),
        ("#991b1b", "Peak"),
    ]
    lx = left_x
    for color, label in legend_items:
        draw.ellipse([lx, y, lx + 16, y + 16], fill=color)
        draw.text((lx + 22, y - 2), label, font=font_legend, fill="#888888")
        lx += 160

    # Bottom branding
    draw.text((left_x, HEIGHT - 100), "rideready.app", font=font_url, fill="#F97316")

    # Ride Ready logo placeholder (top-right)
    logo_size = 120
    logo_x = WIDTH - logo_size - 120
    logo_y = 120
    icon_path = os.path.join(os.path.dirname(__file__), "..", "images", "logo.png")
    if os.path.exists(icon_path):
        icon = Image.open(icon_path).convert("RGBA")
        icon = icon.resize((logo_size, logo_size), Image.LANCZOS)
        img.paste(icon, (logo_x, logo_y), icon)
    else:
        draw.rounded_rectangle(
            [logo_x, logo_y, logo_x + logo_size, logo_y + logo_size],
            radius=20,
            fill="#F97316",
        )
        rr_font = load_font("bold", 48)
        draw.text(
            (logo_x + logo_size // 2, logo_y + logo_size // 2),
            "RR",
            font=rr_font,
            fill="#000000",
            anchor="mm",
        )

    # Save
    filename = f"og-crowd-calendar-{park['slug']}.png"
    output_path = os.path.join(output_dir, filename)
    img.save(output_path, "PNG", optimize=True)
    size_kb = os.path.getsize(output_path) // 1024
    print(f"  Generated: {filename} ({size_kb}KB)")
    return output_path


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "..", "images", "og")
    os.makedirs(output_dir, exist_ok=True)

    print(f"Generating {len(PARKS)} OG images...")
    for park in PARKS:
        generate_park_og(park, output_dir)
    print("Done!")


if __name__ == "__main__":
    main()
