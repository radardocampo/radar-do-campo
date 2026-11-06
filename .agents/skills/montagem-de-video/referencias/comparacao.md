# Comparar a edição do usuário (consulta)

**Desde 06/11/2026:** compare só quando o usuário pedir (até 06/12/2026 vale a pausa de obra: nada de oferecer comparação). Quando uma comparação virar regra, a regra nova **substitui a antiga no lugar dela no SKILL.md**, com a data entre parênteses; o caso (vídeo, tempos, o que ele mudou) vai para `referencias/historico.md`, nunca para o SKILL.md. Desde 06/11 não existem mais os MP4 com-legenda/sem-legenda: o "nosso" é a prévia `_montagem/render/<apelido>-preview.mp4` ou o projeto do CapCut (`compara_capcut.py`, `analisa_capcut.py`), que é o caminho normal porque ele refina no rascunho.

Se o usuário mandar a montagem que ele fez à mão com o mesmo material, rode `casar_fontes.py` nela para ver de onde saiu cada trecho, compare com a sua e proponha mudanças nesta skill. Com ~100 clipes e compactos longos do YouTube, ele leva ~40 min: rode em background e, enquanto isso, faça as folhas do vídeo dele a cada 0,5s (`folha_contato.py --passo 0.5`), transcreva a narração e o vídeo final (faster-whisper) e meça LUFS e trilha. Match com score abaixo de ~0,7 não é confiável quando há ícone, seta ou zoom por cima: confirme olhando o quadro. Os clipes que ele baixou por conta própria (arquivos com o id do TikTok como nome) mostram o que faltou no garimpo: consulte a origem com `yt-dlp --print "%(uploader)s|%(upload_date)s|%(description)s"` e leve a lição para a skill `garimpo-de-videos`.

**Aprendizado diário (pedido do usuário, out/2026):** quando ele disser algo como "compara minha edição de hoje" (ou a rotina do dia achar um vídeo editado por ele ainda não comparado), compare, mostre o que ele mudou e **atualize esta skill no HUB no mesmo dia**: backup `_bak-AAAA-MM-DD-<vídeo>`, regra nova no lugar certo (Passo 3/5/7, "Erros já cometidos"), nova data na linha de versão, `.skill` reempacotado. Grave `<job>/_montagem/cmp/comparado.txt` quando terminar, para a rotina não oferecer de novo.

Se ele refinou a nossa entrega no editor (mesma duração; costuma ficar em `Videos prontos/` como `<título> TIKTOK.mp4`), compare com a base que ele usou (normalmente o `sem-legenda`; antes de 21/10 era o `completo-sem-legenda`):

    python scripts/compara_edicao.py "<nosso>.mp4" "<dele>.mp4" "<job>/_montagem/cmp"
    python scripts/lado_a_lado.py "<nosso>.mp4" "<dele>.mp4" "<job>/_montagem/lado.jpg" <t0> <t1> 0.3

O primeiro lista os trechos de imagem trocados (por região da tela) e as janelas de áudio diferentes; o segundo mostra os dois lado a lado. Resíduo de áudio constante e baixo em todo o vídeo é a trilha dele; picos isolados são SFX. Traduza cada troca numa regra e proponha a mudança nesta skill.

Se ele refinou **no rascunho do CapCut** que geramos (Passo 9), o `compara_edicao.py` acusa diferença em quase tudo, porque os brutos e o filtro P&B do CapCut não batem pixel a pixel com o nosso render. Nesse caso compare **o projeto**, como explicado no Passo 9: cada zoom, keyframe, faixa ligada ou oculta e volume que ele mudou aparece ali. Use o `lado_a_lado.py` só nos trechos que o projeto apontar.
