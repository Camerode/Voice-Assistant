from Skills.Acore import speak, record_action
from PIL import ImageGrab
import platform
import os
from datetime import time

# Take a screenshot
def screen_shot():
    try:
        im = ImageGrab.grab()
        # Define the path to the downloads folder based on the current platform
        system = platform.system()
        if system == "Windows":
            downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        elif system == "Darwin":
            downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        elif system == "Linux":
            downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        else:
            print(f"Warning: unsupported platform {system}.")
            speak(f"Warning: unsupported platform {system}.")
            downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        # Define the filename with timestamp
        filename = f"screenshot_{int(time.time())}.jpg"
        # Save the captured image to the downloads folder
        im.save(os.path.join(downloads_path, filename), "JPEG")
        print(f"Picture saved as {filename} in the Downloads folder.")
        speak(f"Picture saved as {filename} in the Downloads folder.")
        record_action('Screenshot')
    except Exception as e:
        print("An error has occurred in the screenshot command, output has been sent to errors.log")
        speak("An error has occurred in the screenshot command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write("screen_shot: " + str(e) + "\n")