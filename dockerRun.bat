@echo off
docker run -p 8080:5004 -v "%cd%\logs:/app/logs" -v "%cd%\config:/app/config" --name tflaskhmi lcmoreira/tflaskhmi