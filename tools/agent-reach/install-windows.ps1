# Agent Reach installer voor Windows (PowerShell)
# Gebruik: rechtsklik > "Run with PowerShell", of in een terminal:
#   powershell -ExecutionPolicy Bypass -File tools\agent-reach\install-windows.ps1
#
# Wat dit doet:
#   1. Controleert of Python 3.10+ aanwezig is
#   2. Maakt een virtuele omgeving in %USERPROFILE%\.agent-reach-venv
#   3. Installeert agent-reach vanaf GitHub
#   4. Draait de installer (met --system, dus gh CLI / mcporter / yt-dlp config)
#   5. Draait agent-reach doctor

$ErrorActionPreference = "Stop"

function Fail($msg) {
    Write-Host ""
    Write-Host "FOUT: $msg" -ForegroundColor Red
    Write-Host ""
    Read-Host "Druk op Enter om te sluiten"
    exit 1
}

Write-Host "=== Agent Reach installer (Windows) ===" -ForegroundColor Cyan

# 1. Python
$py = $null
foreach ($cmd in @("py -3", "python", "python3")) {
    try {
        $out = & cmd /c "$cmd --version 2>&1"
        if ($out -match "Python 3\.(\d+)") {
            if ([int]$Matches[1] -ge 10) { $py = $cmd; break }
        }
    } catch {}
}
if (-not $py) {
    Fail "Python 3.10 of hoger niet gevonden. Installeer via https://www.python.org/downloads/windows/ en vink 'Add python.exe to PATH' aan. Open daarna dit script opnieuw."
}
Write-Host "Python gevonden: $py" -ForegroundColor Green

# 2. venv
$venv = Join-Path $env:USERPROFILE ".agent-reach-venv"
if (-not (Test-Path (Join-Path $venv "Scripts\python.exe"))) {
    Write-Host "Virtuele omgeving maken in $venv ..."
    & cmd /c "$py -m venv `"$venv`""
    if ($LASTEXITCODE -ne 0) { Fail "venv maken mislukt." }
}
$venvPython = Join-Path $venv "Scripts\python.exe"
$venvScripts = Join-Path $venv "Scripts"

# 3. agent-reach installeren
Write-Host "agent-reach installeren (kan een paar minuten duren) ..."
& $venvPython -m pip install --upgrade pip --quiet
& $venvPython -m pip install --upgrade "https://github.com/Panniantong/agent-reach/archive/main.zip"
if ($LASTEXITCODE -ne 0) { Fail "pip install mislukt. Check je internetverbinding." }

# 4. Scripts-map op PATH zetten voor deze sessie en permanent voor de gebruiker
$env:PATH = "$venvScripts;$env:PATH"
$userPath = [Environment]::GetEnvironmentVariable("PATH", "User")
if ($userPath -notlike "*$venvScripts*") {
    [Environment]::SetEnvironmentVariable("PATH", "$venvScripts;$userPath", "User")
    Write-Host "PATH bijgewerkt: agent-reach werkt vanaf nu in elk nieuw terminalvenster." -ForegroundColor Green
}

# 5. Installer en doctor
Write-Host ""
Write-Host "agent-reach install --env=auto --system" -ForegroundColor Cyan
& (Join-Path $venvScripts "agent-reach.exe") install --env=auto --system

Write-Host ""
Write-Host "agent-reach doctor" -ForegroundColor Cyan
& (Join-Path $venvScripts "agent-reach.exe") doctor

Write-Host ""
Write-Host "Klaar. Open een NIEUW terminalvenster (of VS Code opnieuw) zodat 'agent-reach' overal werkt." -ForegroundColor Green
Write-Host "Extra platforms: agent-reach install --env=auto --system --channels=opencli,reddit,facebook,instagram"
Write-Host ""
Read-Host "Druk op Enter om te sluiten"
