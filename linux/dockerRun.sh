#!/bin/bash

# Start the Python script
python3 ./scriptRunAPI.py &

# Run Docker container in the background
docker run -d -p 8080:5004 -v "$(pwd)/logs:/app/logs" -v "$(pwd)/config:/app/config" --name tflaskhmi lcmoreira/tflaskhmi
