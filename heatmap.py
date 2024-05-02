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

# Remove any rows where all values are zero
data = data[~np.all(data == 0, axis=1)]

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

# Ask user if they want to set custom contour levels
custom_levels = input('Do you want to set custom contour levels? (y/n): ')
if custom_levels.lower() == 'y':
    start_level = float(input('Enter the start level for contours (i.e. 0): '))
    stop_level = float(input('Enter the stop level for contours (i.e. 5): '))
    step_level = float(input('Enter the step level for contours (i.e. 0.1): '))
    fine_levels = np.arange(start_level, stop_level, step_level)
else:
    # Define default fine levels for contour plot
    fine_levels = np.arange(0, 5, 0.1)  # fine levels at 0.1 intervals

# Plotting the contour map
fig, ax = plt.subplots()
contour_plot = plt.contourf(xi, yi, zi, levels=fine_levels, cmap=plt.cm.jet, extend='both')

# Generate the color bar based on the filled contour plot
color_bar = plt.colorbar(contour_plot)  # Show color scale with specified ticks

# Set the background color of the plot to match the highest color in the colormap
ax.set_facecolor(plt.cm.jet(1.0))  # jet(1.0) retrieves the last color in the jet colormap

# Ask user if they want to set custom axis limits
customLimits = input('Do you want to set custom axis ranges? (y/n): ')
if customLimits.lower() == 'y':
    xmin = float(input('Enter minimum x-axis limit: '))
    xmax = float(input('Enter maximum x-axis limit: '))
    ymin = float(input('Enter minimum y-axis limit: '))
    ymax = float(input('Enter maximum y-axis limit: '))
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
else:
    # Automatically setting default limits to fit the range of the data
    ax.set_xlim(x.min(), x.max())
    ax.set_ylim(y.min(), y.max())


# Ask user if they want to customize axis titles
customize_titles = input('Do you want to customize titles? (y/n): ')
if customize_titles.lower() == 'y':
    graph_title = input('Enter custom graph title:')
    x_title = input('Enter custom x-axis title: ')
    y_title = input('Enter custom y-axis title: ')
else:
    graph_title = 'Graph Title'
    x_title = 'Log(K$_A$) (µM)'
    y_title = 'ΔH (kcal/mol)'

plt.xlabel(x_title)
plt.ylabel(y_title)
plt.title(graph_title)
plt.show()
