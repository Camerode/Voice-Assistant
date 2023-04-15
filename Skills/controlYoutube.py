from Skills.Acore import speak, recognize_speech, record_action
import pywhatkit

# Youtube
def youtube_play():
    print("What would you like to play?")
    speak("What would you like to play?")
    query = recognize_speech()
    song = query.replace("play", "")
    pywhatkit.playonyt(song)
    print(f"Now playing {query}")
    speak(f"Now playing {query}")
    record_action(f"Playlist started: {query}")