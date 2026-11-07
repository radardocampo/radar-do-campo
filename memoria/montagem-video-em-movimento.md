---
name: montagem-video-em-movimento
description: "2026-11-07 Tarkowski — reclamou que a montagem \"ficou só imagem\"; todo shot tem que ser vídeo em movimento, imagem/quadro parado só se não existir vídeo do fato"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 028fba3d-95e6-4a6d-82cb-2e71c4af8473
  modified: 2026-11-07T13:24:05.984Z
---

Reclamação do usuário em 07/11/2026 sobre a montagem do Tarkowski/Lampard: "você usou apenas imagens, cadê os vídeos que a gente fazia antes? ... quero a montagem como era antes com vídeos, e imagens só quando é extremamente necessário". Ele gostou das mudanças de 06/11 ([[decisoes-skills-2026-11-06]]), mas não esperava que elas mudassem o resultado.

O que tinha saído parado: Lampard no banco (1,5 s quase sem movimento), gráfico do VAR por 3 s, Ballard em quadro congelado da fonte por 2,2 s, Moyes na coletiva quase estático, replays a 0,6x que parecem foto.

**Why:** o canal é de vídeo; trecho parado parece slideshow e derruba a retenção.
**How to apply:** em toda montagem, cada shot é vídeo em movimento do fato (coletiva = a pessoa falando/gesticulando; reação = take em que ela se mexe; regra/VAR = o lance ou o jogo andando). Quadro congelado, gráfico, card ou foto só quando não existe vídeo daquele fato, por ≤ ~1 s. Antes do rascunho, medir o movimento do corte (YDIF do ffmpeg, Passo 8 item 0 da skill, versão HUB 2026-11-07) e trocar o que estiver parado.

**2ª reclamação no mesmo dia:** "continuo com imagem que dão zoom... o gancho já começa com uma imagem no zoom". A fonte @sabulaug256 (e as janelas do @Topnews1) era foto com Ken Burns do editor; o YDIF contou o zoom como movimento e o inventário do garimpo chamava de "replay em câmera lenta". Refeito com vídeo real (@UTDKarra, @bs.ftbl.lfc, @_ROMemorabilia_, @ArsenalBlessing). Regra: rodar `scripts/movimento_real.py --resumo` em todo clipe antes da EDL e no rascunho; janela FOTO só entra quando não há vídeo do fato (Martinez/Ballard ficaram ~1 s cada).
