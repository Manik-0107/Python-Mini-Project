#install - pip install pybullet

import pybullet as p
import pybullet_data
import time
import random

# Connect to pybullet
physicsClient = p.connect(p.GUI)

# Setup environment
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)

# Load Plane
plane = p.loadURDF("plane.urdf")

# Camera
p.resetDebugVisualizerCamera(
    cameraDistance=8,
    cameraYaw=45,
    cameraPitch=-35,
    cameraTargetPosition=[0,0,0]
)

# Create ball
ball = p.loadURDF("sphere2.urdf", [0, 0, 4])
p.changeVisualShape(ball, -1, rgbaColor=[1, 0, 0, 1])

# Create obstacle boxes
for i in range(6):
    x = random.uniform(-3, 3)
    y = random.uniform(-3, 3)
    z = 0.5

    box = p.loadURDF("cube.urdf", [x, y, z])
    p.changeVisualShape(box, -1, rgbaColor=[random.random(), random.random(), random.random(), 1])

# Simulation Loop
while True:
    if not p.isConnected():
        break

    force = [random.uniform(-10, 10), random.uniform(-10, 10), 0]
    p.applyExternalForce(ball, -1, force,[0, 0, 0], p.WORLD_FRAME)
    p.stepSimulation()
    time.sleep(1./240.)

# Safe Disconnect
if p.isConnected():
    p.disconnect()
