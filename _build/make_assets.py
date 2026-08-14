# -*- coding: utf-8 -*-
"""Παράγει τα στατικά εικαστικά του site από τα πρωτότυπα αρχεία του πελάτη.

    python3 _build/make_assets.py

Πηγές (στη ρίζα του φακέλου του πελάτη):
  • LOGO - Marilena_Tzannetatou_[business-card].jpg  — mockup δύο επαγγελματικών
    καρτών· χρησιμοποιείται ΜΟΝΟ το λογότυπο της πρώτης (αριστερής) κάρτας.
  • PHOTO - DSCF2163.jpg                            — φωτογραφία του γραφείου.

Απαιτεί Pillow:  python3 -m pip install Pillow
"""
import pathlib
from PIL import Image, ImageFilter, ImageDraw
import numpy as np

BASE = pathlib.Path(__file__).resolve().parent.parent
IMG = BASE / "website" / "assets" / "img"
LOGO_SRC = BASE / "LOGO - Marilena_Tzannetatou_[business-card].jpg"
PHOTO_SRC = BASE / "PHOTO - DSCF2163.jpg"

# Το λογότυπο μέσα στο mockup, σε pixel του πρωτοτύπου (2000×1273).
# Βρέθηκε με ανίχνευση του μελανιού μέσα στα όρια της πρώτης κάρτας.
LOGO_BOX = (289, 574, 882, 685)
PAD = 10
INK = (23, 32, 30)        # --cb-ink
LIGHT = (246, 247, 245)   # --color-stone-white
OUT_W = 960               # ~3× το μέγεθος εμφάνισης στο header

# Κατώφλια αποκοπής χαρτιού/μελανιού μετά την εξομάλυνση φωτισμού.
PAPER_LEVEL, INK_LEVEL, FLOOR = 236.0, 105.0, 0.10


def logo_alpha():
    """Απομονώνει το τυπωμένο μελάνι από την υφή του χαρτιού.

    Το mockup έχει κόκκο και άνισο φωτισμό, οπότε ένα σταθερό κατώφλι αφήνει
    γκρίζες κηλίδες. Διαιρούμε πρώτα με μια εκτίμηση του χαρτιού (max-filter +
    έντονο blur): έτσι το χαρτί ισοπεδώνεται στο ~255 και μένει μόνο η γραμμή.
    """
    src = Image.open(LOGO_SRC).convert("L")
    paper = src.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(28))
    norm = np.clip(np.asarray(src, np.float32) /
                   np.maximum(np.asarray(paper, np.float32), 1.0) * 255.0, 0, 255)

    x0, y0, x1, y1 = LOGO_BOX
    sub = norm[y0 - PAD:y1 + PAD, x0 - PAD:x1 + PAD]
    a = np.clip((PAPER_LEVEL - sub) / (PAPER_LEVEL - INK_LEVEL), 0, 1)
    a[a < FLOOR] = 0.0                       # ό,τι μένει από τον κόκκο
    return np.clip((a - FLOOR) / (1 - FLOOR), 0, 1)


def write_logos():
    a = logo_alpha()
    h, w = a.shape
    rgba = np.zeros((h, w, 4), np.uint8)
    rgba[..., 3] = (a * 255).astype(np.uint8)
    im = Image.fromarray(rgba, "RGBA").resize((OUT_W, round(OUT_W * h / w)), Image.LANCZOS)

    # Κβαντισμός του alpha σε 16 στάθμες: ~4× μικρότερο PNG, χωρίς ορατή διαφορά.
    alpha = im.split()[3].point(lambda v: (v // 16) * 17)
    flat = Image.new("L", im.size)

    for name, rgb in (("logo.png", INK), ("logo-light.png", LIGHT)):
        ch = [flat.point(lambda v, c=c: c) for c in rgb]
        Image.merge("RGBA", (*ch, alpha)).save(IMG / name, optimize=True)
        print(name, im.size, (IMG / name).stat().st_size // 1024, "KB")


def write_photo():
    p = Image.open(PHOTO_SRC).convert("RGB")
    p.resize((1400, round(1400 * p.height / p.width)), Image.LANCZOS).save(
        IMG / "grafeio.jpg", quality=84, optimize=True, progressive=True)
    w, h = p.size
    th = round(w * 3 / 4)
    top = round((h - th) * 0.42)
    p.crop((0, top, w, top + th)).resize((900, 675), Image.LANCZOS).save(
        IMG / "grafeio-43.jpg", quality=84, optimize=True, progressive=True)
    print("grafeio.jpg / grafeio-43.jpg")


def write_og():
    og = Image.new("RGB", (1200, 675), "#17201e")
    logo = Image.open(IMG / "logo-light.png")
    lw = 780
    logo = logo.resize((lw, round(lw * logo.height / logo.width)), Image.LANCZOS)
    og.paste(logo, ((1200 - lw) // 2, (675 - logo.height) // 2 - 26), logo)
    ImageDraw.Draw(og).rectangle([(510, 470), (690, 472)], fill="#7fc8b2")
    og.save(IMG / "og-image.jpg", quality=88, optimize=True, progressive=True)
    print("og-image.jpg")


if __name__ == "__main__":
    IMG.mkdir(parents=True, exist_ok=True)
    write_logos()
    write_photo()
    write_og()
