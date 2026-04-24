import pyvista as pv
import numpy as np
import time

# Generate spiral point clod
n = 3000
theta = np.random.rand(n) * 4 * np.pi
r = theta * 0.2

x = r * np.cos(theta)
y = r * np.sin(theta)
z = np.random.rand(n) * 0.2

points = np.vstack((x, y, z)).T
cloud = pv.PolyData(points)

# Create Plotter
plotter = pv.Plotter()
plotter.set_background("black")

# Add Objects
actor1 = plotter.add_mesh(cloud, color="white", point_size=3)
sphere = pv.Sphere(radius=0.3)
actor2 = plotter.add_mesh(sphere, color="yellow")

# Open GIF for saving animation
plotter.open_gif("spiral_animation.gif")

#  Smooth animation loop
for i in range(360):
    actor1.rotate_z(1)      # rotate point cloud
    actor2.rotate_z(2)      # rotate sphere faster

    # optional pulse effect
    actor1.prop.point_size = 2 + abs(np.sin(i * 0.1)) * 3

    plotter.render()
    plotter.write_frame()
    time.sleep(0.01)        # Control Speed

# close animation
plotter.close()
