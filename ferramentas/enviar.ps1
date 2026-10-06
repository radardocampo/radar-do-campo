# Sobe a pasta de um video para a nuvem montar, ja com a narracao preparada
# (a nuvem nao baixa o Whisper, entao cortes e tempos por palavra saem daqui).
# uso:  .\ferramentas\enviar.ps1                 -> pasta mais recente de Shorts
#       .\ferramentas\enviar.ps1 "Nome da pasta"
param([string]$Nome)
$ErrorActionPreference = "Continue"   # o git escreve progresso no stderr
function git { & git.exe @args; if ($LASTEXITCODE) { throw "git $args falhou" } }
$repo = Split-Path $PSScriptRoot -Parent
$shorts = Join-Path (Split-Path $repo -Parent) "Videos prontos\Shorts"
if (-not $Nome) { $Nome = (Get-ChildItem $shorts -Directory | Sort-Object LastWriteTime -Descending | Select-Object -First 1).Name }
$origem = Join-Path $shorts $Nome
if (-not (Test-Path $origem)) { throw "Pasta nao encontrada: $origem" }
Write-Host "Video: $Nome"
$branch = "video/" + ($Nome -replace '[^\w\- ]', '' -replace ' ', '-')
$destino = Join-Path $repo "Videos prontos\Shorts\$Nome"
$scripts = Join-Path $repo ".claude\skills\montagem-de-video\scripts"

# 1) narracao preparada no PC
$prefeito = Get-ChildItem $origem -Recurse -File -Include *.mp4 | Where-Object { $_.Name -match 'pr[eé].?feito' } | Select-Object -First 1
if ($prefeito) {
    # montagem parcial do usuario: a narracao ja esta cortada dentro dela, so precisa dos tempos
    if (-not (Test-Path "$origem\tempos do pre-feito\palavras.json")) {
        Write-Host "Transcrevendo o audio de $($prefeito.Name)..."
        python "$repo\ferramentas\tempos_audio.py" $prefeito.FullName "$origem\tempos do pre-feito\palavras.json"
    }
} else {
    $narr = Get-ChildItem "$origem\*" -File -Include *.wav, *.mp3 | Sort-Object LastWriteTime -Descending | Select-Object -First 1
    if ($narr -and -not (Test-Path "$origem\_montagem\palavras.json")) {
        Write-Host "Preparando a narracao $($narr.Name) (cortes + tempos)..."
        python "$scripts\narracao.py" $narr.FullName "$origem\_montagem"
    }
}

# 2) sobe num branch proprio
Set-Location $repo
git checkout main; git pull --ff-only
git checkout -B $branch
robocopy $origem $destino /E /XD "_registro" /NFL /NDL /NJH /NJS | Out-Null
python ferramentas\pacote.py partir "Videos prontos\Shorts\$Nome"
git add -f "Videos prontos/Shorts/$Nome"
git commit -m "video: $Nome"
git push -u origin $branch --force
git checkout main
if (Test-Path $destino) { Remove-Item $destino -Recurse -Force }   # so a copia do repo; o original em Shorts fica intacto

$pedido = "Monta o video do branch $branch."
Set-Clipboard $pedido
Write-Host "`nEnviado. Abra claude.ai/code, repositorio radar-do-campo, e cole (ja esta copiado):`n  $pedido`n(acrescente o que quiser, ex.: 'parti do meu pre-feito, mantem o inicio')"
