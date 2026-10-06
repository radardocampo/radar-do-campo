---
name: garimpo-coleta-links-chrome
description: "Truques do garimpo de 2026-09-28 (Ronaldo/Oslo) - limite de saída do javascript_tool, busca do Instagram, metadados em lote, vídeo com título enganoso"
metadata:
  node_type: memory
  type: reference
  originSessionId: 33df6bff-c252-4044-837e-798c282c03e3
  modified: 2026-09-28T14:15:54.776Z
---

- O `javascript_tool` do Claude in Chrome trunca a saída em ~1000 caracteres: guardar os links no `localStorage` e devolver em lotes de ~27 `usuario/id` (sem legenda), depois puxar legenda/duração/data com `yt-dlp --skip-download --print` num arquivo (212 links em poucos minutos).
- Busca do Instagram por palavra-chave (`/explore/search/keyword/?q=`) com 3+ palavras volta "Nenhum resultado"; com 2 palavras ("cristiano noruega") funciona.
- No X, extrair `article` → link `/status/` + `[data-testid=tweetText]` + presença de `<video>` resolve a triagem sem abrir post a post.
- Vídeo de torcida postado no dia com título genérico ("ULLEVAAL ERUPTED! Opening Ceremony") era do jogo ANTERIOR no mesmo estádio (Noruega x Dinamarca) — conferir bandeiras/uniformes no gramado, não só a data de upload. Ver [[garimpo-download-sem-cookies]].
- faster-whisper modelo small em CPU leva ~20 min para 16 min de coletiva.
