# %% [markdown]
# # Installing dependencies

# %%
import numpy as np
import cv2 as cv
import datetime
import time

# %% [markdown]
# # Listing available webcams

# %%
def list_available_cameras():
    # Get the list of available cameras
    camera_list = []

    for index in range(10):  # Try checking up to 10 camera indices (you can adjust this number as needed)
        cap = cv.VideoCapture(index)
        
        if not cap.read()[0]:
            break
        else:
            # camera_list.append(index)

            # Get camera properties
            width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv.CAP_PROP_FPS)

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
SLEEP_DURATION_IN_SECONDS = 5
OUTPUT_FOLDER = './pictures'

# %%
cap = cv.VideoCapture(CAMERA_INDEX)

# %%
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# %%
file_format = 'jpg'

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display the resulting frame cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
    
    # Generate the filename based on the current date and time
    current_datetime = datetime.datetime.now()
    filename = current_datetime.strftime("%Y-%m-%d %H-%M-%S") + '.' + file_format

    # Save the frame as a JPEG file
    filepath = f'{OUTPUT_FOLDER}/{filename}'
    cv.imwrite(filepath, gray)

    time.sleep(SLEEP_DURATION_IN_SECONDS)
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
