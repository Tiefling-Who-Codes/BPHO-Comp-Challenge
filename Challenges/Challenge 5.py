import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Load the image
image = input('Image Path: ')
img = Image.open(image)
img_array = np.array(img)

# Define the position for the original image (negative x, positive y)
obj_extent = [-8, -2, 2, 4]  # [left, right, bottom, top]

# Calculate the virtual image extent (reflected across x=0)
virt_extent = [-obj_extent[0], -obj_extent[1], obj_extent[2], obj_extent[3]]

# Create the plot
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_ylim(0, 5)
ax.set_xlim(-10, 10)

# Draw the mirror line at x=0
ax.axvline(x=0, color='red', linestyle='--', linewidth=2, label='Mirror (x=0)')

# Plot the original object in negative-x/positive-y quadrant
ax.imshow(img_array, extent=obj_extent, aspect='auto')

# Plot the virtual image in positive-x/positive-y quadrant (left-right reversed)
ax.imshow(img_array, extent=virt_extent, aspect='auto')

# Add labels, title, and legend
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Reflection by Plane Mirror', fontsize=14)

# Add Grid and adjust layout
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

#Save and Show graph
plt.savefig('Graphs/Reflection in a Plane Mirror.png')
plt.show()