---
name: comparacao-lote-2026-10-27
description: "Comparação de 27/10 (CR7/Girotto, Toney, Neymar Lei Vini, Piqué/Mbappé, Yamal) com analisa_capcut.py; capcut_projeto passou a levar desfoque, setas e música até o fim"
metadata:
  node_type: memory
  type: project
  originSessionId: 2e9ab691-c77d-4de0-98fd-cdf2a4fb6e73
  modified: 2026-10-27T17:37:28.560Z
---

Em 2026-10-27, a pedido dele ("bem minucioso, cada detalhe"), comparei os 5 vídeos de 24–27/10 refinados no CapCut. Ficaram em `<job>/_montagem/cmp/` (analise.txt, diff.txt, pares*.jpg, comparado.txt). Viraram a "Décima sexta rodada" da skill HUB (versão 2026-10-27). O Hinestroza (25/10) não foi editado nem exportado: não marquei como comparado.

Achado principal: metade dos zooms dele eram para esconder marca, porque o `borrar` e as setas da EDL não iam para o rascunho do CapCut. Corrigi o `capcut_projeto.py`: faixa DESFOQUE com cópia, máscara e Desfocar; faixa SETAS em PNG; 2ª trilha até ~1s antes do fim; virada da música no shot `"revelacao": true`. Conferi no CapCut com um rascunho de teste, que depois foi para a Lixeira.

Outras lições:
- gancho no pico físico (Neymar), começando mais perto do pico (Piqué), literal com contexto (Yamal);
- close de cabeça e ombros, não da testa ao queixo;
- punch-in no dado lido e no gesto nomeado;
- câmera lenta progressiva no ponto da polêmica (CR7);
- tradução de legenda estrangeira na tela (Toney);
- caixa do borrar errada (FIFA+) e o "g" da ge sobrando.

**Why:** aprendizado diário pedido por ele.
**How to apply:** a próxima comparação começa depois de 27/10, usando `analisa_capcut.py` + `pares_quadros.py`. Antes de virar regra, confira se o zoom dele não era só para esconder marca. Ver [[comparacao-lote-2026-10-23]] e [[capcut-rascunho-editavel]].
