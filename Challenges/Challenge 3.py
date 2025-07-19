import matplotlib.pyplot as plt
import numpy as np

# Initialise Values & Constants
c = 3.00e8  # speed of light in m/s
n = 1.5      # refractive index
L = 1.0      # Distance between Point A and B in meters
y = 0.1      # perpendicular distance from the reflection surface to points A and B in meters

# Time scale factor: (n / c) * 1e9 To convert to nanoseconds
time_scale = (n / c) * 1e9

# Define x from 0 to L
x = np.linspace(0, L, 500) # creates 500 intervals between 0 and 500

# Calculate travel time in nanoseconds
f_x = np.sqrt(x**2 + y**2) + np.sqrt((L - x)**2 + y**2) # Given Formula to calculate Travel Time
t_ns = time_scale * f_x  # Converts travel time into nanoseconds

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(x, t_ns, 'b-', linewidth=2, label=r'$t$ (ns)')
plt.axvline(x=L/2, color='r', linestyle='--', label=r'$x = L/2$') #Plots a line at point L/2

# Add labels and title
plt.xlabel(r'x (m)', fontsize=14)
plt.ylabel(r'Travel Time t (ns)', fontsize=14)
plt.title(r'Law of reflection', fontsize=16)

# Add Grid and Legend
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()

#Save File
plt.savefig("Graphs/Law of Reflection.png")

# Show plot
plt.show()