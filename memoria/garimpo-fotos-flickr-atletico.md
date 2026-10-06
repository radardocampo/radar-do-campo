---
name: garimpo-fotos-flickr-atletico
description: Atlético-MG publica no Flickr um álbum de fotos profissionais de cada jogo (fonte para a cota de fotos nítidas do garimpo)
metadata:
  node_type: memory
  type: reference
  originSessionId: 5a7ecad7-b48d-4555-a20d-bfcbbbd0c7c5
  modified: 2026-10-04T17:25:47.257Z
---

O site atletico.com.br usa fotos do Flickr do clube: `flickr.com/photos/clubeatleticomineiro/albums/<id>` (ex.: Galo x Bragantino 03/10/2026 = álbum 72177720335970813, 211 fotos, 2560px). Para achar o álbum, abra `flickr.com/photo.gne?id=<id da foto do site>`; o nome do arquivo da foto no site traz esse id (ex.: `55567362051_..._o-scaled.jpg`).

Limite visto em 2026-10-04: o HTML das páginas do álbum só rendeu 62 ids, e 37 deles deram 410 na miniatura `_n`. A rolagem pelo Chrome não carregou mais fotos (travou o renderer). Na próxima vez, abra foto a foto no navegador ou tente outro tamanho.

Relacionado: [[garimpo-coleta-links-chrome]], [[garimpo-download-sem-cookies]].
