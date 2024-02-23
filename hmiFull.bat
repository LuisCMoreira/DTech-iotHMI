@echo off
taskkill /F /IM chrome.exe
start chrome --start-fullscreen http://localhost:8080