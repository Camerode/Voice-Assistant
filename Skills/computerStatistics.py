from Skills.Acore import speak
import math
import psutil

# Computer statistics
def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])
def system_stats():
    try:
        cpu_stats = str(psutil.cpu_percent())
        battery_percent = psutil.sensors_battery().percent
        memory_in_use = convert_size(psutil.virtual_memory().used)
        total_memory = convert_size(psutil.virtual_memory().total)
        stats = f"Currently {cpu_stats} percent of CPU, {memory_in_use} of RAM out of total {total_memory} is being used and " \
                    f"battery level is at {battery_percent}%"
        print(stats)
        speak(stats)
    except Exception as e:
        print("An error has occurred in the computerStatistics command, output has been sent to errors.log")
        speak("An error has occurred in the computerStatistics command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write("system_stats: " + str(e) + "\n")