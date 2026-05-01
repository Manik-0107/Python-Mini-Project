# pip install psutil

import psutil
import matplotlib.pyplot as plt
import time

plt.ion()   # interactive mode

fig, ax = plt.subplots(figsize=(6, 3))

while True:
    battery = psutil.sensors_battery()
    level = battery.percent
    charging = battery.power_plugged

    ax.clear()

    # Color based on level
    if level > 60:
        color = "green"
    elif level > 30:
        color = "orange"
    else:
        color = "red"

    ax.barh(["Battery"], [100], color="lightgray")
    ax.barh(["Battery"], [level], color=color)

    ax.set_xlim(0, 100)
    status = "Charging ⚡" if charging else "Not Charging 🔋"

    ax.set_title(f"Battery: {level}% | {status}", fontsize=14)
    ax.axis("off")

    plt.pause(1)
