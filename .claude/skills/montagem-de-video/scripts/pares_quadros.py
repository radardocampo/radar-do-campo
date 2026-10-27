"""Mosaico nosso x dele nos tempos que o analisa_capcut.py apontou (4 pares por linha, com rotulo da frase).
Uso: pares_quadros.py <nosso sem-legenda>.mp4 <exportado dele>.mp4 <job>/_montagem/cmp/pares.jpg 0.5,3.2,... "rot1|rot2|..."
"""
import subprocess, sys, io
from PIL import Image, ImageDraw, ImageFont
nosso, dele, out, ts = sys.argv[1], sys.argv[2], sys.argv[3], [float(x) for x in sys.argv[4].split(",")]
rots = sys.argv[5].split("|") if len(sys.argv) > 5 else [""] * len(ts)
W, H = 216, 384
def fr(p, t):
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", p, "-frames:v", "1", "-vf", f"scale={W}:{H}", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True)
    try: return Image.open(io.BytesIO(r.stdout)).convert("RGB")
    except Exception: return Image.new("RGB", (W, H), "gray")
cols = 4
n = len(ts); rows = (n + cols - 1) // cols
cw, ch = 2 * W + 8, H + 34
img = Image.new("RGB", (cols * cw + (cols - 1) * 12, rows * ch), "white")
try: f = ImageFont.truetype("arial.ttf", 13)
except Exception: f = ImageFont.load_default()
d = ImageDraw.Draw(img)
for i, t in enumerate(ts):
    x, y = (i % cols) * (cw + 12), (i // cols) * ch
    img.paste(fr(nosso, t), (x, y + 30)); img.paste(fr(dele, t), (x + W + 8, y + 30))
    d.text((x, y), f"{t:.2f}s  NOSSO | DELE", fill="black", font=f)
    d.text((x, y + 15), rots[i][:62] if i < len(rots) else "", fill="darkred", font=f)
img.save(out, quality=82)
print(out, img.size)
