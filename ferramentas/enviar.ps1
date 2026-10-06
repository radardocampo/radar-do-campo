# Sobe a pasta de um video (roteiro, narracao, clipes, inventario) para a nuvem montar.
# uso:  .\ferramentas\enviar.ps1 "Zidane matou a bola na beira do campo"
param([Parameter(Mandatory)][string]$Nome)
$ErrorActionPreference = "Stop"
$repo = Split-Path $PSScriptRoot -Parent
$origem = Join-Path (Split-Path $repo -Parent) "Videos prontos\Shorts\$Nome"
if (-not (Test-Path $origem)) { throw "Pasta nao encontrada: $origem" }
$branch = "video/" + ($Nome -replace '[^\w\- ]', '' -replace ' ', '-')
$destino = Join-Path $repo "Videos prontos\Shorts\$Nome"

Set-Location $repo
git checkout main; git pull --ff-only
git checkout -B $branch
robocopy $origem $destino /E /XD "Videos prontos" "_registro" /NFL /NDL /NJH /NJS | Out-Null
python ferramentas\pacote.py partir "Videos prontos\Shorts\$Nome"
git add -f "Videos prontos/Shorts/$Nome"
git commit -m "video: $Nome"
git push -u origin $branch --force
git checkout main
Remove-Item $destino -Recurse -Force   # so a copia do repo; o original em Shorts fica intacto
Write-Host "`nEnviado no branch $branch. Na sessao da nuvem, peca: monta o video do branch $branch"
