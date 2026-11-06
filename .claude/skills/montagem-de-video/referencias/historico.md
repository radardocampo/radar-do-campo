# Histórico da montagem (consulta)

Este arquivo guarda a história que saiu do SKILL.md na limpeza de 06/11/2026. As regras que valem estão no SKILL.md; aqui ficam os casos que deram origem a elas. Abra só para comparar uma edição do usuário ou para entender por que uma regra existe.

## Linha de versão até 31/10/2026

**Versão 2026-10-31c (selo de andamento no Hub: `--status trabalhando` no começo da montagem e antes do rascunho do CapCut, `--status aguardando` com o texto do próximo passo na entrega, "Esperando refinamento no CapCut", e no rascunho, "No CapCut · esperando títulos e tags"; seções "Hub", Passo 0, Passo 9 e "Fechamento obrigatório: Hub"). Antes: 2026-10-31b (a montagem nunca marca Pronto: na entrega a pauta fica em Montagem com os arquivos e o prompt de títulos e tags, o rascunho do CapCut só anexa, e quem passa para Pronto é a `titulos-e-tags`; pedido do usuário depois do Kaio Jorge, que foi Pronto → Montagem → Pronto). Antes: 2026-10-31 ("Fechamento obrigatório: Hub" no fim do arquivo: na entrega a pauta vai para Pronto com os arquivos e o prompt de títulos e tags; o rascunho do CapCut volta a pauta para Montagem; `{PASTA}` no prompt de títulos). Antes: 2026-10-30 (a pauta do Hub acompanha a montagem: seção "Hub", Passo 0 e Entrega; `{PAUTA}` no prompt de títulos). Antes: 2026-10-29 (regra: shot com enquadramento ruim por sujeira na tela volta ao garimpo atrás do mesmo vídeo limpo, em vez de zoom). Antes: 2026-10-28 (comparação do Bruno Guimarães x Fleetwood; Décima sétima rodada; `capcut_projeto.py` aceita 3 cards empilhados no mesmo shot, faixa CARDS3). Antes: 2026-10-27 (comparação em lote de CR7/Girotto, Toney, Neymar e a Lei Vini Jr, Piqué/Mbappé e Yamal na Bola de Ouro; Décima sexta rodada; o rascunho do CapCut agora leva os desfoques, as setas e a música até o fim, com a virada na revelação; `analisa_capcut.py` e `pares_quadros.py`). Antes: 2026-10-23b (prompt de títulos e tags para chat novo no fim de toda entrega). Antes: 2026-10-23 (comparação em lote de Carlos Miguel, Thiago Silva e Cetré; Décima quinta rodada). Antes: 2026-10-22 (correção no `capcut_projeto.py`: o fim de cada trecho da legenda é arredondado em microssegundos antes de subtrair o início, porque o arredondamento separado sobrepunha trechos e travava o rascunho no Thiago Silva). Antes: 2026-10-21b (entrega reduzida a 2 arquivos, com-legenda e sem-legenda, sem logo do canal; o rascunho do CapCut não herda as logos do modelo). Antes: 2026-10-21 (comparação em lote de Paquetá, Kannemann, Neymar x Soteldo, Neymar x Thiago Mendes e Vitinha, todos refinados no CapCut: gancho com punch-in e pan, janela no lado certo do assunto, fonte limpa do mesmo lance, prova segurada até o fim, trilha do modelo mais baixa, `compara_capcut.py`; Décima quarta rodada).** Anterior: 2026-10-18 (Andreas, Bernal e Leo Flores: rascunho do CapCut, item 22 e item 23). A versão é identificada pela DATA (não por v18/v19: o claude.ai conta os envios com outro número).

## Referências e rodadas de comparação (set–out/2026)

## A referência que manda

`HUB Radar do Campo\Claude\videos exemplos\REFERENCIA MONTAGEM - Carrascal (feito a mao) TIKTOK.mp4`

O usuário montou esse vídeo à mão com o mesmo material que o garimpo baixou, enquanto uma versão automática era montada em paralelo. A comparação das duas deu origem a esta versão da skill. A automática estava tecnicamente correta, mas parecia outro canal. O que separa as duas, em ordem de impacto:

1. **Matéria-prima.** Mais da metade do vídeo dele saiu de um único clipe que a automática nunca abriu: um "react" de 96s cujo miolo (3–57s) eram 54 segundos limpos filmados da arquibancada, seguindo o protagonista. Ele também aproveitou *trechos* de clipes que a automática descartou inteiros (um círculo vermelho de destaque, o ângulo depois de uma legenda queimada).
2. **Torcida em planos longos.** Cerca de 23 planos por minuto, média ~2,6s, com takes de torcida de 5 a 8s cobrindo várias frases seguidas. A automática fez 41 planos por minuto, quase tudo de transmissão.
3. **Protagonista na tela.** Nas falas genéricas ele mostra o jogador andando em campo, não torcida nem estádio. Abre e fecha com o mesmo close do jogador.
4. **Narração enxuta.** Na referência ele acelerou a 1,2x (72,5s viraram 60,3s). Em set/2026 o usuário mudou a regra: **não acelerar**, só cortar as pausas entre os trechos (ver Passo 1).
5. **Lance-chave legível.** Plano aberto do lance inteiro, depois o close, em velocidade normal, depois um 2º ângulo. Nada de câmera lenta esticada.
6. **Legenda karaokê.** A palavra *falada* fica amarela e o amarelo anda palavra por palavra. Uma linha só, fonte menor, no meio da tela.

Segunda referência, **Faiq Bolkiah** (set/2026): `Videos prontos\Shorts\O jogador mais rico do mundo está desempregado\Videos prontos\O jogador mais rico do mundo tá desempregado. TIKTOK.mp4` (e `YOUTUBE`). O usuário remontou à mão partindo do corte automático. O que ele mudou e virou regra:
- **frase-ponte de loop** no fim (Passo 1b)
- **-10 LUFS** e trilha dele por baixo
- **marca do YouTube pequena no canto superior direito**
- **imagem literal** onde a fala nomeia um grupo ou uma coisa (Passo 3, item 7)
- "sem legenda" **sem marca**, porque ele edita a partir dele

Terceira referência, **Palermo e Paulo Diogo** (set/2026): `Videos prontos\Shorts\Jogadores que se machucaram comemorando gol\Videos prontos\Ele perdeu o dedo comemorando… e o juiz ainda deu amarelo TIKTOK.mp4`. O usuário partiu do corte automático e manteve o miolo (33–70s) igual. Isso aprovou a tela cheia com o zoom seguindo o lance e o desfoque do ferimento. O que ele mudou e virou regra:
- **gancho = prévia do lance-chave** (Passo 3, item 9), não o ferimento
- **imagem literal da ação da frase:** "se machucaram comemorando" pede a comemoração, não a ambulância (Passo 3, item 7)
- **gol no replay fechado seguindo a bola**, em vários ângulos, e não o plano aberto em que a bola some (Passo 4)
- **seta vermelha** apontando o protagonista no quadro confuso, com o plano segurado enquanto a narração descreve a lesão (Passo 5)
- **fonte onde o assunto ocupa mais pixels**, e não a mesma cena com zoom de 3,7x (Passo 5)

Quarta rodada, **Kane (Inglaterra x Espanha) e Atlético-GO** (27/set/2026). O que o usuário corrigiu e virou regra:
- **gancho no momento mais forte, já no primeiro segundo:** no Atlético-GO abri no goleiro comemorando no apito e só depois vinha o grito. Ele achou que "não prende". Refeito abrindo direto no goleiro gritando para o camarote (o payoff), e aprovou (Passo 3, item 9)
- **fala factual pede a imagem do fato:** "quatro clássicos, uma derrota, três empates… viu o rival ser campeão goiano" coberto com torcida do jogo = "sem contexto, mostra muita torcida". Trocado por placar dos jogos anteriores, rival comemorando na final, a taça e o rival campeão (Passo 3, item 10)
- **prévia de suspense:** no Kane, logo depois do rosto no gancho, ele pediu o replay com círculo no pé em câmera lenta **cortado antes do escorregão**, para segurar até a revelação (Passo 3, item 11)

Quinta rodada, **Ronaldo no banco e Arrascaeta x Estudiantes** (28/set/2026). Ele refinou no editor em cima do `completo-sem-legenda` (mesma duração, mesmo corte). Comparação quadro a quadro com `compara_edicao.py` e `lado_a_lado.py`:
- **lance-chave inteiro, num take só:** no Arrascaeta, eu abri com a queda como prévia e, na hora da narração ("escorregou sozinho, caiu com o braço esticado e o punho quebrou"), picotei em 4 cortes (círculo vermelho, replay, close caído). Ele trocou tudo pelo **mesmo clipe do gancho, contínuo**, do domínio até ele no chão (Passo 3, item 12)
- **assistência/gol = o lance; sem lance bom = o rosto dele:** "deu assistência do primeiro gol e fez o segundo" estava coberto com replays onde os jogadores ficam pequenos e parados. Ele trocou por closes dele sorrindo e gritando. Regra dele: mostre o lance se houver com qualidade; se não houver, close da reação/emoção; nunca o lance com jogador pequeno e parado (Passo 3, item 13)
- **emoção do protagonista nos fatos dele:** no Ronaldo, "sem entrar em campo" (Euro 2008) virou o close dele chorando, no lugar do plano aberto do jogo; o banco virou enquadramento fechado nele, sem o técnico na frente (Passo 3, item 7)
- **loop pelo rosto:** no Ronaldo ele abriu e fechou com o mesmo close do rosto rindo (Passo 3, item 4)
- **transições sim, SFX não:** manteve o flash/zoom e a grade de arquivo (`posfx.py`), tirou os nossos efeitos sonoros e pôs a trilha dele, a mesma nos dois, começando ~15 dB abaixo da voz e subindo em degraus (~35s e ~53s) até ~8–10 dB abaixo
- **legenda:** refez no CapCut (mesmo estilo, ~55% da altura). A automática dele errou "o punho quebrou" → "Pedro quebrou"; avise nomes e trechos arriscados na entrega (Passo 6)

Sexta rodada, **Vini ofereceu o pênalti ao Bruno (Austrália 2x4 Brasil)** (29/set/2026). Refinou em cima do `completo-sem-legenda` (mesma duração); manteve ~85% do corte: o trecho da Copa com `flashback`, a foto do Ancelotti, os closes do Vini, a entrevista e o loop. O que ele trocou:
- **o chute tem que estar no plano:** "empata… com o Raphinha, de pênalti" estava num ângulo cinematográfico da TNT atrás da trave que começava **depois** do chute (goleiro já no chão). Ele trocou pela transmissão aberta do compacto da ge (corrida → chute → bola na rede), com a logo da ge fora do quadro (Passo 3, item 14)
- **o lance do payoff não repete os quadros do gancho e termina na rede:** em "ele bateu rasteiro e fez o quarto" eu repeti o trecho do gancho, e a câmera saía da bola antes do gol (campo vazio no fim). Ele pôs outra transmissão, **com o placar 2T 34:29 AUS 2x3 BRA na tela**, seguindo até o goleiro caído e a bola na rede. Placar de transmissão é prova, não sujeira (Passo 3, item 14; Passo 5)
- **zoom de aproximação quando a ação está pequena:** no take da arquibancada da discussão na marca, no gol do Bruno visto de longe e no Vini derrubado, ele fechou mais o quadro (punch-in progressivo) até os jogadores ficarem legíveis. Não é o zoom excessivo do Palermo: é fechar na ação quando ela ocupa menos de ~1/4 da largura (Passo 5)
- **fato genérico sem pessoa aleatória:** "segundo amistoso entre os dois em quatro dias" estava no telão com o rosto do Otávio (goleiro que nada tem a ver com o roteiro). Ele trocou pela **roda da Seleção abraçada** no gramado. Não mostre de rosto alguém que o roteiro não cita (Passo 3, item 7)
- **gancho mais seco:** o close do Vini durou ~0,7s (eu fiz 1,1s) e o chute entrou direto, sem o `flash` no primeiro corte
- **áudio:** sem SFX; trilha começando ~17 dB abaixo da voz, subindo em degraus (~32s para ~-11 dB, ~46–54s para ~-8/-9 dB). Publicou a -11,1 LUFS (manteve o nosso nível)
- **legenda:** refez no CapCut a ~62% da altura. A automática errou "Noruega" → "doruega", "Ancelotti" → "ancelote", "Raphinha" → "Rañnha"; liste esses nomes na entrega (Passo 6)

Oitava rodada, **Argentina sem a camisa 10** (01/out/2026). Ele publicou **o nosso corte sem mudar nenhum quadro nem a legenda** (`compara_edicao.py`: zero trechos de imagem trocados), depois de pedir uma troca de gancho: a camisa ROMERO 13 pendurada no vestiário (objeto parado, bonito, mas não prende) virou **o Nico Paz pulando na comemoração, de costas com a 18** (a pista visual da revelação, em movimento). Só acrescentou a trilha, no padrão que o `guia_trilha.py` agora calcula: entra ~1s, ~17 dB abaixo da voz; abaixa ~4s antes da revelação; batida nos `flash`/`flashback_in`; sobe ~3s depois da revelação para ~11–12 dB; sai ~2s antes do fim (loop só com voz). -10,4 LUFS.

Nona rodada, **Modric aplaudido em Sevilha e a raça do Endrick** (comparados em 02/out/2026). Nos dois ele partiu do `completo-sem-legenda` (mesma duração) e manteve **~90% do corte**. Trocou só o **gancho e o shot de loop** (os dois), e no Modric mais dois trechos de fato. Para isso baixou clipes por conta própria (arquivos `<id>.mp4` em `clipes/`):
- **gancho = pessoa em ação, nunca torcida genérica, mesmo que a torcida seja o auge da história:** no Modric eu abri na arquibancada de pé aplaudindo (o clímax do roteiro), e ele trocou pelo **Yamal agachado sentado na bola** (o craque da goleada, num gesto que viralizou), filmado da arquibancada, cobrindo "a Espanha meteu 4 a 1 na Croácia". O loop fecha no mesmo take do Yamal. Gancho de fato coletivo ("a Espanha meteu 4 a 1") = o rosto/gesto de quem representa o fato (item 19), não a massa (Passo 3, item 9)
- **gancho em filmagem de torcida quando ela pega o mesmo momento:** no Endrick eu abri na câmera alta da TV com ele já no chão; ele trocou por um vídeo da arquibancada, na altura dos olhos, do **bolo inteiro acontecendo** (empurra-empurra → mão no rosto → queda), que o garimpo não tinha achado (@trent_1228, "Endrick 1 vs 11"). Mostra a ação e a escala da confusão, e foge do Content ID. O loop fecha no mesmo take (Passo 3, item 9)
- **"depois do título da Copa do Mundo" = imagem do título, de outra data:** eu cobri "primeiro jogo em casa depois do título" com os fogos da entrada; ele pôs **os campeões no túnel da Copa** (Rodri 16, Yamal 19, vídeo de julho/2026 em Los Angeles). Fato de outra data citado na frase vale mais que o ambiente do dia (item 10)
- **gol narrado na transmissão aberta até a rede:** "com dois minutos, Yamal já tinha marcado" estava num take da linha de fundo que acompanhava o Yamal correndo, sem a bola entrar. Ele trocou pela transmissão aberta (chute → goleiro → rede). Torcida só vale para o gol se mostrar a bola entrando (item 14)
- **trilha (a mesma nos dois, mesmo desenho):** entra em ~1s a ~18 dB abaixo da voz; queda curta em ~33–34s (-20/-23 dB); a partir de ~35s sobe para ~-12 dB; em ~53s sobe de novo para ~-9 dB; sai em ~62s (1–2s antes do fim). Três degraus (-18 → -12 → -9), não dois. Sem SFX. -10,7 LUFS.

Sétima rodada, **Raphinha cortado da Seleção** (30/set/2026). Dessa vez ele montou **do zero**, sem partir de entrega nossa: usou os clipes do garimpo (a maior parte do vídeo) e acrescentou o que faltava. `casar_fontes.py` + folhas a cada 0,5s mostraram:
- **gancho de uma história de padrão = a imagem mais forte do padrão, não o evento mais recente:** o roteiro abria com o corte depois da Austrália, mas ele abriu no Raphinha **agachado com a comissão na Copa** (a lesão mais grave), com um **ícone sobre a cabeça dele: o escudo da CBF riscado com um X vermelho** ("foi cortado da Seleção"). Fechou no mesmo take, com o mesmo ícone, emendando no loop (Passo 3, item 15)
- **parte do corpo nomeada = aproximar nela:** em "edema na parte de trás da coxa" ele fez um punch-in na parte de trás da coxa; no infográfico, um zoom nos marcadores da coxa (item 16)
- **lugar nomeado = imagem do lugar:** "fora do jogo contra a Índia" virou um estádio de Calcutá cheio, de outro evento (o jogo ainda não aconteceu) (item 17)
- **enumeração = um corte por item:** "março, junho, setembro" virou três cortes de ~0,5s, cada um numa lesão já mostrada (item 18)
- **instituição = o rosto de quem a representa:** "a Seleção tá sugando o Raphinha?" ficou 3s no close do Ancelotti (item 19)
- **dado-resumo = infográfico de portal:** "sempre na coxa… quarta lesão em um ano" virou uma arte do 365Scores ("ALERTA LIGADO", corpo com as lesões marcadas), com a marca do portal tirada e a imagem ampliada no editor de IA. A IA deformou as letras pequenas: "COSA DIREITA", "ZORA DO MONSO", "MÚRCULO", "AMISTERO" e um escudo inventado no lugar da Austrália (item 20)
- **fato de outra data em filmagem de torcida:** a lesão contra a França veio de um vídeo da arquibancada com **o telão mostrando o placar e o tempo** (prova do jogo) e **seta vermelha** quando ele cai. Ele **segurou o lance ~8,5s**, cobrindo "lesão na coxa de novo, cinco semanas parado e ficou fora das quartas da Champions…", passando o lance **duas vezes** (com seta, depois limpo). Não cortou para Barcelona x Atlético, que tínhamos baixado (itens 6 e 10)
- **ação genérica pode vir de outra data:** "ele voltou pra Barcelona" = ele saindo de boné e mochila pela zona mista da Copa. A fala não afirma que aquilo é o dia do corte (item 7)
- **"não dá pra falar que é corpo mole"** = o momento da lesão (a prova), não um rosto qualquer
- **ritmo ~26–31 cortes/min** (média ~2s), com os inserts de 0,5s do resumo e do gancho
- **reposts de baixa resolução com momento único entraram:** 720x960 dele andando no intervalo visto da arquibancada, 720x960 do close com o médico. Momento certo em 720 vale mais que momento genérico em 1080
- **legenda do CapCut a ~70% da altura**, com erros publicados: "Rafinha" (em vez de Raphinha) várias vezes e, em 54,4–55,3s, **"Rafinha teve uma lesão" no lugar de "a coxa dele tá pedindo socorro"**. Por isso agora entregamos o `.srt` com a grafia certa (Passo 6)
- **narração:** o AI Studio não falou "sábado, em Calcutá" e trocou "inédito" por "difícil" (Passo 0)
- **áudio:** -10,3 LUFS, sem SFX, trilha começando ~14 dB abaixo da voz e subindo até ~10 dB

Décima rodada, **"Lotou pro Messi… mas não pra Seleção" (Índia 0x4 Brasil, 03/out/2026)**. Ele não pediu para refazer, mas apontou quatro defeitos de montagem que viraram regra (Passo 3b, Passo 5 e Passo 8):
- **zoom demais matou o contexto:** planos que existiam para mostrar escala (Salt Lake lotado em 2011, o estádio no hino, a placa, o cartaz do jogo) foram recortados numa fatia de 9:16 com zoom 1,5–1,75 ou upscale de 3,5–5,3x. O espectador não via que o estádio estava cheio, nem que era um estádio. Plano de escala/lugar não leva zoom (Passo 5)
- **torcida genérica no lugar da frase:** "um torcedor resumiu: é um buraco no bolso" foi coberto com arquibancada vazia, quando o garimpo tinha o torcedor revoltado falando do preço do ingresso (CNN, 48–55s). "Bandeira do Brasil era difícil de achar" mostrou justamente o grupinho com bandeiras do Brasil (a imagem contradizia a frase). "Quem chamou atenção cantando o hino foi a própria imprensa brasileira" mostrou fotógrafos indianos numa coletiva. "Ingresso começava em 3.500 rúpias" e "dez meses depois" viraram estádio vazio genérico. Cada frase inteira precisa da imagem do que ela diz (Passo 3b)
- **corte antes do impacto:** o indiano com a camisa 10 da Argentina batendo a cadeira foi cortado em 22,07s, e a cadeira voa em 22,0–22,2s e ele bate de novo em 23,7–24,2s. O momento mais forte do vídeo inteiro saiu sem o golpe (Passo 3b, item 3)
- **gancho fraco:** abri no grupinho de brasileiros no setor vazio (plano parado, de longe). O gancho tinha que ser o take mais chocante do material: o torcedor arrancando e jogando a cadeira, ou o gramado invadido, cortado logo depois do golpe, e só então a narração do "detalhe" (Passo 3b, item 1)

Décima primeira rodada, **"Bruno Duarte apagou e ninguém viu" (Botafogo 1x2 Vasco, 08/out/2026)**. **Aprovado sem nenhuma mudança** ("ficou perfeito e muito bom"). Antes de montar, ele pediu três coisas, e o resultado virou o modelo para roteiro de um incidente (desmaio, lesão, briga):
- **Gancho = prévia do incidente:** o replay fechado da joelhada e da queda já no quadro 1, depois o 2º ângulo (arquibancada) dele de joelhos indo ao chão. Corta antes do socorro.
- **"Que os vídeos se completem":** depois do contexto, o incidente volta **inteiro e em ordem cronológica**, cada frase coberta pelo momento seguinte do mesmo evento: assistência → dividida ao vivo até o chão → replay da joelhada → ele se contorcendo → jogo parado com ele caído no canto → ele sozinho e imóvel → companheiro dando tapinhas (take contínuo) → médicos → maca → substituto entrando → maca saindo vista da arquibancada. Nada de imagem fora daquele trecho (Passo 3, item 21).
- **Jogador sempre bem enquadrado, sem zoom enorme:** zoom de 1,2–1,6 com `keys` seguindo a bola e o jogador. O mesmo zoom tirou as logos de TNT e Prime e o texto da CazéTV.
- **Espinha num clipe só:** um vídeo de transmissão de 50 s (xsports) cobria o incidente inteiro e foi a base, usado em ordem. Quando a frase era maior que o trecho, desacelerou 0,6–0,75x em vez de trocar de assunto.
- **Torcida 16%** e foi aprovado: o incidente só existia na transmissão (Passo 5, meta de torcida não se aplica).
- A revisão a cada 0,1s pegou o que faltava: logos de TNT/Prime, a dividida ao vivo mal enquadrada e a frase "o Colidio lança o David" coberta por outro lance. Foram 3 rodadas de rascunho, e só depois os 4 arquivos.
- A narração do AI Studio veio **sem a frase de abertura** do roteiro (o gancho do Tite). Avise antes de montar (Passo 0).

Décima segunda rodada, **comparação em lote de 17 vídeos (02/out a 17/out/2026)**, `compara_edicao.py` entre o `completo-sem-legenda` e o `TIKTOK.mp4` publicado:
- **8 de 17 saíram sem nenhuma troca de imagem, só a trilha** (Hojlund, Vitor Hugo, Luiz Araujo/Gabigol, CR7 suspenso, Pulgar, Vasco/Bombonera, Bruno Duarte e Cunha, o de 17/out). Padrão atual está certo: não mexa no que a rotina já faz.
- **Gancho literal à primeira frase (Messi, "Todo mundo viu o Messi se despedir"):** abri no Messi rindo com os companheiros (outro momento). Ele abriu no Messi emocionado no telão e nos drones com o 10, a própria homenagem. A imagem de 0–2s mostra o fato da primeira frase, não a pessoa em outro contexto (itens 9 e 10).
- **Sem flash branco no 1º quadro do gancho (Endrick x Roma, Drones):** ele tirou o `flash` do primeiro corte e abriu o quadro um pouco mais (mais da ação visível). Gancho seco, como no Vini. Não ponha `fx: flash` no shot 1.
- **Loop só por rosto ou ação, nunca por react/webcam (Drones):** o último shot era um streamer de webcam (react); ele fechou no close do Messi olhando para cima sorrindo, e o gancho recomeça nos drones. No Isaac Romero ele reajustou o shot final para o gesto do próprio gancho (mão levantada); no Tite encurtou 0,4s e fechou mais no árbitro com o cartão. Confira o último shot no `bordas_XX.jpg`: sem pessoa de webcam nem texto de fonte.
- **Plano de lugar legível (Isaac, 5,8–7,7s):** eu usei o gramado visto de cima, estreito, vertical, com poucas pessoas. Ele pôs o plano horizontal da cerimônia com os times alinhados. Plano de contexto mostra gente e cena, não só grama.
- **Flashback P&B só quando a fonte é antiga e curta (Rossi):** ele tirou a grade escura e preta e branca dos trechos de fato antigo e deixou colorido, e refinou tudo no Concat (65,17s). Com muito trecho de arquivo, o P&B cansa; use `flashback` só em 2 ou 3 shots.
- **Vini expulso:** ele reeditou a segunda metade para 60s, trocando a súmula em texto (36s) pelo árbitro mostrando o cartão em campo e fechando no Vini apontando para a torcida. Fato visual ganha da súmula em texto quando existe o lance.
- **Jorge Jesus (26–27,5s):** só reenquadrou o post do Instagram (mais alto). Calcutá (11,0–11,8s): troca de 0,8s, não identificada.

Décima terceira rodada, **Leo Flores, Andreas Pereira e Bernal x Yamal (17 e 18/out/2026)**. O Leo Flores saiu **sem nenhuma troca de imagem**, só com a trilha (-10,6 LUFS). O Andreas e o Bernal ele refinou **dentro do rascunho do CapCut que nós geramos** (Passo 9). Por isso a comparação foi pelo próprio projeto: o `draft_content.json` que geramos contra o que ele salvou. Ficaram a legenda (fonte, tamanho, altura) e a trilha do modelo dele sem mexer. O que ele mudou:
- **"O motivo da expulsão" = o cartão no quadro (Andreas, 3–8s):** eu enquadrei o árbitro da cintura para cima e o cartão vermelho levantado ficou fora do quadro. Ele desceu o quadro para mostrar o cartão e os jogadores reclamando. A logo da ge entrou no canto, e ele cobriu com um desfoque retangular (máscara no CapCut). A ação vale mais que um quadro sem logo (item 23; Passo 5, marcas).
- **Detalhe pequeno num plano aberto = punch-in progressivo até ele (Andreas, 22–25s):** em "uma bola veio da arquibancada e caiu no gramado", o plano alto da Prime mostrava o campo inteiro e a bola extra era um ponto. Ele fechou de 3,16 para 4,67 seguindo a bola, até ela ficar visível (item 23).
- **Relação no espaço = abrir o quadro (Andreas, 25–32s):** no lance em câmera lenta eu fiquei fechado (1,75) no Andreas. Depois do chute, ele abriu para 1,19, para caber as duas bolas, o Andreas e o atacante. O espectador precisa ver a bola extra acertando a bola do jogo (item 23).
- **Gancho com punch-in no contato (Bernal, 0–1s):** a cabeçada na câmera da TV passou de 1,22 para 1,72 no meio do shot, fechando no instante do contato.
- **Arte parada ganha movimento (Bernal, 9,4–11,8s):** na arte "DONE DEAL" do Betis ele pôs um zoom lento de 1,0 para 1,25. Foto ou arte em tela cheia não fica estática.
- **Pan seguindo a ação** na cabeçada em câmera lenta (23–26s) e no gol do Abde. Este ele teve que refazer, porque o keyframe que eu gravei não andava no CapCut (Passo 9, tempo dos keyframes).
- **Efeitos sonoros ligados nos dois:** ele ativou a faixa SFX (que eu deixava muda) e só baixou o 1º impacto do Andreas de 0,55 para 0,43. A trilha ACIDO do Bernal saiu ~1,4s antes do fim (loop só com voz).
- **Exportou um arquivo só, com a lupa e o logo do YouTube ocultos.** Publicou a -14,4 LUFS (Andreas) e -13,3 LUFS (Bernal), porque o CapCut não normaliza. Os nossos 4 arquivos continuam a -10 LUFS.

Décima quarta rodada, **Paquetá, Kannemann, Neymar x Soteldo, Neymar x Thiago Mendes e Vitinha (19 a 21/out/2026)**. Ele refinou os cinco **dentro do rascunho do CapCut**, e a comparação foi pelo projeto (`compara_capcut.py`). Em nenhum mexeu na legenda. O que se repetiu:
- **Gancho nunca parado:** nos cinco ele mexeu no shot 1. Punch-in (Vitinha 1,05→1,76; Thiago 2,4→2,84) e pan seguindo a ação (Paquetá -0,22→+0,22; Soteldo; Vitinha). No Kannemann foi o contrário: o nosso pan pulava de lado no meio do gancho (+0,28 → -0,55), e ele abriu para 1,23 e deixou a janela quase parada sobre a ação inteira. O shot de loop leva o mesmo quadro (item 23).
- **Gancho = a humilhação/o fato do título acontecendo (Thiago Mendes):** trocou o nosso gancho por um post da ESPN que ele baixou, **os jogadores do Boca comemorando na frente do Thiago Mendes**, fechando nos jogadores (o card do post fica fora do quadro). O título dele era "…após ser humilhado na eliminação". O loop fecha no mesmo clipe a 0,33x.
- **Post citado = o post (Thiago):** em "postou uma montagem feita com inteligência artificial em que rasgava o escudo do Boca", ele pôs **a própria montagem** (repost de perfil de torcida). Item 22 vale também para arte/IA citada.
- **Janela no lado ou na altura errada:** no Soteldo, quase todos os shots da ESPN tinham y 0,26 e ele desceu para ~0 / -0,27. No Kannemann, a coletiva do Renato e os melhores momentos estavam do lado errado (x -0,43 → 0,37). Confira na revisão se o assunto está no centro da janela, não só dentro dela.
- **Duas fontes do mesmo lance: a limpa (Soteldo):** trocou 3 shots do post da ESPN com cards de texto queimados ("…ado ilegal", "NEYMAR PARTIU PARA CIMA DO SOTELDO, MAS…") pelo outro post da ESPN do mesmo lance, sem texto.
- **Enquadramento ruim por sujeira = voltar ao garimpo, não aproximar (regra de 29/out/2026, Giay):** se um shot só fica bem enquadrado com zoom acima de ~1,6 ou com recorte grande para esconder texto, logo, moldura ou tela dividida, procure o MESMO vídeo/lance numa versão limpa (fonte original, outro repost, outra rede) e troque antes de entregar. Vale sempre. Só aproxime ou tampe se não existir versão limpa, e diga na entrega quais shots ficaram assim.
- **Texto queimado sem fonte alternativa = desfoque retangular (Paquetá):** cópia do clipe por cima, com máscara desfocada só sobre o texto. Mesma regra do Andreas (Passo 5, marcas, 1b).
- **Menos cortes no trecho da prova (Thiago, Kannemann):** quatro shots curtos de fontes diferentes viraram o post do Neymar com a camisa do Paredes (punch-in com pan) + uma reação em câmera lenta 0,62x por 6,3s. No Kannemann, tirou um insert de 0,7s de outra fonte no meio de um lance.
- **Prova segurada até o fim (Paquetá):** os cards de comentário (corintiano e palmeirense) entram empilhados e ficam até o último quadro, em vez de entrar e sair um por um.
- **Zoom menor em lance coletivo:** no Thiago ele abriu quase todos os shots do começo (1,5→1,25; 1,67→1,36; 1,93→1,55). Zoom forte só em detalhe ou rosto.
- **Flashback P&B mais longo** (Kannemann 58–68s, Vitinha 46–51s): ele esticou a faixa do filtro para cobrir o trecho de outra época inteiro.
- **Trilha do modelo mais baixa em todos:** de 0,34 para 0,15 / 0,16 / 0,09 / 0,07. O `capcut_projeto.py` agora grava 0,12 na trilha principal do modelo (Passo 9). Nos vídeos sem SFX, ele apagou a faixa SFX vazia.
- **Faltou no garimpo:** o post da ESPN da comemoração na frente do Thiago Mendes e o repost da montagem de IA. Ele baixou os dois.

Décima quinta rodada, **Carlos Miguel e a toalha, Thiago Silva 2008–2026 e Cetré e o pênalti repetido (22 e 23/out/2026)**, comparados pelo projeto do CapCut (`compara_capcut.py`). Legenda intacta nos três. O que ele mudou:
- **Punch-in no lance, de novo:** gancho do Thiago Silva de 1,0 para 2,23; shot 1 do Carlos Miguel com zoom 1,9→2,65 e pan; vários shots do Thiago com pan seguindo a ação onde a nossa janela era fixa. Shot parado com ação acontecendo continua sendo o ajuste nº 1.
- **Gancho pelo pico em câmera lenta (Cetré):** trocou o rosto de 0,6s por um close dos pés a 0,81x com pan, e repetiu esse mesmo take no meio (35,4s e 49,2s) e no loop. O lance-chave volta como refrão visual.
- **Trecho da prova inteiro numa fonte só, em câmera lenta (Carlos Miguel 38,5–44,8s):** dois shots de fontes diferentes viraram um take da getv a 0,5x por 6,3s.
- **Desfoque retangular de texto/logo em série (Cetré):** 9 cópias do clipe da Conmebol por cima, na mesma posição, para mascarar o texto queimado.
- **Flashback P&B:** no Thiago Silva ele apagou o filtro (61s de arquivo em P&B cansava); no Cetré trocou o filtro por outro. Trecho longo de arquivo fica colorido.
- **Trilha ainda mais baixa** (0,08–0,11) e faixa SFX vazia apagada.

Décima sexta rodada, **CR7 e o gol do Girotto, Toney e o vídeo de IA, Neymar e a Lei Vini Jr, Piqué e a manita, Yamal de cara fechada (24 a 27/out/2026)**. Os cinco foram refinados no rascunho do CapCut e comparados corte a corte com `analisa_capcut.py` (a frase narrada e a nota de cada shot ao lado do que ele mudou) e `pares_quadros.py` (nosso x dele no mesmo instante). Legenda intacta nos cinco. O Hinestroza não foi mexido nem exportado. O que ele mudou:
- **Metade dos "reenquadramentos" eram desfoques nossos que não chegavam ao CapCut.** No CR7, os shots 1, 8, 9, 23, 36 e 38 (os que tinham `borrar` na logo da Thmanyah) ganharam zoom 1,2–1,25 deslocado para tirar a logo. No CR7 e no Piqué ele refez à mão 9 desfoques (cópia do clipe + máscara Retângulo + efeito Desfocar). O `capcut_projeto.py` agora leva cada `borrar` assim (faixa DESFOQUE) e as setas/círculos (faixa SETAS) (Passo 9).
- **Marca que escapou do nosso desfoque:** no CR7 a caixa do `borrar` ficou logo acima do "FIFA+", e a logo apareceu nos 5 shots da Copa 2022. No Neymar, o "g" da ge no canto superior direito sobrou em 4 shots do vídeo da ge (ele fechou de 1,20 para 1,22–1,24 e deslocou).
- **Gancho = o pico físico, não a provocação (Neymar):** abri no Neymar de costas, falando com a mão na boca. Ele abriu na confusão (Neymar partindo para cima e sendo segurado, com pan) e fechou o loop no mesmo take a 0,71x. A mão na boca desceu para o shot 2, a 0,63x, em "o nome da regra que tirou ele de campo": a regra pune cobrir a boca, então a imagem é o gesto (item 7). O nosso shot 2 era um reserva de colete amarelo, com o Neymar fora do quadro.
- **Gancho começa perto do pico (Piqué):** a mesma arrancada do Mbappé, mas entrando 2,2s depois (o chute aparece logo), sem pan. O loop acompanhou.
- **Gancho literal com contexto (Yamal):** o nosso era um close extremo do rosto (da testa ao queixo, parado). Ele baixou um vídeo postado no dia seguinte (@kart_x, 960x720) com o Yamal sentado no momento do anúncio e gente se levantando ao lado, com pan a 0,81x, e fechou o loop nele. Também trocou os outros closes extremos ("dessa cena", "ficou em terceiro", "cara fechada") por fotos nítidas (photo mode do TikTok) que mostram cabeça, ombros e quem está do lado, com punch-in lento.
- **O ponto da prova numa câmera lenta progressiva (CR7):** "na câmera lenta começou a dúvida… a cabeça de um zagueiro brasileiro, o Andrei Girotto" (21,8–28,4s) tinha 4 cortes (lupa, círculo, seta, Girotto). Ele pôs o replay da TV do mesmo instante, contínuo, desacelerando 0,64x → 0,23x → 0,17x até o contato da bola com as cabeças. É a regra do Carlos Miguel (prova numa fonte só, em câmera lenta) levada ao extremo: quanto mais perto do detalhe, mais lento.
- **"O mesmo lance" = os mesmos quadros (CR7):** em "não dá pra ver se o Cristiano toca" e em "a Opta olhou o mesmo lance" ele usou o mesmo trecho do vídeo por trás do gol, com pan seguindo o CR7. Quando a frase diz "o mesmo lance", repetir de propósito é a imagem literal.
- **Punch-in no dado lido (CR7, Toney):** na página da Liga, zoom de 2,27 para 3,03 até "Ronaldo 49'"; na súmula, de 1,5 para 2,0 na linha do gol; no post do relatório médico, de 1,0 para 1,41 subindo até o texto da lesão.
- **Detalhe nomeado = punch-in nele (Neymar):** "colocou a mão na frente da boca" e "cobriu a boca" passaram de 1,0 para 1,62–1,67 no Neymar.
- **Ação inteira no quadro:** a falta do Félix com zoom 1,89 cortava o corpo dele, e ele abriu para 1,58. "Ele ainda fez outro" ganhou pan do CR7 até a bola entrar. "O Toney abriu o placar" passou a começar 0,7s antes, no cabeceio, com pan até a rede (item 14).
- **Pessoa nomeada entra na palavra (Yamal):** em "enquanto o Mbappé…", ele puxou o corte do Mbappé na plateia 0,2s para trás, para a imagem cair na própria palavra, e não na pausa seguinte.
- **Texto estrangeiro lido = tradução na tela (Toney):** nos posts do Al-Khaleej com legenda em árabe, ele escreveu a tradução que a narração lê, entre aspas, em Montserrat itálico branco, logo acima da legenda árabe ("Parabéns, era só brincadeira"; "perdemos pro Al-Ahli e vamos ter que aguentar a zoeira por uma semana.").
- **Seta seguindo o protagonista na multidão (Yamal):** em "deu um abraço rápido no Kane", seta vermelha (`imagens edição\seta vermelha e  inclinada.jpg`) com keyframes acompanhando o Yamal por 1,6s.
- **Flash só onde há virada:** tirou o flash do "ele admitiu" (selfie do Neymar) e o da prévia do Yamal caído no clássico. Essa prévia ele trocou pelo salão da cerimônia em "ainda pior pra ele": a imagem de lesão sugeria um fato que não aconteceu.
- **Flashback P&B no trecho de outra época inteiro, e só nele:** no CR7 o filtro parava antes do último shot da Copa 2022 (faltou `flashback` no shot 30), e ele esticou até 64,7s. No Piqué encurtou para só a foto antiga da manita e deixou colorido o telão do Camp Nou de 2010.
- **Música (os cinco):** a 2ª trilha do modelo acabava em ~66s, e ele esticou até ~1s antes do fim em todos. Levou a virada (fim da 1ª trilha + impacto "Dramatic" + entrada da 2ª) para a revelação quando o padrão caía longe dela: no CR7, "gol contra do Girotto" (36,6s); no Piqué, "o jogador que o Piqué tinha escolhido" (45,9s). Subiu o Dramatic de 0,12 para 0,24–0,43 e baixou a 2ª trilha para 0,08–0,10. O `capcut_projeto.py` faz isso agora, se a EDL marcar `"revelacao": true` (Passo 3b).

Décima sétima rodada, **Bruno Guimarães perde pênalti pro Fleetwood (28/out/2026)**, refinado no rascunho do CapCut (`analisa_capcut.py`). Legenda intacta. ~75% do corte ficou igual. O que ele mudou:
- **Gancho com o protagonista grande no contato:** eu abri no take da arquibancada atrás do gol (Bruno pequeno, de longe). Ele pôs por cima, nos mesmos 1,6s, o replay da TV por trás do Bruno, com punch-in de 1,25 para 1,58 e pan até o pé na bola. Arquibancada vale no gancho só se o protagonista for legível; senão, o replay fechado do mesmo instante.
- **Pan seguindo o rosto nos closes** (Bruno cabisbaixo, Arteta, Bruno sorrindo): a janela anda até o rosto ficar centrado, em vez de ficar fixa com ele na borda.
- **Defesa do goleiro:** a nossa janela corria para o lado depois da defesa; ele parou o pan no goleiro e na bola (o desfecho fica no quadro até o fim do shot).
- **Nome de quem comentou desfocado:** nos cards de comentário (Passo 3, item 22) ele desfocou o nome/usuário de cada comentarista (máscara retangular). Comentário anônimo entra sem o nome legível.
- **O comentário-clímax sozinho e grande:** os dois primeiros cards ficam empilhados; no último ("mas é teimoso", o mais curtido) ele tirou os outros e deixou só esse card, ampliado (1,0 → 1,31 com punch-in), sobre o replay do Bruno correndo para a bola. Refina a regra do Paquetá: a prova fica até o fim, mas a frase que fecha o vídeo tem o card dela isolado.
- **Narração:** tirou ~0,8s perto do fim, para a frase final chegar mais seca. Trilha e virada no `"revelacao"` ficaram como geramos.
- **Bug:** o `capcut_projeto.py` travava com 3 cards no mesmo shot (o 3º caía na CARDS2 em cima do 2º). Corrigido com a faixa CARDS3.

Loudness final e altura da legenda ele ajusta sempre no CapCut: no Palermo/Diogo publicou a -7 LUFS com a legenda a ~61%; no Raphinha, -10,3 LUFS com a legenda a ~70%. Os valores do Passo 6 e do Passo 7 são só o ponto de partida.

Em caso de dúvida sobre estilo, extraia quadros dessa referência (`scripts/folha_contato.py`) e compare. Ela vale mais que qualquer número escrito aqui.

## Erros já cometidos (até 28/10/2026)

- Bruno x Fleetwood (28/out/2026): gancho na arquibancada com o Bruno pequeno; nomes dos comentaristas legíveis nos cards; os 3 cards empilhados no clímax em vez do último sozinho; closes com a janela fixa e o rosto na borda.
- CR7, Toney, Neymar, Piqué e Yamal (24–27/out/2026):
  - Rascunho do CapCut sem os desfoques e as setas da EDL: ele refez à mão ou fechou o zoom para esconder a marca. Corrigido no `capcut_projeto.py`.
  - Caixa do `borrar` acima do "FIFA+" (logo à mostra em 5 shots) e o "g" da ge no canto em 4 shots do Neymar.
  - "O nome da regra que tirou ele de campo" coberto com um reserva de colete, com o Neymar fora do quadro.
  - Closes extremos do rosto do Yamal, sem contexto; falta do Félix cortada pelo zoom; prévia de lesão do Yamal sugerindo um fato que não houve.
  - P&B parando antes do último shot da Copa 2022; 2ª trilha acabando 10–14s antes do fim; nenhuma EDL com `"revelacao": true`.
- Thiago Silva (22/out/2026): o `capcut_projeto.py` travou com "SegmentOverlap" na legenda, porque palavras divididas à mão (anos por extenso) tinham tempos que, arredondados separadamente, se sobrepunham em 1 µs. Corrigido no script.

- Andreas Pereira e Bernal x Yamal (18/out/2026):
  - Parar a montagem e pedir narração nova porque deu 59,2s, quando dava para chegar a 60 com a mesma, esticando as respirações (Passo 1).
  - 1ª versão do rascunho do CapCut com o corte renderizado por cima dos brutos: zoom, enquadramento e efeitos ficaram impossíveis de mexer, a legenda saiu com outra fonte e a música do modelo dele não veio (Passo 9).
  - Keyframes gravados relativos ao segmento: no CapCut o pan e o soco ficaram parados em todo clipe com entrada > 0 (Passo 9).
  - Cartão vermelho fora do quadro em "o motivo da expulsão", bola extra invisível no plano aberto e quadro fechado demais para a bola extra acertar a bola do jogo. Ele corrigiu os três no CapCut (item 23).
  - Card "MDS olha essa expulsão", logo da Band e logo da CazéTV só vistos na revisão (Passo 5, item 0).

- Bruno Duarte (08/out/2026, aprovado sem mudanças). Erros pegos na própria revisão, antes da entrega:
  - Logos de TNT e Prime no quadro; dividida ao vivo enquadrada com o lance fora do centro; "o Colidio lança o David" coberto por outro lance. Só a revisão a cada 0,1s mostrou.
  - Narração sem a frase de abertura do roteiro, avisada só na entrega. Compare a transcrição com o roteiro antes de montar.
  - Abrir 4 ou mais folhas de contato por mensagem: várias voltaram "[media removed: request limit]". Junte num mosaico ou abra de 2 em 2.

- Calcutá / Índia x Brasil (03/out/2026). O usuário não pediu refação, mas apontou:
  - Gancho num plano parado (grupinho de brasileiros no setor vazio), com o take do torcedor batendo a cadeira disponível no material.
  - Torcedor com a 10 da Argentina batendo a cadeira cortado em 22,07s, com o golpe em 22,0–22,2s (e o segundo em 23,7–24,2s).
  - Panorama do Salt Lake lotado (2011) recortado numa fatia com upscale de 5,3x; hino, placa e cartaz com zoom 1,5–1,75. O contexto "lotou" e "estádio" sumiu.
  - "Um torcedor resumiu" coberto com arquibancada vazia, com o torcedor da CNN disponível; "bandeira do Brasil era difícil de achar" mostrando bandeiras do Brasil; "a própria imprensa brasileira" mostrando fotógrafos indianos; "ingresso de 3.500 rúpias" e "dez meses depois" com estádio vazio genérico.

- Modric e Endrick (comparados em 02/out/2026):
  - Gancho na massa (torcida de pé aplaudindo) porque era o clímax; ele quer uma pessoa em ação (o Yamal sentado na bola).
  - Gancho do Endrick na câmera alta da TV com ele já no chão, quando existia filmagem da arquibancada do bolo inteiro (o garimpo não achou; ele baixou).
  - "Depois do título da Copa" coberto com fogos do dia, no lugar dos campeões no túnel da Copa.
  - Gol do Yamal num take de torcida que não mostrava a bola entrar.

- Argentina sem a camisa 10 (01/out/2026):
  - Gancho num objeto parado (camisa pendurada no vestiário) escolhido por ser bonito e fechar o loop; ele trocou por ação com a pista visual (Passo 3, item 9).
  - `--shots 01,41` no PowerShell pulou o shot 01 sem aviso; o rascunho saiu com o gancho velho.
  - `--sem-bordas` no vídeo inteiro por causa de um alarme falso num shot só (use `ignorar_bordas` no shot).

- Raphinha cortado da Seleção (30/set/2026). Ele montou do zero; estes são os pontos em que a skill deixava a desejar:
  - Sem ícone de veredito no gancho: ele pôs o escudo da CBF riscado sobre a cabeça do Raphinha (item 15).
  - Gancho pelo evento mais recente num roteiro sobre um padrão: ele abriu na lesão mais forte, a da Copa (item 9).
  - Sem punch-in na parte do corpo narrada, sem imagem do lugar (Calcutá), sem um corte por item na enumeração, sem o rosto do técnico em "a Seleção tá sugando" (itens 16–19).
  - Legenda publicada com erros da automática do CapCut ("Rafinha"; "Rafinha teve uma lesão" no lugar de "a coxa dele tá pedindo socorro"), porque ele não tinha o texto certo para importar. Agora sai o `.srt`.
  - Narração do AI Studio sem "sábado, em Calcutá" e com "difícil" no lugar de "inédito", sem aviso antes da montagem (Passo 0).

- Endrick x Austrália (29/set/2026):
  - Keys de enquadramento escritas em tempo do vídeo final: a janela ficou parada e o gol da arquibancada saiu com a jogada fora do quadro.
  - Quatro defeitos de borda de shot (quadro de outro vídeo com marca "BTB", fusão, quadro de outra cena, quadro escuro) que a auditoria não pegou e o passo de 0,1s quase deixou passar. Agora há as folhas `bordas_XX.jpg`.
  - Montar com a skill instalada desatualizada (sem a v16): o HUB estava na frente. Confira a versão no começo.

- Vini x Austrália (29/set/2026):
  - Pênalti do Raphinha num ângulo da TNT que começava com o goleiro já caído: o chute não aparecia.
  - Payoff ("bateu rasteiro e fez o quarto") repetindo os quadros do gancho, com a câmera saindo da bola antes do gol.
  - Take de arquibancada, gol do Bruno e Vini derrubado com os jogadores pequenos demais; ele fechou o quadro na ação.
  - Telão com o rosto do Otávio em "segundo amistoso entre os dois": pessoa que o roteiro não cita, em close, numa fala genérica.

- Ronaldo e Arrascaeta (28/set/2026):
  - Picotar o lance-chave (a queda do Arrascaeta) em 4 cortes com círculo, câmera lenta e replay, em vez de repetir o take contínuo do gancho no momento da narração.
  - Cobrir "deu assistência… fez o segundo" com compacto horizontal em que os jogadores ficam pequenos e parados. Sem lance com qualidade, o close da comemoração dele.
  - Cobrir "sem entrar em campo" (Euro 2008) com plano aberto do árbitro, em vez do rosto do Ronaldo chorando; banco com o técnico na frente.
  - Deixar passar assinaturas pequenas (@brayanncrf, SportyNet, FUTSTATUS) e uma marca da CONMEBOL até a revisão final.
  - Usar foto de agência (Infobae) e print de post em falas que tinham vídeo do protagonista disponível no próprio garimpo; a revisão pediu vídeo com contexto.

- Kane e Atlético-GO (27/set/2026):
  - Abrir o Atlético-GO no goleiro comemorando no apito, com o grito para o camarote só depois. O auge (o grito) tem que ser o quadro 1.
  - Cobrir retrospecto e título ("quatro clássicos… campeão goiano") com torcida da Serrinha. Fato pede placar, taça e o rival campeão, mesmo que seja de outra data e exija voltar ao garimpo.
  - Deixar passar, até a revisão: pedaço do logo ITV, "diariodegoias.com.br" no rodapé, assinatura "@perfil" na borda de baixo, card do post da ESPN no shot de loop e uma fusão de cena da fonte. Meça cada fonte com `grade.py` antes da EDL (rodapé e 0–5s incluídos) e olhe o fim de cada trecho de compacto.
  - Círculo de destaque posicionado ao lado da bola no 1º render da prévia do Kane. Confira `destaque` no shot renderizado.
  - Rodar o `narracao.py` com o limiar antigo (-35 dB): só 2 pausas, e a auditoria recusaria quase todo corte. O padrão agora é -30 dB/0,12s.

- Fechar o vídeo num close de outro clipe porque o roteiro não tinha frase-ponte (Rayan x Austrália). A imagem tem que fazer loop sempre.

- Palermo/Diogo (set/2026). Na 1ª versão, zoom de até 9x em fotos de repost, que tirou o contexto do lance. Na 2ª, faixa 16:9 com fundo desfocado ("não gostei do desfoque"). O certo é tela cheia com zoom moderado seguindo a bola (`keys`/`segue`).
- Gancho com a mão ferida desfocada no lugar do lance (o Diogo subindo no alambrado). "Ele se machucou comemorando" coberto com a ambulância em vez da comemoração. Gol do Palermo num plano aberto fixo com a bola minúscula e um jogador adversário no centro. Muro caindo numa faixa pequena com zoom de 3,7x (borrão). Corte para o rosto no chão enquanto a narração ainda descrevia o muro sobre a perna (o usuário segurou o plano e pôs seta vermelha).
- Foto de outra pessoa (Wikimedia "Paulo Diogo") usada como o protagonista. Confira identidade contra os quadros do lance.

- Entregar com a marca de outros perfis e emissoras (WAMO, ge, sportv, Paramount+) aparecendo junto com a do canal (Rayan x Austrália). Use enquadramento, nunca `delogo`, que deixa borrão.

- Tampar marcas clonando textura sobre torcida, rosto, camisa e placa (Matheuzinho): ficou "reflexo muito aparente" no vídeo todo, com remendo bege, rostos duplicados e logo duplicado. Enquadre ou troque o trecho.
- Shot atravessando o corte interno da fonte e shots entrando no fade para preto de compilado (Matheuzinho): 1 quadro de outra cena piscando no começo do vídeo. Isso não pode acontecer; a auditoria agora barra.
- Shots com SAR diferente (1756:1755 nos sem máscara), que reiniciavam os filtros no meio do vídeo. O `prep_shots.py` agora força `setsar=1` e as tags de cor bt709.
- Usar o post/print da GE TV com texto no lugar do vídeo do lance, zoom 2x em entrevista cortando o rosto e elenco genérico em "primeira convocação" (Matheuzinho).

- Montar sem abrir os clipes de `_extras`: o melhor material do vídeo ficou de fora.
- Descartar clipe inteiro por ter react, legenda ou círculo; o certo é descartar só o trecho.
- Picar takes contínuos de torcida em vários ângulos de transmissão (41 planos/min contra os ~23 do usuário).
- Cobrir falas genéricas com torcida e estádio em vez do protagonista; abrir no estádio em vez de no jogador.
- Lance-chave em câmera lenta 0,5x esticado por 9s, sem o plano aberto que mostra o jogador voltando.
- Narração com as pausas longas intactas (hoje elas são cortadas; acelerar a 1,2x foi a regra antiga, trocada pelo usuário em set/2026). Legenda com palavra-chave fixa, grande, em 2 linhas e a 74% da altura.
- Marca d'água colada com `paste(logo, pos, logo)`: o alpha aplicou duas vezes e a logo sumiu (opacidade efetiva ~0,03). E a checagem numérica da entrega não pegou; olhe o recorte.
- Encadear 81 `overlay` no ffmpeg para a legenda: metade sumiu em silêncio. Use uma faixa única.
- `adelay`+`amix` para SFX com offset grande: os efeitos depois do primeiro não entraram. Use a cama em numpy.
- `setpts=N/FRAME_RATE/TB` no concat derrubou 1/3 dos quadros. Concatene com `-c copy`.
- Remotion com 1440x2560: o compositor falha no seek. Use o pipeline ffmpeg + PIL.
- Áudio final em -18,9 LUFS, baixo demais. Depois, -13,4; o usuário publica em -10.
- "Sem legenda" com a lupa gravada: o usuário editou a partir dele, e a lupa do TikTok vazou para a versão do YouTube (Faiq Bolkiah).
- Evitar a imagem literal (o time campeão com a taça) por medo de Content ID e cobrir "time principal" com estádio vazio.
