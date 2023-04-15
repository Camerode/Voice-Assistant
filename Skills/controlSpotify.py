from Skills.Acore import speak
import os

# Spotify
def open_spotify():
    print("Opening Spotify...")
    # Assuming that `speak()` is defined and working correctly
    speak("Opening Spotify")
    try:
        with open('Skills/CoreFiles/settings.txt', 'r') as f:
            # Read the contents of the file
            contents = f.read()
        # Split the contents into lines
        lines = contents.split('\n')
        # Search for the variable we're interested in
        for line in lines:
            # Split the line into key and value
            key_value = line.split('=')
            # If the key is the one we're looking for, return the value
            if key_value[0] == 'spotifyPath':
                my_variable = key_value[1]
                os.startfile(my_variable)
                break
        else:
            # If the loop completes without finding the variable, raise an error
            raise ValueError("SpotifyPath not found in settings.txt")
    except Exception as e:
        # Catch any errors and print a message
        print(f"Error opening Spotify: {e}")