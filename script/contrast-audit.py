#!/usr/bin/env python3
"""Check every text/background pair in the site against WCAG 2.1 contrast.

Reads the colour tokens straight out of assets/css/style.css, so changing
the palette and re-running this is enough to re-verify it.

    python3 script/contrast-audit.py

Exits non-zero if anything falls below its threshold. No dependencies.
"""
import re
import sys
from pathlib import Path

CSS = Path(__file__).resolve().parent.parent / "assets" / "css" / "style.css"

# Translucent layers that put text over a blended background.
CHIP_WASH = ("#ef8dae", 0.10)   # .chip.is-active
SCRIM     = ("#0c0518", 0.95)   # .lightbox backdrop

# The intro sits over the sunset glow, whose strength varies by position, so a
# flat "worst case" model is misleading in both directions. These are the
# BRIGHTEST pixel actually rendered behind each element, sampled from the live
# page at 390 / 900 / 1280px wide with the copy hidden. Re-measure after
# changing the glow, --floor-h, --sky-gap, or the intro layout:
#
#   1. bundle exec jekyll serve
#   2. screenshot / with `.intro__copy { visibility: hidden }`
#   3. take the max-luminance pixel inside each element's bounding box
#
# The glow's mask and the intro's bottom padding are what keep these dark;
# see the comment on .intro::after in style.css.
# The body carries a radial that peaks at the very top of every page:
#   radial-gradient(120% 70% at 50% 0%, #22103c, transparent 62%)
# Anything in the first screenful sits on this rather than flat --bg.
PAGE_TOP = "#22103c"

INTRO_BG = {
    "mono label": "#1f0f36",
    "headline":   "#1e0f34",
    "lede":       "#251135",
    "button":     "#652e5b",
}


def tokens(css):
    """Pull `--name: #rrggbb;` declarations out of the :root block."""
    root = re.search(r":root\s*\{(.*?)\}", css, re.S)
    if not root:
        sys.exit("could not find :root block in style.css")
    found = dict(re.findall(r"--([\w-]+):\s*(#[0-9a-fA-F]{6})\s*;", root.group(1)))
    required = {"bg", "bg-alt", "surface", "surface-2", "line",
                "text", "text-2", "text-3", "prose",
                "cream", "gold", "accent", "violet", "cyan"}
    missing = required - found.keys()
    if missing:
        sys.exit(f"missing colour tokens: {', '.join(sorted(missing))}")
    return found


def channel(c):
    c /= 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hexstr):
    h = hexstr.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)


def ratio(a, b):
    la, lb = luminance(a), luminance(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)


def over(fg, alpha, bg):
    """Composite a translucent colour onto an opaque one."""
    f, b = fg.lstrip("#"), bg.lstrip("#")
    return "#%02x%02x%02x" % tuple(
        round(alpha * int(f[i:i + 2], 16) + (1 - alpha) * int(b[i:i + 2], 16))
        for i in (0, 2, 4)
    )


def main():
    t = tokens(CSS.read_text())
    BG, ALT, SURFACE, SURFACE2 = t["bg"], t["bg-alt"], t["surface"], t["surface-2"]
    TEXT, TEXT2, TEXT3, PROSE = t["text"], t["text-2"], t["text-3"], t["prose"]
    ACCENT, CREAM, GOLD, VIOLET, CYAN = (
        t["accent"], t["cream"], t["gold"], t["violet"], t["cyan"])

    CHIP_ON  = over(CHIP_WASH[0], CHIP_WASH[1], BG)
    LIGHTBOX = over(SCRIM[0], SCRIM[1], BG)

    # (label, foreground, background, minimum ratio)
    # 4.5 = AA normal text, 3.0 = AA large text and non-text (focus rings).
    checks = [
        ("body text",                   PROSE,  BG,       4.5),
        ("body text on surface",        PROSE,  SURFACE,  4.5),
        ("headings",                    TEXT,   BG,       3.0),
        ("heading over intro glow",     TEXT,   INTRO_BG["headline"],   3.0),
        ("lede",                        TEXT2,  BG,       4.5),
        ("lede over intro glow",        TEXT2,  INTRO_BG["lede"],       4.5),
        ("lede on alt band",            TEXT2,  ALT,      4.5),
        ("lede on surface",             TEXT2,  SURFACE,  4.5),
        ("mono label",                  TEXT3,  BG,       4.5),
        ("mono label at page top",      TEXT3,  PAGE_TOP, 4.5),
        ("lede at page top",            TEXT2,  PAGE_TOP, 4.5),
        ("body text at page top",       PROSE,  PAGE_TOP, 4.5),
        ("accent at page top",          ACCENT, PAGE_TOP, 4.5),
        ("heading at page top",         TEXT,   PAGE_TOP, 3.0),
        ("nav link at page top",        TEXT2,  PAGE_TOP, 4.5),
        ("mono label over intro glow",  TEXT3,  INTRO_BG["mono label"], 4.5),
        ("mono label on alt band",      TEXT3,  ALT,      4.5),
        ("mono label on surface",       TEXT3,  SURFACE,  4.5),
        ("tag text",                    TEXT3,  SURFACE,  4.5),
        ("accent link",                 ACCENT, BG,       4.5),
        ("accent over intro glow",      ACCENT, INTRO_BG["mono label"], 4.5),
        ("accent on alt band",          ACCENT, ALT,      4.5),
        ("accent on surface",           ACCENT, SURFACE,  4.5),
        ("inline code",                 ACCENT, SURFACE2, 4.5),
        ("active filter chip",          ACCENT, CHIP_ON,  4.5),
        # The primary button is filled with the sunset ramp, so --bg text
        # must clear every stop along it, not just one.
        ("button text on cream stop",   BG,     CREAM,    4.5),
        ("button text on gold stop",    BG,     GOLD,     4.5),
        ("button text on rose stop",    BG,     ACCENT,   4.5),
        ("button text on violet stop",  BG,     VIOLET,   4.5),
        # Gradient headline text: each stop against the page (large text).
        ("headline cream stop",         CREAM,  BG,       3.0),
        ("headline gold stop",          GOLD,   BG,       3.0),
        ("headline rose stop",          ACCENT, BG,       3.0),
        ("headline violet stop",        VIOLET, BG,       3.0),
        ("cyan detail",                 CYAN,   BG,       4.5),
        ("skip link text",              BG,     ACCENT,   4.5),
        ("ghost button text",           TEXT,   BG,       4.5),
        ("ghost button over glow",      TEXT,   INTRO_BG["button"],     4.5),
        ("nav link",                    TEXT2,  BG,       4.5),
        ("footer link",                 TEXT2,  BG,       4.5),
        ("lightbox title",              TEXT,   LIGHTBOX, 4.5),
        ("lightbox meta",               ACCENT, LIGHTBOX, 4.5),
        ("lightbox caption",            TEXT2,  LIGHTBOX, 4.5),
        ("focus ring on page",          ACCENT, BG,       3.0),
        ("focus ring on surface",       ACCENT, SURFACE,  3.0),
    ]

    print(f"accent {ACCENT} on {BG}\n")
    print(f'{"":<28}{"ratio":>9}{"min":>7}  result')
    print("-" * 55)

    failures = []
    for label, fg, bg, need in checks:
        r = ratio(fg, bg)
        if r < need:
            failures.append((label, r, need))
        print(f'{label:<28}{r:>8.2f}:1{need:>6.1f}  {"ok" if r >= need else "FAIL"}')

    print("-" * 55)
    if failures:
        print(f"{len(failures)} of {len(checks)} pairs below threshold:")
        for label, r, need in failures:
            print(f"  {label}: {r:.2f}:1 (needs {need}:1)")
        return 1

    worst = min(ratio(fg, bg) / need for _, fg, bg, need in checks)
    print(f"{len(checks)} pairs checked, all pass. Tightest is {worst:.2f}x its threshold.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
