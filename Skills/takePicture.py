from Skills.Acore import speak, record_action
from PIL import Image
import platform
import os
import cv2
from datetime import time

# Take a picture
def take_picture_and_save():
    # Open the default camera
    cap = cv2.VideoCapture(0)
    # Wait for the camera to warm up
    time.sleep(1)
    # Capture an image from the camera
    ret, frame = cap.read()
    # Release the camera resource
    cap.release()
    # Check if the image was captured successfully
    if not ret:
        print("Error: failed to capture image from camera.")
        speak("Error: failed to capture image from camera.")
        return
    # Convert the OpenCV image to a Pillow image
    img = Image.fromarray(frame)
    # Define the path to the downloads folder based on the current platform
    system = platform.system()
    if system == "Windows":
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == "Darwin":
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    elif system == "Linux":
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    else:
        print(f"Warning: unsupported platform {system}.")
        speak(f"Warning: unsupported platform {system}.")
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    # Define the filename with timestamp
    filename = f"picture_{int(time.time())}.jpg"
    # Save the captured image to the downloads folder
    img.save(os.path.join(downloads_path, filename), "JPEG")
    print(f"Picture saved as {filename} in the Downloads folder.")
    speak(f"Picture saved as {filename} in the Downloads folder.")
    record_action('Camera used')