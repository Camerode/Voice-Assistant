from Skills.Acore import speak, record_action
from speedtest import Speedtest

# Speed test
def run_speed_test():
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