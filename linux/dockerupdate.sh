#!/bin/bash

## run: chmod +x script_name.sh

# Get the full path of the script's directory
batch_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

output_file="$batch_dir/logs/logDocker.csv"

# Set the name of the Docker container
docker_image="lcmoreira/tflaskhmi:latest"

# Stop and remove the Docker container
docker stop tflaskhmi
docker rm tflaskhmi

# Remove the Docker image
docker rmi lcmoreira/tflaskhmi

# Pull the latest Docker image
docker pull lcmoreira/tflaskhmi

# Run docker inspect and filter the output to extract the version (tag)
docker_version=$(docker inspect --format "{{.RepoTags}}" $docker_image | awk -F ': ' '{print $2}')

# Check if the file is empty
if [ ! -s "$output_file" ]; then
    # Ensure the "logs" directory exists
    mkdir -p "$batch_dir/logs"
    echo "Data, Time, moreInfo" > "$output_file"
    echo "File was empty. Added header."
else
    echo "File already contains data. Skipping header addition."
fi

# Add your logic to append this timestamp to your CSV file
echo "Updates , $(date +'%Y-%m-%d %H:%M:%S') , Version is: ${docker_version%?}" >> "$output_file"

# Output any errors or debugging information
echo "Script executed successfully."

# Run Docker container
docker run -p 8080:5004 -v "$batch_dir/logs:/app/logs" -v "$batch_dir/config:/app/config" --name tflaskhmi lcmoreira/tflaskhmi
