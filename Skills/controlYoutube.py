from Skills.Acore import speak, recognize_speech, record_action
import pywhatkit

# Youtube
def youtube_play():
    try:
        print("What would you like to play?")
        speak("What would you like to play?")
        query = recognize_speech()
        song = query.replace("play", "")
        pywhatkit.playonyt(song)
        print(f"Now playing {query}")
        speak(f"Now playing {query}")
        record_action(f"Playlist started: {query}")
    except Exception as e:
        print("An error has occurred in the controlYoutube command, output has been sent to errors.log")
        speak("An error has occurred in the controlYoutube command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write("youtube_play: " + str(e) + "\n")