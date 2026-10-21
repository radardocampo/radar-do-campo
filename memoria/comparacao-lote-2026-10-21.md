---
name: comparacao-lote-2026-10-21
description: "Comparação de 21/10 dos 5 vídeos de 19–21/10 (Paquetá, Kannemann, Neymar/Soteldo, Neymar/Thiago, Vitinha), todos editados no rascunho do CapCut; lições por vídeo"
metadata:
  node_type: memory
  type: project
  originSessionId: 540acc1c-d646-4cb1-bb17-275cd75289d4
  modified: 2026-10-21T22:29:33.721Z
---

Os 5 foram refinados no rascunho do CapCut ("Radar - <job>"). Por isso a comparação é por projeto: regerar o original com capcut_projeto.py --raiz <job>/_montagem/cmp/capcut_orig (modelo 0417…(15), só os JSON) e comparar com scratchpad cmp_draft.py. Diferenças de ±0,01s em st/du são arredondamento do CapCut, não edição. Continua de [[comparacao-lote-2026-10-17]].

**Paquetá (19/10):** manteve os 28 shots, a legenda e a ordem.
- Gancho (ig_getv): acrescentou um pan horizontal (x de -0,22 para +0,22) seguindo o lance. Nada de quadro parado no gancho.
- Num replay (tt_getv, 16,2s), fechou um pouco (1,22→1,25) e reposicionou. Em outro shot (34,8s), pan de 0 para -0,22.
- Take da torcida/jogada do X ColunadoFla (27–33s): pôs uma cópia do clipe por cima, com desfoque retangular sobre o texto queimado da fonte (máscara no CapCut). Mesma regra do Andreas: borrar a sujeira e manter a ação.
- Final (54–66s): os cards de comentário (corintiano + palmeirense) ficam empilhados e **seguram até o fim do vídeo**, em vez de entrarem e saírem um por um.
- Tirou a faixa SFX vazia.

**Kannemann (20/10):** 41→40 shots, legenda igual.
- Gancho (ig_getv): o nosso tinha zoom 1,72 e um pan que pulava de +0,28 para -0,55 no meio. Ele abriu para 1,23, baixou o quadro (y -0,23) e deixou a janela quase parada. **Gancho = a ação inteira legível, sem pan brusco.**
- Shot de 24s (mesmo clipe): o nosso pan pulava; ele reenquadrou no lado da ação (x 0,72).
- 40–41,5s: tirou um insert de 0,7s (tuliocec) e esticou o lance anterior para 1,4s. Insert de 0,7s de outra fonte no meio de um lance = picote.
- Coletiva do Renato (45s) e melhores momentos (55s): reenquadrou, porque a janela estava no lado errado da pessoa ou do lance (x de -0,43 para 0,37, e 0 para -0,6). **Confira se a pessoa que fala está no centro do quadro.**
- Acrescentou um card de comentário em 49,4–53,7s, que nós não tínhamos.
- Esticou o filtro P&B do flashback para 58,2–68,4s.
- Baixou a trilha do modelo de 0,34 para 0,15 (o vídeo tem a coletiva com fala).

**Neymar x Soteldo (20/10):** 25 shots, mesma ordem.
- Trocou 3 shots (2,1s, 12,7s e 22,9s) do post da ESPN 7698126222… (cards "…ado ilegal", "NEYMAR PARTIU PARA CIMA DO SOTELDO, MAS…" e foto queimados) pelo **outro post da ESPN do mesmo lance, limpo** (7698119365…). **Com duas fontes do mesmo momento, use a sem texto queimado**, mesmo que a com texto tenha um ângulo um pouco melhor.
- Reenquadrou na vertical quase todos os shots da ESPN: o nosso y 0,26 virou ~0 ou -0,27 (a janela estava alta demais e cortava os jogadores).
- Gancho (geglobo): pan seguindo a ação (x de -0,4 para 0 e depois para -0,28) e uma cópia do clipe por cima (máscara/desfoque). O shot de loop (59,2s) leva o mesmo enquadramento.
- pedroramos (44s): punch-in de 1,6 para 2,19 no fim do shot.
- Lance em câmera lenta a 0,3x (22,9s) foi mantido.
- Trilha de 0,34 para 0,16. Mexeu na legenda do loop ("lembra do", 59,4s): 227→225 estados.

**Neymar x Thiago Mendes (21/10):** a mudança mais forte do lote. 33→30 shots, legenda igual.
- **Trocou gancho e loop** por um clipe que ele baixou: post da ESPN (7698949006…, 21/10) com os **jogadores do Boca comemorando na frente do Thiago Mendes**, com punch-in de 2,4 para 2,84 na parte de cima do quadro, onde eles estão (o card do post fica fora). O nosso gancho era outro plano (futebolemfoco). O título dele é "…após ser humilhado na eliminação": **o gancho é a humilhação acontecendo, com o personagem do título no quadro.** O loop fecha no mesmo clipe a 0,33x.
- "Postou uma montagem feita com IA em que rasgava o escudo do Boca" (41s): trocou o nosso plano pela **própria montagem** (repost do @aledovasco, 7698405477…, o Thiago com a arte). Regra 22 (print/post real), aplicada também a imagem de IA citada.
- 50–54s: três trechos curtos do golvixtv na faixa de cima, sobrepostos.
- 53,8–64s: tirou 4 shots curtos (braune, TNT, CazéTV, cortesvictor) e cobriu com **o vídeo do Neymar com a camisa do Paredes, punch-in de 4,1 com pan** + **metropoles em câmera lenta 0,62x por 6,3s**. Menos cortes: segurou a prova (o post) e a reação.
- Reenquadrou quase todos os shots do começo (sportbuzz, cortes_arena, cazetv, antifutebol, getv): quase sempre **menos zoom** (1,5→1,25, 1,67→1,36, 1,93→1,55) e pans seguindo quem se mexe.
- Trilha de 0,34 para 0,09. Existe ainda um "VIDEO 2 quase sem musica.mp4", outra exportação com a trilha mais baixa.
**Vitinha (21/10):** 30 shots, mesma ordem e mesmas fontes, legenda igual.
- Gancho (mael_mrd): o nosso estava parado, com zoom 1,05. Ele fechou para 1,76 e fez um pan seguindo a ação (x 0 → -0,46 → -0,76). O loop leva o mesmo quadro.
- Pans seguindo a jogada em quase todo lance (yt_iypUNpcjqDQ a 3s e 44s, gilmar.borges 22–37s). Punch-in de 1,0 para 1,59 no blue_scope (38s).
- Esticou o filtro P&B do flashback para 46,2–51,2s.
- Trilha de 0,34 para 0,07.

**Padrões do lote (valem para a skill):** (1) gancho nunca parado: punch-in + pan seguindo a ação, e o loop com o mesmo quadro; (2) a nossa janela erra o lado ou a altura do assunto com frequência: ele reposiciona; (3) prefere menos zoom quando o lance é coletivo e mais zoom no detalhe; (4) a trilha do modelo caiu de 0,34 para 0,07–0,16 em todos (o modelo está alto); (5) segura a prova/print até o fim (cards e post); (6) desfoque retangular sobre o texto queimado em vez de trocar de fonte, a não ser que exista outra fonte limpa do mesmo lance; (7) a faixa SFX vazia saiu nos dois vídeos sem efeitos.

- Faltou no garimpo: o post da ESPN da comemoração na cara do Thiago e o repost da montagem de IA.
