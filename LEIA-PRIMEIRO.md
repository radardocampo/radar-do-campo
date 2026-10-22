# Radar do Campo — leia primeiro (para qualquer IA)

Este repositório guarda tudo o que uma IA precisa para trabalhar no canal Radar do Campo:
o que o canal é, o fluxo de produção, as skills (passo a passo de cada etapa) e a memória
(as regras e preferências do dono, aprendidas vídeo a vídeo). Responda sempre em português do Brasil, direto e curto.

## O canal
- Shorts/Reels/TikTok verticais de futebol (YouTube, TikTok @_radardocampo, Instagram, Kwai).
- Assuntos: o que aconteceu nos jogos de ontem — lances, polêmicas, brigas, Seleção, bastidores.
- Identidade: "o radar não deixa passar" — detalhe, vigilância, lupa/círculo vermelho. Ver `Base do conteudo.txt`.
- Vídeo final: **mínimo 60 s**, gancho forte nos primeiros segundos, loop no fim, legenda karaokê amarela no meio, marca d'água do radar.

## Fluxo de um vídeo (ordem)
1. **Garimpo de temas** (`garimpo-de-temas`): jogos de ontem → candidatos por jogo, escritos em texto, buscando em todas as redes → o dono escolhe → roteiro de 255–265 palavras (gancho, contexto, payoff).
2. **Títulos e tags** (`titulos-e-tags`): títulos, texto de capa, tags.
3. **Narração**: o dono gera a voz no **Google AI Studio** (no navegador). Entregar o roteiro também sem os rótulos "Gancho/Contexto/Payoff".
4. **Garimpo de vídeos** (`garimpo-de-videos`): baixar clipes de torcida/arquibancada (evitar transmissão oficial por Content ID) em TikTok, Instagram, X, YouTube, Facebook, Kwai, Threads. Inventário dos trechos.
5. **Montagem** (`montagem-de-video`): scripts Python + ffmpeg montam o vídeo em `Videos prontos\Shorts\<vídeo>\`; entrega 2 arquivos, com legenda e sem legenda, **sem logo do canal** (desde 21/10/2026), e o rascunho editável no CapCut, de onde o dono refina e exporta a versão final.
6. O dono revisa/ajusta no CapCut e posta. Quando ele manda a edição dele, compara-se com a nossa e as diferenças viram regra (memórias `referencia-edicao-*` e `comparacao-lote-*`). Desde 18/10 ele refina no rascunho do CapCut que geramos; aí a comparação é pelo projeto (`compara_capcut.py`, ver a skill montagem-de-video).

## Onde está cada coisa
| O quê | Onde |
|---|---|
| Skills (fonte da verdade) | PC: `HUB Radar do Campo\Claude\skills claude\versao-nova-2026-09-22\` · repo: `.claude/skills/` e `.agents/skills/` (cópias idênticas) |
| Memória (regras do dono) | `memoria/MEMORY.md` (índice) + um arquivo por regra em `memoria/` |
| Pasta real de trabalho | `C:\Users\bruno\Desktop\all\BUSINESS\Radar do Campo\` (`Videos prontos\`, `logos\`, `Sons edição\`, `Musicas edição\`) |
| Instruções por ferramenta | `CLAUDE.md` (Claude na nuvem) · `GEMINI.md` (Antigravity no PC) · `AGENTS.md` (outras IAs) |
| Scripts de apoio | `ferramentas/` (`sincronizar.ps1`, `enviar.ps1`/`receber.ps1` da nuvem) |

## Antes de qualquer tarefa
1. `git pull`.
2. Leia `memoria/MEMORY.md` inteiro e abra as memórias ligadas à tarefa. **Valem tanto quanto as skills**; se conflitarem, vale a mais recente.
3. Siga o `SKILL.md` da tarefa passo a passo.

## Regras de ouro (resumo — o detalhe está na memória)
- Gancho = momento mais forte do material; ação mostrada até o impacto; fala factual pede imagem do fato.
- Nada de políticos em cena; nada de comentário de anônimo como pauta.
- Placar e fatos conferidos (acréscimos!) antes de afirmar.
- Nunca abaixo de 60 s; loudness e marcas conforme a skill de montagem.
- Nunca apagar arquivos do dono: o que sai vai para a Lixeira.
- Mostrar sempre a lista de candidatos escrita, não só resumo.

## Manter tudo atualizado (regra do dono, 2026-10-21)
Toda mudança — skill, regra, memória, fluxo, contexto — só termina quando está igual em **todos** os lugares:
HUB (+ `.skill`), repo (`.claude/skills`, `.agents/skills`, `memoria/`, este arquivo, `CLAUDE.md`, `GEMINI.md`, `AGENTS.md`), upload no claude.ai.
Depois de mudar, rodar `ferramentas\sincronizar.ps1` (commit + push). Revisar se este arquivo ainda descreve o fluxo certo.
