---
name: montagem-versao-extra-com-sfx
description: "Quando houver efeitos sonoros, entregar um 5º arquivo (TikTok COM EFEITOS) além dos 4 padrão sem SFX"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 33df6bff-c252-4044-837e-798c282c03e3
  modified: 2026-09-28T22:25:42.349Z
---

Em 2026-09-28 (Ronaldo no banco), perguntado se queria SFX, o usuário pediu: além dos 4 vídeos de sempre, entregar mais um com os efeitos sonoros — "caso eu não goste eu apenas descarto e não preciso ter que pedir para tirar depois".

**Why:** ele quer decidir vendo, sem uma nova rodada para remover efeitos.
**How to apply:** os 4 arquivos padrão saem SEM SFX; renderizar à parte com `--sfx` (saída em `_montagem/com_sfx`) e copiar só `video pronto para o TIKTOK - COM EFEITOS SONOROS.mp4` para `Videos prontos/`. Ele também pediu transições (flash branco + soco de zoom nos momentos-chave e grade "arquivo" P&B nos trechos de outra época) — script `posfx.py` no `_montagem/scripts` do job. Ver [[skill-montagem-versao-nova-local]].

Em 2026-09-28 (Arrascaeta) ele pediu de novo SFX + as mesmas transições e disse que depois vai atualizar a skill de montagem para já fazer isso. Até lá: copiar `posfx.py` do job do Ronaldo para o `_montagem/scripts` do job, marcar `"fx"` na EDL e rodar `posfx.py` depois do `prep_shots.py` (as transições entram nos 4 arquivos; só o SFX fica no 5º).
