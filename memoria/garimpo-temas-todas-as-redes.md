---
name: garimpo-temas-todas-as-redes
description: rotina do dia com redes = passar TODAS as 7 redes por candidato no Chrome do usuário e mostrar a grade; X e Kwai (/discover/) funcionaram em 06/10
metadata:
  node_type: memory
  type: feedback
  originSessionId: 5ecbcc92-f980-4f5f-91ce-4dbb153dc5ad
  modified: 2026-10-06T15:38:21.251Z
---

Na rotina (garimpo-de-temas, modo redes), o usuário quer a busca feita no navegador dele (Claude in Chrome) em todas as redes, para cada candidato. Em 2026-10-05 só passei no TikTok e ele reclamou.

**Why:** as outras redes trouxeram o melhor material do dia (bandeirão do Talleres com 104 mil curtidas só no Instagram; coletiva do Jorge Jesus na CazéTV).

**How to apply:** TikTok → Instagram → YouTube → Facebook → X → Threads → Kwai, uma busca por candidato, e entregar a grade candidato × rede sem célula vazia. Rede que falhar: avisar. Em 05/10 o x.com não abria pela extensão (a aba voltava pra nova guia) e o Kwai web sem login não busca. **Atualização 2026-10-06:** o X abriu normal (`/search?q=...&f=top`, ler `article` + aria-label do `[role=group]` pra curtidas/visualizações; não devolver `location.href` no JS, a extensão bloqueia a saída por ter query string) e o Kwai busca por `https://www.kwai.com/discover/<termo>` (texto do body depois de "Reservados."). Instagram: nome próprio sozinho às vezes volta "Nenhum resultado" (gyokeres, kerkez ucrania); trocar a 2ª palavra resolve. Fixtures do dia: a API `site.api.espn.com/apis/site/v2/sports/soccer/<liga>/scoreboard?dates=AAAAMMDD` (fetch no Chrome) é a fonte confiável; páginas "jogos de hoje" (Lance/Goal) erraram a data em 06/10. Instruções e truques de JS gravados na skill HUB versao-nova-2026-09-22/garimpo-de-temas (backup em _bak-2026-10-05-redes). Relacionado: [[garimpo-coleta-links-chrome]].
