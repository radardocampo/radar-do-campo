---
name: referencia-montagem-faiq
description: "Comparação da montagem à mão do usuário (Faiq Bolkiah, 2026-09-24) com a automática; o que ele mudou e o que virou proposta para as skills"
metadata:
  node_type: memory
  type: project
  originSessionId: 65ce680f-fd21-4e90-a903-8a565318bd79
  modified: 2026-09-24T22:58:25.302Z
---

Em 2026-09-24 o usuário remontou à mão o vídeo do Faiq Bolkiah. Os arquivos são `Videos prontos/O jogador mais rico do mundo tá desempregado. TIKTOK/YOUTUBE.mp4`, na pasta do job. A base foi o meu corte, e a análise foi feita com o `casar_fontes.py`.

O que ele fez diferente:
- **Narração:** velocidade original com as pausas cortadas (60,07s). Por isso a regra nova de narração.
- **Frase-ponte no fim:** "É por esse motivo que o J…", cortada no meio, que emenda com o início "o jogador mais rico…". É o recurso de loop, e não estava no roteiro.
- **Volume:** -10 LUFS (eu entreguei -13,4) e trilha por baixo, uns 14 dB abaixo da voz.
- **Marca do YouTube:** "Radar Do Campo" pequena, no canto superior direito (~28% da largura, centro em ~80%/9,7%), bem transparente. A lupa do TikTok ficou onde eu coloquei.
- **Vazamento de marca:** ele editou a partir do meu "sem legenda", que já tinha a lupa gravada. Com isso, a lupa do TikTok aparece em ~metade da versão dele do YouTube.
- **Imagens:**
  - usou a taça oficial do LCFC em "não jogou um único minuto pelo time principal / Nenhum"; eu tinha evitado por causa do Content ID
  - usou o palácio em "dinheiro pra comprar o clube inteiro"
  - usou uma foto nova e nítida do Faiq no Chonburi, que não estava no garimpo
- **Legenda:** às vezes em 2 linhas; números por extenso.
- **Possível erro dele:** o jovem de farda branca do clipe do banquete (apoio_palacio-banquete, 13s) foi usado como se fosse o Faiq. Provavelmente é o príncipe Abdul Mateen. Avisei.

Em 2026-09-24 ele aprovou todas as propostas, e elas foram aplicadas na cópia do HUB:
- **`render_final.py`:** o "sem legenda" sai sem marca; marca do YouTube no topo direito com 28% da largura; -10 LUFS.
- **`loop_final.py` (novo):** corta a narração quando o fim repete a abertura.
- **`prep_shots.py`:** aceita foto (.jpg/.png) como clipe.
- **Garimpo:** passo 3b, com 3 fotos nítidas do protagonista.
- **Montagem:** passo 3 item 7 (imagem literal) e item 8 (identidade).

A trilha continua sendo dele, no CapCut.

**How to apply:** nas próximas montagens, siga essas regras. Na análise de uma nova montagem dele, compare também com esta. Relacionado: [[referencia-montagem-carrascal]], [[skill-montagem-versao-nova-local]].
