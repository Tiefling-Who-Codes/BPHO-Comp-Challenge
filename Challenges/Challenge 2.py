import matplotlib.pyplot as plt
import numpy as np

# Initialize values
u = np.array(np.arange(20, 60, 5))
v = np.array([65.5, 40, 31, 27, 25, 23.1, 21.5, 20.5])

# Calculate coordinates
x_axis = 1/u  # 1/u values
y_axis = 1/v  # 1/v values

# Calculate line of best fit
slope, intercept = np.polyfit(x_axis, y_axis, 1) # gives us the slope and intercept of the line of best fit
best_fit_line = slope * x_axis + intercept # equation for the line of best fit in the form y = mx + b

# Focal Length (f)
Focal_length = 1/float(intercept)
Focal_length = str(Focal_length)

# Create the plot
plt.figure(figsize=(6, 10)) # updated graph size to help match graph with the one provided in the question
plt.scatter(x_axis, y_axis, color='blue', label='Data Points') 
plt.plot(x_axis, best_fit_line, color='red', label='Line of Best Fit') 

# Add labels and title
plt.suptitle("Thin Lens Graph", fontsize=15)
plt.title("Focal Length: " + Focal_length, fontsize= 12)
plt.xlabel("1/u", fontsize=12)
plt.ylabel("1/v", fontsize=12)
plt.xlim(0,0.06)
plt.ylim(0,0.06)


# Add grid and legend
plt.grid(linestyle='--', alpha=0.70)  # Fixed typo (graduate → grid)
plt.legend()  # Show legend with labels

# Save and show
plt.tight_layout()
plt.savefig("Graphs/Thin Lens Graph.png")
plt.show()