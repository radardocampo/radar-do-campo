---
name: entrega-2-arquivos-sem-logo
description: desde 2026-10-21 a montagem entrega só <apelido>-com-legenda e <apelido>-sem-legenda, sem logo do canal; acabaram TIKTOK/YOUTUBE/com-legenda-sem-marca/5º com SFX
metadata:
  type: feedback
---

Pedido do usuário em 2026-10-21: tirar da entrega o vídeo para TikTok e o vídeo para YouTube. Ficam só `<apelido>-com-legenda.mp4` e `<apelido>-sem-legenda.mp4` em `Videos prontos/`, nenhum com logo. Ele deixou de usar a logo do canal.

**Why:** ele sempre abre no CapCut, refina e renderiza a versão final de lá; só usa a entrega final dele.
**How to apply:** `render_final.py` (HUB 2026-10-21b) já gera só os 2; o rascunho é `_montagem/render/rascunho.mp4`. SFX vai só na faixa do rascunho do CapCut (não há mais 5º arquivo). O `capcut_projeto.py` não herda as faixas de logo do modelo. Substitui a parte de entrega de [[skill-montagem-versao-nova-local]] e [[montagem-versao-extra-com-sfx]].
