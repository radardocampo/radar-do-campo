# -*- coding: utf-8 -*-
"""Apaga marca d'agua de terceiros (WAMO, ge, sportv, Paramount+...) clonando textura da propria
cena, quadro a quadro, como o carimbo do Photoshop: copia um pedaco vizinho (mesma altura na
arquibancada/gramado), ajusta cor pelo anel em volta e mistura com borda suave. Nao deixa o borrao
do delogo.

uso (normalmente chamado pelo prep_shots.py):
  python limpar_marcas.py <entrada.mp4> <saida.mp4> '<json caixas>'
caixas: [[x, y, larg, alt], ...] ou [{"box": [x, y, larg, alt], "de": "esq|dir|baixo|cima|cor"}, ...]
em fracao do quadro. Sem "de", tenta esquerda, direita, baixo, cima (o primeiro que couber).
"cor" pinta com a cor media do entorno: use em area lisa (telao, placa, ceu), onde clonar
copiaria letras ou rostos vizinhos.
"""
import json, subprocess, sys
import cv2
import numpy as np


def preparar(caixas, w, h):
    out = []
    for c in caixas:
        if isinstance(c, dict):
            b, de = c["box"], c.get("de")
        else:
            b, de = c, None
        x, y, bw, bh = int(b[0] * w), int(b[1] * h), int(b[2] * w), int(b[3] * h)
        m = max(6, int(0.35 * min(bw, bh)))                     # margem de mistura
        rx0, ry0 = max(0, x - m), max(0, y - m)
        rx1, ry1 = min(w, x + bw + m), min(h, y + bh + m)
        rw, rh = rx1 - rx0, ry1 - ry0
        cand = {"esq": (-(rw + 4), 0), "dir": (rw + 4, 0), "baixo": (0, rh + 4), "cima": (0, -(rh + 4))}
        ordem = [de] if de else ["esq", "dir", "baixo", "cima"]
        if de == "cor":
            dx = dy = None
        for d in ([] if de == "cor" else ordem):
            dx, dy = cand[d]
            if 0 <= rx0 + dx and rx1 + dx <= w and 0 <= ry0 + dy and ry1 + dy <= h:
                break
        else:
            if de != "cor":
                sys.exit(f"ERRO: nao ha area limpa ao redor da caixa {b}")
        # mascara cheia (1,0) em toda a caixa: a borda suave fica so do lado de FORA.
        # (antes o desfoque centrado na borda deixava a marca 50% visivel nas beiradas)
        mask = np.zeros((rh, rw), np.float32)
        e = m // 2
        mask[max(0, y - ry0 - e):y - ry0 + bh + e, max(0, x - rx0 - e):x - rx0 + bw + e] = 1.0
        k = m | 1
        mask = cv2.GaussianBlur(mask, (k * 2 + 1, k * 2 + 1), m / 4.0)
        mask[y - ry0:y - ry0 + bh, x - rx0:x - rx0 + bw] = 1.0
        mask = np.clip(mask, 0, 1)
        anel = (mask > 0.02) & (mask < 0.6)                      # onde o original ainda aparece
        out.append((rx0, ry0, rx1, ry1, dx, dy, mask[..., None], anel))
    return out


def limpar(fr, prep):
    for rx0, ry0, rx1, ry1, dx, dy, mask, anel in prep:
        alvo = fr[ry0:ry1, rx0:rx1].astype(np.float32)
        if dx is None:                                          # modo "cor": area lisa
            fonte = np.empty_like(alvo); fonte[:] = np.median(alvo[anel], 0)
        else:
            fonte = fr[ry0 + dy:ry1 + dy, rx0 + dx:rx1 + dx].astype(np.float32)
        if dx is not None and anel.any():                                          # casa a cor com o entorno
            fonte += alvo[anel].mean(0) - fonte[anel].mean(0)
        fr[ry0:ry1, rx0:rx1] = np.clip(fonte * mask + alvo * (1 - mask), 0, 255).astype(np.uint8)
    return fr


def main(ent, sai, caixas):
    cap = cv2.VideoCapture(ent)
    w, h = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    prep = preparar(caixas, w, h)
    enc = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "bgr24",
                            "-s", f"{w}x{h}", "-r", f"{fps:.6f}", "-i", "-", "-c:v", "libx264", "-crf", "12",
                            "-preset", "veryfast", "-pix_fmt", "yuv420p", "-an", sai], stdin=subprocess.PIPE)
    while True:
        ok, fr = cap.read()
        if not ok:
            break
        enc.stdin.write(limpar(fr, prep).tobytes())
    cap.release(); enc.stdin.close(); enc.wait()
    if enc.returncode:
        sys.exit("ERRO: ffmpeg falhou ao gravar " + sai)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], json.loads(sys.argv[3]))
