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
    # referencias/ (hub.md, historico.md e, na montagem, capcut/comparacao/limpeza) desde 06/11/2026
    $refHub  = Join-Path $hub "$s\referencias"
    $refRepo = Join-Path ".claude\skills" "$s\referencias"
    if (Test-Path $refHub) {
        if (Test-Path $refRepo) { Remove-Item $refRepo -Recurse -Force }
        Copy-Item $refHub $refRepo -Recurse -Force
    }
}

# 2. Espelho para o Antigravity (.agents/skills = mesmo conteudo de .claude/skills)
if (Test-Path ".agents\skills") { Remove-Item ".agents\skills" -Recurse -Force }
New-Item -ItemType Directory -Force ".agents" | Out-Null
Copy-Item ".claude\skills" ".agents\skills" -Recurse -Force
Get-ChildItem ".agents\skills" -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force

# 3. Memorias (so acrescenta/atualiza; nao apaga as que vieram de outro lugar)
Copy-Item "$mem\*.md" "memoria\" -Force
# memorias aposentadas (fora do indice) ficam em memoria/arquivo, desde 06/11/2026
$memArq = Join-Path $mem "arquivo"
if (Test-Path $memArq) {
    New-Item -ItemType Directory -Force (Join-Path "memoria" "arquivo") | Out-Null
    Copy-Item (Join-Path $memArq "*.md") (Join-Path "memoria" "arquivo") -Force
    # a copia antiga no topo de memoria/ sai do repo (git rm); o conteudo continua em memoria/arquivo/
    Get-ChildItem (Join-Path $memArq "*.md") | ForEach-Object {
        $velho = Join-Path "memoria" $_.Name
        if (Test-Path $velho) { git rm -q -f -- "memoria/$($_.Name)" | Out-Null }
    }
}

git add .claude/skills .agents/skills memoria GEMINI.md CLAUDE.md AGENTS.md LEIA-PRIMEIRO.md ferramentas/sincronizar.ps1
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    git commit -q -m "Sincroniza skills e memorias ($(Get-Date -Format yyyy-MM-dd))"
    git push -q
    Write-Host "Sincronizado e enviado ao GitHub."
} else {
    Write-Host "Ja estava tudo igual."
}
