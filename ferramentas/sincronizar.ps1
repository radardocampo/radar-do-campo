# Deixa o repo igual ao PC: skills do HUB -> .claude/skills e .agents/skills (Antigravity),
# memorias do Claude -> memoria/. Depois commit e push.
# Uso: powershell -ExecutionPolicy Bypass -File ferramentas\sincronizar.ps1
$ErrorActionPreference = "Stop"
$repo   = Split-Path -Parent $PSScriptRoot
$hub    = Join-Path $repo "..\Claude\skills claude\versao-nova-2026-09-22"
$mem    = "C:\Users\bruno\.claude\projects\C--Users-bruno-Desktop-all-BUSINESS-Radar-do-Campo\memory"
$skills = "garimpo-de-temas", "garimpo-de-videos", "montagem-de-video", "titulos-e-tags"

Set-Location $repo
git pull -q --ff-only

# 1. SKILL.md do HUB (fonte da verdade). Scripts do repo ja estao adaptados ao RADAR_BASE: nao sobrescrever.
foreach ($s in $skills) {
    Copy-Item "$hub\$s\SKILL.md" ".claude\skills\$s\SKILL.md" -Force
}

# 2. Espelho para o Antigravity (.agents/skills = mesmo conteudo de .claude/skills)
if (Test-Path ".agents\skills") { Remove-Item ".agents\skills" -Recurse -Force }
New-Item -ItemType Directory -Force ".agents" | Out-Null
Copy-Item ".claude\skills" ".agents\skills" -Recurse -Force
Get-ChildItem ".agents\skills" -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force

# 3. Memorias (so acrescenta/atualiza; nao apaga as que vieram da nuvem)
Copy-Item "$mem\*.md" "memoria\" -Force

git add .claude/skills .agents/skills memoria GEMINI.md ferramentas/sincronizar.ps1
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    git commit -q -m "Sincroniza skills e memorias ($(Get-Date -Format yyyy-MM-dd))"
    git push -q
    Write-Host "Sincronizado e enviado ao GitHub."
} else {
    Write-Host "Ja estava tudo igual."
}
