@echo off
:: Check if the script is running as Administrator
openfiles >nul 2>nul
if %errorlevel% neq 0 (
    echo Requesting administrator privileges...
    powershell -Command "Start-Process cmd -ArgumentList '/c, %~s0' -Verb RunAs"
    exit /b
)

:: If it's already running as Administrator, execute your bot script
cd /d %~dp0\..
python3 wpkgi.py
pause