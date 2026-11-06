# Espaço em disco: fechar os vídeos postados (consulta)

Em 05/10/2026 o disco C: chegou a 22 GB livres. Cada vídeo ocupava ~5 GB: ~2,3 GB de `clipes`, ~3 GB de `_montagem/render` e só ~1 GB de finais. O usuário pediu um **registro final** (o "end-point") de cada vídeo postado. Mas os clipes **não podem sair na entrega**, porque ele pode pedir correção ou remontagem depois. Por isso:

- **Na entrega** saem só os cortes regeneráveis (ver Entrega). O vídeo fica com ~3 GB.
- **Quando ele pedir** ("fecha os vídeos antigos", "limpa os vídeos já postados"), rode o `fechar_videos.py` sobre os vídeos com mais de 15 dias:

      python scripts/fechar_videos.py                 # mostra o que faria, sem mexer em nada
      python scripts/fechar_videos.py --executar      # [--dias 15] [--so "<pasta>"] [--limite-gb 140]

  O script cria `<job>/_registro/` (receita da montagem, inventário, links das fontes, notas, transcrições e `lista_clipes.txt`), manda `clipes`, `_montagem`, `frames` e `transcricoes` para a Lixeira e refaz `Shorts/Registro dos vídeos postados.csv`. Esse CSV é o único arquivo que a skill grava fora de uma pasta de vídeo, com autorização dele. O vídeo fecha com ~1 GB. Para remontar um vídeo fechado, os links estão no `_registro`, mas alguma fonte pode ter saído do ar.
- **Antes de rodar,** peça para ele esvaziar a Lixeira. Ela tem 150 GB; passando disso, o Windows apaga para sempre o que estiver lá dentro. O script para sozinho em `--limite-gb`.
- **Nunca apague de vez:** tudo vai para a Lixeira (`scripts/lixeira.py`), e quem esvazia é ele. Se a "Proteção contra ransomware" do Defender estiver ligada e a pasta for protegida, o arquivo não sai e o script avisa. Não desligue a proteção: avise o usuário.
