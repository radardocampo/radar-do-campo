# Garimpo do "Riram do show de drones do Messi" - links achados na nuvem, download no PC.
# Roda sozinho: baixa links.txt, faz buscas extras no YouTube (so posts de 06/10 em diante),
# copia os clipes que servem do job "Messi nao queria ir embora" e no fim manda tudo para a nuvem.
# uso (PowerShell, dentro desta pasta):  .\baixar_clipes.ps1
$ErrorActionPreference = "Continue"
$job = $PSScriptRoot
$clipes = Join-Path $job "clipes"; $apoio = Join-Path $clipes "apoio"
New-Item -ItemType Directory -Force $clipes, $apoio | Out-Null
$ytdlp = (Get-Command yt-dlp -ErrorAction SilentlyContinue).Source
if (-not $ytdlp) { $ytdlp = "C:\Users\bruno\AppData\Local\Microsoft\WinGet\Packages\yt-dlp.yt-dlp_Microsoft.Winget.Source_8wekyb3d8bbwe\yt-dlp.exe" }
$comum = @("-f", "bv*+ba/b", "-S", "res,fps,vcodec:h264,ext:mp4:m4a", "--merge-output-format", "mp4",
           "--retries", "5", "--fragment-retries", "10", "--no-playlist",
           "--download-archive", (Join-Path $job ".baixados.txt"))
$log = Join-Path $job "log_download.txt"
$falhas = @()

# 1) links achados na nuvem
foreach ($l in Get-Content (Join-Path $job "links.txt")) {
    if ($l -match '^\s*(#|$)') { continue }
    $p = ($l -split '#')[0].Trim() -split '\s+'
    if ($p.Count -lt 2) { continue }
    $nome, $url = $p[0], $p[1]
    Write-Host ">> $nome"
    & $ytdlp @comum -o (Join-Path $clipes "$nome.%(ext)s") $url *>> $log
    if ($LASTEXITCODE) {   # X/Instagram as vezes pedem cookies
        & $ytdlp @comum --cookies-from-browser firefox -o (Join-Path $clipes "$nome.%(ext)s") $url *>> $log
        if ($LASTEXITCODE) { $falhas += "$nome $url" }
    }
}

# 2) buscas extras no YouTube (so de 06/10/2026 em diante, ate 10 min)
$buscas = "messi drones sancor seguros", "messi drones diestro", "show de drones despedida messi monumental",
          "silbidos sancor seguros monumental", "messi drone show farewell right foot", "despedida messi tribuna drones"
foreach ($q in $buscas) {
    Write-Host ">> busca: $q"
    & $ytdlp @comum --match-filter "upload_date>=20261006 & duration<600" --max-downloads 4 `
        -o (Join-Path $clipes "yt_%(id)s.%(ext)s") "ytsearch10:$q" *>> $log
}

# 3) reaproveita o job do mesmo jogo (copia, nao move)
$outro = Join-Path (Split-Path $job -Parent) "Messi nao queria ir embora\clipes"
if (Test-Path $outro) {
    $reuso = "yt_sYO6xTMVC7E.mp4", "yt_uYmdGLcCIo0.mp4", "yt_ZQqH_lmsG3M.mp4",               # penalti 71 (3x0)
             "TikTok_7319432558382007329_7693706933689142561.mp4", "tt_ligaprofesional_7693705969905306887.mp4",
             "tt_rushfx_10_7693710355926682887.mp4", "Twitter_siempreconargok_2107617561059737600.mp4",  # Monumental lotado (minuto 10)
             "TikTok_7319432558382007329_7693677364030606624.mp4",                               # Messi chorando
             "tt_fertomas3_7693718797252889887.mp4", "tt_y_va_el_3ero_7693703721804418322.mp4"   # torcida do dia
    foreach ($f in $reuso) { $s = Join-Path $outro $f; if (Test-Path $s) { Copy-Item $s $apoio -Force } }
    foreach ($f in "yt_6HaHNYjnghE.mp4", "yt_e6a6lppWZkQ.mp4", "yt_IP-4WLBS1xc.mp4") {          # final da Copa (Messi levantando a taca)
        $s = Join-Path $outro "apoio\$f"; if (Test-Path $s) { Copy-Item $s $apoio -Force }
    }
}

# 4) inventario simples (a nuvem mapeia as janelas na montagem)
$inv = Join-Path $clipes "LEIA - onde esta cada trecho.txt"
"Clipes baixados $(Get-Date -f 'dd/MM HH:mm'). Janelas: a nuvem mapeia pelos frames na montagem." | Set-Content $inv -Encoding utf8
Get-ChildItem $clipes -Recurse -Filter *.mp4 | ForEach-Object {
    $d = & ffprobe -v error -show_entries format=duration:stream=width,height -of csv=p=0 $_.FullName 2>$null
    "$($_.FullName.Substring($job.Length + 1))  |  $($d -join ' ')" } | Add-Content $inv -Encoding utf8
if ($falhas) { "`n[BAIXAR MANUALMENTE]" | Add-Content $inv; $falhas | Add-Content $inv }

Write-Host "`nBaixados: $((Get-ChildItem $clipes -Recurse -Filter *.mp4).Count). Falhas: $($falhas.Count)"
$falhas | ForEach-Object { Write-Host "  falhou: $_" }

# 5) manda para a nuvem
$repo = Join-Path (Split-Path (Split-Path (Split-Path $job -Parent) -Parent) -Parent) "nuvem"
if (Test-Path "$repo\ferramentas\enviar.ps1") { & "$repo\ferramentas\enviar.ps1" (Split-Path $job -Leaf) }
