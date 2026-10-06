---
name: "garimpo-de-temas"
description: "Usar quando o usuário pede a rotina/temas de roteiro do dia (jogos de futebol de ontem), ou pede a repercussão/o que está sendo falado sobre um jogo específico que ele já identificou — monta resumo por jogo e escreve os roteiros escolhidos."
---

# Garimpar temas e montar roteiros de futebol (Radar do Campo)

Objetivo: ao invés de partir de um roteiro pronto pra achar clipes-fonte (isso é a skill `garimpo-de-videos`), aqui o ponto de partida é o próprio calendário de jogos — encontrar, entre os jogos de futebol de um período (padrão: o dia anterior, fuso America/Sao_Paulo), quais têm um ângulo forte o bastante pra virar roteiro do canal Radar do Campo, montar um resumo por jogo pro usuário escolher, e só então escrever o(s) roteiro(s) completo(s) dos ângulos escolhidos. Também cobre o caso de o usuário já chegar com um jogo específico em mente (Passo 13).

Essa skill assume que já foi decidido que é hora de rodar esse fluxo (normalmente porque as instruções do projeto do usuário mandam chamar essa skill quando ele pede "a rotina/os temas do dia") — ela não precisa reconhecer a frase-gatilho sozinha, só executar o fluxo abaixo assim que for chamada.

## Exclusão fixa — futebol feminino fora da busca
O canal não cobre futebol feminino. Jogos de competições femininas (Brasileirão Feminino, Champions Feminina, NWSL, Copa do Mundo Feminina, categorias de base femininas etc.) **nunca** entram como candidatos: nem pela busca das ligas prioritárias (Passo 3), nem pela checada dos jogos "fracos" (Passo 4), nem pelo fallback (Passo 5), nem pela repercussão nas redes (Passo 8) — mesmo que seja uma final, tenha viralizado ou tenha o melhor ângulo do dia. Se o dia só rendeu jogo feminino, vá pro fallback do Passo 5 ou diga que não teve tema, em vez de trazer um candidato feminino.

Duas exceções, e só essas: (a) o usuário pedir explicitamente um jogo ou tema de futebol feminino; (b) o Passo 13, quando o jogo específico que ele trouxe for feminino — aí a escolha foi dele, não da busca.

## Passo 0 — Edições do usuário ainda não comparadas (aprendizado diário)
Antes do Passo 1, olhe as pastas de `C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\Videos prontos\Shorts\` modificadas nos últimos 3 dias. Em cada uma, se `Videos prontos\` tiver um vídeo editado por ele (nome diferente dos nossos 4: `video pronto para o TIKTOK.mp4`, `video pronto para o YOUTUBE.mp4`, `*-completo-sem-legenda.mp4`, `*-com-legenda-sem-marca.mp4` ou `*-limpo.mp4`; normalmente `<título> TIKTOK.mp4`) e não existir `_montagem\cmp\comparado.txt`, avise em uma linha e pergunte se ele quer que, depois da rotina, a edição seja comparada e a skill `montagem-de-video` atualizada (o fluxo está na seção "Aprendizado diário" dela). Não faça a comparação antes da rotina sem ele pedir.

## Passo 1 — Perguntar o modo de busca
Antes de começar a buscar, pergunte ao usuário (com a ferramenta de pergunta de múltipla escolha, quando disponível; em texto simples se não estiver) qual modo ele quer:
1. **Busca padrão** — só a busca de sempre (Passos 3-7), sem entrar nas redes sociais.
2. **Busca padrão + redes sociais** — a mesma busca de sempre, e também checar nas redes sociais o que está sendo falado de cada jogo encontrado (Passo 8).

Espere a resposta antes de continuar. Se estiver rodando sem ninguém pra responder (ex.: tarefa agendada/sessão desacompanhada), assuma o modo 2 (mais completo) e avise no início da resposta que assumiu isso.

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

**Resumo automático de busca não é fonte.** O texto-resumo que a ferramenta de busca devolve junto dos links pode inventar: em 27/set/2026 um desses resumos afirmou "Manchester City 5x3 Sunderland em 26/09", num dia de Data FIFA sem Premier League. Só vale como confirmado o que está numa página aberta (WebFetch ou navegador) com data explícita. Também confira o calendário antes de listar ligas: em Data FIFA não há Brasileirão, Premier League, La Liga nem Champions, mas pode haver Série B, Nations League, amistosos e ligas de outros continentes. O jogo feminino que aparecer nessas datas (ex.: Corinthians x São Paulo feminino) continua fora (exclusão fixa).

O detalhe obscuro também precisa ser tão verificável quanto o placar: nunca invente, arredonde ou "engorde" um número, uma fala ou uma ação pra deixar o gancho mais forte.

Lances controversos (pênalti duvidoso, decisão de arbitragem) entram como polêmica/repercussão ("a decisão gerou revolta e virou polêmica"), nunca como veredito ("foi um roubo") — a menos que haja confirmação objetiva do erro (revisão do VAR, comunicado oficial da arbitragem).

## Passo 8 — Repercussão nas redes sociais (só no modo 2 do Passo 1, ou sempre no Passo 13)
Se o usuário escolheu o modo "busca + redes" (ou pediu diretamente a repercussão de um jogo específico, Passo 13), pra CADA jogo relevante, vá nas redes sociais ver o que está sendo comentado.

**Mecanismo:** essa etapa usa o navegador de verdade do usuário — Claude in Chrome (`mcp__claude-in-chrome__*`) — nas abas já logadas de cada rede, do mesmo jeito que a skill `garimpo-de-videos` faz. X, Instagram e Facebook só mostram resultado de busca completo pra quem está logado — isso é só uma exigência técnica dessas redes, não define prioridade de cobertura. Se o Claude in Chrome não estiver disponível na sessão, avise o usuário que essa etapa não pode ser feita completa e ofereça seguir só com a busca padrão (ou só o Passo 6-7, no caso do Passo 13) em vez de tentar simular via busca web geral.

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

URLs e truques que funcionam (Claude in Chrome):
- TikTok: `https://www.tiktok.com/search?q=<busca>`; ler os cards com JS em `a[href*="/video/"]` (curtidas + legenda), esperando ~4 s.
- Instagram: `https://www.instagram.com/explore/search/keyword/?q=<2 palavras>` (mais que 2 palavras costuma vir vazio; acento também pode zerar). A grade não traz legenda: pegue os ids de `a[href*="/p/"]` e, na mesma aba, faça `fetch('/p/<id>/')` e leia a `meta og:description` ("104K likes, 4,857 comments - conta no October 4, 2026: legenda"). Assim dá pra ler vários posts sem navegar. Pra ler comentários, abra o post.
- YouTube: na aba do YouTube, `fetch('/results?search_query=<busca>')` e extraia título + `viewCountText` do HTML; várias buscas numa chamada só.
- Facebook: `https://www.facebook.com/search/videos/?q=<busca>`; ler o `[role="main"]` (remover a repetição "Facebook").
- Threads: `https://www.threads.com/search?q=<busca>&serp_type=default`; texto do body já traz posts com curtidas.
- X: `https://x.com/search?q=<busca>&f=live`. Em 05/out/2026 o X não abriu de jeito nenhum pelo Claude in Chrome (a aba voltava pra nova guia ou travava). Se acontecer, avise o usuário: provavelmente o x.com está bloqueado nas permissões de site da extensão ou o X está instalado como app no Chrome e captura os links. Não troque por busca web.
- Kwai: a URL de busca não funciona, e o campo de busca da home no navegador sem login devolve só o feed. Registre "falhou: busca do Kwai web sem login" e siga.

## Passo 9 — Montar o resumo por jogo (prévia de candidatos)
Antes de escrever qualquer roteiro completo, entregue uma lista curta pro usuário escolher. Para cada jogo analisado, mostre em poucas linhas: o jogo e o que aconteceu (resultado/destaque rápido); o detalhe obscuro resumido do Passo 6-7 (SEM redigir o gancho nem o roteiro em si), se houver um confirmado; o tipo de detalhe (tático, estatístico, comportamental/gesto, arbitragem, reação de torcida); no modo 2, o resumo da repercussão nas redes do Passo 8; e a fonte/link que confirma cada ponto.

Traga de 4 a 6 candidatos sempre que o dia permitir, variando os tipos entre eles — mesmo sabendo que só 2 a 4 vão virar roteiro. Não desenvolva o roteiro completo nessa etapa.

## Passo 10 — Esperar a escolha do usuário
Pare aqui e espere o usuário responder quais candidatos quer transformar em roteiro (por número, "todos", ou pedindo mais opções se nenhum convencer). Só depois disso, siga pro Passo 11.

## Passo 11 — Desenvolver o(s) roteiro(s) completo(s) dos escolhidos
Escreva no estilo do canal Radar do Campo, usando o canal @Onfirefut (https://www.youtube.com/@Onfirefut) como referência de estilo e ritmo (ele não é o canal do usuário, é só benchmark estético). Entregue pronto pra revisão, sem enrolação.

Duração: narração de ~70 segundos (considerando pausas/cortes de edição, o vídeo final fica em 60s) — cerca de 220-240 palavras.

Estrutura obrigatória, cada parte identificada com etiqueta curta no texto entregue:
- **Gancho:** 1-2 frases que geram curiosidade sem entregar a resposta. Padrão de contraste: "Todo mundo viu [fato óbvio do lance], mas o detalhe que ninguém percebeu [depois/antes] é [mais interessante/engraçado] ainda" — exemplo: "Todo mundo viu o jogo do Santos e do Internacional, mas ninguém percebeu o detalhe que teve no final do jogo." Nunca revelar no gancho qual é o detalhe.
- **Contexto:** rápido, do personagem/time.
- **Desenvolvimento:** em "loop" — empilhe fatos que aumentam a tensão, sem resolver a curiosidade ainda.
- **Reviravolta:** dado ou fato inesperado, se houver.
- **Payoff:** resolução só no final, fechando o gancho inicial. Nunca revele o desfecho antes dessa etapa.

Se mais de um candidato for escolhido no mesmo lote, varie a fraseologia do gancho entre eles — mantenha o padrão de contraste, mas não repita a frase-molde palavra por palavra em todos os roteiros do lote.

Ao final de cada roteiro, informe a contagem aproximada de palavras (pra conferir o tempo) e a fonte (link) do detalhe destacado.

Depois do roteiro com etiquetas, entregue também um bloco **"Texto para o AI Studio"**, corrido e sem as etiquetas (Gancho, Contexto, Desenvolvimento, Reviravolta, Payoff). Em 02/out/2026 o roteiro foi colado com as etiquetas e a voz leu "Contexto", "Reviravolta" e "Payoff", que precisaram ser cortadas na montagem.

## Passo 12 — Dois modos de entrada alternativos (material pronto)
Esse fluxo (Passos 1-11) é o padrão quando a skill é chamada pra buscar temas do zero. Mas o usuário pode entrar direto com material, pulando tudo isso:
- Se enviar material bruto (transcrição de vídeo, vídeos, textos de referência), pule os Passos 1-10 e monte um roteiro do zero a partir desse conteúdo, seguindo a estrutura e as regras do Passo 11.
- Se enviar um roteiro já escrito só pra reformular, preserve o gancho, a estrutura e as escolhas de palavras originais ao máximo — corrija apenas o que estiver factualmente incorreto ou com problema de fluidez, sem reescrever do zero.

O usuário avisa qual dos dois casos é ao enviar o material.

## Passo 13 — Modo jogo específico (fora da rotina diária)
Além do fluxo completo (Passos 1-11) e dos modos de entrada do Passo 12, o usuário pode pedir informação sobre UM jogo específico que ele já identificou — nomeando os times, a data, ou mandando um link — em vez de pedir a rotina do dia inteiro. Sinais desse pedido: "o que estão falando do jogo de [time A] e [time B]", "quero saber a repercussão desse jogo [link/data]", "esse jogo que está passando agora, [time A] x [time B]".

Nesse modo:
- Pule os Passos 1-5 (não precisa perguntar o modo de busca, nem definir janela, nem filtrar por liga/relevância — o jogo já foi escolhido pelo usuário, não está concorrendo com outros). A exclusão fixa de futebol feminino também não se aplica aqui: se o usuário trouxe o jogo, é porque ele quer.
- Vá direto pro Passo 6 (levantar resultado/destaques/lances) e Passo 7 (checar fonte) pra esse jogo.
- Faça também o Passo 8 (repercussão nas redes sociais) automaticamente, sem precisar perguntar o modo — foi isso que o usuário pediu.
- Se o jogo ainda estiver em andamento no momento do pedido, avise isso explicitamente e deixe claro que o placar/estatísticas podem mudar até o fim da partida — nunca apresente informação parcial de um jogo em andamento como se fosse o resultado final.
- Entregue um resumo direto (o que aconteceu até agora + o que está sendo falado nas redes), sem montar a "prévia de candidatos" do Passo 9 nem esperar escolha (Passo 10) — isso só faz sentido quando há vários jogos concorrendo por um roteiro. Só desenvolva o roteiro completo (Passo 11) depois, se o usuário pedir isso explicitamente sobre esse jogo específico.