---
name: "garimpo-de-temas"
description: "Usar quando o usuário pede a rotina/temas de roteiro do dia (jogos de futebol de ontem), ou pede a repercussão/o que está sendo falado sobre um jogo específico que ele já identificou — monta resumo por jogo e escreve os roteiros escolhidos."
---

# Garimpar temas e montar roteiros de futebol (Radar do Campo)

**Versão 2026-11-06** (limpeza: gancho afirmativo com o nome do protagonista no lugar do "Todo mundo viu…" fixo, opinião + assinatura no fim, até 3 nomes além do protagonista, 245–255 palavras, comentário de anônimo fora, etiqueta de força na lista de candidatos). O histórico está em `referencias/historico.md`.

Objetivo: ao invés de partir de um roteiro pronto pra achar clipes-fonte (isso é a skill `garimpo-de-videos`), aqui o ponto de partida é o próprio calendário de jogos — encontrar, entre os jogos de futebol de um período (padrão: o dia anterior, fuso America/Sao_Paulo), quais têm um ângulo forte o bastante pra virar roteiro do canal Radar do Campo, montar um resumo por jogo pro usuário escolher, e só então escrever o(s) roteiro(s) completo(s) dos ângulos escolhidos. Também cobre o caso de o usuário já chegar com um jogo específico em mente (Passo 13).

Essa skill assume que já foi decidido que é hora de rodar esse fluxo (normalmente porque as instruções do projeto do usuário mandam chamar essa skill quando ele pede "a rotina/os temas do dia") — ela não precisa reconhecer a frase-gatilho sozinha, só executar o fluxo abaixo assim que for chamada.

## Hub

Comandos e regras gerais: `referencias/hub.md`. Nesta skill: só os candidatos **escolhidos** viram pauta (Passo 10); na abertura de cada roteiro, `status <id> trabalhando` ("Escrevendo roteiro"); no fim, o "Fechamento obrigatório: Hub" com `--status aguardando` ("Esperando garimpo"). Se o `hub.py` falhar, diga em uma linha e siga.

## Exclusão fixa — futebol feminino fora da busca
O canal não cobre futebol feminino. Jogos de competições femininas (Brasileirão Feminino, Champions Feminina, NWSL, Copa do Mundo Feminina, categorias de base femininas etc.) **nunca** entram como candidatos: nem pela busca das ligas prioritárias (Passo 3), nem pela checada dos jogos "fracos" (Passo 4), nem pelo fallback (Passo 5), nem pela repercussão nas redes (Passo 8) — mesmo que seja uma final, tenha viralizado ou tenha o melhor ângulo do dia. Se o dia só rendeu jogo feminino, vá pro fallback do Passo 5 ou diga que não teve tema, em vez de trazer um candidato feminino.

Duas exceções, e só essas: (a) o usuário pedir explicitamente um jogo ou tema de futebol feminino; (b) o Passo 13, quando o jogo específico que ele trouxe for feminino — aí a escolha foi dele, não da busca.

## Passo 0 — Comparação de edição só quando ele pedir
Não procure nem ofereça comparar edições dele na rotina (pausa de obra até 06/12/2026; depois disso, também só quando ele pedir). O fluxo está na skill `montagem-de-video` (`referencias/comparacao.md`).

## Passo 1 — Sempre busca padrão + redes sociais (sem perguntar)
Desde 12/out/2026, por pedido do usuário, a rotina **sempre** faz a busca padrão (Passos 3-7) **e** a repercussão em todas as redes sociais (Passo 8). Não pergunte o modo de busca: vá direto. Só pule as redes se o próprio usuário pedir isso na mensagem (ex.: "sem redes", "só busca padrão").

## Passo 2 — Definir a janela de busca
- Sem outra instrução, a janela é o dia anterior, considerado no fuso America/Sao_Paulo.
- Se o usuário pedir um período diferente ("essa rodada", "final de semana", uma data específica), use o período pedido.

## Passo 3 — Buscar jogos nas ligas prioritárias
- Ligas prioritárias, nessa ordem: Copa do Brasil, Brasileirão, Champions League, Premier League, La Liga.
- Um jogo é "relevante" quando bate pelo menos um destes critérios: clássico/rivalidade conhecida; disputa direta por título, vaga ou rebaixamento; um dos times está entre os favoritos da liga; repercussão viral já visível na cobertura esportiva.
- Analise pelo menos os 4-5 jogos mais fortes do dia antes de decidir quais avançam pra próxima etapa.
- Aplique a exclusão fixa: competições femininas ficam de fora da varredura.

## Passo 4 — Não ignorar os jogos "fracos"
Mesmo jogos fora dessas ligas ou sem nenhum critério de relevância acima merecem uma checada rápida: aconteceu briga, expulsão polêmica, confusão, provocação ou comemoração fora do comum? Se sim, esse jogo vira candidato por conta própria, mesmo sem ser relevante pelo critério padrão. A exclusão fixa continua valendo: um incidente em jogo feminino não vira candidato.

## Passo 5 — Fallback quando as ligas prioritárias não renderem nada
- Se nenhuma liga prioritária tiver jogo relevante no período, busque automaticamente a próxima competição de peso disponível (Champions League, Libertadores etc.) — sem perguntar antes — e avise brevemente por que as prioritárias ficaram de fora. O fallback também é só masculino: nunca caia numa competição feminina como alternativa.
- Se mesmo essa busca alternativa não achar partida com peso real, diga isso claramente em vez de forçar um jogo pequeno só pra preencher cota de candidatos do dia.

## Passo 6 — Extrair o ângulo de cada jogo candidato
Para cada jogo que passou pelos Passos 3-5, levante em fontes esportivas tradicionais (busca web, sites de notícia, Sofascore, comunicados oficiais): resultado e destaques da partida; jogadores em destaque ou atuações ruins; lances fora do comum (gol bonito, provocação, briga, expulsão, virada, goleada de time grande).

O foco do roteiro NUNCA é o placar/resultado óbvio — é o detalhe obscuro, estatístico ou comportamental que passou despercebido na cobertura padrão (ex.: tempo de substituição gerando punição de um jogador a menos, um gesto humano fora da jogada que ninguém repercutiu, uma sequência estatística que ninguém juntou). Prefira esse tipo de ângulo sempre que houver um disponível para o jogo.

## Passo 7 — Checar a fonte antes de aceitar qualquer informação como confirmada
Antes de apresentar qualquer informação factual como confirmada — resultado, data, evento, número, status atual de algo — confirme que a fonte tem data explícita e inequívoca do dia/período certo. Nunca presuma que uma fonte é recente só por aparecer numa busca ou por estar em página com branding do ano atual. Redobre a atenção em casos onde o mesmo tipo de evento se repete periodicamente (confrontos recorrentes, edições anuais, relatórios cíclicos) — são os que mais geram risco de uma ocorrência antiga passar por atual.

Essa regra vale tanto pro placar/resultado básico quanto pro detalhe obscuro que é o centro do roteiro — mas o remédio muda dependendo do que fica incerto:
- Se o que não dá pra confirmar é o **detalhe obscuro/ângulo**, descarte esse ângulo (ou esse jogo inteiro) e procure outro em vez de levar adiante sem certeza — sempre vai ter outro jogo/ângulo pra tentar.
- Se o que não dá pra confirmar é uma **informação básica da partida** (placar, data, competição, se o jogo realmente aconteceu como descrito), não apresente como fato: declare a incerteza explicitamente e peça confirmação ao usuário antes de seguir, em vez de simplesmente descartar o jogo ou inventar em cima.

**Post de rede social também não é fonte.** Ele serve de pista, mas o fato vai para a lista e para o roteiro só depois de achado numa matéria com data. Em 18/out/2026 um post do Facebook dizia que o Barreto, do Criciúma, "também foi expulso" por chutar a segunda bola em 2024. A matéria mostrou que deu pênalti, não expulsão. Na lista de candidatos, marque o que veio só de post como "ainda não conferido".

**Resumo automático de busca não é fonte.** O texto-resumo que a ferramenta de busca devolve junto dos links pode inventar: em 27/set/2026 um desses resumos afirmou "Manchester City 5x3 Sunderland em 26/09", num dia de Data FIFA sem Premier League. Só vale como confirmado o que está numa página aberta (WebFetch ou navegador) com data explícita. Também confira o calendário antes de listar ligas: em Data FIFA não há Brasileirão, Premier League, La Liga nem Champions, mas pode haver Série B, Nations League, amistosos e ligas de outros continentes. O jogo feminino que aparecer nessas datas (ex.: Corinthians x São Paulo feminino) continua fora (exclusão fixa).

O detalhe obscuro também precisa ser tão verificável quanto o placar: nunca invente, arredonde ou "engorde" um número, uma fala ou uma ação pra deixar o gancho mais forte.

Lances controversos (pênalti duvidoso, decisão de arbitragem) entram como polêmica/repercussão ("a decisão gerou revolta e virou polêmica"), nunca como veredito ("foi um roubo") — a menos que haja confirmação objetiva do erro (revisão do VAR, comunicado oficial da arbitragem).

## Passo 8 — Repercussão nas redes sociais (sempre, na rotina e no Passo 13)
Pra CADA jogo relevante, vá nas redes sociais ver o que está sendo comentado.

**Mecanismo:** essa etapa usa o navegador de verdade do usuário — Claude in Chrome (`mcp__claude-in-chrome__*`) — nas abas já logadas de cada rede, do mesmo jeito que a skill `garimpo-de-videos` faz. X, Instagram e Facebook só mostram resultado de busca completo pra quem está logado — isso é só uma exigência técnica dessas redes, não define prioridade de cobertura.

**Sem o Chrome, a rotina não está pronta (reclamação de 18/out/2026, "já é o segundo dia").** Duas rotinas seguidas terminaram sem passar nas redes pelo navegador dele, e a entrega saiu assim mesmo. Por isso:
- Se o Claude in Chrome não responder, tente de novo (outro `tabs_context_mcp`, outra aba) enquanto adianta os Passos 3–7.
- Se mesmo assim não conectar, **não entregue a lista como pronta**. Diga que a etapa das redes está pendente, peça para ele reconectar a extensão e continue quando ele avisar. Não troque por busca web nem pelo navegador embutido: a busca do TikTok no navegador embutido exige login e volta "Algo deu errado".

**Prioridade de cobertura:** comece pelo **TikTok** — é a rede que o usuário mais usa pra buscar e baixar vídeo (alinhado com a própria conta @_radardocampo), e costuma render bem pra ver se um lance ou gesto virou meme/trend. Procure pelo nome do jogador/time + palavra-chave do lance e olhe os comentários dos vídeos mais engajados, não só a legenda. Depois complemente com as outras redes, na referência de cobertura da skill `garimpo-de-videos` (Instagram, X, YouTube, Facebook, Kwai, Threads) — aqui o objetivo é ler o que está sendo dito (posts, comentários, hashtags), não achar clipe limpo pra baixar:
- **X (Twitter)** costuma ser a fonte mais rápida pra reação/controvérsia em tempo real — busque pelo time/jogador + o jogo, ordenando por mais recente.
- **Instagram** também mostra bem se algo virou trend, de forma parecida ao TikTok.
- Comentários/respostas em contas de jornalistas e páginas oficiais dos clubes costumam concentrar a repercussão mais relevante — vale checar direto.
- Anote, por jogo, um resumo curto (2-3 linhas) do clima geral nas redes e de qualquer reação específica que se destaque. No fluxo padrão (Passo 1-11), isso entra no resumo do Passo 9 e pode virar candidato próprio (tipo "reação de torcida"), mesmo que o Passo 6-7 não tenha achado ângulo pra aquele jogo.
- Se a repercussão que aparecer for de jogo feminino, ignore: a exclusão fixa vale aqui também, inclusive pra candidato do tipo "reação de torcida".

**Cobertura obrigatória: todas as redes, todos os candidatos.** Em 05/out/2026 a rotina passou só no TikTok e entregou a lista; o usuário reclamou ("não está fazendo a pesquisa pelo meu navegador em todas as redes"). Ao refazer, as outras redes trouxeram o melhor material do dia: post da ESPN Argentina com 104 mil curtidas sobre o bandeirão do Talleres que falhou (só no Instagram), vídeo da CazéTV com Jorge Jesus discutindo na coletiva (Instagram), a Grécia que nunca tinha vencido a Alemanha (Facebook/YouTube). Por isso:
- Pra CADA candidato, passe nas 7 redes, nesta ordem: TikTok → Instagram → YouTube → Facebook → X → Threads → Kwai. Uma busca por rede por candidato, no mínimo.
- Antes de entregar o Passo 9, monte a grade candidato × rede e marque cada célula: o que achou (com curtidas/visualizações), "nada relevante" ou "falhou: motivo". Entregue essa grade junto da lista. Célula em branco não pode existir.
- Rede que falhar: tente de novo uma vez, por outro caminho, antes de marcar "falhou". Diga ao usuário qual rede falhou e por quê, sem passar por cima calado.

URLs e truques que funcionam (Claude in Chrome; em 18/out/2026 as 7 redes funcionaram):
- **Fixtures do dia:** a API `site.api.espn.com/apis/site/v2/sports/soccer/<liga>/scoreboard?dates=AAAAMMDD` (fetch no Chrome) é a fonte confiável. Páginas "jogos de hoje" (Lance, Goal) erraram a data em 06/out.
- TikTok: `https://www.tiktok.com/search?q=<busca>`; ler `[data-e2e=search_top-item]` → `[data-e2e=video-views]` + `search-card-video-caption` + `search-card-user-unique-id` (o antigo `a[href*="/video/"]` também serve para juntar links), esperando ~4 s. A página do vídeo abre em branco pela extensão: legenda, curtidas e views do vídeo saem com `yt-dlp --skip-download --write-info-json`. Para ler os comentários, abra o vídeo mais curtido e leia o painel de comentários; em 18/out o mais curtido do Bernal x Yamal (415) virou frase do roteiro.
- Instagram: `https://www.instagram.com/explore/search/keyword/?q=<2 palavras>` (mais que 2 palavras costuma vir vazio; acento também pode zerar; nome próprio sozinho às vezes volta "Nenhum resultado", e trocar a 2ª palavra resolve). A grade não traz legenda: pegue os ids de `a[href*="/p/"]` e, na mesma aba, faça `fetch('/p/<id>/')` e leia a `meta og:description` ("104K likes, 4,857 comments - conta no October 4, 2026: legenda"). Assim dá pra ler vários posts sem navegar. Pra ler comentários, abra o post.
- YouTube: na aba do YouTube, `fetch('/results?search_query=<busca>')` e extraia título + `viewCountText` do HTML; várias buscas numa chamada só.
- Facebook: `https://www.facebook.com/search/videos/?q=<busca>`; ler o `[role="main"]` (remover a repetição "Facebook").
- Threads: `https://www.threads.com/search?q=<busca>&serp_type=default`; texto do body já traz posts com curtidas. Termo em inglês às vezes volta vazio: marque "nada encontrado" depois de 2 buscas.
- X: `https://x.com/search?q=<busca>&f=top` (ou `&f=live` para o mais recente); leia os `article` e o aria-label do `[role=group]` (curtidas e visualizações). Não devolva `location.href` no JS: a extensão bloqueia a saída por ter query string. Se o X não abrir (aconteceu em 05/out: a aba voltava para nova guia), avise o usuário: provavelmente o x.com está bloqueado nas permissões de site da extensão ou instalado como app no Chrome. Não troque por busca web.
- Kwai: `https://www.kwai.com/discover/<termo>` e leia o texto do body depois de "Reservados." (a URL `/search` e o campo de busca da home não funcionam sem login). Nome comum mistura com outro jogador (em 18/out, "Bernal" trouxe o Marc Bernal): confira o time no texto.

## Passo 8b — Canais do mesmo nicho e tema saturado
Pedido de 18/out/2026: "pesquise em canais do mesmo nicho e bem parecido com o meu estilo de vídeo, mas procure por canais que tenham engajamento no assunto". Faça em toda rotina, depois do Passo 8:
- **Quem medir:** o @Onfirefut (YouTube @Onfirefut e TikTok; ~241 mil inscritos e ~174 mil seguidores em out/2026) é o mais próximo do formato de storytelling ("a atitude de…", "ninguém percebeu…"). Procure também os canais "irmãos" que aparecem nas buscas com o mesmo formato. As contas grandes (TNT, SportsCenter, CazéTV) medem o volume do assunto, mas não o formato.
- **O que medir:**
  - os vídeos dele que mais rendem e o tipo: em out/2026, atitude e provocação (Pulgar 911 mil, Carrascal 394 mil);
  - se ele **já postou** sobre cada candidato, com o título e as views.
- **Na lista:** candidato que o Onfirefut já fez ganha **"saturado no nicho"**, com os títulos dele. No Bernal x Yamal ele já tinha dois ("Yamal entrou na mente do Facundo", 17 mil; "O espetáculo debochado do Yamal", 33 mil). Saturado não descarta: se o usuário escolher, o roteiro vai por um **ângulo que ele não usou**. No Bernal foi a súmula e o risco de perder o Clássico (Passo 11).
- Feche a lista com uma linha sobre o que os canais parecidos mostraram (formato que está rendendo, tema que ninguém fez em português).

## Passo 9 — Montar o resumo por jogo (prévia de candidatos)
**A lista vai escrita no texto da resposta, inteira** (reclamação de 18/out/2026: "não mostra os candidatos pra mim escolher, só os números"). Eu tinha fechado a rotina só com a caixa de resumo do fim do turno, e ele nunca viu a lista. Escreva cada candidato com título, o que aconteceu, o detalhe obscuro, o tipo, as redes (com números) e as fontes.

**Etiqueta de força (desde 06/11/2026), em todo candidato**, pelo que os números do canal mostram (seção no fim):
- **forte — detalhe escondido/regra** (algo que muda o lance: "não valeria", "a 10 sumiu", "o gesto já expulsava");
- **forte — incidente físico** (apagou, lesão, briga, agressão);
- **forte — estrela + conflito** (Kane, CR7, Neymar, Messi, Haaland, Yamal em atrito);
- **fraco — resumo de jogo** (golaço sem polêmica, provocação ou histórico sem fato novo, jogo sem estrela).
Ele continua escolhendo; a etiqueta só deixa claro o risco. Candidato fraco vai para o fim da lista, com a observação do porquê. Depois venha a grade candidato × rede, a linha dos canais do nicho (Passo 8b) e a sua leitura (quais têm mais engajamento no Brasil, qual está aberto, qual está saturado). Só então a caixa de resumo com a pergunta.

Antes de escrever qualquer roteiro completo, entregue uma lista curta pro usuário escolher. Para cada jogo analisado, mostre em poucas linhas: o jogo e o que aconteceu (resultado/destaque rápido); o detalhe obscuro resumido do Passo 6-7 (SEM redigir o gancho nem o roteiro em si), se houver um confirmado; o tipo de detalhe (tático, estatístico, comportamental/gesto, arbitragem, reação de torcida); o resumo da repercussão nas redes do Passo 8; e a fonte/link que confirma cada ponto.

Traga de 4 a 6 candidatos sempre que o dia permitir, variando os tipos entre eles — mesmo sabendo que só 2 a 4 vão virar roteiro. Não desenvolva o roteiro completo nessa etapa.

## Passo 10 — Esperar a escolha do usuário
Pare aqui e espere o usuário responder quais candidatos quer transformar em roteiro (por número, "todos", ou pedindo mais opções se nenhum convencer). Só depois disso, siga pro Passo 11.

**Hub:** só os candidatos **escolhidos** viram pauta (os outros não, para a lista do Hub não encher todo dia). Para cada escolhido, antes de escrever: `buscar` pelo protagonista (ele pode ter salvo a pauta pela extensão do Chrome); se não houver, `criar "<título curto do tema>" --etapa pauta --notas-arquivo <resumo.txt> --refs-json <posts.json> --status trabalhando`; se achou, `status <id> trabalhando` (selo "Escrevendo roteiro"). O resumo leva o que aconteceu, o detalhe obscuro e as fontes com link; os posts das redes do Passo 8 entram como `{"url": ..., "kind": "referencia", "note": "104 mil curtidas, comentários citados"}`.

## Passo 11 — Desenvolver o(s) roteiro(s) completo(s) dos escolhidos

Escreva na voz do Radar do Campo. **A referência são os hits do próprio canal** (o pênalti do Kane que não valeria, a camisa 10, o Matheuzinho, o Bruno Duarte, o Haaland x Enzo), não outro canal: o @Onfirefut serve só para checar saturação (Passo 8b). Entregue pronto para revisão, sem enrolação.

**Tamanho:** mire **245–255 palavras** no "Texto para o AI Studio". O vídeo final nunca pode ficar abaixo de 60 s, e o ideal é fechar em 60–66 s (no YouTube, 1:01–1:05 fica em 80–90% assistido; 1:14–1:21 cai para ~70%). A montagem corta as pausas e o loop, e estica as respirações se faltar tempo; com 235 palavras deu 59,2 s, então não desça de 245. O mesmo arquivo vai para as 7 redes: não existe versão curta.

**Estrutura** (etiquetas curtas no texto com etiquetas; nunca no texto do AI Studio):
- **Gancho (1–2 frases):** afirmativo, com o **nome do protagonista** e a promessa de um detalhe, sem dizer onde ele está. Reveze entre estes modelos, e nunca use o mesmo em dois roteiros seguidos:
  1. Fato + promessa: "O Haaland perdeu a paciência com o Enzo Fernández no meio do jogo. E o motivo é mais simples do que parece."
  2. Regra que muda o lance: "O pênalti do Kane não valeria nem se a bola tivesse entrado."
  3. Contraste de números: "Lotou pro Messi… mas não pra Seleção Brasileira."
  4. Consequência em aberto: "O Andreas foi expulso por chutar uma bola. Só que não era a bola do jogo."
  5. Pergunta direta ao torcedor, só quando ela já carrega o fato: "Por que nenhum jogador da Argentina usou a 10 contra a Bolívia?"
  "Todo mundo viu…" e "ninguém percebeu…" deixaram de ser o padrão (decisão de 06/11/2026): no máximo uma vez a cada 5 roteiros. O gancho não descreve o que a imagem já mostra e não aponta onde está a revelação ("o que veio depois é ainda mais estranho", nunca "o que o juiz escreveu na súmula").
- **Contexto:** só o que leva ao payoff. Placar, rodada, recorde ou histórico entram só se explicam o fato. Sem apresentar o personagem ("venezuelano, ex-companheiro").
- **Desenvolvimento:** fatos que aumentam a tensão, sem resolver a curiosidade.
- **Reviravolta:** o dado inesperado, se houver.
- **Payoff:** a resolução, só no fim, fechando o gancho.
- **Opinião (1 frase, desde 06/11/2026):** a leitura do canal sobre o caso, marcada como opinião ("Pra mim…", "Na real…"). Interpreta o fato, nunca acusa: nada de "foi roubo", nada de fato não confirmado, nada de ataque pessoal.
- **Assinatura (fixa):** "O radar não deixa passar." Vem logo depois da opinião.
- **Frase-ponte de loop:** a última frase repete o começo do gancho (ou termina em aberto e o gancho completa), para o vídeo emendar.

**Regras do texto:**
- **No máximo 3 nomes além do protagonista** no roteiro inteiro. Goleiro, zagueiro e árbitro secundários viram função ("o goleiro", "o zagueiro do Arsenal"). Cada nome a mais é um motivo para arrastar.
- **Roteiro de situação/incidente vai direto:** o nome do jogador já no gancho ("perdeu a paciência com o Enzo Fernández", nunca "com um companheiro"), só a situação do jogo e o motivo. Nada de views de TikTok, de "câmera da arquibancada" ou de quem disse o quê sobre a briga.
- **Comentário de rede social (decisão de 06/11/2026):** só de pessoa relevante (jogador, técnico, clube, jornalista), ou quando a polêmica é o próprio comentário. Comentário de anônimo e contagem de curtidas não viram pauta nem payoff. Quando entrar, anote quem escreveu e onde, para o garimpo trazer o print.
- **Duas versões que não batem viram polêmica, nunca veredito.** Versão de um jornal só, sem outra fonte, fica de fora.
- **Ao trocar a primeira frase, confira os pronomes** da seguinte.
- **Tema saturado no nicho (Passo 8b):** ângulo que o concorrente não usou.
- Fato e número só confirmados (Passo 7).

Se mais de um candidato for escolhido no mesmo lote, use um modelo de gancho diferente em cada um.

**Hub:** com o roteiro e o prompt do Passo 11b prontos, siga o "Fechamento obrigatório: Hub". Se ele pedir mudança no roteiro depois, rode o fechamento de novo.

Ao final de cada roteiro, informe a contagem de palavras do texto do AI Studio e a fonte (link) do detalhe destacado.

Depois do roteiro com etiquetas, entregue o bloco **"Texto para o AI Studio"**, corrido e sem as etiquetas (a voz lê "Contexto" e "Payoff" se elas forem coladas). Ele gera a voz no AI Studio, como sempre.

Feche com 3–4 linhas de **ideias para a montagem**: a imagem do gancho (o pico do material), a prova de cada fato forte, o que mostrar na revelação e o rosto/gesto do protagonista para a opinião e a assinatura.

## Passo 11b — Prompt para garimpar num chat novo (SEMPRE, depois de todo roteiro)
Desde 21/out/2026 é padrão: todo roteiro entregue termina com este prompt, sem ele pedir (cada etapa roda num chat novo para economizar token, e o mesmo prompt serve para o Antigravity como plano B).
Em 18/out/2026 ele pediu "gere um prompt com o contexto para garimpar os vídeos desse roteiro em um chat novo", e o garimpo que saiu dele foi bom. Entregue num bloco de código, pronto para colar:
1. `Use a skill garimpo-de-videos para garimpar e baixar os clipes deste roteiro do canal Radar do Campo.` e, logo abaixo, `PAUTA DO HUB: <id>`.
2. **CONTEXTO DO TEMA (já confirmado):** jogo, competição, data, estádio, minuto a minuto do lance, nomes completos (inclusive goleiro e árbitro), o que veio depois (coletiva, pedido de desculpas, súmula) e as datas futuras citadas.
3. **ROTEIRO (narração final):** o texto corrido que foi para o AI Studio.
4. **O QUE CADA TRECHO PRECISA DE IMAGEM:** lista numerada, um item por frase forte, dizendo a imagem literal e a preferência (arquibancada, dois ângulos, print do comentário, print da súmula, "se não houver, close de X").
5. **POSTS QUE JÁ ACHEI NA PESQUISA (começar por eles):** os links das redes com curtidas, inclusive o post onde estão os comentários citados.
6. **OBSERVAÇÕES:** canais concorrentes cujos clipes não devem ser usados (Onfirefut), ângulos que eles já usaram, buscas úteis em português e na língua do jogo.

Esse mesmo texto vai para a pauta do Hub no fechamento (fim deste arquivo), e o botão do Hub copia ele.

## Passo 12 — Dois modos de entrada alternativos (material pronto)
Esse fluxo (Passos 1-11) é o padrão quando a skill é chamada pra buscar temas do zero. Mas o usuário pode entrar direto com material, pulando tudo isso:
- Se enviar material bruto (transcrição de vídeo, vídeos, textos de referência), pule os Passos 1-10 e monte um roteiro do zero a partir desse conteúdo, seguindo a estrutura e as regras do Passo 11.
- Se enviar um roteiro já escrito só pra reformular, preserve o gancho, a estrutura e as escolhas de palavras originais ao máximo — corrija apenas o que estiver factualmente incorreto ou com problema de fluidez, sem reescrever do zero.

O usuário avisa qual dos dois casos é ao enviar o material.

## Passo 13 — Modo jogo específico (fora da rotina diária)
Além do fluxo completo (Passos 1-11) e dos modos de entrada do Passo 12, o usuário pode pedir informação sobre UM jogo específico que ele já identificou — nomeando os times, a data, ou mandando um link — em vez de pedir a rotina do dia inteiro. Sinais desse pedido: "o que estão falando do jogo de [time A] e [time B]", "quero saber a repercussão desse jogo [link/data]", "esse jogo que está passando agora, [time A] x [time B]".

Nesse modo:
- Pule os Passos 2-5 (não precisa definir janela, nem filtrar por liga/relevância — o jogo já foi escolhido pelo usuário, não está concorrendo com outros). A exclusão fixa de futebol feminino também não se aplica aqui: se o usuário trouxe o jogo, é porque ele quer.
- Se o pedido trouxer `PAUTA DO HUB: <id>` (veio do botão "Copiar prompt" do Hub), rode `status <id> trabalhando` (selo "Escrevendo roteiro") e `ler <id>`, e use as notas, as referências e os clipes salvos como ponto de partida; o roteiro e a etapa vão para essa mesma pauta.
- Vá direto pro Passo 6 (levantar resultado/destaques/lances) e Passo 7 (checar fonte) pra esse jogo.
- Faça também o Passo 8 (repercussão nas redes sociais) automaticamente — foi isso que o usuário pediu.
- Se o jogo ainda estiver em andamento no momento do pedido, avise isso explicitamente e deixe claro que o placar/estatísticas podem mudar até o fim da partida — nunca apresente informação parcial de um jogo em andamento como se fosse o resultado final.
- Entregue um resumo direto (o que aconteceu até agora + o que está sendo falado nas redes), sem montar a "prévia de candidatos" do Passo 9 nem esperar escolha (Passo 10) — isso só faz sentido quando há vários jogos concorrendo por um roteiro. Só desenvolva o roteiro completo (Passo 11) depois, se o usuário pedir isso explicitamente sobre esse jogo específico.

**Candidato colado de outra rotina** ("pesquise e confirme mais informações e monte o roteiro perfeito para viralizar", 18/out/2026, Bernal x Yamal):
- confira cada ponto do candidato numa página com data (Passo 7) e diga o que confirmou, o que não achou (o minuto do amarelo) e o que ficou de fora por ter uma fonte só (o tapa do Lo Celso);
- passe nas 7 redes pelo Chrome (Passo 8), lendo os comentários mais curtidos;
- veja os ângulos que o Onfirefut já usou (Passo 8b);
- escreva o roteiro já nesta resposta (Passo 11), com as fontes do detalhe.
## O que os números do canal mostram (YouTube e TikTok Studio, 04/11/2026)

Use para escolher o tema e escrever o gancho:
- **Mediana por Short:** ~6,7 mil no manual (ago–23/set) e ~21 mil com as skills (24/set–03/nov). O que subiu foi a escolha de tema e a constância.
- **Ganham:** (1) detalhe escondido/regra ("o pênalti do Kane não valeria", 984 mil; "nenhum jogador usou a 10", 268 mil; Matheuzinho, 453 mil); (2) incidente físico (Hulk vomita e faz 2 gols, 2,1 mi; apagou em campo, 215 mil); (3) estrela + conflito (Kane x Yamal na Bola de Ouro, 789 mil; Haaland x Enzo, 190 mil).
- **Perdem:** resumo de jogo e golaço sem polêmica (Bruno Guimarães 6,8 mil, Thiago Silva 6,4 mil, Alisson 11 mil), provocação/histórico sem fato novo (Toney 5,5 mil).
- **Tema de massa vence tudo:** os 9 vídeos do álbum/figurinha da Copa (maio) somaram 13,8 mi, mais que os 60 vídeos de set–nov juntos. Quando um assunto atinge quem nem acompanha futebol, ele passa na frente.
- **TikTok:** a maioria sai no 1º segundo; a primeira frase tem que prometer o detalhe ou a regra, não o contexto. ~40% das views lá vêm da busca: o nome do jogador e o fato precisam estar no texto.
- **YouTube:** % assistida de 70–90% em quase todos; o que decide é o feed escolher o vídeo (tema + gancho). Passou de ~1:10, cai para ~70%.
- **Sensível:** vídeo de morte rendeu US$ 0 no TikTok; tragédia não paga e pode limitar anúncio.

## Fechamento obrigatório: Hub (último passo de todo roteiro)

Depois de entregar o roteiro e o prompt do Passo 11b, para **cada** roteiro escrito e antes de encerrar a resposta:

1. Grave na pasta temporária da skill: `roteiro.txt` (o "Texto para o AI Studio"), `notas.txt` (jogo e data, o detalhe, as fontes com link, as ideias de montagem e as redes com números) e `prompt garimpo.txt` (o prompt do Passo 11b exatamente como foi entregue, com a linha `PAUTA DO HUB`).
2. Com a pauta conhecida (Passo 10 ou `PAUTA DO HUB` no pedido):

       python "C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\HUB Radar do Campo\radardocampohub1.0\scripts\hub.py" --fonte garimpo-de-temas atualizar <id> --etapa roteiro --roteiro-arquivo roteiro.txt --notas-arquivo notas.txt --proximo-prompt-arquivo "prompt garimpo.txt" --status aguardando --nota "roteiro com N palavras"

   Sem pauta, crie antes de escrever o prompt, para o id ir na linha `PAUTA DO HUB`: `criar "<título curto>" --etapa roteiro --roteiro-arquivo roteiro.txt --notas-arquivo notas.txt --refs-json posts.json --status aguardando`; depois grave o prompt com `prompt <id> "prompt garimpo.txt"`.
3. Se ele pedir mudança no roteiro depois, repita 1 e 2 com o texto novo (o prompt também muda).
4. Feche a resposta com uma linha por pauta: `Hub: <título> em Roteiro (esperando garimpo), com o prompt de garimpo.` Se o `hub.py` falhar, diga o erro nessa linha e siga (seção "Hub").

O Passo 13 sem roteiro (só o resumo do jogo) não tem fechamento: nada mudou na esteira.
