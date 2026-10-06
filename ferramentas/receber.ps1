# Traz da nuvem os videos prontos e a legenda do CapCut para a pasta do video no PC.
# uso:  .\ferramentas\receber.ps1                 -> branch de video mais recente
#       .\ferramentas\receber.ps1 "Nome da pasta"
param([string]$Nome)
$ErrorActionPreference = "Continue"   # o git escreve progresso no stderr
function git { & git.exe @args; if ($LASTEXITCODE) { throw "git $args falhou" } }
$repo = Split-Path $PSScriptRoot -Parent
$shorts = Join-Path (Split-Path $repo -Parent) "Videos prontos\Shorts"
$tmp = Join-Path $env:TEMP "radar-receber"
Set-Location $repo
git fetch origin --prune

if ($Nome) {
    $branch = "video/" + ($Nome -replace '[^\w\- ]', '' -replace ' ', '-')
} else {
    $branch = (git for-each-ref --sort=-committerdate --format="%(refname:lstrip=3)" refs/remotes/origin/video | Select-Object -First 1)
}
$ref = "origin/$branch"
# nome real da pasta, como esta no branch
$Nome = (git ls-tree --name-only "${ref}:Videos prontos/Shorts" | Select-Object -First 1)
Write-Host "Recebendo: $Nome"
$job = Join-Path $shorts $Nome
$base = "Videos prontos/Shorts/$Nome"

# so as entregas (subpasta de videos prontos, legenda e receita), sem baixar os clipes de novo
$itens = git ls-tree --name-only "${ref}:$base" | Where-Object { $_ -match '^(Videos [Pp]rontos|legenda para o CapCut\.srt|_montagem)$' } | ForEach-Object { "$base/$_" }
if (-not $itens) { throw "O branch $branch ainda nao tem entregas. A nuvem terminou?" }
if (Test-Path $tmp) { Remove-Item $tmp -Recurse -Force }
New-Item -ItemType Directory $tmp | Out-Null
git archive $ref @itens -o "$tmp\entrega.zip"
Expand-Archive "$tmp\entrega.zip" $tmp
python ferramentas\pacote.py juntar "$tmp\$base" --apagar-partes
robocopy "$tmp\$base" $job /E /XF *.parte* /NFL /NDL /NJH /NJS | Out-Null
Remove-Item $tmp -Recurse -Force
Write-Host "`nEntregas em: $job"
Start-Process explorer.exe $job
