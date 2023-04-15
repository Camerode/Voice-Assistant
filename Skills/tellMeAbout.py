from Skills.Acore import speak, recognize_speech, record_action
import wikipedia
import re

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