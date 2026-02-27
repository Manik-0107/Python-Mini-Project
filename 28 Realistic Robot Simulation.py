import pybullet as p
import pybullet_data
import time


class RobotSimulation:
    def __init__(self):
        # Connect to physics server
        self.client = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)

        # Load environment
        self.plane_id = p.loadURDF("plane.urdf")

        # Add multiple robots
        self.robots = []
        positions = [[0, 0, 0.5], [2, 0, 0.5], [0, 2, 0.5]]
        colors = [[1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]]

        for i, pos in enumerate(positions):
            robot_id = p.loadURDF("r2d2.urdf", pos, [0, 0, 0, 1])
            self.robots.append({
                'id': robot_id,
                'color': colors[i],
                'position': pos
            })

        # Add GUI controls
        self.add_gui_controls()

        # Camera setup
        p.resetDebugVisualizerCamera(cameraDistance=5, cameraYaw=50, cameraPitch=-35, cameraTargetPosition=[1, 1, 0.5])

    def add_gui_controls(self):
        """Add GUI sliders and buttons"""
        # Sliders for controlling robot 0
        self.x_slider = p.addUserDebugParameter("Robot 0 - X Force", -500, 500, 0)
        self.y_slider = p.addUserDebugParameter("Robot 0 - Y Force", -500, 500, 0)
        self.z_slider = p.addUserDebugParameter("Robot 0 - Z Force", -500, 500, 0)

        # Buttons
        self.reset_btn = p.addUserDebugParameter("Reset All", 1, 0, 0)
        self.pause_btn = p.addUserDebugParameter("Pause", 1, 0, 0)

        # Text parameters
        self.info_text = p.addUserDebugParameter("Info", 1, 0, 0)

    def apply_force_to_robot(self, robot_idx, force):
        """Apply force to specific robot"""
        p.applyExternalForce(self.robots[robot_idx]['id'], -1, force, [0, 0, 0], p.LINK_FRAME)

    def reset_simulation(self):
        """Reset all robots to initial positions"""
        initial_positions = [[0, 0, 0.5], [2, 0, 0.5], [0, 2, 0.5]]
        for i, robot in enumerate(self.robots):
            p.resetBasePositionAndOrientation(robot['id'], initial_positions[i], [0, 0, 0, 1])
            p.resetBaseVelocity(robot['id'], [0, 0, 0], [0, 0, 0])

    def run(self):
        """Main simulation loop"""
        paused = False
        step_count = 0

        print("Simulation running. Use GUI sliders to control Robot 0.")
        print("Press Ctrl+C to exit")

        try:
            while True:
                if not paused:
                    # Read GUI controls
                    x_force = p.readUserDebugParameter(self.x_slider)
                    y_force = p.readUserDebugParameter(self.y_slider)
                    z_force = p.readUserDebugParameter(self.z_slider)

                    # Check reset button
                    if p.readUserDebugParameter(self.reset_btn) > 0.5:
                        self.reset_simulation()
                        # Reset the button
                        p.removeUserDebugParameter(self.reset_btn)
                        self.reset_btn = p.addUserDebugParameter("Reset All", 1, 0, 0)

                    # Check pause button
                    if p.readUserDebugParameter(self.pause_btn) > 0.5:
                        paused = True
                        print("Simulation paused")
                        # Reset the button
                        p.removeUserDebugParameter(self.pause_btn)
                        self.pause_btn = p.addUserDebugParameter("Pause", 1, 0, 0)

                    # Apply forces to robot 0
                    if abs(x_force) > 0 or abs(y_force) > 0 or abs(z_force) > 0:
                        self.apply_force_to_robot(0, [x_force, y_force, z_force])

                    # Get and display robot positions
                    if step_count % 240 == 0:  # Update every second
                        for i, robot in enumerate(self.robots):
                            pos, _ = p.getBasePositionAndOrientation(robot['id'])
                            print(f"Robot {i} position: ({pos[0]:.2f}, {pos[1]:.2f}, {pos[2]:.2f})")

                    p.stepSimulation()
                    step_count += 1

                time.sleep(1 / 240)

        except KeyboardInterrupt:
            print("\nSimulation stopped by user")
        finally:
            p.disconnect()


# Run the simulation
if __name__ == "__main__":
    sim = RobotSimulation()
    sim.run()
