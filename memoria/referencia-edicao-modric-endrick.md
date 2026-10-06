---
name: referencia-edicao-modric-endrick
description: "2026-10-02 comparação das edições dele do Modric e do Endrick — trocou só gancho+loop (pessoa em ação, torcida do mesmo momento), título da Copa literal, trilha em 3 degraus"
metadata:
  node_type: memory
  type: project
  originSessionId: ff64ded1-225b-40fc-90a7-3673d8735510
  modified: 2026-10-02T20:00:11.211Z
---

O usuário refinou os vídeos do Modric (Espanha 4x1 Croácia) e do Endrick (Austrália 2x4 Brasil) em cima do `completo-sem-legenda` e manteve ~90% do corte. Comparei em 02/10/2026 e gravei as regras na skill montagem-de-video do HUB, versão 2026-10-02. O `.skill` foi reempacotado, mas ele ainda precisa reenviar pelo claude.ai.

- **Gancho e loop trocados nos dois.**
  - Modric: a torcida de pé virou o Yamal sentado na bola, filmado da arquibancada.
  - Endrick: a câmera alta da TV virou um vídeo da arquibancada com o bolo inteiro (@trent_1228, "Endrick 1 vs 11"), que o garimpo não tinha achado.
- **Modric, frase "depois do título da Copa":** trocou os fogos do dia pelos campeões no túnel da Copa (vídeo de julho/2026, Los Angeles). No gol do Yamal, trocou o take de torcida sem a bola entrando pela transmissão aberta até a rede.
- **Trilha:** a mesma nos dois, em 3 degraus: -18 dB até ~33s, queda curta e -12 dB, depois -9 dB a partir de ~53s, saída 1–2s antes do fim. Sem SFX, -10,7 LUFS. O `guia_trilha.py` foi atualizado com esses degraus.

As regras de garimpo que saíram daqui (take de torcida do gancho, imagem do título de passagem) também foram para a skill garimpo-de-videos. Relacionados: [[referencia-edicao-camisa10]], [[montagem-gancho-e-contexto-literal]].
