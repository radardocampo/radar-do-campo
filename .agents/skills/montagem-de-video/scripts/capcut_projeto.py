# -*- coding: utf-8 -*-
"""Gera um rascunho do CapCut (desktop) com a montagem da entrega, TUDO editavel no proprio CapCut,
partindo do rascunho-modelo do usuario (musica e configuracoes dele; as logos do modelo NAO entram desde 21/10/2026).

uso: python capcut_projeto.py "<pasta do video>" --nome "<nome do rascunho>" [--modelo "<rascunho modelo>"]
     (FECHE o CapCut antes: com ele aberto o indice root_meta_info.json e reescrito e o rascunho some)

Faixas:
  VIDEO   (principal) - os clipes brutos de cada shot: corte, velocidade, zoom/posicao (Transformar) e pan em keyframes;
            a cor da entrega (+18% saturacao, +12% contraste) vai gravada nas copias em _montagem/capcut_clipes,
            porque keyframe de Ajuste aparece no painel mas nao renderiza
  FLASH   - clarao branco (PNG com keyframe de opacidade) nos shots com fx flash/flashback_in; o "soco" de zoom
            fica como keyframe de escala no proprio shot
  CARDS/CARDS2 - destaques "icone" da EDL (cards de comentario, prints) como PNG editavel por cima
  FLASHBACK - filtro P&B do CapCut no trecho de outra data
  musica do modelo (trilhas e efeitos dele; as faixas de logo do modelo ficam de fora), cortados na duracao do video
  LEGENDA - texto karaoke: um trecho por palavra, palavra falada em amarelo (#FAFE05), fonte da entrega
  NARRACAO e SFX (SFX ligado: ele ligou a faixa nos dois primeiros rascunhos; --sfx-mudo deixa muda)

Keyframes: o CapCut grava o tempo do keyframe em TEMPO DA FONTE (o mesmo do source_timerange), nao relativo ao
inicio do segmento. Na 1a versao (Andreas/Bernal, 18/10/2026) gravei relativo: em clipe com entrada > 0 todos os
keyframes caiam antes do trecho e o pan e o soco ficavam parados (ele refez o pan do gol do Abde a mao).
"""
import argparse, json, os, subprocess, uuid, copy, shutil, glob
import pycapcut as cc
from pycapcut import trange
from pycapcut.keyframe import KeyframeProperty as KP
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("job"); ap.add_argument("--nome", required=True)
ap.add_argument("--modelo", help="rascunho do CapCut usado de base (padrao: o mais recente que nao seja Radar - ...)")
ap.add_argument("--raiz", default=os.path.join(os.environ.get("LOCALAPPDATA", ""), "CapCut", "User Data", "Projects", "com.lveditor.draft"))
ap.add_argument("--sfx-mudo", action="store_true", help="cria a faixa SFX muda (padrao: ligada)")
a = ap.parse_args()
job = os.path.abspath(a.job); M = os.path.join(job, "_montagem")
edl = json.load(open(os.path.join(M, "edl.json"), encoding="utf-8"))
W, H, FPS = 1080, 1920, 60
AMARELO = [250 / 255, 254 / 255, 5 / 255]
# mesma fonte da entrega (Montserrat ExtraBold Italic, instancia fixa do VF da skill)
FONTE = os.path.join(M, "assets", "Montserrat-ExtraBoldItalic.ttf").replace("\\", "/")

def probe(p):
    o = json.loads(subprocess.run(["ffprobe", "-v", "quiet", "-print_format", "json", "-show_streams", "-show_format", p],
                                  capture_output=True, text=True).stdout)
    v = [s for s in o["streams"] if s["codec_type"] == "video"][0]
    w, h = int(v["width"]), int(v["height"]); rot = 0
    for sd in v.get("side_data_list", []):
        if "rotation" in sd: rot = int(sd["rotation"])
    return (h, w) if abs(rot) % 180 == 90 else (w, h)

def us(t): return int(round(t * 1_000_000))

# ---------- modelo ----------
if a.modelo: modelo = os.path.join(a.raiz, a.modelo)
else:
    cand = [p for p in glob.glob(os.path.join(a.raiz, "*", "draft_content.json")) if not os.path.basename(os.path.dirname(p)).startswith(("Radar - ", "_tmp"))]
    modelo = os.path.dirname(max(cand, key=os.path.getmtime))
tpl = json.load(open(os.path.join(modelo, "draft_content.json"), encoding="utf-8"))
print("modelo:", os.path.basename(modelo))

# ---------- monta as faixas novas num rascunho temporario (pycapcut) ----------
tmpnome = "_tmp_radar_" + uuid.uuid4().hex[:6]
sc = cc.DraftFolder(a.raiz).create_draft(tmpnome, W, H, FPS)
sc.add_track(cc.TrackType.video, "VIDEO", relative_index=0)
sc.add_track(cc.TrackType.video, "FLASH", relative_index=1)
sc.add_track(cc.TrackType.video, "CARDS", relative_index=2)
sc.add_track(cc.TrackType.video, "CARDS2", relative_index=3)
sc.add_track(cc.TrackType.text, "LEGENDA")
sc.add_track(cc.TrackType.audio, "NARRACAO")
sc.add_track(cc.TrackType.audio, "SFX", mute=a.sfx_mudo)

# cor da entrega aplicada nos clipes (copias em _montagem/capcut_clipes): o resto fica editavel no CapCut
cdir = os.path.join(M, "capcut_clipes"); os.makedirs(cdir, exist_ok=True)
mats, tam = {}, {}
for k, p in edl["clips"].items():
    src = os.path.normpath(os.path.join(M, p)); dst = os.path.join(cdir, os.path.splitext(os.path.basename(src))[0] + ".mp4")
    if not os.path.exists(dst):
        foto = src.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
        subprocess.run(["ffmpeg", "-y", "-v", "error", *(["-loop", "1", "-framerate", "30", "-t", "12"] if foto else []), "-i", src,
                        "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2,eq=saturation=1.18:contrast=1.12", "-an",
                        "-c:v", "libx264", "-crf", "15", "-preset", "veryfast", "-pix_fmt", "yuv420p", dst], check=True)
    mats[k] = cc.VideoMaterial(dst); tam[k] = probe(dst)

def janela_centro(w, h, f, cx, cy):
    cw, ch = W / f, H / f
    x0 = min(max(cx * w - cw / 2, 0), max(w - cw, 0)); y0 = min(max(cy * h - ch / 2, 0), max(h - ch, 0))
    return (x0 + cw / 2) / w, (y0 + ch / 2) / h

branco = os.path.join(M, "flash_branco.png")
if not os.path.exists(branco): Image.new("RGB", (W, H), "white").save(branco)
mbranco = cc.VideoMaterial(branco)
SAT, CON = 0.18, 0.12          # cor da entrega (saturacao 1,18 / contraste 1,12)
dur_total = edl["shots"][-1]["tEnd"]
pb_ranges = []
for s in edl["shots"]:
    w, h = tam[s["clip"]]
    contain, cover = min(W / w, H / h), max(W / w, H / h)
    f = cover * s.get("zoom", 1.0); escala = f / contain
    dur = s["tEnd"] - s["tStart"]; rate = s.get("rate", 1.0)
    def pos(cx, cy):
        ex, ey = janela_centro(w, h, f, cx, cy)
        return (0.5 - ex) * w * f / (W / 2), (ey - 0.5) * h * f / (H / 2)
    s.setdefault("cx", 0.5); s.setdefault("cy", 0.5)
    tx, ty = pos(s["cx"], s["cy"])
    seg = cc.VideoSegment(mats[s["clip"]], trange(us(s["tStart"]), us(dur)),
                          source_timerange=trange(us(s["in"]), us(dur * rate)), speed=rate, volume=0.0,
                          clip_settings=cc.ClipSettings(scale_x=escala, scale_y=escala, transform_x=tx, transform_y=ty))
    def tf(t_shot):                              # tempo no shot (0..dur) -> tempo da fonte, como o CapCut le
        return us(s["in"] + min(max(t_shot, 0), dur) * rate)
    for k in s.get("keys") or []:
        kx, ky = pos(k[1], k[2] if len(k) > 2 else s["cy"]); t = tf(k[0])
        seg.add_keyframe(KP.position_x, t, kx); seg.add_keyframe(KP.position_y, t, ky)
    fx = s.get("fx")
    pb = fx in ("flashback", "flashback_in")
    if pb: pb_ranges.append((s["tStart"], s["tEnd"]))
    if fx in ("flash", "flashback_in"):         # soco de zoom: 1,12x -> 1x em 0,25s
        seg.add_keyframe(KP.uniform_scale, tf(0), escala * 1.12); seg.add_keyframe(KP.uniform_scale, tf(0.25), escala)
        fl = cc.VideoSegment(mbranco, trange(us(s["tStart"]), us(min(0.2, dur))))
        fl.add_keyframe(KP.alpha, 0, 0.95); fl.add_keyframe(KP.alpha, us(min(0.2, dur)) - 1, 0.0)
        sc.add_segment(fl, "FLASH")
    sc.add_segment(seg, "VIDEO")
    for kd, d in enumerate(s.get("destaque", [])):             # cards de comentario (PNG) por cima, editaveis
        if d.get("tipo") != "icone": continue
        t0 = min(d.get("t0", 0), dur); t1 = min(d.get("t1", dur), dur)
        cm = cc.VideoMaterial(d["arquivo"])
        sc.add_segment(cc.VideoSegment(cm, trange(us(s["tStart"] + t0), us(t1 - t0)),
                       clip_settings=cc.ClipSettings(scale_x=d.get("tam", 0.3), scale_y=d.get("tam", 0.3),
                                                     transform_y=(0.5 - d["y"]) * 2, transform_x=(d["x"] - 0.5) * 2)), "CARDS2" if kd else "CARDS")

# flashback em preto e branco: filtro do CapCut (editavel/removivel) no trecho de outra data
if pb_ranges:
    sc.add_track(cc.TrackType.filter, "FLASHBACK")
    ini_pb, fim_pb = min(r[0] for r in pb_ranges), max(r[1] for r in pb_ranges)
    sc.add_filter(cc.FilterType.褪色黑白, trange(us(ini_pb), us(fim_pb - ini_pb)), "FLASHBACK", intensity=100.0)
_nm = cc.AudioMaterial(os.path.join(M, "narracao_final.wav"))
sc.add_segment(cc.AudioSegment(_nm, trange(0, min(us(dur_total), _nm.duration))), "NARRACAO")
sfx_p = os.path.join(M, "sfx.json")
if os.path.exists(sfx_p):
    lst = sorted(json.load(open(sfx_p, encoding="utf-8")), key=lambda x: x["t"])
    for i, x in enumerate(lst):
        prox = lst[i + 1]["t"] if i + 1 < len(lst) else dur_total
        am = cc.AudioMaterial(x["arquivo"]); d = min(am.duration, us(prox - x["t"]))
        if d > 0: sc.add_segment(cc.AudioSegment(am, trange(us(x["t"]), d), volume=x.get("vol", 1.0)), "SFX")

# legenda: medida para ficar do tamanho da entrega (Montserrat 79px/2560 ~ 47-50% da largura em "todo mundo viu")
blocos = json.load(open(os.path.join(M, "blocos_legenda.json"), encoding="utf-8"))
pal = json.load(open(os.path.join(M, "palavras.json"), encoding="utf-8"))
estilo = cc.TextStyle(size=10.0, bold=False, italic=True, color=(1, 1, 1), align=1)
borda = cc.TextBorder(color=(0, 0, 0), width=25.0)
sombra = cc.TextShadow(color=(0, 0, 0), alpha=0.9, diffuse=25.0, distance=2.0, angle=-90.0)
pos_leg = cc.ClipSettings(transform_y=-(0.54 - 0.5) * 2)
destaques = {}
for bi, b in enumerate(blocos):
    if bi + 1 < len(blocos) and 0 < blocos[bi + 1]["ini"] - b["fim"] < 0.6:
        b = dict(b, fim=blocos[bi + 1]["ini"])
    toks = b["texto"].split()
    ws = [p for p in pal if b["ini"] - 0.02 <= p["ini"] < b["fim"] - 0.01]
    ini = ([b["ini"]] + [p["ini"] for p in ws[1:]]) if len(ws) == len(toks) else \
          [b["ini"] + i * (b["fim"] - b["ini"]) / len(toks) for i in range(len(toks))]
    fim = ini[1:] + [b["fim"]]; pc = 0
    for i, tok in enumerate(toks):
        a0 = b["texto"].index(tok, pc); pc = a0 + len(tok)
        if fim[i] - ini[i] < 0.02: continue
        tseg = cc.TextSegment(b["texto"], trange(us(ini[i]), us(min(fim[i], dur_total)) - us(ini[i])), font=cc.FontType.Montserrat,
                              style=copy.deepcopy(estilo), border=borda, shadow=sombra, clip_settings=copy.deepcopy(pos_leg))
        sc.add_segment(tseg, "LEGENDA"); destaques[tseg.material_id] = (a0, pc)
sc.save()
tmpdir = os.path.join(a.raiz, tmpnome)
d = json.load(open(os.path.join(tmpdir, "draft_content.json"), encoding="utf-8"))
shutil.rmtree(tmpdir)
for t in d["materials"]["texts"]:
    if t["id"] not in destaques: continue
    a0, a1 = destaques[t["id"]]; c = json.loads(t["content"]); base = c["styles"][0]; n = len(c["text"]); novos = []
    for r0, r1, am in ((0, a0, False), (a0, a1, True), (a1, n, False)):
        if r1 <= r0: continue
        st = copy.deepcopy(base); st["range"] = [r0, r1]
        if os.path.exists(FONTE): st["font"] = {"id": "", "path": FONTE}
        if am: st["fill"]["content"]["solid"]["color"] = AMARELO
        novos.append(st)
    c["styles"] = novos; t["content"] = json.dumps(c, ensure_ascii=False)
    if os.path.exists(FONTE): t["font_path"] = FONTE

# ---------- junta com o modelo: musica e efeitos dele, cortados na duracao ----------
D = us(dur_total)
out = copy.deepcopy(tpl)
for k, v in d["materials"].items():
    if isinstance(v, list): out["materials"].setdefault(k, []); out["materials"][k] = out["materials"][k] + v
novas = {t["name"]: t for t in d["tracks"]}
herdadas = []
for t in tpl["tracks"]:
    if t["type"] == "video": continue   # trilha vazia do modelo e as logos (lupa/YouTube): sem logo desde 21/10/2026
    segs = []
    for s in t["segments"]:
        st, du = s["target_timerange"]["start"], s["target_timerange"]["duration"]
        if st >= D: continue
        if st + du > D:
            nd = D - st; s = copy.deepcopy(s); sp = s.get("speed", 1.0) or 1.0
            s["target_timerange"]["duration"] = nd
            if s.get("source_timerange"): s["source_timerange"]["duration"] = int(nd * sp)
        segs.append(s)
    t = copy.deepcopy(t); t["segments"] = segs; herdadas.append(t)
    if t["type"] == "audio":                                        # trilha principal: ele baixa 0,34 -> 0,07-0,16 (21/10)
        for s in t["segments"]:
            if s.get("volume", 1.0) > 0.2: s["volume"] = 0.12
for t in herdadas:                                                 # logos acima do video e do flash
    for s in t["segments"]:
        if t["type"] == "video": s["render_index"] = (s.get("render_index") or 0) + 10
out["tracks"] = [novas["VIDEO"], novas["FLASH"]] + [novas[n] for n in ("CARDS", "CARDS2") if n in novas and novas[n]["segments"]] + ([novas["FLASHBACK"]] if "FLASHBACK" in novas else []) + [t for t in herdadas if t["type"] == "video"] + \
                [novas["NARRACAO"], novas["SFX"]] + [t for t in herdadas if t["type"] == "audio"] + \
                [t for t in herdadas if t["type"] not in ("video", "audio")] + [novas["LEGENDA"]]
out["duration"] = D
out["canvas_config"] = {**tpl["canvas_config"], "ratio": "9:16", "width": W, "height": H}

# ---------- grava: copia a pasta do modelo e troca o conteudo ----------
pasta = os.path.join(a.raiz, a.nome)
if os.path.exists(pasta): shutil.rmtree(pasta)
shutil.copytree(modelo, pasta, ignore=shutil.ignore_patterns(".locked", "subdraft", "*.bak", "template*.tmp", "draft_cover.jpg"))
alvos = [os.path.join(pasta, "draft_content.json")] + glob.glob(os.path.join(pasta, "Timelines", "*", "draft_content.json"))
for p in glob.glob(os.path.join(pasta, "Timelines", "*", "*")):
    if p.endswith((".bak", ".tmp")) or os.path.basename(p) == "draft_cover.jpg": os.remove(p)
for p in alvos: json.dump(out, open(p, "w", encoding="utf-8"), ensure_ascii=False)
mi = os.path.join(pasta, "draft_meta_info.json")
meta = json.load(open(mi, encoding="utf-8")); novo_id = str(uuid.uuid4()).upper()
meta.update({"draft_name": a.nome, "draft_id": novo_id, "draft_fold_path": pasta.replace("\\", "/"),
             "draft_root_path": a.raiz.replace("\\", "/"), "tm_duration": D})
json.dump(meta, open(mi, "w", encoding="utf-8"), ensure_ascii=False)

rm = os.path.join(a.raiz, "root_meta_info.json")
r = json.load(open(rm, encoding="utf-8"))
r["all_draft_store"] = [x for x in r["all_draft_store"] if x.get("draft_name") not in (a.nome, tmpnome)]
ref = [x for x in r["all_draft_store"] if x.get("draft_fold_path", "").rstrip("/").endswith(os.path.basename(modelo))]
ent = copy.deepcopy(ref[0] if ref else r["all_draft_store"][0]); fold = pasta.replace("\\", "/")
ent.update({"draft_fold_path": fold, "draft_json_file": fold + "/draft_content.json", "draft_cover": fold + "/draft_cover.jpg",
            "draft_name": a.nome, "draft_id": novo_id, "tm_duration": D, "draft_timeline_materials_size": 0})
r["all_draft_store"].insert(0, ent)
json.dump(r, open(rm, "w", encoding="utf-8"), ensure_ascii=False)
print(f"rascunho '{a.nome}': {len(edl['shots'])} shots, {len(destaques)} estados de legenda, {dur_total:.2f}s, "
      f"faixas herdadas do modelo: {[(t['type'], len(t['segments'])) for t in herdadas]}")
