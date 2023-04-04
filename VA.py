import os
import speech_recognition as sr
import pyttsx3
import json
from datetime import datetime
from modules import *
from icecream import ic

# Load the intents file
with open("intents.json") as file:
    intents = json.load(file)

# Initialize the text-to-speech engine
engine = pyttsx3.init()


# Define a function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Get voice mode settings configuration
def use_voice_setting():
    with open('settings.txt', 'r') as f:
        contents = f.read()
    lines = contents.split('\n')
    for line in lines:
        key_value = line.split('=')
        if key_value[0] == 'useVoice':
            useVoice = key_value[1].strip()
            return True if useVoice.lower() == 'true' else False
    raise ValueError("useVoice not found in settings.txt")

useVoice = use_voice_setting()

# Define a function to recognize speech
def recognize_speech(use_voice=useVoice):
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

# Runs a setup if the program has never ran before
def run_setup():
    print("Setting up program, please customize the settings file...")
    speak("Setting up program, please customize the settings file...")
    settings()
    print("To open this file again, say... \"open settings\"")
    speak("To open this file again, say. open settings")

# Mapping commands to their corresponding functions
def process_command(command):
    command_mapping = {
        "volume": volume,
        "lock": lock_computer,
        "settings": settings,
        "date": get_datetime,
        "time": get_datetime,
        "computer statistics": system_stats,
        "search": google_search,
        "map": get_map,
        "tell me about": tell_me_about,
        "screenshot": screen_shot,
        "take a picture": take_picture_and_save,
        "speed test": run_speed_test,
        "joke": tell_joke,
        "weather": get_current_weather,
        "forecast": weather_forecast,
        "news": read_unread_rss,
        "spotify": open_spotify,
        "youtube": youtube_play,
        "translate": process_translation,
        "shut down": quit
    }

    # Run the corresponding function if the command exists in the mapping
    command_func = command_mapping.get(command)
    if command_func:
        return command_func()
    else:
        return handle_unrecognized_command()

# Define a function to process translations
def process_translation():
    language_mapping = {
        "german": translate_to_german,
        "hindi": translate_to_hindi,
        "spanish": translate_to_spanish,
        "french": translate_to_french,
        "russian": translate_to_russian,
        "japanese": translate_to_japanese,
        "italian": translate_to_italian,
        "greek": translate_to_greek,
        "swedish": translate_to_swedish,
        "hungarian": translate_to_hungarian
    }
    for lang, func in language_mapping.items():
        if lang in text:
            func()
            break

def handle_unrecognized_command():
    try:
        with open('settings.txt', 'r') as f:
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

def record_action(action):
    current_time = datetime.now()
    with open('actions.log', 'a') as log_file:
        log_file.write(f'{current_time}: {action}\n')

def main_loop():
    if not os.path.isfile('setup_complete.txt'):
        run_setup()
        open('setup_complete.txt', 'w').close()

    while True:
        text = recognize_speech()
        if "wake" in text:
            record_action("Woken up")
            hour = datetime.now().hour
            if hour >= 0 and hour < 12:
                morning = "Good morning"
                print(morning)
                speak(morning)
                break
            elif hour >= 12 and hour < 16:
                afternoon = "Good afternoon"
                print(afternoon)
                speak(afternoon)
                break
            else:
                evening = "Good evening"
                print(evening)
                speak(evening)
                break

    previous_response = ""
    while True:
        text = recognize_speech()
        if "sleep" in text:
            print("Going to sleep until wake word")
            speak("Going to sleep until wake word")
            record_action('Slept')
            main_loop()
        elif "repeat" in text:
            speak(previous_response)
            record_action('Repeated: ' + previous_response)
        else:
            previous_response = process_command(text)

if __name__ == "__main__":
    main_loop()