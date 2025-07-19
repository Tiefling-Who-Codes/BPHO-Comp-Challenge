import matplotlib.pyplot as plt
import numpy as np


#Initialise Values
Frequency_Thz = np.arange(405, 740, 5)
Frequency_Thz = np.array(Frequency_Thz)
refractive_index_n = []
rgb = []


for f in Frequency_Thz:
    n = np.sqrt( 1 + np.sqrt(1 / (1.731 - (2.61 * (10 ** -7) * (f ** 2) ) ) )) # rearanged equation to solve n given value f in THz
    n = float(n)
    refractive_index_n.append(n)

#Provided code for sorting frequencies into RGB colour scheme. Adapted for Python
    if f < 405:
        R, G, B = float('nan'), float('nan'), float('nan')
        colour_str = 'Infra Red'
    elif 405 <= f < 480:
        R, G, B = 1.0, 0.0, 0.0
        colour_str = 'Red'
    elif 480 <= f < 510:
        R, G, B = 1.0, 127/255, 0.0
        colour_str = 'Orange'
    elif 510 <= f < 530:
        R, G, B = 1.0, 1.0, 0.0
        colour_str = 'Yellow'
    elif 530 <= f < 600:
        R, G, B = 0.0, 1.0, 0.0
        colour_str = 'Green'
    elif 600 <= f < 620:
        R, G, B = 0.0, 1.0, 1.0
        colour_str = 'Cyan'
    elif 620 <= f < 680:
        R, G, B = 0.0, 0.0, 1.0
        colour_str = 'Blue'
    elif 680 <= f <= 790:
        R, G, B = 127/255, 0.0, 1.0
        colour_str = 'Violet'
    else:  # f > 790
        R, G, B = float('nan'), float('nan'), float('nan')
        colour_str = 'Ultra Violet'
    
    #Converts the R G and B variable into an rgb array
    argb = [R,G,B]
    #Adds array to tupple: rgb
    rgb.append(argb)

    

# Create the plot
plt.figure(figsize=(10, 6))
plt.scatter(Frequency_Thz, refractive_index_n, c=rgb, s=100)

# Add labels and title
plt.title("Refractive Index (n) vs Frequency / THz", fontsize=14)
plt.xlabel("Frequency / THz", fontsize=12)
plt.ylabel("Refractive Index (n)", fontsize=12)

# Add grid and adjust layout
plt.grid(True, linestyle='--', alpha=0.70)
plt.tight_layout()


#Save File
plt.savefig("Graphs/Refractive Index (n) vs Frequency(THz).png")

# Show the plot
plt.show()