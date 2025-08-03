import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Load the image
image = input('Image Path: ')
img = Image.open(image)
img_array = np.array(img) # creates a pixel array from an image

# defines the range of cordinates for the object and calculates the virtual image coordinates
# The object is placed at x = -8 to -2 and y = 2 to 4 for example
obj_extent = [-8, -2, 2, 4] # Start x, End x, Start y, End y
# The virtual image is a reflection across the y-axis, so we invert the x-coordinates
# The y-coordinates remain the same
vir_obj_extent = [-1 * obj_extent[0], -1 * obj_extent[1], obj_extent[2], obj_extent[3]] # Start x = 8, End x = 2, Start y = 2, End y = 4 
#Start x is 8 and End x is 2, this means the virtual image is a mirror reflection of the object across the y-axis

#create plot
fig, ax = plt.subplots(figsize=(10,8))


# Draw mirror line
ax.axvline(x=0, color='red', linestyle='--', linewidth= '2')

#Show images
ax.imshow(img_array, extent= obj_extent, aspect= 'auto')
ax.imshow(img_array, extent= vir_obj_extent, aspect= 'auto')

# Add labels, title, and legend
ax.set_xlabel('x', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Reflection by Plane Mirror', fontsize=14)

# Add Grid and adjust layout
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.xlim(-10, 10)
plt.ylim(0,5)

#Save and Show graph
plt.savefig('Graphs/Reflection in a Plane Mirror.png')
plt.show() 