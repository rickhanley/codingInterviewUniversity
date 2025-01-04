import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Constants
GRAVITY = .08      # Acceleration due to gravity
INITIAL_VELOCITY_Y = 2  # Initial vertical velocity upwards
DAMPING = .7        # Energy loss on each bounce (damping factor)
GROUND_Y = 0            # The Y position of the ground
LIFETIME = 1000         # Maximum number of frames (animation duration)
REST_THRESHOLD = 0.05   # Threshold for resting (when velocity is small enough)

# Initialize particle data
class Particle:
    def __init__(self):
        self.x = 0   # Initial X position (centered horizontally)
        self.y = 3   # Initial Y position (near the top)
        
        self.vx = 0  # No horizontal movement
        self.vy = INITIAL_VELOCITY_Y  # Initial vertical velocity
        
        self.life = LIFETIME  # Lifetime in frames

    def update(self):
        # Apply gravity to vertical velocity
        self.vy -= GRAVITY
        
        # Update the position of the particle
        self.x += self.vx
        self.y += self.vy
        
        # If the particle hits the ground (Y position reaches 0)
        if self.y <= GROUND_Y:
            self.y = GROUND_Y  # Reset position to the ground
            self.vy = -self.vy * DAMPING  # Reverse and dampen the velocity
            
            # Stop the particle if the velocity is small enough
            if abs(self.vy) < REST_THRESHOLD:
                self.vy = 0
                self.life = 0  # Stop updating after coming to rest

        # Decrease lifetime to eventually stop the animation
        self.life -= 1

# Initialize figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)  # Set x-axis range
ax.set_ylim(0, 6)   # Set y-axis range (ground at y=0)

# Scatter plot for the particle
scat = ax.scatter([], [], s=100, c="blue")

# Create the particle
particle = Particle()

# Animation update function
def update(frame):
    particle.update()  # Update the particle position and velocity
    
    # If the particle is still "alive", update the scatter plot
    if particle.life > 0:
        scat.set_offsets([particle.x, particle.y])
    return scat,

# Create the animation with a reasonable frame rate
ani = FuncAnimation(fig, update, frames=200, interval=30, blit=True)

plt.show()
