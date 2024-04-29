import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, radians

# Parameters
num_particles = 1
num_steps = 1000
box_size = 10

# Initialize particles' positions
positions = np.random.uniform(0, box_size, size=(num_particles, 2))

# Initialize figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0, box_size])
ax.set_ylim([0, box_size])

# Monte Carlo simulation
for i in range(num_steps):
    angle_of_incidence = radians(30)
    max_deviation = radians(10)
    
    # Propose new positions
    new_positions = positions + np.random.uniform(-0.5, 0.5, size=(num_particles, 2))
    
    # Check if particles are still inside the box
    inside_box = np.all((new_positions >= 0) & (new_positions < box_size), axis=1)
    
    # Reflection check
    for j in range(num_particles):
        if inside_box[j] == False:
            angle_of_reflection = angle_of_incidence + np.random.uniform(-max_deviation, max_deviation)
            while angle_of_reflection < 0 or angle_of_reflection > np.pi/2:
                angle_of_reflection = angle_of_incidence + np.random.uniform(-max_deviation, max_deviation)
                
            # Reflect the particle
            if new_positions[j,0] < 0:
                new_positions[j,0] = abs(new_positions[j,0])
            elif new_positions[j,0] > box_size:
                new_positions[j,0] = 2*box_size - new_positions[j,0]
                
            if new_positions[j,1] < 0:
                new_positions[j,1] = abs(new_positions[j,1])
            elif new_positions[j,1] > box_size:
                new_positions[j,1] = 2*box_size - new_positions[j,1]
            
            # Update position and angle
            positions[j] = new_positions[j]
    
    # Update positions of particles that are still inside the box
    positions[inside_box] = new_positions[inside_box]
    
    # Plot particles
    #ax.clear()
    ax.set_xlim([0, box_size])
    ax.set_ylim([0, box_size])
    ax.scatter(positions[:, 0], positions[:, 1], s=10, c="green")
    plt.pause(0.01)

plt.show()
