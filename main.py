# main.py — renders entry.png (1024x1024) for news-image-20261122 v4.
# "The World in One Day" — Sunday 22 November 2026.
# Written fresh in this session. Run: python3 main.py
import math
from PIL import Image, ImageDraw, ImageFont
from stories import (LEADS, REGIONS, SPORT, STATS, TIMELINE,
                     DATE_CHECK, MAP_PINS)

W, H = 1024, 1024
PAPER = (250, 246, 236)
INK = (26, 26, 26)
MUTED = (90, 86, 76)
RULE = (26, 26, 26)
NAVY = (20, 33, 61)
GOLD = (244, 211, 94)
WHITE = (255, 255, 255)
CREAM = (250, 246, 236)

FDIR = "/usr/share/fonts/truetype/dejavu/"
def F(name, size):
    return ImageFont.truetype(FDIR + name, size)

SERIF_B = lambda s: F("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: F("DejaVuSerif.ttf", s)
SANS_B = lambda s: F("DejaVuSans-Bold.ttf", s)
SANS = lambda s: F("DejaVuSans.ttf", s)

CONF_COLOR = {
    "CONFIRMED": (22, 101, 52),
    "CLAIM": (180, 83, 9),
    "REPORTED": (29, 78, 216),
    "PENDING": (100, 100, 100),
}

def wrap(d, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_wrapped(d, x, y, text, font, max_w, fill=INK, lh=None):
    if lh is None:
        lh = int(font.size * 1.22)
    lines = wrap(d, text, font, max_w)
    for ln in lines:
        d.text((x, y), ln, font=font, fill=fill)
        y += lh
    return y

def text_h(font):
    return int(font.size * 1.2)

def fit_line(d, text, font, max_w):
    """Truncate text with an ellipsis so it fits on one line."""
    if d.textlength(text, font=font) <= max_w:
        return text
    while text and d.textlength(text + "…", font=font) > max_w:
        text = text[:-1]
    return text + "…"

# ---------------- mini icons (14x14 box, drawn with simple shapes) ----------------
def draw_icon(d, x, y, kind, color):
    # x,y = top-left of 14x14 box
    if kind == "drone":
        d.line([(x+1, y+1), (x+13, y+13)], fill=color, width=2)
        d.line([(x+13, y+1), (x+1, y+13)], fill=color, width=2)
        d.ellipse([x+5, y+5, x+9, y+9], fill=color)
    elif kind == "fire":
        d.polygon([(x+7, y+1), (x+12, y+8), (x+10, y+13), (x+4, y+13), (x+2, y+8)],
                  fill=color)
        d.ellipse([x+5, y+8, x+9, y+12], fill=PAPER)
    elif kind == "bolt":
        d.polygon([(x+8, y+1), (x+3, y+8), (x+6, y+8), (x+5, y+13),
                   (x+11, y+6), (x+8, y+6)], fill=color)
    elif kind == "ship":
        d.polygon([(x+2, y+8), (x+12, y+8), (x+10, y+12), (x+4, y+12)], fill=color)
        d.rectangle([x+6, y+2, x+8, y+8], fill=color)
        d.polygon([(x+8, y+3), (x+12, y+7), (x+8, y+7)], fill=color)
    elif kind == "candle":
        d.rectangle([x+6, y+5, x+8, y+13], fill=color)
        d.ellipse([x+5, y+1, x+9, y+5], fill=(230, 140, 30))
    elif kind == "march":
        d.ellipse([x+6, y+1, x+9, y+4], fill=color)
        d.rectangle([x+6, y+5, x+8, y+10], fill=color)
        d.line([(x+7, y+10), (x+4, y+13)], fill=color, width=2)
        d.line([(x+7, y+10), (x+10, y+13)], fill=color, width=2)
    elif kind == "plane":
        d.polygon([(x+7, y+1), (x+9, y+6), (x+13, y+7), (x+9, y+8),
                   (x+8, y+13), (x+6, y+13), (x+5, y+8), (x+1, y+7),
                   (x+5, y+6)], fill=color)
    elif kind == "bridge":
        d.line([(x+1, y+11), (x+13, y+11)], fill=color, width=2)
        d.line([(x+3, y+11), (x+3, y+4)], fill=color, width=2)
        d.line([(x+11, y+11), (x+11, y+4)], fill=color, width=2)
        d.arc([x+3, y+4, x+11, y+12], 180, 360, fill=color, width=2)
    elif kind == "rocket":
        d.polygon([(x+7, y+1), (x+10, y+6), (x+9, y+11), (x+5, y+11),
                   (x+4, y+6)], fill=color)
        d.polygon([(x+4, y+9), (x+2, y+13), (x+5, y+11)], fill=color)
        d.polygon([(x+10, y+9), (x+12, y+13), (x+9, y+11)], fill=color)
    elif kind == "truck":
        d.rectangle([x+1, y+5, x+9, y+11], fill=color)
        d.rectangle([x+9, y+7, x+12, y+11], fill=color)
        d.ellipse([x+3, y+11, x+6, y+13], fill=color)
        d.ellipse([x+9, y+11, x+12, y+13], fill=color)
    elif kind == "vote":
        d.rectangle([x+2, y+4, x+12, y+13], outline=color, width=2)
        d.line([(x+4, y+9), (x+6, y+11), (x+11, y+4)], fill=color, width=2)
    elif kind == "court":
        d.line([(x+2, y+12), (x+12, y+12)], fill=color, width=2)
        d.rectangle([x+6, y+2, x+8, y+12], fill=color)
        d.polygon([(x+2, y+2), (x+12, y+2), (x+7, y+5)], fill=color)
    elif kind == "money":
        d.ellipse([x+2, y+3, x+12, y+11], outline=color, width=2)
        d.text((x+5, y+3), "$", font=SANS_B(9), fill=color)
    elif kind == "trophy":
        d.polygon([(x+4, y+1), (x+10, y+1), (x+9, y+7), (x+5, y+7)], fill=color)
        d.rectangle([x+6, y+7, x+8, y+10], fill=color)
        d.rectangle([x+4, y+10, x+10, y+13], fill=color)
    elif kind == "health":
        d.rectangle([x+5, y+1, x+9, y+13], fill=color)
        d.rectangle([x+1, y+5, x+13, y+9], fill=color)
    elif kind == "hack":
        d.rectangle([x+2, y+6, x+12, y+12], outline=color, width=2)
        d.arc([x+4, y+2, x+10, y+8], 180, 360, fill=color, width=2)
    elif kind == "storm":
        d.ellipse([x+2, y+6, x+9, y+11], fill=color)
        d.ellipse([x+6, y+4, x+12, y+9], fill=color)
        d.polygon([(x+6, y+10), (x+4, y+13), (x+7, y+13)], fill=(230, 140, 30))
    elif kind == "quake":
        d.line([(x+7, y+1), (x+5, y+5), (x+9, y+8), (x+6, y+13)], fill=color, width=2)
        d.line([(x+2, y+12), (x+12, y+12)], fill=color, width=2)
    else:
        d.rectangle([x+3, y+3, x+11, y+11], fill=color)

# ---------------- lead illustrations ----------------
def ill_drones(d, x, y, w, h):
    # night sky over a city, drones + explosions
    sky = (24, 32, 58)
    d.rectangle([x, y, x + w, y + h], fill=sky)
    # stars
    for sx, sy in [(12, 10), (60, 22), (110, 8), (170, 16), (230, 9), (290, 20),
                   (40, 34), (150, 30), (260, 34), (200, 8), (90, 40)]:
        d.ellipse([x + sx - 1, y + sy - 1, x + sx + 1, y + sy + 1], fill=(220, 220, 230))
    # skyline
    base = y + h
    buildings = [(0, 34, 46), (46, 58, 26), (72, 46, 40), (112, 66, 30),
                 (142, 40, 44), (186, 60, 24), (210, 48, 42), (252, 62, 28),
                 (280, 44, 40)]
    for bx, bw, bh in buildings:
        d.rectangle([x + bx, base - bh, x + bx + bw, base], fill=(12, 16, 30))
        for wy in range(base - bh + 5, base - 4, 9):
            for wx in range(bx + 5, bx + bw - 3, 10):
                if (wx * 7 + wy * 3) % 5 == 0:
                    d.rectangle([x + wx, wy, x + wx + 3, wy + 4], fill=(244, 211, 94))
    # explosion bursts (relative to illustration top)
    for ex, ey, r in [(70, h - 62, 16), (235, h - 58, 13)]:
        for ang in range(0, 360, 30):
            rad = math.radians(ang)
            d.line([(x + ex, y + ey), (x + ex + r * math.cos(rad),
                     y + ey + r * math.sin(rad))], fill=(255, 140, 40), width=3)
        d.ellipse([x + ex - 7, y + ey - 7, x + ex + 7, y + ey + 7], fill=(255, 190, 60))
        d.ellipse([x + ex - 3, y + ey - 3, x + ex + 3, y + ey + 3], fill=(255, 240, 180))
    # smoke
    d.ellipse([x + 55, y + 18, x + 95, y + 34], fill=(120, 120, 130))
    d.ellipse([x + 220, y + 22, x + 255, y + 36], fill=(120, 120, 130))
    # drones (X silhouettes with rotor dots)
    for dx, dy in [(150, 22), (265, 40), (105, 48)]:
        d.line([(x + dx - 7, y + dy - 4), (x + dx + 7, y + dy + 4)], fill=(200, 200, 210), width=2)
        d.line([(x + dx + 7, y + dy - 4), (x + dx - 7, y + dy + 4)], fill=(200, 200, 210), width=2)
        d.ellipse([x + dx - 2, y + dy - 2, x + dx + 2, y + dy + 2], fill=(255, 80, 60))

def ill_cop(d, x, y, w, h):
    # Antalya summit hall: teal sky, sun, hall with dome + flags
    d.rectangle([x, y, x + w, y + h], fill=(14, 116, 144))
    d.ellipse([x + w - 52, y + 8, x + w - 16, y + 44], fill=(244, 211, 94))
    d.ellipse([x + 14, y + 12, x + 46, y + 44], fill=(255, 255, 255))
    d.ellipse([x + 20, y + 18, x + 40, y + 38], fill=(14, 116, 144))
    # hall
    base = y + h
    d.rectangle([x + 60, base - 52, x + w - 60, base], fill=(250, 246, 236))
    d.pieslice([x + w // 2 - 34, base - 86, x + w // 2 + 34, base - 18],
               180, 360, fill=(250, 246, 236))
    d.rectangle([x + w // 2 - 3, base - 92, x + w // 2 + 3, base - 52], fill=(180, 35, 24))
    for i in range(7):
        fx = x + 74 + i * 30
        d.rectangle([fx, base - 40, fx + 12, base - 14], fill=(20, 33, 61))
    # flags row
    flag_cols = [(180, 35, 24), (29, 78, 216), (22, 101, 52), (244, 211, 94),
                 (109, 40, 217), (194, 65, 12), (14, 116, 144)]
    for i, c in enumerate(flag_cols):
        fx = x + 30 + i * 40
        d.line([(fx, y + 62), (fx, y + 84)], fill=(255, 255, 255), width=2)
        d.polygon([(fx, y + 62), (fx + 22, y + 67), (fx, y + 72)], fill=c)

def ill_iran(d, x, y, w, h):
    # night over the Gulf: radar dish + missile trails
    d.rectangle([x, y, x + w, y + h], fill=(30, 18, 46))
    for sx, sy in [(20, 12), (80, 8), (150, 18), (220, 10), (290, 16), (50, 30), (180, 32)]:
        d.ellipse([x + sx - 1, y + sy - 1, x + sx + 1, y + sy + 1], fill=(220, 220, 230))
    # sea
    d.rectangle([x, y + h - 26, x + w, y + h], fill=(16, 60, 90))
    for wx in range(8, w - 8, 26):
        d.line([(x + wx, y + h - 14), (x + wx + 12, y + h - 14)], fill=(120, 180, 220), width=2)
    # radar dish (left)
    cx, cy = x + 70, y + h - 30
    d.arc([cx - 34, cy - 58, cx + 34, cy + 10], 180, 360, fill=(240, 240, 240), width=4)
    d.line([(cx, cy - 24), (cx, cy)], fill=(240, 240, 240), width=4)
    d.line([(cx - 18, cy), (cx + 18, cy)], fill=(240, 240, 240), width=4)
    # missile trails (right): diagonal streaks with bright heads
    for tx, ty, ln in [(205, 52, 46), (245, 30, 60), (280, 62, 36)]:
        d.line([(x + tx, y + ty + ln), (x + tx + 34, y + ty)], fill=(255, 200, 80), width=3)
        d.ellipse([x + tx + 30, y + ty - 4, x + tx + 40, y + ty + 6], fill=(255, 120, 40))
        d.ellipse([x + tx + 33, y + ty - 1, x + tx + 37, y + ty + 3], fill=(255, 240, 180))
    # base silhouette
    d.rectangle([x + w - 60, y + h - 52, x + w - 8, y + h - 26], fill=(12, 12, 20))

# ---------------- world map ----------------
CONTINENTS = [
    [(-168, 66), (-140, 70), (-120, 72), (-95, 80), (-80, 73), (-60, 60), (-55, 47),
     (-70, 42), (-75, 35), (-80, 26), (-90, 21), (-97, 16), (-105, 20), (-115, 28),
     (-125, 40), (-145, 60), (-168, 66)],
    [(-80, 10), (-60, 8), (-50, 0), (-35, -8), (-40, -20), (-48, -28), (-58, -35),
     (-65, -45), (-70, -55), (-73, -40), (-75, -20), (-80, -5), (-80, 10)],
    [(-10, 36), (0, 44), (-2, 48), (5, 53), (8, 57), (18, 56), (21, 60), (28, 70),
     (40, 68), (45, 60), (40, 50), (30, 45), (23, 40), (19, 42), (12, 44), (3, 42),
     (-9, 43), (-10, 36)],
    [(-17, 15), (-10, 30), (0, 35), (10, 37), (20, 32), (32, 31), (35, 28),
     (43, 12), (51, 11), (48, 0), (40, -15), (35, -25), (28, -33), (18, -35),
     (12, -18), (9, 4), (-8, 5), (-17, 15)],
    [(40, 68), (60, 70), (80, 73), (110, 77), (140, 72), (160, 70), (178, 66),
     (170, 60), (160, 55), (142, 50), (140, 40), (130, 35), (127, 40), (120, 30),
     (110, 20), (105, 10), (100, 8), (95, 15), (90, 22), (80, 8), (77, 8),
     (72, 20), (66, 25), (60, 25), (55, 26), (50, 29), (48, 30), (43, 35),
     (40, 36), (40, 68)],
    [(113, -22), (114, -30), (120, -34), (130, -32), (140, -38), (150, -37),
     (153, -27), (146, -19), (142, -11), (136, -12), (132, -11), (126, -14),
     (122, -17), (113, -22)],
]

def draw_map(d, x, y, w, h):
    # equirectangular: lon -180..190 -> x..x+w ; lat 78..-58 -> y..y+h
    def proj(lon, lat):
        px = x + (lon + 180) / 370.0 * w
        py = y + (78 - lat) / 136.0 * h
        return (px, py)
    d.rectangle([x, y, x + w, y + h], fill=(214, 232, 240))
    for poly in CONTINENTS:
        pts = [proj(lon, lat) for lon, lat in poly]
        d.polygon(pts, fill=(120, 160, 110), outline=(70, 110, 70))
    for num, name, lon, lat in MAP_PINS:
        px, py = proj(lon, lat)
        r = 7
        d.ellipse([px - r, py - r, px + r, py + r], fill=(180, 35, 24),
                  outline=WHITE, width=1)
        d.text((px - 2, py - 5), str(num), font=SANS_B(7), fill=WHITE)

# ---------------- layout ----------------
def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 8  # margin

    # outer frame
    d.rectangle([2, 2, W - 3, H - 3], outline=INK, width=3)
    d.rectangle([6, 6, W - 7, H - 7], outline=INK, width=1)

    # ---- masthead ----
    y = 14
    d.text((W // 2, y), "THE SUNDAY EDITION  ·  ALL STORIES VERIFIED FOR 22 NOVEMBER 2026",
           font=SANS_B(10), fill=MUTED, anchor="ma")
    y = 28
    d.text((W // 2, y), "THE WORLD IN ONE DAY", font=SERIF_B(52), fill=INK, anchor="ma")
    y = 84
    d.line([(M, y), (W - M, y)], fill=INK, width=2)
    y = 90
    left = "SUNDAY, 22 NOVEMBER 2026"
    mid = "36 STORIES  ·  7 REGIONS  ·  ONE DAY"
    right = "PRICE: ONE DAY OF NEWS"
    d.text((M, y), left, font=SANS_B(10), fill=INK)
    d.text((W // 2, y), mid, font=SANS_B(10), fill=INK, anchor="ma")
    d.text((W - M, y), right, font=SANS_B(10), fill=INK, anchor="ra")
    y = 106
    d.line([(M, y), (W - M, y)], fill=INK, width=1)

    # ---- stats bar ----
    sy, sh = 110, 52
    d.rectangle([M, sy, W - M, sy + sh], fill=NAVY)
    cell_w = (W - 2 * M) / len(STATS)
    for i, (num, label) in enumerate(STATS):
        cx = M + cell_w * i + cell_w / 2
        d.text((cx, sy + 6), num, font=SERIF_B(24), fill=GOLD, anchor="ma")
        d.text((cx, sy + 34), label, font=SANS_B(8), fill=WHITE, anchor="ma")
        if i:
            d.line([(M + cell_w * i, sy + 6), (M + cell_w * i, sy + sh - 6)],
                   fill=(255, 255, 255), width=1)

    # ---- leads ----
    ly, lh = 170, 240
    col_w = (W - 2 * M - 16) // 3
    ill_fns = [ill_drones, ill_cop, ill_iran]
    for i, lead in enumerate(LEADS):
        x0 = M + i * (col_w + 8)
        ill_fns[i](d, x0, ly, col_w, 100)
        yy = ly + 106
        d.text((x0, yy), lead["kicker"], font=SANS_B(9), fill=(180, 35, 24))
        yy += 13
        yy = draw_wrapped(d, x0, yy, lead["headline"], SERIF_B(15), col_w, lh=18)
        yy += 2
        yy = draw_wrapped(d, x0, yy, lead["body"], SANS(9), col_w, lh=12)
        yy += 5
        d.text((x0, yy), lead["confidence"] + "  ·  " + lead["source"],
               font=SANS_B(7), fill=CONF_COLOR[lead["confidence"]])
    d.line([(M, ly + lh + 4), (W - M, ly + lh + 4)], fill=INK, width=1)

    # ---- region sections (two columns) ----
    ry = 418
    region_h = 420
    col_w2 = (W - 2 * M - 12) // 2
    left_regs = [REGIONS[0], REGIONS[1]]   # EUROPE, MIDDLE EAST & AFRICA
    right_regs = [REGIONS[2], REGIONS[3], REGIONS[4]]  # ASIA-PACIFIC, AMERICAS, WORLD
    for col_idx, regs in enumerate([left_regs, right_regs]):
        x0 = M + col_idx * (col_w2 + 12)
        yy = ry
        for reg in regs:
            d.rectangle([x0, yy, x0 + col_w2, yy + 20], fill=reg["color"])
            d.text((x0 + 6, yy + 4), reg["name"], font=SANS_B(11), fill=WHITE)
            d.text((x0 + col_w2 - 6, yy + 4), str(reg["count"]) + " STORIES",
                   font=SANS_B(9), fill=WHITE, anchor="ra")
            yy += 24
            for headline, body, source, conf, icon in reg["items"]:
                draw_icon(d, x0 + 2, yy + 1, icon, reg["color"])
                tx = x0 + 20
                d.text((tx, yy), headline, font=SANS_B(9), fill=INK)
                d.text((x0 + col_w2, yy), conf, font=SANS_B(8),
                       fill=CONF_COLOR[conf], anchor="ra")
                yy += 12
                bl = fit_line(d, body + "  — " + source, SANS(8), col_w2 - 20)
                d.text((tx, yy), bl, font=SANS(8), fill=MUTED)
                yy += 12
            yy += 6
    d.line([(M, ry + region_h), (W - M, ry + region_h)], fill=INK, width=1)

    # ---- sport strip ----
    spy = 844
    d.rectangle([M, spy, W - M, spy + 18], fill=(22, 101, 52))
    d.text((M + 6, spy + 3), "SPORT IN BRIEF", font=SANS_B(11), fill=WHITE)
    d.text((W - M - 6, spy + 3), "6 STORIES", font=SANS_B(9), fill=WHITE, anchor="ra")
    yy = spy + 22
    scol_w = (W - 2 * M - 16) // 3
    for i, (headline, body, source, conf) in enumerate(SPORT):
        x0 = M + (i % 3) * (scol_w + 8)
        row = i // 3
        y0 = yy + row * 22
        d.text((x0, y0), headline, font=SANS_B(9), fill=INK)
        bl = fit_line(d, body + " — " + source, SANS(8), scol_w)
        d.text((x0, y0 + 11), bl, font=SANS(8), fill=MUTED)
    d.line([(M, 910), (W - M, 910)], fill=INK, width=1)

    # ---- bottom row: map / timeline / date check ----
    by = 918
    bh = 88
    bw = (W - 2 * M - 16) // 3
    # map
    x0 = M
    d.text((x0, by), "WHERE IT HAPPENED", font=SANS_B(10), fill=INK)
    draw_map(d, x0, by + 14, bw, 50)
    d.text((x0, by + 68), "1 Kyiv · 2 Odesa · 3 Gulf of Finland · 4 Tbilisi · 5 Antalya · 6 Bahrain",
           font=SANS(7), fill=MUTED)
    d.text((x0, by + 77), "7 Khartoum · 8 Hong Kong · 9 Cikande · 10 Wellington · 11 Brasília · 12 Las Vegas",
           font=SANS(7), fill=MUTED)
    # timeline
    x0 = M + bw + 8
    d.text((x0, by), "THE DAY IN UTC", font=SANS_B(10), fill=INK)
    yy = by + 15
    for t, ev in TIMELINE:
        d.text((x0, yy), t, font=SANS_B(8), fill=(180, 35, 24))
        d.text((x0 + 36, yy), ev, font=SANS(8), fill=INK)
        yy += 11
    # date check
    x0 = M + 2 * (bw + 8)
    d.rectangle([x0 - 4, by - 2, x0 + bw + 4, by + bh + 2], outline=(180, 35, 24), width=1)
    d.text((x0, by), "DATE CHECK — LEFT OUT (NOT 22 NOV)", font=SANS_B(9), fill=(180, 35, 24))
    yy = by + 15
    for name, when in DATE_CHECK:
        d.text((x0, yy), "✕ " + name, font=SANS(8), fill=INK)
        d.text((x0 + bw, yy), when, font=SANS_B(8), fill=(180, 35, 24), anchor="ra")
        yy += 9

    # ---- footer ----
    d.text((W // 2, 1010),
           "Sources: Reuters · AP · AFP · BBC · Al Jazeera · Ukrinform · SBS · Focus Taiwan · Jiji Press — Every story on this page is dated 22 November 2026.",
           font=SANS(7), fill=MUTED, anchor="ma")

    import os
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, optimize=True)
    print("saved", out)

if __name__ == "__main__":
    main()
