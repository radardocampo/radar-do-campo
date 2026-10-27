---
name: garimpo-temas-todas-as-redes
description: rotina do dia com redes = passar TODAS as 7 redes por candidato no Chrome do usuário e mostrar a grade; X e Kwai (/discover/) funcionaram em 06/10
metadata:
  node_type: memory
  type: feedback
  originSessionId: 5ecbcc92-f980-4f5f-91ce-4dbb153dc5ad
  modified: 2026-10-26T12:33:56.175Z
---

Na rotina (garimpo-de-temas, modo redes), o usuário quer a busca feita no navegador dele (Claude in Chrome) em todas as redes, para cada candidato. Em 2026-10-05 só passei no TikTok e ele reclamou.

**Why:** as outras redes trouxeram o melhor material do dia (bandeirão do Talleres com 104 mil curtidas só no Instagram; coletiva do Jorge Jesus na CazéTV).

**How to apply:** TikTok → Instagram → YouTube → Facebook → X → Threads → Kwai, uma busca por candidato, e entregar a grade candidato × rede sem célula vazia. Rede que falhar: avisar. Em 05/10 o x.com não abria pela extensão (a aba voltava pra nova guia) e o Kwai web sem login não busca. **Atualização 2026-10-06:** o X abriu normal (`/search?q=...&f=top`, ler `article` + aria-label do `[role=group]` pra curtidas/visualizações; não devolver `location.href` no JS, a extensão bloqueia a saída por ter query string) e o Kwai busca por `https://www.kwai.com/discover/<termo>` (texto do body depois de "Reservados."). Instagram: nome próprio sozinho às vezes volta "Nenhum resultado" (gyokeres, kerkez ucrania); trocar a 2ª palavra resolve. Fixtures do dia: a API `site.api.espn.com/apis/site/v2/sports/soccer/<liga>/scoreboard?dates=AAAAMMDD` (fetch no Chrome) é a fonte confiável; páginas "jogos de hoje" (Lance/Goal) erraram a data em 06/10. Instruções e truques de JS gravados na skill HUB versao-nova-2026-09-22/garimpo-de-temas (backup em _bak-2026-10-05-redes). Relacionado: [[garimpo-coleta-links-chrome]].

**Atualização 2026-10-12:** a pedido dele, a rotina SEMPRE faz busca + 7 redes, sem perguntar o modo (skill v9 no claude.ai, HUB e nuvem). TikTok: ler `[data-e2e=search_top-item]` → `[data-e2e=video-views]` + `search-card-video-caption` + `search-card-user-unique-id`; a página do vídeo abre em branco pela extensão, então legenda/curtidas/views do vídeo via `yt-dlp --skip-download --write-info-json` (comentários do TikTok não vieram). Threads às vezes volta vazio para termos em inglês: marcar "nada encontrado" depois de 2 buscas.

**Atualização 2026-10-26:** o Kwai `/discover/<termo>` passou a devolver o mesmo feed genérico para qualquer termo (frase ou palavra única), então marcar "falhou" e avisar. A busca web (WebSearch) estava com índice velho e não achava os jogos da véspera. O que funcionou para achar matérias com data foi o RSS do Google Notícias, buscado de dentro de uma aba do news.google.com no Chrome: `fetch('/rss/search?q=<termo> when:2d&hl=pt-BR&gl=BR&ceid=BR:pt-419')`, lendo título + pubDate por regex (o DOMParser é bloqueado por TrustedHTML). Para abrir a matéria, fazer `location.href = <link do item>` e depois `get_page_text`. A extensão bloqueia mostrar o link (base64), então não dá para imprimir. Saídas maiores que ~1000 caracteres: guardar em `window.R` e ler em fatias.
