from VA import recognize_speech, speak, record_action
import psutil
import math
import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
import tkinter as tk
import os
import wikipedia
import re
from PIL import ImageGrab
import cv2
from PIL import Image
import platform
from deep_translator import GoogleTranslator
from langdetect import detect
import requests
import geocoder
import feedparser
from sys import platform
from pathlib import Path
import platform as pl
import json
from speedtest import Speedtest
import ctypes
import subprocess
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

###################################################################################################
# Settings/Volume
###################################################################################################
# Opens settings text file
def settings():
    speak("Opening settings...")
    print("Opening settings...")
    file_path = "settings.txt"
    if os.path.exists(file_path):
        if platform == "win32":
            os.system(f"start {file_path}")  # Windows
        elif platform == "darwin":
            os.system(f"open {file_path}")  # macOS
        elif platform.startswith("linux"):
            os.system(f"xdg-open {file_path}")  # Linux
        else:
            print("Unsupported platform")
            speak("Unsupported platform")
            record_action("Settings opened")
    else:
        print(f"File {file_path} not found")
        speak(f"File {file_path} not found")

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
###################################################################################################
# Modules
###################################################################################################
# Computer statistics
def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])
def system_stats():
    cpu_stats = str(psutil.cpu_percent())
    battery_percent = psutil.sensors_battery().percent
    memory_in_use = convert_size(psutil.virtual_memory().used)
    total_memory = convert_size(psutil.virtual_memory().total)
    stats = f"Currently {cpu_stats} percent of CPU, {memory_in_use} of RAM out of total {total_memory} is being used and " \
                f"battery level is at {battery_percent}%"
    print(stats)
    speak(stats)

# Google search
def google_search():
    query = recognize_speech()
    print('Searching')
    speak('Searching')
    if 'image' in query:
        query += "&tbm=isch"
    query = query.replace('images', '')
    query = query.replace('image', '')
    query = query.replace('search', '')
    query = query.replace('show', '')
    query = query.replace('google', '')
    query = query.replace('tell me about', '')
    query = query.replace('for', '')
    webbrowser.open("https://www.google.com/search?q=" + query)
    record_action('Searched: ' + query)
    print('Search completed')
    speak('Search completed') 

# Map
def get_map():
    print('What do you want to search for on the map?')
    speak('What do you want to search for on the map?')
    query = recognize_speech()
    print('Searching')
    speak('Searching')
    webbrowser.open(f'https://www.google.com/maps/search/{query}')
    record_action('Map Search: ' + query)
    print('Search completed')
    speak('Search completed')

# Tell me
def tell_me_about():
    print('What would you like to be told about?')
    speak('What would you like to be told about?')
    query = recognize_speech()
    try:
        topic = query.replace("tell me about ", "") #re.search(r'([A-Za-z]* [A-Za-z]* [A-Za-z]*)$', query)[1]
        result = wikipedia.summary(topic, sentences=3)
        result = re.sub(r'\[.*]', '', result)
        print(result)
        speak(result)
        record_action('Told about: ' + query)
    except (wikipedia.WikipediaException, Exception) as e:
        return None

# Take a screenshot
def screen_shot():
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

# Take a picture
def take_picture_and_save():
    # Open the default camera
    cap = cv2.VideoCapture(0)
    # Wait for the camera to warm up
    time.sleep(1)
    # Capture an image from the camera
    ret, frame = cap.read()
    # Release the camera resource
    cap.release()
    # Check if the image was captured successfully
    if not ret:
        print("Error: failed to capture image from camera.")
        speak("Error: failed to capture image from camera.")
        return
    # Convert the OpenCV image to a Pillow image
    img = Image.fromarray(frame)
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
    filename = f"picture_{int(time.time())}.jpg"
    # Save the captured image to the downloads folder
    img.save(os.path.join(downloads_path, filename), "JPEG")
    print(f"Picture saved as {filename} in the Downloads folder.")
    speak(f"Picture saved as {filename} in the Downloads folder.")
    record_action('Camera used')

# Speed test
def run_speed_test():
    speak(f"Running speed test, this can take up to a minute")
    # Create a Speedtest object
    st = Speedtest()
    # Get the download and upload speeds
    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000
    # Print the results
    print(f"Download speed: {download_speed:.2f} Mbps")
    print(f"Upload speed: {upload_speed:.2f} Mbps")
    speak(f"Download speed: {download_speed:.2f} Mbps")
    speak(f"Upload speed: {upload_speed:.2f} Mbps")
    record_action(f"Speed test - Download speed: {download_speed:.2f} Mbps")
    record_action(f"Speed test - Upload speed: {upload_speed:.2f} Mbps")

# Joke
def tell_joke():   
    def jokes(f):
        data = requests.get(f)
        tt = json.loads(data.text)
        return tt
    f = r"https://official-joke-api.appspot.com/random_joke"
    a = jokes(f)
    for i in (a):
        #print(a["type"])
        print(a["setup"])
        speak(a["setup"])
        print(a["punchline"], "\n")
        speak(a["punchline"])
        print("Would you like another joke?")
        speak("Would you like another joke?")
        break
      
# Current weather
def get_current_weather():
    g = geocoder.ip('me', timeout=10)
    latitude, longitude = g.latlng
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    temperature = str(data['current_weather']['temperature'])
    wind_speed = str(data['current_weather']['windspeed'])
    weather_type = str(data['current_weather']['weathercode'])
    if weather_type == '0':
        weather_type = ' weather type is unkown, cloud development not observed or not observable'
    elif weather_type == '1': 
        weather_type = 'the sky is becoming clear, clouds are generally disolving or becoming less developed'
    elif weather_type == '2': 
        weather_type = 'the sky is clear'
    elif weather_type == '3': 
        weather_type = 'the sky is almost clear, clouds are forming'
    elif weather_type == '4': 
        weather_type = 'the sky visibility is reduced due to smoke, possible due to examples like forest fires, industrial smoke or volcanic ashes'
    elif weather_type == '5': 
        weather_type = 'the sky is hazey'
    elif weather_type == '6': 
        weather_type = 'there is widespread dust in suspension in the air, not raised by wind at or near the station at the time of observation'
    elif weather_type == '7': 
        weather_type = 'dust or sand raised by wind at or near the station at the time of observation, but no well developed dust whirl(s) or sand whirl(s), and no duststorm or sandstorm seen'
    elif weather_type == '8': 
        weather_type = 'there are well developed dust whirl(s) or sand whirl(s) seen at or near the station during the preceding hour or at the time ot observation, but no duststorm or sandstorm'
    elif weather_type == '9': 
        weather_type = 'there is a duststorm or sandstorm within sight at the time of observation, or at the station during the preceding hour'
    elif weather_type == '10': 
        weather_type = 'the weather is misty'
    elif weather_type == '11': 
        weather_type = 'there are patches of rain in the area'
    elif weather_type == '12': 
        weather_type = 'there is more or less continous rain'
    elif weather_type == '13': 
        weather_type = 'there is lightning visible, no thunder heard'
    elif weather_type == '14': 
        weather_type = 'there is precipitation in sight, but is not reaching the ground or surface of the sea'
    elif weather_type == '15': 
        weather_type = 'there is precipitation within sight, reaching the ground or the surface of the sea, but distant, i.e. estimated to be more than 5 km from the station'
    elif weather_type == '16': 
        weather_type = 'there is precipitation within sight, reaching the ground or the surface of the sea, near to, but not at the station'
    elif weather_type == '17': 
        weather_type = 'there is a thunderstorm, but no precipitation at the time of observation'
    elif weather_type == '18': 
        weather_type = 'there are gusts of winds or a localized storm'
    elif weather_type == '19': 
        weather_type = 'funnel cloud(s) have been observed'
    elif weather_type == '20': 
        weather_type = 'there is a Drizzle (not freezing) or snow grains'
    elif weather_type == '21': 
        weather_type = 'there is rain (not freezing)'
    elif weather_type == '22': 
        weather_type = 'there is snow'
    elif weather_type == '23': 
        weather_type = 'there is rain and snow or ice pellets'
    elif weather_type == '24': 
        weather_type = 'there is a freezing drizzle or freezing rain'
    elif weather_type == '25': 
        weather_type = 'shower(s) of rain have been observed'
    elif weather_type == '26': 
        weather_type = 'shower(s) of snow, or of rain and snow have been observed'
    elif weather_type == '27': 
        weather_type = 'shower(s) of hail, or of rain and hail have been observed'
    elif weather_type == '28': 
        weather_type = 'fog or ice fog has been observed'
    elif weather_type == '29': 
        weather_type = 'there is a thunderstorm (with or without precipitation)'
    elif weather_type == '30': 
        weather_type = 'there is a slight or moderate duststorm or sandstorm'
    elif weather_type == '31': 
        weather_type = 'there is a slight or moderate duststorm or sandstorm'
    elif weather_type == '32': 
        weather_type = 'there is a slight or moderate duststorm or sandstorm'
    elif weather_type == '33': 
        weather_type = 'there is a severe duststorm or sandstorm'
    elif weather_type == '34': 
        weather_type = 'there is a severe duststorm or sandstorm'
    elif weather_type == '35': 
        weather_type = 'there is a severe duststorm or sandstorm'
    elif weather_type == '36': 
        weather_type = 'there is a slight or moderate blowing snow'
    elif weather_type == '37': 
        weather_type = 'there is a heavy drifting snow'
    elif weather_type == '38': 
        weather_type = 'there is a slight or moderate blowing snow'
    elif weather_type == '39': 
        weather_type = 'there is a heavy drifting snow'
    elif weather_type == '40': 
        weather_type = 'there is a fog or ice fog at a distance at the time of observation, but not at the station during the preceding hour, the fog or ice fog extending to a level above that of the observer'
    elif weather_type == '41': 
        weather_type = 'there is a fog or ice fog in patches'
    elif weather_type == '42': 
        weather_type = 'there is a fog or ice fog, sky is visible'
    elif weather_type == '43': 
        weather_type = 'there is a fog or ice fog, sky is invisible'
    elif weather_type == '44': 
        weather_type = 'there is a fog or ice fog, sky is visible'
    elif weather_type == '45': 
        weather_type = 'there is a fog or ice fog, sky is invisible'
    elif weather_type == '46': 
        weather_type = 'there is a fog or ice fog, sky is visible'
    elif weather_type == '47': 
        weather_type = 'there is a fog or ice fog, sky is invisible'
    elif weather_type == '48': 
        weather_type = 'there is a fog, depositing rime, sky is visible'
    elif weather_type == '49': 
        weather_type = 'there is a fog, depositing rime, sky is invisible'
    elif weather_type == '50': 
        weather_type = 'there is a drizzle, not freezing, intermittent'
    elif weather_type == '51': 
        weather_type = 'there is a drizzle, not freezing, continuous'
    elif weather_type == '52': 
        weather_type = 'there is a drizzle, not freezing, intermittent'
    elif weather_type == '53': 
        weather_type = 'there is a drizzle, not freezing, continuous'
    elif weather_type == '54': 
        weather_type = 'there is a drizzle, not freezing, intermittent'
    elif weather_type == '55': 
        weather_type = 'there is a drizzle, not freezing, continuous'
    elif weather_type == '56': 
        weather_type = 'there is a drizzle, freezing, slight'
    elif weather_type == '57': 
        weather_type = 'there is a drizzle, freezing, moderate or heavy (dence)'
    elif weather_type == '58': 
        weather_type = 'there is a drizzle and rain, slight'
    elif weather_type == '59': 
        weather_type = 'there is a drizzle and rain, moderate or heavy'
    elif weather_type == '60': 
        weather_type = 'there is rain, not freezing, intermittent'
    elif weather_type == '61': 
        weather_type = 'there is rain, not freezing, continuous'
    elif weather_type == '62': 
        weather_type = 'there is rain, not freezing, intermittent'
    elif weather_type == '63': 
        weather_type = 'there is rain, not freezing, continuous'
    elif weather_type == '64': 
        weather_type = 'there is rain, not freezing, intermittent'
    elif weather_type == '65': 
        weather_type = 'there is rain, not freezing, continuous'
    elif weather_type == '66': 
        weather_type = 'there is rain, freezing, slight'
    elif weather_type == '67': 
        weather_type = 'there is rain, freezing, moderate or heavy (dence)'
    elif weather_type == '68': 
        weather_type = 'there is rain or drizzle and snow, slight'
    elif weather_type == '69': 
        weather_type = 'there is rain or drizzle and snow, moderate or heavy'
    elif weather_type == '70': 
        weather_type = 'there is an intermittent fall of snowflakes'
    elif weather_type == '71': 
        weather_type = 'there is a continuous fall of snowflakes'
    elif weather_type == '72': 
        weather_type = 'there is an intermittent fall of snowflakes'
    elif weather_type == '73': 
        weather_type = 'there is a continuous fall of snowflakes'
    elif weather_type == '74': 
        weather_type = 'there is an intermittent fall of snowflakes'
    elif weather_type == '75': 
        weather_type = 'there is a continuous fall of snowflakes'
    elif weather_type == '76': 
        weather_type = 'there is diamond dust (with or without fog)'
    elif weather_type == '77': 
        weather_type = 'there are now grains (with or without fog)'
    elif weather_type == '78': 
        weather_type = 'there are isolated star-like snow crystals (with or without fog)'
    elif weather_type == '79': 
        weather_type = 'there are ice pellets'
    elif weather_type == '80': 
        weather_type = 'slight rain shower(s) have been observed'
    elif weather_type == '81': 
        weather_type = 'moderate or heavy rain shower(s) have been observed'
    elif weather_type == '82': 
        weather_type = 'violent rain shower(s) have been observed'
    elif weather_type == '83': 
        weather_type = 'slight shower(s) of rain and snow mixed have been observed'
    elif weather_type == '84': 
        weather_type = 'moderate or heavy shower(s) of rain and snow mixed have been observed'
    elif weather_type == '85': 
        weather_type = 'slight snow shower(s) have been observed'
    elif weather_type == '86': 
        weather_type = 'moderate or heavy snow shower(s) have been observed'
    elif weather_type == '87': 
        weather_type = 'shower(s) of snow pellets or small hail, with or without rain or rain and snow mixed have been observed'
    elif weather_type == '88': 
        weather_type = 'shower(s) of snow pellets or small hail, with or without rain or rain and snow mixed have been observed'
    elif weather_type == '89': 
        weather_type = 'shower(s) of hail, with or without rain or rain and snow mixed that are not associated with thunder have been observed'
    elif weather_type == '90': 
        weather_type = 'shower(s) of hail, with or without rain or rain and snow mixed that are not associated with thunder have been observed'
    elif weather_type == '91': 
        weather_type = 'there is slight rain at time of observation'
    elif weather_type == '92': 
        weather_type = 'there is moderate or heavy rain at time of observation'
    elif weather_type == '93': 
        weather_type = 'there is slight snow, or rain and snow mixed or hail at time of observation'
    elif weather_type == '94': 
        weather_type = 'moderate or heavy snow, or rain and snow mixed or hail at time of observation'
    elif weather_type == '95': 
        weather_type = 'there is a thunderstorm, slight or moderate, without hail but with rain and/or snow at time of observation'
    elif weather_type == '96': 
        weather_type = 'there is a thunderstorm, slight or moderate, with hail at time of observation'
    elif weather_type == '97': 
        weather_type = 'there is a thunderstorm, heavy, without hail but with rain and/or snow at time of observation'
    elif weather_type == '98': 
        weather_type = 'there is a thunderstorm combined with duststorm or sandstorm at time of observation'
    elif weather_type == '99': 
        weather_type = 'there is a thunderstorm, heavy, with hail at time of observation'
    print('The temperature is at ' + temperature + ' degrees Celcius, wind speed is ' + wind_speed + ' meters per second and ' + weather_type)
    speak('The temperature is at ' + temperature + ' degrees Celcius, wind speed is ' + wind_speed + ' meters per second and ' + weather_type)
    record_action(f"Getting weather - Temp: {temperature}, Wind speed: {wind_speed}, Weather Type: {weather_type}")
# Website: https://www.meteomatics.com/en/api/available-parameters/derived-weather-and-convenience-parameters/general-weather-state/

# Weather forecast
def weather_forecast():
    print('Getting your weather forecast')
    speak('Getting your weather forecast')
    webbrowser.open('https://www.google.com/search?q=weather+forecast')
    print('Search completed')   
    speak('Search completed')
    record_action('Weather forecast')

# News
def read_unread_rss():
    # Load the RSS feed
    feed_url = 'https://feeds.bbci.co.uk/news/world/rss.xml'
    feed = feedparser.parse(feed_url)
    # Load previously read article IDs and spoken article IDs from separate files
    try:
        with open('read_articles.txt', 'r') as f:
            read_article_ids = set(f.read().splitlines())
    except FileNotFoundError:
        read_article_ids = set()
    try:
        with open('spoken_articles.txt', 'r') as f:
            spoken_article_ids = set(f.read().splitlines())
    except FileNotFoundError:
        spoken_article_ids = set()
    # Check for unread articles
    unread_articles = []
    for entry in feed.entries:
        if entry.id not in read_article_ids and entry.id not in spoken_article_ids:
            unread_articles.append(entry)
    # Print out the unread articles
    if unread_articles:
        print(f'Found {len(unread_articles)} unread articles:')
        speak(f'Found {len(unread_articles)} unread articles:')
        for entry in unread_articles:
            print(f'Title: {entry.title} | Date: {entry.published} | Link: {entry.link} | Summary: {entry.summary}')
            speak(f'Title. {entry.title}. Date published. {entry.published}. Summary. {entry.summary}\n')
            record_action(f'News Read -  Title: {entry.title} | Link: {entry.link}')
            print('Would you like to read the next article?')
            speak('Would you like to read the next article?')
            decision = recognize_speech()
            if 'no' in decision:
                spoken_article_ids.add(entry.id)
                print('News reading ended')
                speak('News reading ended')
                break
            elif 'yes' in decision:
                spoken_article_ids.add(entry.id)
    # Update the list of read article IDs and spoken article IDs
    with open('read_articles.txt', 'a') as f:
        for entry in spoken_article_ids:
            f.write(entry + '\n')
    if not unread_articles:
        print('All articles have been read')
        speak('All articles have been read')
        print('Would you like to open BBC news?')
        speak('Would you like to open BBC news?')
        text = recognize_speech()
        if 'yes' in text:
            webbrowser.open('https://www.bbc.co.uk/news/world')

# Computer locker
def lock_computer():
    if platform == "win32":
        ctypes.windll.user32.LockWorkStation()  # Windows
    elif platform == "darwin":
        subprocess.call(["/System/Library/CoreServices/Menu Extras/User.menu/Contents/Resources/CGSession", "-suspend"])  # Mac
    elif platform.startswith("linux"):
        subprocess.call(["gnome-screensaver-command", "-l"])  # Linux
    else:
        print("Unsupported platform")
        speak("Unsupported platform")

# Get Date and time
def get_datetime():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H:%M")
    formatted_date = current_time.strftime("%d/%m/%Y")

    hour = datetime.now().hour
    if hour >= 0 and hour < 12:
        morning = "in the morning"
        print(f"The time is now {formatted_time} {morning}, the date is the {formatted_date}.")
        speak(f"The time is now {formatted_time} {morning}, the date is the {formatted_date}.")
    elif hour >= 12 and hour < 16:
        afternoon = "in the afternoon"
        print(f"The time is now {formatted_time} {afternoon}, the date is the {formatted_date}.")
        speak(f"The time is now {formatted_time} {afternoon}, the date is the {formatted_date}.")
    else:
        evening = "in the evening"
        print(f"The time is now {formatted_time} {evening}, the date is the {formatted_date}.")
        speak(f"The time is now {formatted_time} {evening}, the date is the {formatted_date}.")

###################################################################################################
# Open applications & Application commands
###################################################################################################

# Spotify
def open_spotify():
    print("Opening Spotify...")
    # Assuming that `speak()` is defined and working correctly
    speak("Opening Spotify")
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
            if key_value[0] == 'spotifyPath':
                my_variable = key_value[1]
                os.startfile(my_variable)
                break
        else:
            # If the loop completes without finding the variable, raise an error
            raise ValueError("SpotifyPath not found in settings.txt")
    except Exception as e:
        # Catch any errors and print a message
        print(f"Error opening Spotify: {e}")

###################################################################################################
# Module Translators
###################################################################################################

# German
def translate_to_german():
    speak('What would you like to translate into German?')
    text = recognize_speech()
    # Detect language
    detected_language = detect(text)
    # Translate
    language_translation = GoogleTranslator(source=detected_language, target='de').translate(text)
    print(language_translation)
    speak(language_translation)
    record_action('Translated: ' + text + ' | into: German')

# Hindi
def translate_to_hindi():
    speak('What would you like to translate into Hindi?')
    text = recognize_speech()
    # Detect language
    detected_language = detect(text)
    # Translate
    language_translation = GoogleTranslator(source=detected_language, target='hi').translate(text)
    print(language_translation)
    speak(language_translation)
    record_action('Translated: ' + text + ' | into: Hindi')

# Spanish
def translate_to_spanish():
    speak('What would you like to translate into Spanish?')
    text = recognize_speech()
    # Detect language
    detected_language = detect(text)
    # Translate
    language_translation = GoogleTranslator(source=detected_language, target='es').translate(text)
    print(language_translation)
    speak(language_translation)
    record_action('Translated: ' + text + ' | into: Spanish')

# French
def translate_to_french():
    speak('What would you like to translate into French?')
    text = recognize_speech()
    # Detect language
    detected_language = detect(text)
    # Translate
    language_translation = GoogleTranslator(source=detected_language, target='fr').translate(text)
    print(language_translation)
    speak(language_translation)
    record_action('Translated: ' + text + ' | into: French')

# Russian
def translate_to_russian():
    speak('What would you like to translate into Russian?')
    text = recognize_speech()
    # Detect language
    detected_language = detect(text)
    # Translate
    language_translation = GoogleTranslator(source=detected_language, target='ru').translate(text)
    print(language_translation)
    speak(language_translation)
    record_action('Translated: ' + text + ' | into: Russian')

# Japanese
def translate_to_japanese():
    speak('What would you like to translate into Japanese?')
    text = recognize_speech()
    # Detect language
    detected_language = detect(text)
    # Translate
    language_translation = GoogleTranslator(source=detected_language, target='ja').translate(text)
    print(language_translation)
    speak(language_translation)
    record_action('Translated: ' + text + ' | into: Japanese')

# Italian
def translate_to_italian():
    speak('What would you like to translate into Italian?')
    text = recognize_speech()
    # Detect language
    detected_language = detect(text)
    # Translate
    language_translation = GoogleTranslator(source=detected_language, target='it').translate(text)
    print(language_translation)
    speak(language_translation)
    record_action('Translated: ' + text + ' | into: Italian')

# Greek
def translate_to_greek():
    speak('What would you like to translate into Greek')
    text = recognize_speech()
    # Detect language
    detected_language = detect(text)
    # Translate
    language_translation = GoogleTranslator(source=detected_language, target='el').translate(text)
    print(language_translation)
    speak(language_translation)
    record_action('Translated: ' + text + ' | into: Greek')

# Swedish
def translate_to_swedish():
    speak('What would you like to translate into Swedish?')
    text = recognize_speech()
    # Detect language
    detected_language = detect(text)
    # Translate
    language_translation = GoogleTranslator(source=detected_language, target='sv').translate(text)
    print(language_translation)
    speak(language_translation)
    record_action('Translated: ' + text + ' | into: Swedish')

def translate_to_hungarian():
    speak('What would you like to translate into Hungarian?')
    text = recognize_speech()
    # Detect language
    detected_language = detect(text)
    # Translate
    language_translation = GoogleTranslator(source=detected_language, target='hu').translate(text)
    print(language_translation)
    speak(language_translation)
    record_action('Translated: ' + text + ' | into: Hungarian')