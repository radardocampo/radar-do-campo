# -*- coding: utf-8 -*-
"""Mede movimento REAL de um clipe, descontando zoom/pan (foto com Ken Burns do editor da fonte).
Para cada par de quadros (passo --passo s) estima a transformacao de semelhanca (ORB + RANSAC),
alinha o quadro seguinte ao anterior e mede o residuo. Residuo baixo = imagem parada (mesmo que tenha zoom).

uso: python movimento_real.py <video> [--ini 0] [--fim <s>] [--passo 0.2] [--limiar 4]
saida: uma linha por segundo:  t  residuo  (FOTO se residuo < limiar)
Origem: Tarkowski 07/11/2026 - o clipe @sabulaug256 era foto com zoom e o YDIF contou o zoom como movimento.
"""
import argparse, cv2, numpy as np
ap = argparse.ArgumentParser(); ap.add_argument("video")
ap.add_argument("--ini", type=float, default=0); ap.add_argument("--fim", type=float)
ap.add_argument("--passo", type=float, default=0.2); ap.add_argument("--limiar", type=float, default=4.0)
ap.add_argument("--resumo", action="store_true", help="so as faixas FOTO/VIDEO")
a = ap.parse_args()
cap = cv2.VideoCapture(a.video); fps = cap.get(cv2.CAP_PROP_FPS) or 30
dur = cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps; fim = min(a.fim or dur, dur)
orb = cv2.ORB_create(1500); bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
def quadro(t):
    cap.set(cv2.CAP_PROP_POS_MSEC, t * 1000); ok, f = cap.read()
    if not ok: return None
    g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY); h, w = g.shape; s = 480 / max(h, w)
    return cv2.resize(g, (int(w * s), int(h * s)))
res = []; t = a.ini; prev = quadro(t)
while t + a.passo < fim and prev is not None:
    cur = quadro(t + a.passo)
    if cur is None: break
    k1, d1 = orb.detectAndCompute(prev, None); k2, d2 = orb.detectAndCompute(cur, None)
    r = float(np.mean(cv2.absdiff(prev, cur)))
    if d1 is not None and d2 is not None and len(k1) > 20 and len(k2) > 20:
        m = bf.match(d1, d2)
        if len(m) > 15:
            p1 = np.float32([k1[x.queryIdx].pt for x in m]); p2 = np.float32([k2[x.trainIdx].pt for x in m])
            M, _ = cv2.estimateAffinePartial2D(p2, p1, method=cv2.RANSAC, ransacReprojThreshold=2)
            if M is not None:
                al = cv2.warpAffine(cur, M, (prev.shape[1], prev.shape[0]))
                mask = cv2.warpAffine(np.ones_like(cur) * 255, M, (prev.shape[1], prev.shape[0])) > 0
                mask = cv2.erode(mask.astype(np.uint8), np.ones((9, 9), np.uint8)) > 0
                if mask.sum() > 1000: r = float(np.mean(cv2.absdiff(prev, al)[mask]))
    res.append((t, r)); prev = cur; t += a.passo
if a.resumo:
    seg = []
    for t, r in res:
        k = "FOTO" if r < a.limiar else "VIDEO"
        if seg and seg[-1][0] == k: seg[-1][2] = t + a.passo
        else: seg.append([k, t, t + a.passo])
    print(" | ".join(f"{k} {i:.1f}-{f:.1f}" for k, i, f in seg))
else:
    for t, r in res: print(f"{t:6.1f} {r:5.1f} {'FOTO' if r < a.limiar else ''}")
