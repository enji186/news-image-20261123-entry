#!/usr/bin/env python3
"""Draw the 23 November 2026 world-news infographic with Pillow.

Build-time script only (not the entrypoint). Writes entry.png next to
this file: 1024x1024, navy header naming the date, six numbered story
cards, footer with sources. All text is drawn with DejaVu fonts so it
stays crisp and legible.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "entry.png"

NAVY = (15, 34, 56)
GOLD = (212, 175, 55)
CARD = (255, 255, 255)
INK = (20, 30, 43)
GREY = (90, 104, 122)
FOOT = (170, 185, 205)

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

STORIES = [
    ("1", "TECHNOLOGY", (37, 99, 235),
     "Nvidia reinstates Huang as CEO",
     "Nvidia brings back Jensen Huang on Monday after Trump pressed for his return."),
    ("2", "PACIFIC", (13, 148, 136),
     "Magnitude 6.5 quake jolts Vanuatu",
     "The deep quake struck at 1:40 p.m. local time; no casualties or damage reported."),
    ("3", "LAW & TECH", (124, 58, 237),
     "Two US states sue SpaceX over Grok",
     "Virginia and Oregon say the chatbot's 'spicy mode' made sexualised images of real people."),
    ("4", "WAR", (185, 28, 28),
     "Ukraine says it sank a Russian warship",
     "Zelenskyy says naval drones hit the ship off Libya in Sunday's attack."),
    ("5", "POLITICS", (30, 64, 175),
     "Democrats win 258 House seats",
     "Their largest House majority since 1992, sealed by a North Carolina recount win."),
    ("6", "SPACE", (194, 65, 12),
     "Mercury probe safe after glitch",
     "ESA says BepiColombo is in a stable orbit and on track after a thruster fault."),
]


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Wrap text to lines that fit max_w pixels."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_globe(draw, cx, cy, r):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=GOLD, width=4)
    draw.ellipse([cx - r * 0.55, cy - r, cx + r * 0.55, cy + r],
                 outline=GOLD, width=3)
    draw.line([cx - r, cy, cx + r, cy], fill=GOLD, width=3)
    draw.line([cx - r, cy - r * 0.45, cx + r, cy - r * 0.45], fill=GOLD, width=2)
    draw.line([cx - r, cy + r * 0.45, cx + r, cy + r * 0.45], fill=GOLD, width=2)


def main():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # Header
    d.text((36, 28), "23 NOVEMBER 2026", font=font(SANS_BOLD, 68), fill=(255, 255, 255))
    d.text((38, 108), "World News in One Image", font=font(SANS, 34), fill=GOLD)
    draw_globe(d, 930, 78, 52)
    d.line([0, 158, W, 158], fill=GOLD, width=3)

    # Cards: 2 columns x 3 rows
    margin, gap = 36, 24
    cw = (W - 2 * margin - gap) // 2
    ch = 252
    top = 178
    for i, (num, tag, color, headline, summary) in enumerate(STORIES):
        row, col = divmod(i, 2)
        x0 = margin + col * (cw + gap)
        y0 = top + row * (ch + gap)
        x1, y1 = x0 + cw, y0 + ch
        d.rounded_rectangle([x0, y0, x1, y1], radius=14, fill=CARD)
        d.rectangle([x0, y0 + 14, x0 + 10, y1 - 14], fill=color)
        # Number circle + tag
        d.ellipse([x0 + 24, y0 + 20, x0 + 66, y0 + 62], fill=color)
        d.text((x0 + 45, y0 + 26), num, font=font(SANS_BOLD, 28),
               fill=(255, 255, 255), anchor="ma")
        d.text((x0 + 80, y0 + 28), tag, font=font(SANS_BOLD, 24), fill=color)
        # Headline
        hl_font = font(SANS_BOLD, 29)
        hl_lines = wrap(d, headline, hl_font, cw - 48)
        hy = y0 + 78
        for line in hl_lines:
            d.text((x0 + 24, hy), line, font=hl_font, fill=INK)
            hy += 36
        # Summary
        sm_font = font(SANS, 21)
        sm_lines = wrap(d, summary, sm_font, cw - 48)
        sy = hy + 6
        for line in sm_lines:
            d.text((x0 + 24, sy), line, font=sm_font, fill=GREY)
            sy += 28

    # Footer
    d.text((36, 988), "Sources: Reuters, AP, Xinhua, ESA, NHK  |  23 Nov 2026",
           font=font(SANS, 19), fill=FOOT)

    img.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT} {img.size}")


if __name__ == "__main__":
    main()
