from Skills.Acore import speak
from datetime import datetime

# Get Date and time
def get_datetime():
    try:
        current_time = datetime.now()
        formatted_time = current_time.strftime("%H:%M")
        formatted_date = current_time.strftime("%d/%m/%Y")

        hour = datetime.now().hour
        if hour >= 0 and hour < 12:
            morning = "in the morning"
            print(f"The time is now {formatted_time} {morning}, the date is the {formatted_date}.")
            speak(f"The time is now {formatted_time} {morning}, the date is the {formatted_date}.")
        elif hour >= 12 and hour < 16:
            afternoon = "in the afternoon"
            print(f"The time is now {formatted_time} {afternoon}, the date is the {formatted_date}.")
            speak(f"The time is now {formatted_time} {afternoon}, the date is the {formatted_date}.")
        else:
            evening = "in the evening"
            print(f"The time is now {formatted_time} {evening}, the date is the {formatted_date}.")
            speak(f"The time is now {formatted_time} {evening}, the date is the {formatted_date}.")
    except Exception as e:
        print("An error has occurred in the dateTeller command, output has been sent to errors.log")
        speak("An error has occurred in the dateTeller command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write("get_datetime: " + str(e) + "\n")