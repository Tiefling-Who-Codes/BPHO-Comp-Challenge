import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Load the image
image = input('Image Path: ')
img = Image.open(image)
img_array = np.array(img) # creates a pixel array from an image

obj_extent = [-8, -2, 2, 4]
vir_obj_extent = [-1 * obj_extent[0], -1 * obj_extent[1], obj_extent[2], obj_extent[3]]

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