@echo off

start "" python ./scriptRunAPI.py

start "" docker run -p 8080:5004 -v "%cd%\logs:/app/logs" -v "%cd%\config:/app/config" --name tflaskhmi lcmoreira/tflaskhmi

taskkill /F /IM chrome.exe
start chrome --start-fullscreen http://localhost:8080