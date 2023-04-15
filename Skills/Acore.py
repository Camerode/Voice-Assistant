import speech_recognition as sr
import pyttsx3
from datetime import datetime
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import os
import subprocess
import platform
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from playsound import playsound
from time import sleep

# Action recorder
def record_action(action):
    current_time = datetime.now()
    with open('Skills/CoreFiles/actions.log', 'a') as log_file:
        log_file.write(f'{current_time}: {action}\n')

# Define a function to speak text
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    current_time = datetime.now()
    with open('Skills/CoreFiles/voice.log', 'a') as log_file:
        log_file.write(f'{current_time}: {text}\n')
    
# Voice/text commands
def use_Voice():
    useVoice = 'True'
    try:
        with open('Skills/CoreFiles/settings.txt', 'r') as f:
            contents = f.read()
        lines = contents.split('\n')
        for line in lines:
            key_value = line.split('=')
            if key_value[0] == 'useVoice':
                useVoice = key_value[1]
                useVoice = True if useVoice.lower() == 'true' else False
                break
        else:
            raise ValueError("useVoice not found in settings.txt")
    except Exception as e:
        print(f"Error changing text/voice mode: {e}")
    return useVoice
def recognize_speech(use_voice=None):
    if use_voice is None:
        use_voice = use_Voice()
    r = sr.Recognizer()
    if use_voice:
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print(f"You said: {text}")
                return text.lower()
            except:
                print("Sorry, I do not have a response...")
                return ""
    else:
        text = input("Enter text: ")
        return text.lower()
    
# Silent Mode
def silent_Mode():
    # Silent mode
    try:
        with open('Skills/CoreFiles/settings.txt', 'r') as f:
            contents = f.read()
        lines = contents.split('\n')
        for line in lines:
            key_value = line.split('=')
            if key_value[0] == 'silentMode':
                my_variable = key_value[1]
                if my_variable.lower() == "off":
                    speak("Sorry, I do not have a response...")
                break
        else:
            raise ValueError("silentMode not found in settings.txt")
    except Exception as e:
        print(f"Error changing to silentMode: {e}") 
    
# Set-up
def run_setup():
    print("Setting up program, please customize the settings file...")
    speak("Setting up program, please customize the settings file...")
    settings()
    print("To open this file again, say... \"open settings\"")
    speak("To open this file again, say. open settings")

def repeat(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        last_line = lines[-1]
        message = last_line.split(': ')[-1].strip()
        return message

# Settings
def settings():
    speak("Opening settings...")
    print("Opening settings...")
    file_path = "Skills/CoreFiles/settings.txt"
    if os.path.exists(file_path):
        if platform.system() == "Windows":
            os.system(f"start {file_path}")  # Windows
        elif platform.system() == "Darwin":
            os.system(f"open {file_path}")  # macOS
        elif platform.system() == "Linux":
            os.system(f"xdg-open {file_path}")  # Linux
        else:
            print("Unsupported platform")
            speak("Unsupported platform")
            record_action("Settings opened")
    else:
        print(f"File {file_path} not found")
        speak(f"File {file_path} not found")

# Alarms
def open_alarms():
    speak("Opening alarms file...")
    print("Opening alarms file...")
    file_path = "Skills/CoreFiles/alarms.txt"
    if os.path.exists(file_path):
        if platform.system() == "Windows":
            os.system(f"start {file_path}")  # Windows
        elif platform.system() == "Darwin":
            os.system(f"open {file_path}")  # macOS
        elif platform.system() == "Linux":
            os.system(f"xdg-open {file_path}")  # Linux
        else:
            print("Unsupported platform")
            speak("Unsupported platform")
            record_action("Alarms file opened")
    else:
        print(f"File {file_path} not found")
        speak(f"File {file_path} not found")

# Alarms
def check_alarms():
    while True:
        with open("Skills/CoreFiles/alarms.txt", "r") as f:
            alarms = [line.strip() for line in f]
        now = datetime.now().strftime("%H:%M %p,%A")
        for alarm in alarms:
            time_day = alarm.split(',')
            if time_day[0] == now.split(',')[0]:
                if time_day[1] == 'all' or time_day[1].lower() == now.split(',')[1].lower():
                    playsound('Skills/CoreFiles/alarm.mp3')
                    alarms.remove(alarm)
                    record_action(f"Alarm gone off: {alarm}")
                    with open("alarms.txt", "w") as f:
                        for alarm in alarms:
                            f.write(alarm + "\n")
        sleep(1)

# Volume command
def volume():
    print("What percent would you like the volume?")
    speak("What percent would you like the volume?")
    volume2 = recognize_speech()
    try:
        volume2 = int(volume2)
        if volume2 < 0 or volume2 > 100:
            raise ValueError
    except ValueError:
        print("Please enter a valid volume value between 0 and 100.")
        return
    
    if platform == "win32": # Windows
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        # Convert percent to a scalar value between 0 and 1
        scalar = float(volume2) / 100.0
        # Set the volume
        volume.SetMasterVolumeLevelScalar(scalar, None)
        record_action(f"Volume set to {volume2}%")
        print(f"Volume has been set to {volume2}%")
        speak(f"Volume has been set to {volume2}%")
    elif platform == "darwin": # macOS
    # Convert percent to dB
            dB = int((volume2 / 100) * 20) - 20
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
                IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            volume.SetMasterVolumeLevel(dB, None)
            record_action(f"Volume set to {volume2}%")
            print(f"Volume has been set to {volume2}%")
            speak(f"Volume has been set to {volume2}%")
    elif platform.startswith("linux"): # Linux
            subprocess.run(['amixer', 'set', 'Master', f'{volume2}%'])
            record_action(f"Volume set to {volume2}%")
            print(f"Volume has been set to {volume2}%")
            speak(f"Volume has been set to {volume2}%")
    else:
        print("Unsupported platform")
        speak("Unsupported platform")