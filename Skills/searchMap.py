from Skills.Acore import speak, recognize_speech, record_action
import webbrowser

# Map
def get_map():
    try:
        print('What do you want to search for on the map?')
        speak('What do you want to search for on the map?')
        query = recognize_speech()
        print('Searching')
        speak('Searching')
        webbrowser.open(f'https://www.google.com/maps/search/{query}')
        record_action('Map Search: ' + query)
        print('Search completed')
        speak('Search completed')
    except Exception as e:
        print("An error has occurred in the searchMap command, output has been sent to errors.log")
        speak("An error has occurred in the searchMap command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write("get_map: " + str(e) + "\n")