import numpy as np
import matplotlib.pyplot as plt

# Define the system of differential equations (x, y are the position and velocity respectively)
def system_of_equations(z):
    x, y = z
    # Define your functions for dx/dt and dy/dt here
    dxdt = -y  # velocity (change in x)
    dydt = x   # acceleration (change in velocity y)
    return np.array([dxdt, dydt])

# Symplectic (Leapfrog) integrator
def leapfrog_step(z, dt):
    x, y = z
    # Half step for velocity (y)
    y_half = y + 0.5 * dt * system_of_equations([x, y])[1]
    
    # Full step for position (x)
    x_new = x + dt * y_half
    
    # Full step for velocity (y) using the updated position
    y_new = y_half + 0.5 * dt * system_of_equations([x_new, y_half])[1]
    
    return np.array([x_new, y_new])

# Define initial conditions and time spans
initial_conditions = [
    {"init_cond": [1, 0], "time_span": (0, 10)},  # First set
    {"init_cond": [0, 1], "time_span": (0, 20)},  # Second set
    {"init_cond": [2, 2], "time_span": (0, 15)},  # Third set
]

# Create a color map for different initial conditions
colors = plt.cm.viridis(np.linspace(0, 1, len(initial_conditions)))

# Set plot limits
plot_xlim = (-5, 5)
plot_ylim = (-5, 5)

# Set up the figure and axis
plt.figure(figsize=(8, 6))
plt.title('Leapfrog Integration of x and y over time')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(plot_xlim)
plt.ylim(plot_ylim)

# Time step for the integrator
dt = 0.01

# Solve the system for each set of initial conditions
for i, condition in enumerate(initial_conditions):
    z = np.array(condition["init_cond"])  # initial condition
    t_start, t_end = condition["time_span"]
    num_steps = int((t_end - t_start) / dt)
    
    # Initialize arrays to store the results
    xs = np.zeros(num_steps)
    ys = np.zeros(num_steps)
    
    # Initial values
    xs[0], ys[0] = z
    
    # Perform the integration using leapfrog
    for step in range(1, num_steps):
        z = leapfrog_step(z, dt)
        xs[step], ys[step] = z
    
    # Plot the result
    plt.plot(xs, ys, color=colors[i], label=f'IC {i+1}: {condition["init_cond"]}')

# Add a legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
