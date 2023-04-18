from Skills.Acore import speak
import json
import requests

# Joke
def tell_joke():   
    try:
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
    except Exception as e:
        print("An error has occurred in the jokeTeller command, output has been sent to errors.log")
        speak("An error has occurred in the jokeTeller command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write("tell_joke: " + str(e) + "\n")