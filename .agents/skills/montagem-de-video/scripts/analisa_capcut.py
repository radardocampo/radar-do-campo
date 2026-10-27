"""Comparacao minuciosa (27/10/2026): o rascunho do CapCut que geramos x o que ele salvou, corte a corte, com a frase
narrada naquele trecho e a nota do shot na EDL. Mostra tambem mascaras, efeitos (Desfocar), animacoes, fades de audio,
textos novos e as faixas por cima (sobreposicoes, desfoques, setas), que o compara_capcut.py nao mostra.
Antes: regere o original em <job>/_montagem/cmp/capcut_orig (Passo 9).
Uso: analisa_capcut.py "<job>" "Radar - <titulo>"   (grava <job>/_montagem/cmp/analise.txt)
Cuidado ao ler: shot que ele so fechou o zoom pode ser um desfoque nosso que nao ia para o rascunho (antes de 27/10)."""
import json, os, sys
job, nome = sys.argv[1], sys.argv[2]
M = os.path.join(job, "_montagem")
R = os.path.join(os.environ["LOCALAPPDATA"], "CapCut", "User Data", "Projects", "com.lveditor.draft")
A = os.path.join(M, "cmp", "capcut_orig", nome, "draft_content.json")
B = os.path.join(R, nome, "draft_content.json")
edl = json.load(open(os.path.join(M, "edl.json"), encoding="utf-8"))
pal = json.load(open(os.path.join(M, "palavras.json"), encoding="utf-8"))

def fala(t0, t1):
    return " ".join(p["w"] for p in pal if p["fim"] > t0 + 0.02 and p["ini"] < t1 - 0.02)

def nota(t):
    for s in edl["shots"]:
        if s["tStart"] - 0.01 <= t < s["tEnd"] - 0.01:
            return f'#{s["id"]} {s["clip"]} in={s["in"]}: {s.get("nota", "")}'
    return ""

def load(p):
    d = json.load(open(p, encoding="utf-8"))
    mats = {}
    for k, v in d["materials"].items():
        if isinstance(v, list):
            for m in v:
                if isinstance(m, dict) and "id" in m: mats[m["id"]] = (k, m)
    return d, mats

def desc(s, mats, tr):
    k, m = mats.get(s.get("material_id"), ("?", {}))
    n = (m.get("path") or m.get("name") or m.get("material_name") or "").replace("\\", "/").split("/")[-1]
    if k == "texts":
        try: n = json.loads(m.get("content", "{}")).get("text", "")
        except Exception: pass
    c = s.get("clip") or {}
    st = s["target_timerange"]["start"] / 1e6; du = s["target_timerange"]["duration"] / 1e6
    src = (s.get("source_timerange") or {}).get("start", 0) / 1e6
    extra = []
    for r in s.get("extra_material_refs", []):
        kk, mm = mats.get(r, ("?", {}))
        if kk == "material_animations":
            for an in mm.get("animations", []):
                extra.append(f'anim:{an.get("type")}:{an.get("name")}:{an.get("duration",0)/1e6:.2f}s')
        elif kk in ("video_effects", "effects"):
            extra.append(f'efeito:{mm.get("name")}' + (f' {[(a.get("name") or a.get("adjust_key") or "?", round(a.get("value",0),2)) for a in mm.get("adjust_params",[])][:4]}' if mm.get("adjust_params") else ""))
        elif kk == "common_mask":
            cfg = mm.get("config", {})
            extra.append(f'mascara:{mm.get("name") or mm.get("resource_type")} cx={cfg.get("centerX",0):.2f} cy={cfg.get("centerY",0):.2f} w={cfg.get("width",0):.2f} h={cfg.get("height",0):.2f} feather={cfg.get("feather",0):.2f} inv={cfg.get("invert")}')
        elif kk == "audio_fades":
            extra.append(f'fade in={mm.get("fade_in_duration",0)/1e6:.2f} out={mm.get("fade_out_duration",0)/1e6:.2f}')
        elif kk == "audio_effects":
            extra.append(f'efeito_audio:{mm.get("name")}')
        elif kk == "transitions":
            extra.append(f'transicao:{mm.get("name")}:{mm.get("duration",0)/1e6:.2f}s')
        elif kk == "speeds" and mm.get("curve_speed"):
            extra.append("curva_vel")
    kf = []
    for g in s.get("common_keyframes", []):
        pt = g.get("property_type", "").replace("KFType", "")
        kf.append(pt + ":" + ",".join(f'{(f["time_offset"]/1e6):.2f}={[round(x,2) for x in f.get("values",[])]}' for f in g.get("keyframe_list", [])))
    crop = c.get("crop") or (m.get("crop") if isinstance(m, dict) else None)
    cr = ""
    if isinstance(crop, dict) and any(abs(crop.get(q, d)) > 1e-3 and abs(crop.get(q, d) - d) > 1e-3 for q, d in (("upper_left_x", 0), ("upper_left_y", 0), ("lower_right_x", 1), ("lower_right_y", 1))):
        cr = f' crop=({crop.get("upper_left_x",0):.2f},{crop.get("upper_left_y",0):.2f})-({crop.get("lower_right_x",1):.2f},{crop.get("lower_right_y",1):.2f})'
    return dict(tr=tr, k=k, n=n, st=st, du=du, src=src, sp=s.get("speed", 1), sc=(c.get("scale") or {}).get("x", 1),
                tx=(c.get("transform") or {}).get("x", 0), ty=(c.get("transform") or {}).get("y", 0), rot=c.get("rotation", 0),
                alpha=c.get("alpha", 1), vol=s.get("volume", 1), vis=s.get("visible", True), flip=(c.get("flip") or {}),
                kf=kf, extra=extra, cr=cr)

def segs(p):
    d, mats = load(p)
    out = []
    for ti, t in enumerate(d["tracks"]):
        tr = f'{ti}:{t.get("name") or "-"}:{t["type"]}{" MUDA" if t.get("attribute") else ""}'
        for s in t["segments"]:
            out.append(desc(s, mats, tr))
    return d, out

da, sa = segs(A); db, sb = segs(B)
fmt = lambda x: (f'{x["n"][:38]:38s} src={x["src"]:.2f} sp={x["sp"]:.2f} sc={x["sc"]:.2f} pos=({x["tx"]:.2f},{x["ty"]:.2f})'
                 + (f' rot={x["rot"]:.0f}' if abs(x["rot"]) > .5 else "") + (f' alpha={x["alpha"]:.2f}' if x["alpha"] < .99 else "")
                 + (" OCULTO" if not x["vis"] else "") + x["cr"] + (f' vol={x["vol"]:.2f}' if x["k"] in ("audios",) else "")
                 + (" kf[" + " | ".join(x["kf"]) + "]" if x["kf"] else "") + (" " + " ".join(x["extra"]) if x["extra"] else ""))
L = []
L.append(f"ANALISE {nome}\ndur orig {da['duration']/1e6:.2f}s  dele {db['duration']/1e6:.2f}s")
for lab, d in (("orig", da), ("dele", db)):
    L.append(f"faixas {lab}: " + "; ".join(f'{i}:{t.get("name") or "-"}:{t["type"]}({len(t["segments"])}){" muda" if t.get("attribute") else ""}' for i, t in enumerate(d["tracks"])))

# faixa principal de video: alinhar por tempo
va = [x for x in sa if x["tr"].startswith("0:")]; vb = [x for x in sb if x["tr"].startswith("0:")]
L.append("\n=== FAIXA PRINCIPAL (VIDEO), corte a corte ===")
cuts = sorted(set([round(x["st"], 2) for x in va + vb] + [round(da["duration"] / 1e6, 2)]))
def em(lst, t):
    for x in lst:
        if x["st"] - 0.02 <= t < x["st"] + x["du"] - 0.02: return x
for i in range(len(cuts) - 1):
    t0, t1 = cuts[i], cuts[i + 1]
    if t1 - t0 < 0.03: continue
    a, b = em(va, (t0 + t1) / 2), em(vb, (t0 + t1) / 2)
    same = a and b and a["n"] == b["n"] and abs(a["sp"] - b["sp"]) < .01 and abs(a["sc"] - b["sc"]) < .01 and abs(a["tx"] - b["tx"]) < .01 and abs(a["ty"] - b["ty"]) < .01 and a["kf"] == b["kf"] and a["extra"] == b["extra"] and abs((a["src"] - a["st"] * a["sp"]) - (b["src"] - b["st"] * b["sp"])) < .05 and a["vis"] == b["vis"]
    L.append(f'\n[{t0:6.2f}-{t1:6.2f}] {"igual" if same else "DIFERENTE"}  fala: "{fala(t0, t1)}"')
    L.append(f'   nota EDL: {nota((t0+t1)/2)}')
    if not same:
        L.append(f'   nosso: {fmt(a) if a else "-"}')
        L.append(f'   dele : {fmt(b) if b else "-"}')

L.append("\n=== OUTRAS FAIXAS (sobreposicoes, flash, cards, filtros, audio) ===")
for lab, ss in (("nosso", sa), ("dele", sb)):
    L.append(f"--- {lab}")
    for x in ss:
        if x["tr"].startswith("0:") or x["k"] == "texts": continue
        L.append(f'  {x["tr"]:22s} {x["st"]:6.2f}+{x["du"]:5.2f}  {fmt(x)}  | fala: "{fala(x["st"], x["st"]+x["du"])[:80]}"')
# legenda
ta = [x for x in sa if x["k"] == "texts"]; tb = [x for x in sb if x["k"] == "texts"]
dif = [(a, b) for a, b in zip(ta, tb) if a["n"] != b["n"] or abs(a["st"] - b["st"]) > .02 or abs(a["tx"] - b["tx"]) > .01 or abs(a["ty"] - b["ty"]) > .01 or abs(a["sc"] - b["sc"]) > .01]
L.append(f"\n=== LEGENDA: {len(ta)} x {len(tb)} trechos, {len(dif)} diferentes ===")
for a, b in dif[:30]:
    L.append(f'  {a["st"]:.2f} "{a["n"]}" ({a["tx"]:.2f},{a["ty"]:.2f},sc {a["sc"]:.2f}) -> {b["st"]:.2f} "{b["n"]}" ({b["tx"]:.2f},{b["ty"]:.2f},sc {b["sc"]:.2f})')
out = os.path.join(M, "cmp", "analise.txt")
open(out, "w", encoding="utf-8").write("\n".join(L))
print(out, len(L))
