#!/bin/bash

# Stop and remove the Docker container
docker stop tflaskhmi
docker rm tflaskhmi

# Remove the Docker image
docker rmi lcmoreira/tflaskhmi:latest

# Kill Python processes (replace 'scriptRunAPI.py' with your actual script name)
pkill -f "python3.9 scriptRunAPI.py"
