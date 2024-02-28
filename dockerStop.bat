@echo off
docker stop tflaskhmi
docker rm tflaskhmi
docker rmi lcmoreira/tflaskhmi:latest

taskkill /F /IM python3.9.exe /T