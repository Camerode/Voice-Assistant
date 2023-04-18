from Skills.Acore import recognize_speech, speak, record_action
import webbrowser

# Google search
def google_search():
    try:
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
    except Exception as e:
        print("An error has occurred in the searchGoogle command, output has been sent to errors.log")
        speak("An error has occurred in the searchGoogle command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write("google_search: " + str(e) + "\n")