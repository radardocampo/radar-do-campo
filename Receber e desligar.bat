@echo off
rem Espera a nuvem terminar o video do Messi, puxa para o PC e desliga o computador.
rem Coloque este arquivo na mesma pasta do "Receber da nuvem.bat" e de dois cliques.
setlocal
set "SCRIPT="
for /f "delims=" %%F in ('dir /s /b "%~dp0receber.ps1" 2^>nul') do if not defined SCRIPT set "SCRIPT=%%F"
if not defined SCRIPT (echo Nao achei o receber.ps1 & pause & exit /b 1)

:tentar
echo [%time%] Verificando se o video do Messi ja esta pronto...
powershell -NoProfile -ExecutionPolicy Bypass -File "%SCRIPT%" "Messi nao queria ir embora"
if errorlevel 1 (
  echo Ainda nao. Tento de novo em 5 minutos. Feche esta janela para cancelar.
  timeout /t 300 /nobreak >nul
  goto tentar
)

echo Video recebido. O PC desliga em 2 minutos. Para cancelar: shutdown /a
shutdown /s /t 120
