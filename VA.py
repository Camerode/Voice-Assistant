# Version 0.9.4
# Added a youtube play command & other minor changes

# Import libraries
import os
import speech_recognition as sr
import pyttsx3
import json
from datetime import datetime
# Import modules.py
from modules import *

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
useVoice = 'True'  # default value
# Searches settings.txt for the recognize_speech type. Assigns variable as boolean
try:
    with open('settings.txt', 'r') as f:
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

# Define a function to recognize speech | Uses the settings.txt to define where it should be text or voice
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

# Define a function to process a command
def process_command(command):
    # Volume command
    if "volume" in command:
        return volume()

    for intent in intents["intents"]:
        if command in intent["patterns"]:
            response = intent["responses"][0]
            print(response)
            speak(response)
            return
    # Silent mode
    try:
        with open('settings.txt', 'r') as f:
            # Read the contents of the file
            contents = f.read()
        # Split the contents into lines
        lines = contents.split('\n')
        # Search for the variable we're interested in
        for line in lines:
            # Split the line into key and value
            key_value = line.split('=')
            # If the key is the one we're looking for, return the value
            if key_value[0] == 'silentMode':
                my_variable = key_value[1]
                if my_variable.lower() == "off":
                    speak("Sorry, I do not have a response...")
                break
        else:
            # If the loop completes without finding the variable, raise an error
            raise ValueError("silentMode not found in settings.txt")
    except Exception as e:
        # Catch any errors and print a message
        print(f"Error changing to silentMode: {e}") 

# Record actions
def record_action(action):
    # Get the current date and time
    current_time = datetime.now()
    # Open the log file in append mode
    with open('actions.log', 'a') as log_file:
        # Write the action and timestamp to the log file
        log_file.write(f'{current_time}: {action}\n')

# Define the main loop
def main_loop():
    # Check if the program has been run before
    if not os.path.isfile('setup_complete.txt'):
        # If not, run the setup function
        run_setup()
        # Create a file to indicate that setup has been completed
        open('setup_complete.txt', 'w').close()

    # Wait for the wake word
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

    # Listen for commands #
    # "Repeat" command store
    previous_response = ""
    while True:
        text = recognize_speech()
        # Sleep command
        if "sleep" in text:
            print("Going to sleep until wake word")
            speak("Going to sleep until wake word")
            record_action('Slept')
            main_loop()
        # Locks computer
        if "lock" in text:
            print("Locking computer...")
            speak("Locking computer...")
            record_action('Locking computer')
            lock_computer()
        # Settings command
        if "settings" in text:
            settings()
        # Repeat command
        elif "repeat" in text:
            speak(previous_response)
            record_action('Repeated: ' + previous_response)
        # Date/Time command
        elif "date" in text:
            get_datetime()
        elif "time" in text:
            get_datetime()
        # Computer statistics command
        elif "computer statistics" in text:
            speak("Diagnosing computer statistics")
            system_stats()
        # Search command
        elif "search" in text:
            speak("What would you like to search?")
            google_search()
        # Map command
        elif "map" in text:
            get_map()
        # Tell me about command
        elif "tell me about" in text:
            tell_me_about()
        # Screenshot command
        elif "screenshot" in text:
            screen_shot()
        # Take a picture command
        elif "take a picture" in text:
            take_picture_and_save()
        # Speed test command
        elif "speed test" in text:
            run_speed_test()
        # Joke command
        elif "joke" in text:
            while True:
                tell_joke()
                user_input = recognize_speech()
                if "no" in user_input:
                    break
        #Weather command
        elif "weather" in text:
            # Users Forecast
            if "forecast" in text:
                weather_forecast()
            # My weather location
            else:
                get_current_weather()
        # News command
        elif "news" in text:
            read_unread_rss()
        # Spotify command
        elif "spotify" in text:
            open_spotify()
        # Youtube command
        elif "youtube" in text:
            youtube_play()
        # Translation modules
        elif "translate" in text:
            if "german" in text:
                translate_to_german()
            if "hindi" in text:
                translate_to_hindi()
            if "spanish" in text:
                translate_to_spanish()
            if "french" in text:
                translate_to_french()
            if "russian" in text:
                translate_to_russian()
            if "japanese" in text:
                translate_to_japanese()
            if "italian" in text:
                translate_to_italian()
            if "greek" in text:
                translate_to_greek()
            if "swedish" in text:
                translate_to_swedish()
            if "hungarian" in text:
                translate_to_hungarian()
        # Shut down command
        elif "shut down" in text:
            speak("Shutting down")
            record_action('Shut down')
            quit()
        else:
            previous_response = process_command(text)

# Start the program
if __name__ == "__main__":
    main_loop()