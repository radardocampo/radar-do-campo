---
name: python-store-nao-le-appdata-roaming
description: O python do Windows (Microsoft Store) não enxerga scripts das skills em AppData\Roaming; copiar antes de rodar
metadata:
  node_type: memory
  type: reference
  originSessionId: 922ce71e-6a5d-4bb7-989f-8616afd51959
  modified: 2026-09-25T21:12:17.801Z
---

O `python` desta máquina é o da Microsoft Store, que roda isolado e dá "No such file" para scripts em `C:\Users\bruno\AppData\Roaming\Claude\...\skills\...`. Em 2026-09-25 isso quebrou a skill `watch` e o `folha_contato.py` do garimpo.

Solução: copiar a pasta `scripts/` da skill para a pasta do job (garimpo) ou para o scratchpad (watch) e rodar a cópia. O `watch.py` também falha na extração de quadros porque o ffmpeg local não aceita `-vsync`. Nesse caso, extraia os quadros direto com `ffmpeg -vf fps=...,tile=...`. As legendas que ele baixa continuam servindo.

Relacionado: [[garimpo-download-sem-cookies]].
