# Project Name: Python Screenshot Tool (Save images instantly)
# Install: pip install pyautogui

import pyautogui
import time

# Wait before taking screenshot
time.sleep(2)

# Take screenshot
screenshot = pyautogui.screenshot()

# File name with timestamp
file_name = f"screenshot_{int(time.time())}.png"

# Save screenshot
screenshot.save(file_name)

print(f"Screenshot saved as {file_name}")
