import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# SETUP
fig, ax = plt.subplots(figsize=(7,7))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Background STARS
stars_x = list(np.random.rand(300))
stars_y = list(np.random.rand(300))
stars = ax.scatter(stars_x, stars_y, s=5, color="white")

# Galaxy Black Hole Swirl
num_galaxy = 500
theta = np.linspace(0, 6*np.pi, num_galaxy)
r = np.linspace(0.01, 0.45, num_galaxy)
galaxy = ax.scatter([], [], s=2, color='white', alpha=0.6)

# SUN
sun = plt.Circle((0.5, 0.5), 0.05, color='yellow')
ax.add_patch(sun)

# Planets (Multiple)
planets = [
    {"radius" : 0.12, "speed":1.5, "size":5, "color":"cyan"},
    {"radius" : 0.18, "speed":1.2, "size":6, "color":"orange"},
    {"radius" : 0.25, "speed":0.9, "size":7, "color":"lime"},
    {"radius" : 0.32, "speed":0.7, "size":4, "color":"red"}
]

planet_objs = []
for p in planets:
    obj, = ax.plot([], [], 'o', color=p["color"], markersize=p["size"])
    planet_objs.append(obj)

#Shooting Star
shoot_x, shoot_y = [], []
shoot, = ax.plot([], [], color="white", lw=2)

# Controls
zoom = 1.0
speed = 1.0

def on_key(event):
    global zoom, speed
    if event.key == "up":
        zoom *= 0.9
    elif event.key == "down":
        zoom *= 1.1
    elif event.key == "right":
        speed *= 1.2
    elif event.key == "left":
        speed *= 0.8
fig.canvas.mpl_connect("key_press_event", on_key)

# Mouse Click  --> Add STAR
def on_click(event):
    if event.xdata is not None and event.ydata is not None:
        stars_x.append(event.xdata)
        stars_y.append(event.ydata)
        stars.set_offsets(np.c_[stars_x, stars_y])
fig.canvas.mpl_connect('button_press_event', on_click)

# Animation
angle = 0
def update(frame):
    global angle
    angle += 0.05 * speed

    # Black Hole Swirl Effect
    swirl_theta = theta + angle * (1 / (r + 0.1))
    x = 0.5 + r * np.cos(swirl_theta)
    y = 0.5 + r * np.sin(swirl_theta)
    galaxy.set_offsets(np.c_[x, y])

    # Planets Orbit
    for i, p in enumerate(planets):
        px = 0.5 + p["radius"] * np.cos(angle * p["speed"])
        py = 0.5 + p["radius"] * np.sin(angle * p["speed"])
        planet_objs[i].set_data([px], [py])

    # Shooting STAR
    if frame % 60 == 0:
        shoot_x.clear()
        shoot_y.clear()

    if len(shoot_x) < 15:
        shoot_x.append(0.1 + len(shoot_x)*0.03)
        shoot_y.append(0.9 - len(shoot_y)*0.03)

    shoot.set_data(shoot_x, shoot_y)

    # Zoom Control
    ax.set_xlim(0.5 - 0.5 * zoom, 0.5 + 0.5 * zoom)
    ax.set_ylim(0.5 - 0.5 * zoom, 0.5 + 0.5 * zoom)

    return galaxy, shoot, *planet_objs, stars

# AXIS
ax.axis("off")
ani = FuncAnimation(fig, update, frames=500, interval=40)

plt.show()
