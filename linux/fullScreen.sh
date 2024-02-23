#!/bin/bash

window_title="Google Chrome"  # Replace with the title of your window

while true; do
    # Get the window ID using xdotool
    window_id=$(xdotool search --name "$window_title")

    if [ -z "$window_id" ]; then
        echo "Window with title '$window_title' not found."
    else
        # Get the window geometry using xdotool
        window_geometry=$(xdotool getwindowgeometry $window_id)

        # Extract width and height from the window_geometry variable
        eval "$window_geometry"

        isFullScreen=false
        if [ $WIDTH -gt 1535 ] && [ $HEIGHT -gt 863 ]; then
            isFullScreen=true
        fi

        if [ "$isFullScreen" = true ]; then
            echo "Chrome is in full-screen mode. Doing nothing."
        else
            echo "Chrome is not in full-screen mode. Running batch file..."
            # Replace 'hmiFull.sh' with your actual shell script
            ./hmiFull.sh
        fi
    fi

    sleep 10  # Adjust the sleep interval (in seconds) as needed
done
