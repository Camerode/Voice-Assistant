from Skills.Acore import recognize_speech, speak, record_action
import webbrowser

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