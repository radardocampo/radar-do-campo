# -*- coding: utf-8 -*-
"""Descobre de qual clipe da biblioteca veio cada trecho de um video montado.
Use quando o usuario mostrar a montagem que ele fez a mao com o mesmo material:
revela quais clipes/trechos ele escolheu (inclusive os que a montagem automatica ignorou).
Correlacao normalizada em miniaturas, tolerante a zoom/reenquadramento.

uso (rodar dentro da pasta do job):
  python casar_fontes.py "<video montado>.mp4"
gera <job>/fontes_ref.json e imprime os trechos agrupados por clipe de origem.
"""
import subprocess, glob, os, json, sys
import numpy as np

TW, TH = 24, 42
REF = sys.argv[1]
# o json vai para a pasta do job (nunca para "Videos prontos" do job, que so guarda os 4 videos)
_d = os.path.dirname(os.path.abspath(REF))
JOB = os.path.dirname(_d) if os.path.basename(_d).lower() == "videos prontos" else _d
from pasta_job import dentro_do_job
SAIDA_JSON = dentro_do_job(os.path.join(JOB, "fontes_ref.json"))

def thumbs(path, fps):
    """frames 9:16 (crop central) em cinza, 96x170"""
    vf = (f"fps={fps},crop='min(iw,ih*9/16)':'min(ih,iw*16/9)',"
          f"scale=96:170,format=gray")
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", vf,
                          "-f", "rawvideo", "-"], capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.uint8).reshape(-1, 170, 96).astype(np.float32)

def reduz(img):
    from PIL import Image
    return np.asarray(Image.fromarray(img).resize((TW, TH), Image.BILINEAR), dtype=np.float32)

def norm(v):
    v = v.reshape(v.shape[0], -1)
    v = v - v.mean(1, keepdims=True)
    return v / (np.linalg.norm(v, axis=1, keepdims=True) + 1e-6)

def variantes(img):
    """o frame inteiro + recortes com zoom em 9 posicoes"""
    out = [reduz(img)]
    H, W = img.shape
    for z in (1.35, 1.8):
        h, w = int(H / z), int(W / z)
        for fy in (0.0, 0.5, 1.0):
            for fx in (0.0, 0.5, 1.0):
                y, x = int((H - h) * fy), int((W - w) * fx)
                out.append(reduz(img[y:y + h, x:x + w]))
    return out

arquivos = sorted(set(glob.glob("clipes/*.mp4") + glob.glob("clipes/apoio/*.mp4") +
                      glob.glob("clipes/_extras/*.mp4") + glob.glob("clipes/_rejeitados/*.mp4") +
                      glob.glob("clipes/_duplicados/*.mp4")))
vecs, idx = [], []
for a in arquivos:
    fr = thumbs(a, 2)
    for i, f in enumerate(fr):
        for v in variantes(f):
            vecs.append(v); idx.append((a.replace("\\", "/"), i / 2.0))
    print(f"  {len(fr):4d} frames  {a}", file=sys.stderr)
L = norm(np.stack(vecs))

ref = thumbs(REF, 2)
R = norm(np.stack([reduz(f) for f in ref]))
S = R @ L.T
res = []
for i in range(len(ref)):
    j = int(S[i].argmax())
    res.append({"t": i / 2.0, "clip": idx[j][0], "src_t": idx[j][1], "score": round(float(S[i, j]), 3)})
json.dump(res, open(SAIDA_JSON, "w", encoding="utf-8"), indent=0, ensure_ascii=False)

# agrupa trechos consecutivos do mesmo clipe
atual = None
for r in res:
    nome = os.path.basename(r["clip"]) if r["score"] > 0.55 else "(sem match confiavel)"
    if atual and atual["nome"] == nome:
        atual["fim"] = r["t"] + 0.5; atual["sc"].append(r["score"]); atual["src"].append(r["src_t"])
    else:
        if atual: print_linha = True
        if atual:
            print(f"{atual['ini']:5.1f}-{atual['fim']:5.1f}s  {atual['nome']:<66} src {min(atual['src']):5.1f}-{max(atual['src']):5.1f}s  score {np.mean(atual['sc']):.2f}")
        atual = {"nome": nome, "ini": r["t"], "fim": r["t"] + 0.5, "sc": [r["score"]], "src": [r["src_t"]]}
print(f"{atual['ini']:5.1f}-{atual['fim']:5.1f}s  {atual['nome']:<66} src {min(atual['src']):5.1f}-{max(atual['src']):5.1f}s  score {np.mean(atual['sc']):.2f}")
