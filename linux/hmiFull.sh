#!/bin/bash

# Kill any running instances of chrome
pkill -f "chrome"

# Start chrome in fullscreen mode with the specified URL
google-chrome --start-fullscreen http://localhost:8080
