#!/bin/bash

# Get the full path of the script's directory
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Set the path for the output file
output_file="$script_dir/logs/logDocker.csv"

# Set the name of the Docker container
docker_image="lcmoreira/tflaskhmi:latest"

# Stop and remove the Docker container
docker stop tflaskhmi
docker rm tflaskhmi

# Remove the Docker image
docker rmi $docker_image

# Pull the latest Docker image
docker pull $docker_image

# Run docker inspect and filter the output to extract the version (tag)
docker_version=$(docker inspect --format '{{ index .RepoTags 0 }}' $docker_image)

# Check if the file is empty
if [ ! -s "$output_file" ]; then
    # Ensure the "logs" directory exists
    mkdir -p "$script_dir/logs"
    echo "Data, Time, moreInfo" > "$output_file"
    echo "File was empty. Added header."
else
    echo "File already contains data. Skipping header addition."
fi

# Add your logic to append this timestamp to your CSV file
echo "Updates , $(date '+%Y-%m-%d %H:%M:%S') , Version is: ${docker_version%?}" >> "$output_file"

# Output any errors or debugging information
echo "Script executed successfully."

# Run Docker container in the background
docker run -d -p 8080:5004 -v "$script_dir/logs:/app/logs" -v "$script_dir/config:/app/config" --name tflaskhmi $docker_image

# Kill any existing Chromium processes and start Chromium in fullscreen mode
pkill chromium-browser
sudo -u $non_root_user chromium-browser --no-sandbox --start-fullscreen http://localhost:8080