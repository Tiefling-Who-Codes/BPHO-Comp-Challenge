import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize_scalar

# Symbol bank
# Theta: θ
# Subscript 1 : ₁
# Subscript 1 : ₂

############################### Initialise Values and Constants #########################################
c = 3.00e8  # speed of light in a vaccum in m/s
L = 1.0       # Distance between Points A and B in meters
y1 = 1.0      # perpendicular distance from the reflection surface to point A in meters
y2 = 1.0      # perpendicular distance from the reflection surface to point B in meters
n1 = 1.5      # Refractive Index for medium 1; In this case glass
n2 = 1.333    # Refractive Index for medium 2; In this case water

# Speed of light in different mediums
c1 = c/n1     # Speed of light in medium 1
c2 = c/n2     # Speed of light in medium 2

##########################################################################################################


########## Equation for travel time given input x (coordinate of refraction on x axis) #####################

def travel_time(x):
    #Give equation for travel time:
    d1 = np.sqrt( (x**2) + (y1**2) )
    d2 = np.sqrt( ( (L - x)**2 ) + (y2**2) )
    t_seconds = ( (d1)  /  (c1) ) + ( (d2) / (c2) )

    # Convert to nanoseconds (1 second = 1e9 nanoseconds)
    return t_seconds * 1e9

##########################################################################################################


############################## Generate values for x and t ##############################################
x_values = np.linspace(0, L, 500) #Creates 500 intervals between 0 and L
t_values = travel_time(x_values)  # Calculates travel time for each position

#########################################################################################################


########################### Find point where travel time is the least ###################################
result = minimize_scalar(
    travel_time,      # Function to minimize
    bounds=(0, L),    # Search between x=0 and x=L
    method='bounded'  # Use bounded optimization method
)
# Extract results
x_min = result.x      # x-position of minimum time
t_min = travel_time(x_min)  # Minimum travel time

#########################################################################################################


#################### Calculate angles at minimum point & hence verifying Snell's Law #######################################

# Calculate angle of Incidence:
θ1 = np.degrees(np.arctan(x_min/y1))

# Calculate angle of Refraction
θ2 = np.degrees(np.arctan( (L - x_min) / (y2) ))

# Convert angles to radians for trigonometric functions
θ1_rad = np.radians(θ1)
θ2_rad = np.radians(θ2)

# Calculate both sides of Snell's Law equation: n1*sinθ1 = n2*sinθ2
n1_sin_θ1 = n1 * np.sin(θ1_rad)
n2_sin_θ2 = n2 * np.sin(θ2_rad)

# Create text showing Snell's Law verification 
textstr = '\n'.join((
    r'n₁sinθ₁ = n₂sinθ₂',  # Snell's Law equation
    r'$%.2f \times \sin(%.1f^\circ) = %.4f$' % (n1, θ1, n1_sin_θ1), # Refractive index of medium 1 * sinθ₁
    r'$%.2f \times \sin(%.1f^\circ) = %.4f$' % (n2, θ2, n2_sin_θ2), # Refractive index of medium 2 * sinθ₂
    
))

##########################################################################################################


######################################### Create the plot ################################################
plt.figure(figsize=(10, 6))
plt.plot(x_values, t_values, marker='', linestyle='-', color='b', linewidth=2) # Plot graph x vs t
plt.plot(x_min, t_min, marker= 'o', color='r') # plots point of least travel time

# Add labels and title
plt.title("Snell's Law demonstration using Fermat's Principle of least time:", fontsize=14)
plt.xlabel("Point of refraction on X axis, x /m", fontsize=12)
plt.ylabel(" Travel time, t /ns", fontsize=12)

# Add vertical line at minimum position
plt.axvline(
    x_min,                      # x-position of minimum
    color='r',                  # Red color
    linestyle='--',             # Dashed line
    alpha=0.5                   # Semi-transparent
)

# Add a text box proving Snells Law
plt.text(
    0.05, 0.95,                # x,y position (5% from left, 95% from bottom)
    textstr,                    # Text content
    transform=plt.gca().transAxes,  # Use axis coordinates
    verticalalignment='top',    # Align to top
                   # Apply box properties
    fontsize=12                 # Font size
)

# Add grid and adjust layout
plt.grid(True, linestyle='--', alpha=0.70)
plt.tight_layout()

#Save File
plt.savefig("Graphs/Snell's Law of Refraction.png")

# Show the plot
plt.show()

# Print Values
print("\n" + "="*50)
print("Snell's Law Verification:")
print(f"Minimum time at x = {x_min:.3f} m")
print(f"θ1 = {θ1:.1f}°, θ2 = {θ2:.1f}°")
print(f"n1·sinθ1 = {n1_sin_θ1:.6f}")
print(f"n2·sinθ2 = {n2_sin_θ2:.6f}")

###########################################################################################################