from Skills.Acore import *
from datetime import datetime
from playsound import playsound
from time import sleep
import re
import dateutil.relativedelta as relativedelta

# Alarm activate
def check_alarms():
    while True:
        with open("Skills/CoreFiles/alarms.txt", "r") as f:
            alarms = [line.strip() for line in f]
        now = datetime.now().strftime("%H:%M %p,%A")
        for alarm in alarms:
            time_day = alarm.split(',')
            if time_day[0] == now.split(',')[0]:
                if time_day[1] == 'all' or time_day[1].lower() == now.split(',')[1].lower():
                    if "autodelete" in alarm:
                        with open("Skills/CoreFiles/alarms.txt", "w") as f:
                            for line in alarms:
                                if line != alarm:
                                    f.write(line + "\n")
                        break
                    record_action(f"Alarm gone off: {alarm}")
                    playsound('Skills/CoreFiles/alarm.mp3')
        sleep(1)

# Open alarms file
def open_alarms():
    speak("Opening alarms file...")
    print("Opening alarms file...")
    file_path = "Skills/CoreFiles/alarms.txt"
    if os.path.exists(file_path):
        if platform.system() == "Windows":
            os.system(f"start {file_path}")  # Windows
        elif platform.system() == "Darwin":
            os.system(f"open {file_path}")  # macOS
        elif platform.system() == "Linux":
            os.system(f"xdg-open {file_path}")  # Linux
        else:
            print("Unsupported platform")
            speak("Unsupported platform")
            record_action("Alarms file opened")
    else:
        print(f"File {file_path} not found")
        speak(f"File {file_path} not found")

# Alarm creator
def create_alarm():
    print("When do you want to set the alarm? ")
    speak("When do you want to set the alarm? ")
    time_str = recognize_speech()
    time_str = time_str.replace(".", "")
    # Check if the user has specified a time interval in minutes or hours
    interval = 0
    m = re.search(r"(\d+) (minute|hour)", time_str)
    if m:
        interval = int(m.group(1))
        unit = m.group(2)
        if unit == "hour":
            interval *= 60  # convert hours to minutes
    # Parse the time string if a specific time was not given
    if not interval:
        time_str = time_str.replace(":", "")
        time_obj = datetime.strptime(time_str, "%H%M %p")
        time_str_24h = time_obj.strftime("%H:%M %p").replace(" 0", " ")
        print("What days would you like the alarm? ")
        speak("What days would you like the alarm? ")
        days_str = recognize_speech()
        days_list = days_str.split()
        days_str_comma = ",".join(days_list)
        print("Would you like this alarm to be one time?")
        speak("Would you like this alarm to be one time?")
        decision = recognize_speech()
        if "yes" in decision:
            days_str_comma = "autodelete"
        else:
            pass
    else:
        now = datetime.now()
        alarm_time = now + relativedelta.relativedelta(minutes=interval)
        time_str_24h = alarm_time.strftime("%H:%M %p")
        print("Would you like this alarm to be one time?")
        speak("Would you like this alarm to be one time?")
        decision = recognize_speech()
        if "yes" in decision:
            days_str_comma = "all,autodelete"
        else:
            days_str_comma = "all"
    
    with open("Skills/CoreFiles/alarms.txt", "a") as f:
        f.write(f"{time_str_24h},{days_str_comma}\n")
    print("Alarm has been created")
    speak("Alarm has been created")
    record_action(f"Alarm created for: {time_str_24h}, {days_str_comma}")