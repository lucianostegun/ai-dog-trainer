# %% [markdown]
# # Installing dependencies

# %%
#!pip3 install opencv-python
#!pip3 install dlib


# %%
import numpy as np
import cv2
import datetime
import time


# %% [markdown]
# # Listing available webcams

# %%
def list_available_cameras():
    # Get the list of available cameras
    camera_list = []

    for index in range(10):  # Try checking up to 10 camera indices (you can adjust this number as needed)
        cap = cv2.VideoCapture(index)
        
        if not cap.read()[0]:
            break
        else:
            # camera_list.append(index)

            # Get camera properties
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)

            camera_list.append({"index": index, "width": width, "height": height, "fps": fps})

        cap.release()

    return camera_list

# Call the function to get the list of available cameras
available_cameras = list_available_cameras()

# Print the list of available cameras
print("Available cameras:", available_cameras)


# %% [markdown]
# ## Configuration

# %%
CAMERA_INDEX = 0
SLEEP_DURATION_IN_SECONDS = 1
OUTPUT_FOLDER = './pictures'

IMAGE_WIDTH = 640
IMAGE_HEIGHT = 480


# %%
cap = cv2.VideoCapture(CAMERA_INDEX)


# %%
if not cap.isOpened():
    print("Cannot open camera")
    exit()


# %%
def save_frame(frame, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate a filename based on the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    filename = os.path.join(output_dir, f"motion_{timestamp}.jpg")

    resized_frame = cv2.resize(frame, (IMAGE_WIDTH, IMAGE_HEIGHT))

    # Save the frame to a JPG file
    cv2.imwrite(filename, resized_frame)
    print(f"Frame saved to {filename}")

# %%
import datetime
import os

# Initialize the video capture object
cap = cv2.VideoCapture(0)  # Use 0 for the default camera, you may need to change it based on your setup

# Parameters for motion detection
min_area = 500  # Minimum area to consider as motion
motion_detected = False

# Set initial time for frame saving
next_save_time = time.time() + 60  # Save the first frame immediately

# Main loop
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to the frame to reduce noise
    blur = cv2.GaussianBlur(gray, (21, 21), 0)

    # Store the initial frame for background subtraction
    if not motion_detected:
        initial_frame = blur
        motion_detected = True
        continue

    # Compute the absolute difference between the current frame and the initial frame
    frame_delta = cv2.absdiff(initial_frame, blur)

    # Threshold the frame delta
    _, thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)

    # Dilate the thresholded image to fill in holes
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check for motion
    motion_detected = False
    for contour in contours:
        if cv2.contourArea(contour) > min_area:
            motion_detected = True
            break

    current_second = datetime.datetime.now().second

    # If motion is detected, log the timestamp
    if motion_detected or current_second == 0:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_frame(gray, f"pictures/{timestamp[:10]}")
        
        if motion_detected:
          print(f"Motion detected at {timestamp}")
          motion_detected = False
          time.sleep(SLEEP_DURATION_IN_SECONDS)

        next_save_time = time.time() + 60

    # Display the frame
    # cv2.imshow("Frame", gray)

    # Check for the 'q' key to quit the program
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()



