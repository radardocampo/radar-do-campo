---
name: video-final-sempre-60s
description: "Short nunca pode fechar abaixo de 60s (vídeo final, depois do corte de pausas+loop); acima de 60 é aceito (73s aprovado em 15/10); roteiro ~255 palavras"
metadata:
  node_type: memory
  type: feedback
  originSessionId: fc57a633-b005-4be0-8131-efb3fe58574d
  modified: 2026-10-18T22:20:49.764Z
---

Regra atual (2026-10-15): o vídeo final **não pode ficar abaixo de 60 segundos**. Acima de 60 tudo bem: no Endrick x Roma a narração deu 73,9s depois do corte de pausas e ele disse "pode ficar em 73 segundos mesmo, o que não pode é ficar abaixo de 60".

Origem: em 2026-10-13 (Pulgar/Fla-Flu) o roteiro de 231 palavras virou 54,8s finais e ele reclamou ("preciso que feche sempre com 60 segundos; se não for possível, peça pra eu gerar novamente ou você ajusta o roteiro").

**Why:** a montagem corta as pausas (não acelera) e o loop corta a frase-ponte (~2,5–3s), então o roteiro encolhe ~10%; vídeo curto demais é o problema, não o longo.

**How to apply:**
- Ao escrever roteiro: mirar ~255 palavras no texto do AI Studio. A taxa da voz varia: Pulgar ~4,0 pal/s depois do corte de pausas; Endrick x Roma 3,44 pal/s. Errar para mais, nunca para menos.
- Na montagem, depois do `narracao.py` + `loop_final.py`: se a duração final ficar **abaixo de 60s**, primeiro alongar as respirações com a mesma narração (`--manter` de 0,12 até ~0,2s; ganho ≈ nº de emendas × diferença). Em 2026-10-18 (Andreas) eu parei e pedi narração nova para 59,2s, e ele respondeu "ajuste os cortes para que fique em 60 segundos com essa mesmo": `--manter 0.17` nas 25 emendas deu 60,19s. Só se nem assim chegar a 60, parar e propor frase a acrescentar (só com fato confirmado) para ele gerar de novo. Acima de 60s, seguir sem perguntar.
- Roteiro de 235 palavras deu 59,2s (Andreas): mirar 255–265 no texto do AI Studio.
- Desde 2026-10-18 a regra está nas skills (montagem Passo 1; garimpo-de-temas Passo 11 com 255–265 palavras).
- Relacionado: [[narracao-feita-no-ai-studio]], [[narracao-le-rotulos-do-roteiro]].
