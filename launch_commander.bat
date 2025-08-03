@echo off
title 🧠 Commander Ammad's Custom Browser
echo Launching CommanderNet...

:: Start HTTP Server in background
start cmd /k "cd /d C:\Path\To\Your\Browser\Folder && python -m http.server 8000"

:: Wait a bit for the server to start
timeout /t 2 /nobreak >nul

:: Launch your browser
start "" "C:\Path\To\Your\Browser\Folder\commander_browser.py"

echo Commander Browser launched!
exit
