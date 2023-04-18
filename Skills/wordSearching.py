import requests
from bs4 import BeautifulSoup
from Skills.Acore import *

def get_definition():
    try:
        print("What is the word you would like defined?")
        speak("What is the word you would like defined?")
        word = recognize_speech()
        url = "https://www.dictionary.com/browse/{}".format(word)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        definition = soup.find('span', class_='one-click-content').text.strip()
        print(word + " is defined as " + definition)
        speak(word + " is defined as " + definition)
        record_action(word + " was defined as " + definition)
    except Exception as e:
        print("An error has occurred in the create_alarm command, output has been sent to errors.log")
        speak("An error has occurred in the create_alarm command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write("get_definition: " + str(e) + "\n")