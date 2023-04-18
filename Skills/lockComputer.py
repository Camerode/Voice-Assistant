from Skills.Acore import *
import subprocess
import ctypes
import sys

# Computer locker
def lock_computer():
    try:
        platform = sys.platform
        if platform == "win32":
            ctypes.windll.user32.LockWorkStation()  # Windows
        elif platform == "darwin":
            subprocess.call(["/System/Library/CoreServices/Menu Extras/User.menu/Contents/Resources/CGSession", "-suspend"])  # Mac
        elif platform.startswith("linux"):
            subprocess.call(["gnome-screensaver-command", "-l"])  # Linux
        else:
            print("Unsupported platform")
            speak("Unsupported platform")
    except Exception as e:
        print("An error has occurred in the lockComputer command, output has been sent to errors.log")
        speak("An error has occurred in the lockComputer command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write("lock_computer: " + str(e) + "\n")