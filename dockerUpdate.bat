@echo off
REM Get the full path of the batch file's directory
set "batch_dir=%~dp0"

set "output_file=%batch_dir%logs/logDocker.csv"

REM Set the name of the Docker container
set docker_image="lcmoreira/tflaskhmi:latest"


docker stop tflaskhmi
docker rm tflaskhmi
docker rmi lcmoreira/tflaskhmi
docker pull lcmoreira/tflaskhmi



REM Run docker inspect and filter the output to extract the version (tag)
for /f "tokens=2 delims=: " %%a in ('docker inspect --format "{{.RepoTags}}" %docker_image%') do (
    set docker_version=%%a
)

REM Check if the file is empty
for %%I in ("%output_file%") do if %%~zI equ 0 (
    REM Ensure the "logs" directory exists
    mkdir "%batch_dir%logs" 2>nul
    echo Data, Time, moreInfo > "%output_file%"
    echo File was empty. Added header.
) else (
    echo File already contains data. Skipping header addition.
)

REM Add your logic to append this timestamp to your CSV file
echo Updates , %date% %time:~0,-3% , Version is: %docker_version:~0,-1% >> "%output_file%"

REM Output any errors or debugging information
echo Script executed successfully.


start "" docker run -p 8080:5004 -v "%cd%\logs:/app/logs" -v "%cd%\config:/app/config" --name tflaskhmi lcmoreira/tflaskhmi

taskkill /F /IM chrome.exe
timeout /t 5 /nobreak >nul
start chrome --start-fullscreen http://localhost:8080