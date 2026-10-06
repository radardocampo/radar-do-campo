# Traz da nuvem os videos prontos e a legenda do CapCut para a pasta do video no PC.
# uso:  .\ferramentas\receber.ps1 "Zidane matou a bola na beira do campo"
param([Parameter(Mandatory)][string]$Nome)
$ErrorActionPreference = "Stop"
$repo = Split-Path $PSScriptRoot -Parent
$job = Join-Path (Split-Path $repo -Parent) "Videos prontos\Shorts\$Nome"
$branch = "video/" + ($Nome -replace '[^\w\- ]', '' -replace ' ', '-')
$tmp = Join-Path $env:TEMP "radar-receber"

Set-Location $repo
git fetch origin $branch
if (Test-Path $tmp) { Remove-Item $tmp -Recurse -Force }
New-Item -ItemType Directory $tmp | Out-Null
# extrai so as entregas do branch, sem trocar de branch nem baixar os clipes de novo
git archive "origin/$branch" "Videos prontos/Shorts/$Nome/Videos prontos" "Videos prontos/Shorts/$Nome/legenda para o CapCut.srt" -o "$tmp\entrega.zip"
Expand-Archive "$tmp\entrega.zip" $tmp
python ferramentas\pacote.py juntar "$tmp\Videos prontos\Shorts\$Nome"
robocopy "$tmp\Videos prontos\Shorts\$Nome" $job /E /NFL /NDL /NJH /NJS | Out-Null
Remove-Item $tmp -Recurse -Force
Write-Host "Entregas em: $job\Videos prontos"
