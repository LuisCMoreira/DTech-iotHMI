import os
import time
import subprocess
import pygetwindow as gw

def is_chrome_fullscreen():
    chrome_windows = gw.getWindowsWithTitle('Google Chrome')

    if not chrome_windows:
        print("Chrome is not running.")
        return False

    # Assuming the first Chrome window is the one you are interested in
    chrome_window = chrome_windows[0]
    print(chrome_window)
    width, height = chrome_window.width, chrome_window.height

    isFullScreen=False
    if width>1535 and height > 863:
        isFullScreen=True

    # Check if the window is in full-screen mode
    return isFullScreen

def run_batch_file():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    batch_file_path = os.path.join(script_directory, 'hmiFull.bat')  # Replace 'your_file.bat' with your actual batch file name
    subprocess.run([batch_file_path])

if __name__ == "__main__":
    while True:
        if not is_chrome_fullscreen():
            print("Chrome is not in full-screen mode. Running batch file...")
            run_batch_file()
        else:
            print("Chrome is in full-screen mode. Doing nothing.")
        time.sleep(10)  # Adjust the sleep interval (in seconds) as needed
