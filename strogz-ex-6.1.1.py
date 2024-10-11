import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# originally written by chatgpt, modified by ato
# prompt was:
# Write me the boilerplate for a python code that will integrate two functions x and y over some time, starting with some initial condition. The code will also plot the results using matplotlib. Different initial conditions in the plot will have different colors, the limits of the plot should be set by variables defined near the beginning.

t_start = 0

plot_xlim = (-2.5, 1.5)
plot_ylim = (-2.5, 2.5)

# The system of differential equations
def system_of_equations(t, z):
    x, y = z
    # Define your functions for dx/dt and dy/dt here
    dxdt = y-y*y*y
    dydt = -x-y*y
    return [dxdt, dydt]

# Initial conditions
IC_dt = [
    [1.1, 0.1,  2],  # First set of initial conditions
    [0.1, 1.1,  3],  # Second set
    [2.1, 2.1,  1],  # Third set, and so on
    [ 2,   4,   5],
    [-0.6, 0.6, 18],
    [-1+0.01, 1-0.01, 10],
]

initial_conditions = [ (x[0], x[1]) for x in IC_dt ]
dt = [ x[2] for x in IC_dt ]

# Create a color map for different initial conditions
colors = plt.cm.viridis(np.linspace(0, 1, len(initial_conditions)))


# Set up the figure and axis
plt.figure(figsize=(8, 6))
plt.title('Integration of x and y over time')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(plot_xlim)
plt.ylim(plot_ylim)

# Solve the system for each set of initial conditions
for i, init_cond in enumerate(initial_conditions):
    t_end = t_start + dt[i]
    # Time points where the solution is computed
    t_eval = np.linspace(t_start, t_end, 500)
    
    sol = solve_ivp(system_of_equations, [t_start, t_end], init_cond, t_eval=t_eval)
    
    # Plot the result
    plt.plot(sol.y[0], sol.y[1], color=colors[i], label=f'IC {i+1}: {init_cond}')

# Add a legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
