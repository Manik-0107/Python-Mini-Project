import ctypes, os, random

folder = input("Enter the folder path: ")
files = [f for f in os.listdir(folder) if f.endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp"))]

wall = random.choice(files)
path = os.path.abspath(folder + "/" + wall)

ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
print(f"Wallpaper changed to: {wall}")
