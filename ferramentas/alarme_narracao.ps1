# Alarme barulhento para o usuario gerar a narracao no AI Studio (fluxo automatico).
# Copia o texto para o AI Studio, abre o site e o texto, mostra um aviso por cima de tudo
# e toca bipes a cada 30 s ate aparecer um audio novo (Downloads ou pasta do video). So bipe, sem voz (pedido do usuario).
# Quando o audio chega, copia para a pasta do video como "Narracao.<ext>" e sai com codigo 0.
# uso:  .\ferramentas\alarme_narracao.ps1 -Pasta "<pasta do video em Shorts>" [-MaxMin 180]
param([Parameter(Mandatory)][string]$Pasta, [int]$MaxMin = 180)
$ErrorActionPreference = "Continue"
if (-not (Test-Path $Pasta)) { throw "Pasta nao encontrada: $Pasta" }
$inicio = Get-Date
$downloads = Join-Path ([Environment]::GetFolderPath('UserProfile')) "Downloads"
$texto = Get-ChildItem $Pasta -File -Filter "texto para o AI Studio*.txt" | Select-Object -First 1
if (-not $texto) { $texto = Get-ChildItem $Pasta -File -Filter "roteiro*.txt" | Select-Object -First 1 }

Add-Type -AssemblyName System.Windows.Forms

function Audio-Novo {
    foreach ($dir in @($Pasta, $downloads)) {
        $a = Get-ChildItem $dir -File -ErrorAction SilentlyContinue |
            Where-Object { $_.Extension -match '^\.(wav|mp3)$' -and $_.LastWriteTime -gt $inicio } |
            Sort-Object LastWriteTime -Descending | Select-Object -First 1
        if ($a) { return $a }
    }
}

function Alarme {
    foreach ($i in 1..3) { foreach ($f in 1000, 1500) { [console]::Beep($f, 250) } }
}

# 1) deixa tudo pronto para colar
if ($texto) {
    Get-Content $texto.FullName -Raw -Encoding UTF8 | Set-Clipboard
    Start-Process notepad.exe $texto.FullName
}
Start-Process "https://aistudio.google.com/generate-speech"
$wsh = New-Object -ComObject WScript.Shell
1..15 | ForEach-Object { $wsh.SendKeys([char]175) }   # sobe o volume do Windows
$aviso = "NARRACAO DO VIDEO`n`nO texto para o AI Studio ja esta copiado (Ctrl+V) e aberto no Bloco de Notas.`n`n" +
         "1. No AI Studio: Gemini 2.5 Pro TTS, voz Puck, seu Sample Context de sempre.`n" +
         "2. Cole o texto, gere e baixe o audio (pode deixar em Downloads).`n`n" +
         "O Claude pega o arquivo sozinho e sobe para a nuvem montar.`nPasta: $Pasta"
$cmd = "Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.MessageBox]::Show('" + ($aviso -replace "'", "''") +
       "', 'Radar do Campo - gerar narracao', 'OK', 'Warning', 'Button1', 'DefaultDesktopOnly') | Out-Null"
$b64 = [Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($cmd))   # sem briga de aspas/quebras de linha
Start-Process powershell.exe -ArgumentList "-NoProfile", "-WindowStyle", "Hidden", "-EncodedCommand", $b64

# 2) insiste ate o audio aparecer
$proximo = Get-Date
while (((Get-Date) - $inicio).TotalMinutes -lt $MaxMin) {
    $a = Audio-Novo
    if ($a) {
        do { $t = $a.Length; Start-Sleep 3; $a.Refresh() } while ($a.Length -ne $t)   # espera terminar de baixar
        $dest = Join-Path $Pasta ("Narracao" + $a.Extension)
        if ($a.FullName -ne $dest) { Copy-Item $a.FullName $dest -Force }
        [console]::Beep(1200, 150); [console]::Beep(1600, 400)   # bipe curto de "recebido"
        Write-Host "NARRACAO_OK $dest"
        exit 0
    }
    if ((Get-Date) -ge $proximo) { Alarme; $proximo = (Get-Date).AddSeconds(30) }
    Start-Sleep 10
}
Write-Host "NARRACAO_TIMEOUT depois de $MaxMin min"
exit 1
