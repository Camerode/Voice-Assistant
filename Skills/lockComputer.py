from Skills.Acore import *
import subprocess
import ctypes
import sys

# Computer locker
def lock_computer():
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