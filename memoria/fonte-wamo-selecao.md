---
name: fonte-wamo-selecao
description: Perfil @canalwamo (WAMO) filma jogos da Seleção da arquibancada — melhor fonte de torcida para garimpo de jogos do Brasil
metadata:
  node_type: memory
  type: reference
  originSessionId: d926dd2f-45e1-4c62-a9bc-e947c66e26ef
  modified: 2026-09-29T21:02:02.813Z
---

No garimpo de Austrália 1x1 Brasil (2026-09-25), o perfil **@canalwamo** (TikTok e Instagram, marca "WAMO") tinha ~20 vídeos do jogo filmados da arquibancada em 1080x1920: aquecimento, entrada dos times, gol anulado, gols, e o único vídeo do Rayan cumprimentando o Hugo Souza (o payoff do roteiro). A ND+ usou o vídeo deles como fonte.

Busca por palavra-chave no TikTok não trouxe esses vídeos; foi preciso listar o perfil com `yt-dlp --flat-playlist --playlist-end 30 https://www.tiktok.com/@canalwamo` (o Chrome travou ao abrir o perfil).

Em 2026-09-29 (Endrick) o `yt-dlp` passou a falhar em `https://www.tiktok.com/@canalwamo` ("Unable to extract secondary user ID"). Funcionou pegar o `channel_id` de um vídeo dele (`--print "%(channel_id)s"`) e listar `tiktokuser:<channel_id>`.

**How to apply:** em [[garimpo-de-videos]] de jogo da Seleção, liste o perfil do canalwamo logo no começo. Marca WAMO discreta no topo do quadro; legenda do autor só nos 2-3s iniciais.
