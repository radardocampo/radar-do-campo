@echo off
rem Espera a nuvem terminar o video do Messi, puxa para o PC e desliga o computador.
rem Coloque este arquivo na mesma pasta do "Receber da nuvem.bat" e de dois cliques.
setlocal
set "SCRIPT="
for /f "delims=" %%F in ('dir /s /b "%~dp0receber.ps1" 2^>nul') do if not defined SCRIPT set "SCRIPT=%%F"
if not defined SCRIPT (echo Nao achei o receber.ps1 & pause & exit /b 1)
for %%D in ("%SCRIPT%\..\..") do set "REPO=%%~fD"
set "BRANCH=video/Messi-nao-queria-ir-embora"
set "PASTA=Videos prontos/Shorts/Messi nao queria ir embora"

:tentar
echo [%time%] Verificando se o video do Messi ja esta pronto...
rem So conta como pronto quando a subpasta "Videos prontos" (os mp4 finais) estiver no branch.
rem A pasta _montagem sozinha e so a receita e ja esta la desde antes.
powershell -NoProfile -Command "Set-Location -LiteralPath '%REPO%'; git fetch -q origin %BRANCH% 2>$null; $i = git ls-tree --name-only 'origin/%BRANCH%:%PASTA%' 2>$null; if ($i -match '^Videos [Pp]rontos$') { exit 0 } else { exit 1 }"
if errorlevel 1 (
  echo Ainda nao. Tento de novo em 5 minutos. Feche esta janela para cancelar.
  timeout /t 300 /nobreak >nul
  goto tentar
)

echo Video pronto na nuvem. Recebendo...
powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPT%" "Messi nao queria ir embora"
if errorlevel 1 (
  echo Deu erro ao receber. O PC NAO sera desligado. Tento de novo em 5 minutos.
  timeout /t 300 /nobreak >nul
  goto tentar
)

echo Video recebido. O PC desliga em 2 minutos. Para cancelar: shutdown /a
shutdown /s /t 120
