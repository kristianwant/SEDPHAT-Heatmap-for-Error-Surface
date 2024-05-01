import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

if len(sys.argv) < 2:
    print("Usage: python runscript.py <filename>")
    sys.exit(1)

filename = sys.argv[1]
data_file = filename
data = np.loadtxt(data_file)

# Extracting x, y, and z columns
x = data[:, 0]
y = data[:, 1]
z = data[:, 2]

# Creating a grid for contour plotting
xi = np.linspace(x.min(), x.max(), 100)
yi = np.linspace(y.min(), y.max(), 100)
xi, yi = np.meshgrid(xi, yi)

# Interpolating z values on the created grid using scipy's griddata
zi = griddata((x, y), z, (xi, yi), method='linear')

# Define fine levels for contour plot and tick levels for color bar
fine_levels = np.arange(0, 3.6, 0.1)  # fine levels at 0.1 intervals
tick_levels = np.arange(0, 3.6, 0.5)  # tick levels at 0.5 intervals

# Plotting the contour map
fig, ax = plt.subplots()
contour_plot = plt.contourf(xi, yi, zi, levels=fine_levels, cmap=plt.cm.jet, extend='both')
#plt.contour(xi, yi, zi, levels=[0.49], colors='black', linewidths=0.5)  # Adding contour line at z = 0.4
color_bar = plt.colorbar(contour_plot, ticks=tick_levels)  # Show color scale with specified ticks

# Set the background color of the plot to match the highest color in the colormap
ax.set_facecolor(plt.cm.jet(1.0))  # jet(1.0) retrieves the last color in the jet colormap

# Setting the limits of the y-axis and x-axis
ax.set_ylim(-18, -14)
ax.set_xlim(5.5, 6.0)

plt.xlabel('Log(K$_A$) (µM)')
plt.ylabel('ΔH (kcal/mol)')
plt.title(u'ISCU into (NIAU)\u2082')
plt.show()
