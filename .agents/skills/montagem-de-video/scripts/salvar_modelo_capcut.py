# -*- coding: utf-8 -*-
"""Salva o MODELO FIXO do CapCut fora da pasta de projetos, a partir de um rascunho "Radar - ..." que ja tem a musica dele.

Por que existe (07/11/2026): o capcut_projeto.py usava como modelo "o projeto mais recente que nao comeca com
'Radar - '" (o "0417-copia... (15)"). Ele mantem so os 10 projetos mais recentes no CapCut; com 10 rascunhos
"Radar - ..." mais novos, o modelo saiu na limpeza e a proxima montagem quebraria. O modelo fixo fica em
HUB Radar do Campo\\Claude\\capcut-modelo\\Radar MODELO\\, fora da lista do CapCut, e o capcut_projeto.py usa ele por padrao.

uso: python salvar_modelo_capcut.py "Radar - <titulo de um rascunho com a musica certa>" [--virada 44.6]
  - fica so a musica (as faixas de audio sem nome: 2 trilhas + o impacto "Dramatic"); narracao, SFX, legenda,
    video, cards e filtros do video de origem saem, e os materiais sem uso tambem
  - a virada (fim da 1a trilha, Dramatic, entrada da 2a) volta para --virada (padrao 44,6 s, a posicao do modelo original)
  - nao copia a midia do rascunho (Resources, aigc_material, matting, imagens soltas): a pasta fica pequena
Para trocar a musica do canal: monte um rascunho com a musica nova, salve no CapCut e rode este script nele.
"""
import argparse, copy, json, os, shutil

ap = argparse.ArgumentParser()
ap.add_argument("origem", help='nome do rascunho de origem, ex.: "Radar - Tarkowski puxa cabelo e Lampard sem penalti"')
ap.add_argument("--virada", type=float, default=44.6)
ap.add_argument("--raiz", default=os.path.join(os.environ.get("LOCALAPPDATA", ""), "CapCut", "User Data", "Projects", "com.lveditor.draft"))
ap.add_argument("--destino", default=r"C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\HUB Radar do Campo\Claude\capcut-modelo\Radar MODELO")
a = ap.parse_args()
US = 1_000_000
src = os.path.join(a.raiz, a.origem)
d = json.load(open(os.path.join(src, "draft_content.json"), encoding="utf-8"))

musica = [t for t in d["tracks"] if t["type"] == "audio" and not t.get("name")]
duas = [t for t in musica if len(t["segments"]) == 2]
uma = [t for t in musica if len(t["segments"]) == 1]
if not (len(duas) == 1 and len(uma) == 1):
    raise SystemExit(f"a origem nao tem 2 trilhas + 1 impacto sem nome (achei {[len(t['segments']) for t in musica]}); escolha outro rascunho")
s1, s2 = sorted(duas[0]["segments"], key=lambda x: x["target_timerange"]["start"]); dram = uma[0]["segments"][0]
# devolve a virada para a posicao do modelo, guardando as distancias que o capcut_projeto.py usa
v = int(a.virada * US); delta = v - dram["target_timerange"]["start"]
for sg in (dram, s2): sg["target_timerange"]["start"] += delta
s1["target_timerange"]["duration"] += delta
s1["source_timerange"]["duration"] = int(s1["target_timerange"]["duration"] * (s1.get("speed") or 1))
d["tracks"] = [copy.deepcopy(duas[0]), copy.deepcopy(uma[0])]
fim = max(s["target_timerange"]["start"] + s["target_timerange"]["duration"] for t in d["tracks"] for s in t["segments"])
d["duration"] = fim

# materiais: so os que a musica usa
usados = set()
for t in d["tracks"]:
    for s in t["segments"]:
        usados.add(s["material_id"]); usados.update(s.get("extra_material_refs") or [])
for k, lst in d["materials"].items():
    if isinstance(lst, list): d["materials"][k] = [m for m in lst if m.get("id") in usados]

# pasta pequena: so as configuracoes do rascunho, sem midia nem cache
if os.path.exists(a.destino): shutil.rmtree(a.destino)
os.makedirs(a.destino)
PULA_DIR = {"Resources", "aigc_material", "matting", "smart_crop", "qr_upload", "subdraft", "video", "video_effect",
            "color_match", "adjust_mask", "agent", "common_attachment", "materials", "draft_settings"}
for n in os.listdir(src):
    p = os.path.join(src, n)
    if os.path.isdir(p):
        if n == "Timelines":   # project.json + uma pasta por timeline (so os .json e o draft.extra)
            os.makedirs(os.path.join(a.destino, "Timelines"), exist_ok=True)
            for tl in os.listdir(p):
                q = os.path.join(p, tl)
                if os.path.isfile(q):
                    if tl.endswith(".json"): shutil.copy2(q, os.path.join(a.destino, "Timelines", tl))
                    continue
                os.makedirs(os.path.join(a.destino, "Timelines", tl), exist_ok=True)
                for f in os.listdir(q):
                    if os.path.isfile(os.path.join(q, f)) and (f.endswith(".json") or f == "draft.extra"):
                        shutil.copy2(os.path.join(q, f), os.path.join(a.destino, "Timelines", tl, f))
        continue               # o resto (Resources, matting, aigc_material...) e midia/cache do video de origem
    if n.endswith((".jpg", ".png", ".bak", ".tmp")) or n.startswith("crypto_key_store"): continue
    shutil.copy2(p, os.path.join(a.destino, n))
alvos = [os.path.join(a.destino, "draft_content.json")]
tl_dir = os.path.join(a.destino, "Timelines")
if os.path.isdir(tl_dir):
    alvos += [os.path.join(tl_dir, tl, "draft_content.json") for tl in os.listdir(tl_dir)
              if os.path.exists(os.path.join(tl_dir, tl, "draft_content.json"))]
for p in alvos: json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False)
mi = os.path.join(a.destino, "draft_meta_info.json")
if os.path.exists(mi):
    meta = json.load(open(mi, encoding="utf-8")); meta["draft_name"] = "Radar MODELO"
    json.dump(meta, open(mi, "w", encoding="utf-8"), ensure_ascii=False)
tam = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(a.destino) for f in fs)
mats = {k: len(v) for k, v in d["materials"].items() if isinstance(v, list) and v}
print(f"modelo fixo salvo em {a.destino} ({tam / 1e6:.1f} MB) a partir de '{a.origem}'")
print(f"virada em {a.virada:.1f}s; faixas: {[len(t['segments']) for t in d['tracks']]}; materiais: {mats}")
