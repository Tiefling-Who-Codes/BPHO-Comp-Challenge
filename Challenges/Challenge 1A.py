import matplotlib.pyplot as plt
import numpy as np


#Sellmier Coefficients
a = [1.03961212, 0.231792344, 1.01146945]
b = [0.00600069867, 0.0200179144, 103.560653]

#Intialise Values
# wavelength_nm = np.array([400, 500, 600, 700, 800]) 
wavelength_nm = np.arange(400, 801, 1) # finds all interger values between 400 and 801
wavelenth_μm = []
refractive_index_n = []

#convert wavelength_nm to wavelenth_μm

for i in wavelength_nm:
    x = i/1000
    wavelenth_μm.append(x)

#print(wavelenth_μm)

# solve for n

for i in wavelenth_μm:
    t1 = a[0] * i**2 / (i**2 - b[0]) 
    t2 = a[1] * i**2 / (i**2 - b[1]) 
    t3 = a[2] * i**2 / (i**2 - b[2]) 
    x = t1 + t2 + t3
    n = np.sqrt(1+x)
    print(n)
    refractive_index_n.append(n)

#print(refractive_index_n)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(wavelength_nm, refractive_index_n, marker='', linestyle='-', color='b', linewidth=2)

# Add labels and title
plt.title("Refractive Index (n) vs. Wavelength (λ)", fontsize=14)
plt.xlabel("Wavelength (λ) in nm", fontsize=12)
plt.ylabel("Refractive Index (n)", fontsize=12)

# Add grid and adjust layout
plt.grid(True, linestyle='--', alpha=0.70)
plt.tight_layout()
plt.xlim(400, 800)
plt.ylim(1.51,1.535)


#Save File
plt.savefig("Graphs/Refractive Index of Crown Glass.png")

# Show the plot
plt.show()


