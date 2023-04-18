from Skills.Acore import speak, recognize_speech, record_action
import wikipedia
import re

# Tell me
def tell_me_about():
    try:
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
    except Exception as e:
        print("An error has occurred in the tellMeAbout command, output has been sent to errors.log")
        speak("An error has occurred in the tellMeAbout command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write("tell_me_about: " + str(e) + "\n")