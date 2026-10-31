---
name: "garimpo-de-temas"
description: "Usar quando o usuário pede a rotina/temas de roteiro do dia (jogos de futebol de ontem), ou pede a repercussão/o que está sendo falado sobre um jogo específico que ele já identificou — monta resumo por jogo e escreve os roteiros escolhidos."
---

# Garimpar temas e montar roteiros de futebol (Radar do Campo)

**Atualizada em 2026-10-31:** todo roteiro termina com o "Fechamento obrigatório: Hub" (fim do arquivo): a pauta vai para Roteiro com o roteiro, as notas e o prompt de garimpo. **Antes, 2026-10-30:** a pauta do Hub acompanha a rotina (seção "Hub" e Passos 10, 11, 11b e 13). **Antes, 2026-10-18:** a rotina não fecha sem as 7 redes no Chrome dele e a lista escrita (Passos 8 e 9); canais do mesmo nicho e tema saturado (Passo 8b); roteiro com 255–265 palavras, gancho curto que não aponta a revelação e foco só no incidente (Passo 11); prompt de garimpo para chat novo (Passo 11b).

Objetivo: ao invés de partir de um roteiro pronto pra achar clipes-fonte (isso é a skill `garimpo-de-videos`), aqui o ponto de partida é o próprio calendário de jogos — encontrar, entre os jogos de futebol de um período (padrão: o dia anterior, fuso America/Sao_Paulo), quais têm um ângulo forte o bastante pra virar roteiro do canal Radar do Campo, montar um resumo por jogo pro usuário escolher, e só então escrever o(s) roteiro(s) completo(s) dos ângulos escolhidos. Também cobre o caso de o usuário já chegar com um jogo específico em mente (Passo 13).

Essa skill assume que já foi decidido que é hora de rodar esse fluxo (normalmente porque as instruções do projeto do usuário mandam chamar essa skill quando ele pede "a rotina/os temas do dia") — ela não precisa reconhecer a frase-gatilho sozinha, só executar o fluxo abaixo assim que for chamada.

## Hub: a pauta acompanha o trabalho (desde 30/out/2026)

Pedido do usuário em 30/out/2026: "todo o processo de escolher os roteiros, garimpagem e montagem do vídeo sincronizado certinho com as pautas e a esteira do Hub". Cada vídeo é uma **pauta** no Hub (radardocampo.online → Vídeos → Pautas), e a esteira anda: pauta → roteiro → garimpo → montagem → pronto → no ar. Esta skill avisa o Hub pelo script `hub.py`:

    python "C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\HUB Radar do Campo\radardocampohub1.0\scripts\hub.py" --fonte garimpo-de-temas <comando>

- **Comandos:** `buscar [termo]`, `ler <id>`, `criar "<título>" [--etapa E] [--notas-arquivo F] [--roteiro-arquivo F] [--refs-json F] [--proximo-prompt-arquivo F]`, `etapa <id> <etapa> [--nota "..."]`, `atualizar <id> [--roteiro-arquivo F] [--notas-arquivo F] [--pasta P] [--arquivo "rótulo=caminho"] [--titulo T] [--proximo-prompt-arquivo F] [--etapa E] [--nota "..."]`, `prompt <id> <arquivo> [--etapa E]` (só o prompt do próximo passo), `clipe <id> <url> [--tipo clipe|referencia] [--trecho gancho|lance|torcida|reacao|contexto] [--inicio 0:12] [--fim 0:25] [--nota "..."]`, `clipes <id> <lista.json>`. Saída em JSON.
- **Achar o id da pauta:** procure a linha `PAUTA DO HUB: <id>` no pedido (o botão "Copiar prompt" do Hub e os prompts de chat novo das skills trazem essa linha). Sem ela, rode `buscar "<jogador ou time>"` e use a pauta que bater; se nenhuma bater, crie uma.
- **Passe o id adiante:** todo prompt para chat novo que esta skill gerar leva `PAUTA DO HUB: <id>` na primeira linha depois do pedido.
- **O prompt do próximo passo vai para a pauta (desde 31/out/2026).** O prompt de chat novo que esta skill entrega é gravado na pauta com `--proximo-prompt-arquivo <arquivo>` (ou `prompt <id> <arquivo>`). O Hub mostra o bloco "Prompt para o próximo passo" com botão de copiar, e ele cola num chat novo direto de lá.
- **O fluxo só termina com o "Fechamento obrigatório: Hub"** (última seção deste arquivo). Pedido de 31/out/2026: a esteira anda sozinha quando cada fluxo termina, sem depender de alguém lembrar de chamar o `hub.py`.
- **O Hub nunca trava o vídeo.** Se o `hub.py` der erro (sem internet, senha ausente, pauta excluída), diga em uma linha na resposta e siga o trabalho. Nunca peça para o usuário consertar o Hub no meio da rotina.
- Arquivo temporário para o `hub.py` (roteiro, lista JSON) segue a regra de pastas desta skill.

## Exclusão fixa — futebol feminino fora da busca
O canal não cobre futebol feminino. Jogos de competições femininas (Brasileirão Feminino, Champions Feminina, NWSL, Copa do Mundo Feminina, categorias de base femininas etc.) **nunca** entram como candidatos: nem pela busca das ligas prioritárias (Passo 3), nem pela checada dos jogos "fracos" (Passo 4), nem pelo fallback (Passo 5), nem pela repercussão nas redes (Passo 8) — mesmo que seja uma final, tenha viralizado ou tenha o melhor ângulo do dia. Se o dia só rendeu jogo feminino, vá pro fallback do Passo 5 ou diga que não teve tema, em vez de trazer um candidato feminino.

Duas exceções, e só essas: (a) o usuário pedir explicitamente um jogo ou tema de futebol feminino; (b) o Passo 13, quando o jogo específico que ele trouxe for feminino — aí a escolha foi dele, não da busca.

## Passo 0 — Edições do usuário ainda não comparadas (aprendizado diário)
Antes do Passo 1, olhe as pastas de `C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\Videos prontos\Shorts\` modificadas nos últimos 3 dias. Em cada uma, se `Videos prontos\` tiver um vídeo editado por ele (nome diferente dos nossos 4: `video pronto para o TIKTOK.mp4`, `video pronto para o YOUTUBE.mp4`, `*-completo-sem-legenda.mp4`, `*-com-legenda-sem-marca.mp4` ou `*-limpo.mp4`; normalmente `<título> TIKTOK.mp4`) e não existir `_montagem\cmp\comparado.txt`, avise em uma linha e pergunte se ele quer que, depois da rotina, a edição seja comparada e a skill `montagem-de-video` atualizada (o fluxo está na seção "Aprendizado diário" dela). Não faça a comparação antes da rotina sem ele pedir.

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

**Prioridade de cobertura:** comece pelo **TikTok** — é a rede que o usuário mais usa pra buscar e baixar vídeo (alinhado com a própria conta @radardocampo_), e costuma render bem pra ver se um lance ou gesto virou meme/trend. Procure pelo nome do jogador/time + palavra-chave do lance e olhe os comentários dos vídeos mais engajados, não só a legenda. Depois complemente com as outras redes, na referência de cobertura da skill `garimpo-de-videos` (Instagram, X, YouTube, Facebook, Kwai, Threads) — aqui o objetivo é ler o que está sendo dito (posts, comentários, hashtags), não achar clipe limpo pra baixar:
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
**A lista vai escrita no texto da resposta, inteira** (reclamação de 18/out/2026: "não mostra os candidatos pra mim escolher, só os números"). Eu tinha fechado a rotina só com a caixa de resumo do fim do turno, e ele nunca viu a lista. Escreva cada candidato com título, o que aconteceu, o detalhe obscuro, o tipo, as redes (com números) e as fontes. Depois venha a grade candidato × rede, a linha dos canais do nicho (Passo 8b) e a sua leitura (quais têm mais engajamento no Brasil, qual está aberto, qual está saturado). Só então a caixa de resumo com a pergunta.

Antes de escrever qualquer roteiro completo, entregue uma lista curta pro usuário escolher. Para cada jogo analisado, mostre em poucas linhas: o jogo e o que aconteceu (resultado/destaque rápido); o detalhe obscuro resumido do Passo 6-7 (SEM redigir o gancho nem o roteiro em si), se houver um confirmado; o tipo de detalhe (tático, estatístico, comportamental/gesto, arbitragem, reação de torcida); o resumo da repercussão nas redes do Passo 8; e a fonte/link que confirma cada ponto.

Traga de 4 a 6 candidatos sempre que o dia permitir, variando os tipos entre eles — mesmo sabendo que só 2 a 4 vão virar roteiro. Não desenvolva o roteiro completo nessa etapa.

## Passo 10 — Esperar a escolha do usuário
Pare aqui e espere o usuário responder quais candidatos quer transformar em roteiro (por número, "todos", ou pedindo mais opções se nenhum convencer). Só depois disso, siga pro Passo 11.

**Hub:** só os candidatos **escolhidos** viram pauta (os outros não, para a lista do Hub não encher todo dia). Para cada escolhido, antes de escrever: `buscar` pelo protagonista (ele pode ter salvo a pauta pela extensão do Chrome); se não houver, `criar "<título curto do tema>" --etapa pauta --notas-arquivo <resumo.txt> --refs-json <posts.json>`. O resumo leva o que aconteceu, o detalhe obscuro e as fontes com link; os posts das redes do Passo 8 entram como `{"url": ..., "kind": "referencia", "note": "104 mil curtidas, comentários citados"}`.

## Passo 11 — Desenvolver o(s) roteiro(s) completo(s) dos escolhidos
Escreva no estilo do canal Radar do Campo, usando o canal @Onfirefut (https://www.youtube.com/@Onfirefut) como referência de estilo e ritmo (ele não é o canal do usuário, é só benchmark estético). Entregue pronto pra revisão, sem enrolação.

Duração: o vídeo final **nunca pode ficar abaixo de 60s** (acima é aceito; 73s passou). A montagem corta as pausas (não acelera) e o loop corta a frase-ponte, então o texto encolhe ~10%. Mire **255–265 palavras** no texto do AI Studio. Em 18/out/2026 o roteiro do Andreas tinha 235 palavras e deu 59,2s. A voz varia de 3,4 a 4 palavras/s depois do corte: erre para mais, nunca para menos.

Estrutura obrigatória, cada parte identificada com etiqueta curta no texto entregue:
- **Gancho:** 1-2 frases que geram curiosidade sem entregar a resposta. Padrão de contraste: "Todo mundo viu [fato óbvio do lance], mas o detalhe que ninguém percebeu [depois/antes] é [mais interessante/engraçado] ainda" — exemplo: "Todo mundo viu o jogo do Santos e do Internacional, mas ninguém percebeu o detalhe que teve no final do jogo." Nunca revelar no gancho qual é o detalhe.
- **Contexto:** rápido, do personagem/time.
- **Desenvolvimento:** em "loop" — empilhe fatos que aumentam a tensão, sem resolver a curiosidade ainda.
- **Reviravolta:** dado ou fato inesperado, se houver.
- **Payoff:** resolução só no final, fechando o gancho inicial. Nunca revele o desfecho antes dessa etapa.

O que ele mudou no roteiro do Bernal x Yamal (18/out/2026), e vale para todos:
- **Gancho falado curto, no padrão "Todo mundo viu…".** Eu abri com "Olha esse momento: o volante do Betis agarra o Lamine Yamal pelo pescoço, e o Yamal vai pro chão segurando o rosto. Todo mundo viu a cabeçada." Ele cortou a descrição e deixou "Todo mundo viu a cabeçada que o Lamine Yamal recebeu." Quando ele diz "o gancho pode começar com a cena", a cena é **a imagem** (a montagem abre nela). A voz não narra o que a imagem já mostra.
- **O gancho não aponta onde está a revelação.** "Mas quase ninguém leu o que o juiz escreveu na súmula depois" entregava que o segredo estava na súmula. Ele pediu para trocar, e ficou "Mas o que veio depois dessa cabeçada é ainda mais estranho." Diga que existe um detalhe, nunca em que documento, fala ou momento ele está.
- **Roteiro de incidente fala só do incidente.** Ele pediu "inteiramente sobre a situação": saíram o recorde do Barça (9 vitórias em 9) e o placar final, que não levavam à cabeçada. O dado do jogo só entra se explica o incidente (o "acabado de diminuir pra três a dois" ficou, porque explica o clima).
- **Ao trocar a primeira frase, confira os pronomes.** Com o gancho falando "a cabeçada que o Lamine Yamal recebeu", a frase seguinte "O nome dele é Facundo Bernal" passou a parecer que falava do Yamal. Virou "Quem deu a cabeçada foi o Facundo Bernal".
- **Tema saturado no nicho (Passo 8b): ângulo que o concorrente não usou.** No Bernal, o Onfirefut tinha feito "Yamal entrou na mente" e "espetáculo debochado"; o nosso foi a súmula e o Clássico.
- **Duas versões que não batem viram polêmica, nunca veredito:** "um jornal espanhol diz que foi o Yamal quem empurrou primeiro; um jornal de Barcelona diz que foi o Bernal". Versão de um jornal só, sem outra fonte (o tapa do Lo Celso), fica de fora.
- **Comentário real é material de roteiro.** "Nos comentários, chamaram ele de nova princesa e de melhor ator de Hollywood… vermelho claríssimo pro Vini" saiu dos comentários mais curtidos do post da ESPN Deportes. Anote quem escreveu e onde, para o garimpo trazer o print (a montagem mostra o print real).

Se mais de um candidato for escolhido no mesmo lote, varie a fraseologia do gancho entre eles — mantenha o padrão de contraste, mas não repita a frase-molde palavra por palavra em todos os roteiros do lote.

**Hub:** com o roteiro e o prompt do Passo 11b prontos, siga o "Fechamento obrigatório: Hub" (fim deste arquivo). Se ele pedir mudança no roteiro depois, rode o fechamento de novo.

Ao final de cada roteiro, informe a contagem aproximada de palavras (pra conferir o tempo) e a fonte (link) do detalhe destacado.

Depois do roteiro com etiquetas, entregue também um bloco **"Texto para o AI Studio"**, corrido e sem as etiquetas (Gancho, Contexto, Desenvolvimento, Reviravolta, Payoff). Em 02/out/2026 o roteiro foi colado com as etiquetas e a voz leu "Contexto", "Reviravolta" e "Payoff", que precisaram ser cortadas na montagem.

Feche com 3–4 linhas de **ideias para a montagem**: a imagem do gancho, a prova de cada fato forte e o que mostrar na revelação. Ex.: "gancho = a cabeçada até o Yamal cair, como prévia; 'um jornal diz… outro diz' = os dois ângulos do empurrão; comentários = prints reais; 'terminou a partida' = o Yamal de pé no resto do jogo".

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
- Se o pedido trouxer `PAUTA DO HUB: <id>` (veio do botão "Copiar prompt" do Hub), rode `ler <id>` e use as notas, as referências e os clipes salvos como ponto de partida; o roteiro e a etapa vão para essa mesma pauta.
- Vá direto pro Passo 6 (levantar resultado/destaques/lances) e Passo 7 (checar fonte) pra esse jogo.
- Faça também o Passo 8 (repercussão nas redes sociais) automaticamente — foi isso que o usuário pediu.
- Se o jogo ainda estiver em andamento no momento do pedido, avise isso explicitamente e deixe claro que o placar/estatísticas podem mudar até o fim da partida — nunca apresente informação parcial de um jogo em andamento como se fosse o resultado final.
- Entregue um resumo direto (o que aconteceu até agora + o que está sendo falado nas redes), sem montar a "prévia de candidatos" do Passo 9 nem esperar escolha (Passo 10) — isso só faz sentido quando há vários jogos concorrendo por um roteiro. Só desenvolva o roteiro completo (Passo 11) depois, se o usuário pedir isso explicitamente sobre esse jogo específico.

**Candidato colado de outra rotina** ("pesquise e confirme mais informações e monte o roteiro perfeito para viralizar", 18/out/2026, Bernal x Yamal):
- confira cada ponto do candidato numa página com data (Passo 7) e diga o que confirmou, o que não achou (o minuto do amarelo) e o que ficou de fora por ter uma fonte só (o tapa do Lo Celso);
- passe nas 7 redes pelo Chrome (Passo 8), lendo os comentários mais curtidos;
- veja os ângulos que o Onfirefut já usou (Passo 8b);
- escreva o roteiro já nesta resposta (Passo 11), com as fontes do detalhe.
## O que os números do canal mostram (medido em 28/10/2026, vídeos de 24/09 a 28/10)

Use isto para escolher o tema e escrever o gancho:
- **Ganham nos 3 apps:** (1) o detalhe escondido ou a regra que muda o lance ("o pênalti do Kane não valeria", "nenhum jogador usou a 10", "o gesto já tinha expulsado o Kaio Jorge", "o gol talvez nem seja dele"); (2) incidente físico (apagou em campo, punho quebrado, briga); (3) estrela + conflito (Kane, CR7, Neymar, Messi).
- **Perdem:** provocação ou histórico sem fato novo (Piqué, Toney), golaço sem polêmica (Paquetá), jogo sem estrela.
- **TikTok:** a maioria sai no 1º segundo. Os que seguraram até 0:04 tiveram 27–30% de vídeo completo e mais views. A primeira frase tem que prometer o detalhe ou a regra, não o contexto.
- **YouTube:** a % assistida fica em 70–90% em quase todos. O que decide é o tema e o gancho fazerem o feed escolher o vídeo. Roteiro que passa de ~1:10 cai para ~70% assistido; mire 60–65s.
- **Instagram:** só a camisa 10 passou de 100 mil; a capa com frase curta de mistério ("A 10 SUMIU", "CHUTOU A BANDEIRA") puxa.

## Fechamento obrigatório: Hub (último passo de todo roteiro)

Depois de entregar o roteiro e o prompt do Passo 11b, para **cada** roteiro escrito e antes de encerrar a resposta:

1. Grave na pasta temporária da skill: `roteiro.txt` (o "Texto para o AI Studio"), `notas.txt` (jogo e data, o detalhe, as fontes com link, as ideias de montagem e as redes com números) e `prompt garimpo.txt` (o prompt do Passo 11b exatamente como foi entregue, com a linha `PAUTA DO HUB`).
2. Com a pauta conhecida (Passo 10 ou `PAUTA DO HUB` no pedido):

       python "C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\HUB Radar do Campo\radardocampohub1.0\scripts\hub.py" --fonte garimpo-de-temas atualizar <id> --etapa roteiro --roteiro-arquivo roteiro.txt --notas-arquivo notas.txt --proximo-prompt-arquivo "prompt garimpo.txt" --nota "roteiro com N palavras"

   Sem pauta, crie antes de escrever o prompt, para o id ir na linha `PAUTA DO HUB`: `criar "<título curto>" --etapa roteiro --roteiro-arquivo roteiro.txt --notas-arquivo notas.txt --refs-json posts.json`; depois grave o prompt com `prompt <id> "prompt garimpo.txt"`.
3. Se ele pedir mudança no roteiro depois, repita 1 e 2 com o texto novo (o prompt também muda).
4. Feche a resposta com uma linha por pauta: `Hub: <título> em Roteiro, com o prompt de garimpo.` Se o `hub.py` falhar, diga o erro nessa linha e siga (seção "Hub").

O Passo 13 sem roteiro (só o resumo do jogo) não tem fechamento: nada mudou na esteira.
