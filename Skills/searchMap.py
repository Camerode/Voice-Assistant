from Skills.Acore import speak, recognize_speech, record_action
import webbrowser

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