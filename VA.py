# Import libraries
import os
import json
from datetime import datetime
import threading
# Import Skills
from Skills.Acore import *
from Skills.computerStatistics import *
from Skills.controlSpotify import *
from Skills.controlYoutube import *
from Skills.dateTeller import *
from Skills.jokeTeller import *
from Skills.lockComputer import *
from Skills.newsTeller import *
from Skills.screenshot import *
from Skills.searchGoogle import *
from Skills.searchMap import *
from Skills.takePicture import *
from Skills.tellMeAbout import *
from Skills.translate import *
from Skills.weatherTeller import *
from Skills.webSpeedTest import *

with open("Skills/CoreFiles/intents.json") as file:
    intents = json.load(file)

def process_command(command):
    # Volume command
    if "volume" in command:
        return volume()
    # Intents
    for intent in intents["intents"]:
        if command in intent["patterns"]:
            response = intent["responses"][0]
            print(response)
            speak(response)
            return
    silent_Mode()

# Define the main loop
def main_loop():
    if not os.path.isfile('Skills/CoreFiles/voice.log'):
        run_setup()
        open('Skills/CoreFiles/voice.log', 'w').close()
    # Start the alarm thread
    alarm_thread = threading.Thread(target=check_alarms)
    alarm_thread.start()
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
        elif "settings" in text:
            settings()
        elif "alarms" in text:
            open_alarms()
        elif "repeat" in text:
            last_line = repeat("Skills/CoreFiles/voice.log")
            print(last_line)
            speak(last_line)
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
        if "shut down" in text:
            speak("Shutting down")
            record_action('Shut down')
            quit()

# Start the program
if __name__ == "__main__":
    main_loop()