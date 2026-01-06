# Project name: Desktop Screen Recording Tool
# Install: pip install pyautogui

import pyautogui
import cv2
import numpy as np

resolution = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*"mp4v")
filename = "Recording.mp4"
fps = 60.0

out = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 370)

print("Screen Recording Started... Press Q to stop")

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)

    # Convert RGB → BGR (for OpenCV)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    out.write(frame)
    cv2.imshow("Live", frame)

    if cv2.waitKey(1) == ord("q"):
        break

# these must be OUTSIDE the loop
out.release()
cv2.destroyAllWindows()
print("Recording Saved!")
