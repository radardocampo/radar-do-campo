"""Compara draft_content.json original (gerado) x o salvo pelo usuario. Uso: cmp_draft.py orig.json dele.json"""
import json, sys
def load(p):
    d = json.load(open(p, encoding="utf-8"))
    mats = {}
    for k, v in d.get("materials", {}).items():
        if isinstance(v, list):
            for m in v:
                if isinstance(m, dict) and "id" in m:
                    mats[m["id"]] = (k, m)
    return d, mats
def nome(seg, mats):
    k, m = mats.get(seg.get("material_id"), ("?", {}))
    n = m.get("path") or m.get("name") or m.get("material_name") or ""
    if k == "texts":
        try: n = json.loads(m.get("content", "{}")).get("text", "")[:30]
        except Exception: n = "txt"
    return k, n.replace("\\", "/").split("/")[-1][:40]
def segs(d, mats):
    out = []
    for ti, t in enumerate(d["tracks"]):
        tn = t.get("name") or t.get("type")
        for s in t["segments"]:
            k, n = nome(s, mats)
            c = s.get("clip") or {}
            kf = []
            for g in s.get("common_keyframes", []):
                for f in g.get("keyframe_list", []):
                    kf.append((g.get("property_type", "")[-12:], round(f["time_offset"] / 1e6, 2), [round(x, 2) for x in f.get("values", [])]))
            out.append(dict(tr=f"{ti}:{tn}:{t.get('type')}", k=k, n=n,
                st=round(s["target_timerange"]["start"] / 1e6, 2), du=round(s["target_timerange"]["duration"] / 1e6, 2),
                src=round((s.get("source_timerange") or {}).get("start", 0) / 1e6, 2), sp=round(s.get("speed", 1), 2),
                sc=round((c.get("scale") or {}).get("x", 1), 2), tx=round((c.get("transform") or {}).get("x", 0), 2), ty=round((c.get("transform") or {}).get("y", 0), 2),
                vol=round(s.get("volume", 1), 2), vis=s.get("visible", True), kf=kf,
                fx=len(s.get("extra_material_refs", []))))
    return out
a, ma = load(sys.argv[1]); b, mb = load(sys.argv[2])
print("faixas orig:", [(t.get("name"), t.get("type"), len(t["segments"]), t.get("attribute")) for t in a["tracks"]])
print("faixas dele:", [(t.get("name"), t.get("type"), len(t["segments"]), t.get("attribute")) for t in b["tracks"]])
print("dur", a["duration"] / 1e6, b["duration"] / 1e6)
A = segs(a, ma); B = segs(b, mb)
key = lambda s: (s["k"], s["n"], s["src"])
ia = {}
for s in A: ia.setdefault(key(s), []).append(s)
campos = ["st", "du", "sp", "sc", "tx", "ty", "vol", "vis", "kf"]
for s in B:
    if s["k"] == "texts": continue
    l = ia.get(key(s))
    if not l:
        print(f"NOVO  {s['tr']} {s['n']} t={s['st']}+{s['du']} src={s['src']} sp={s['sp']} sc={s['sc']} pos=({s['tx']},{s['ty']}) vol={s['vol']} kf={s['kf'][:6]}")
        continue
    o = l.pop(0)
    dif = {c: (o[c], s[c]) for c in campos if o[c] != s[c]}
    if dif:
        if "kf" in dif: dif["kf"] = (o["kf"][:6], s["kf"][:6])
        print(f"MUDOU {s['tr']} {s['n']} t={s['st']}: {dif}")
for l in ia.values():
    for o in l:
        if o["k"] != "texts":
            print(f"SAIU  {o['tr']} {o['n']} t={o['st']}+{o['du']} src={o['src']}")
ta = [s for s in A if s["k"] == "texts"]; tb = [s for s in B if s["k"] == "texts"]
print("textos:", len(ta), len(tb), "| dele (amostra):", [(s["n"], s["st"]) for s in tb if s["n"] not in {x["n"] for x in ta}][:15])
