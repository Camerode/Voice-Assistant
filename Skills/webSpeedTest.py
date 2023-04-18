from Skills.Acore import speak, record_action
from speedtest import Speedtest

# Speed test
def run_speed_test():
    try:
        speak(f"Running speed test, this can take up to a minute")
        # Create a Speedtest object
        st = Speedtest()
        # Get the download and upload speeds
        download_speed = st.download() / 1_000_000
        upload_speed = st.upload() / 1_000_000
        # Print the results
        print(f"Download speed: {download_speed:.2f} Mbps")
        print(f"Upload speed: {upload_speed:.2f} Mbps")
        speak(f"Download speed: {download_speed:.2f} Mbps")
        speak(f"Upload speed: {upload_speed:.2f} Mbps")
        record_action(f"Speed test - Download speed: {download_speed:.2f} Mbps")
        record_action(f"Speed test - Upload speed: {upload_speed:.2f} Mbps")
    except Exception as e:
        print("An error has occurred in the webSpeedTest command, output has been sent to errors.log")
        speak("An error has occurred in the webSpeedTest command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write(str(e) + "\n")