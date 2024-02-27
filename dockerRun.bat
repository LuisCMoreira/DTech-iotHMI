@echo off
start "" docker run -p 8080:5004 -v "%cd%\logs:/app/logs" -v "%cd%\config:/app/config" -v "%cd%\auxScripts:/app/auxScripts" --name tflaskhmi lcmoreira/tflaskhmi