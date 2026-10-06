---
name: garimpo-download-sem-cookies
description: "No PC do usuário, cookies do Chrome/Edge falham no yt-dlp, mas TikTok e YouTube baixam sem cookies"
metadata:
  node_type: memory
  type: reference
  originSessionId: 28d61b0f-8ec4-43d3-8538-39bc650fdb15
  modified: 2026-09-23T18:52:32.161Z
---

Em 2026-09-23 (garimpo da camisa amarela), `--cookies-from-browser chrome` falhou ("Could not copy Chrome cookie database", Chrome aberto) e `edge` falhou com DPAPI; não há Firefox instalado. Mesmo assim TikTok e YouTube baixaram normalmente **sem** cookies (o job do Carrascal, de 2026-09-22, também baixou só do TikTok).

Um 403 esporádico no YouTube se resolveu repetindo com `--retries 5 --fragment-retries 10`; `player_client=tv,web_safari` piorou ("page needs to be reloaded").

A busca do TikTok funciona pelo Claude in Chrome (sessão logada) extraindo `a[href*="/video/"]` via javascript; o browser embutido não carregou os resultados.

Em 2026-09-25 (Austrália x Brasil), 13 de 13 posts do X baixaram sem cookies; um vídeo longo do YouTube (APT Sports) falhou repetidamente por conexão cortada ("bytes read, more expected"), mesmo em 720p.

**How to apply:** no [[garimpo-de-videos]], não trave nos cookies — tente sem cookies primeiro para TikTok/YouTube; Instagram/Facebook/X continuam dependendo de cookies (pedir para fechar o Chrome se precisar).
