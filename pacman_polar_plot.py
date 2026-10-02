import numpy as np
import matplotlib.pyplot as plt

# Create a polar subplot
ax = plt.subplot(projection='polar')

# Create an array of theta angles
theta = np.linspace(-np.pi, np.pi, 1000)

# Calculate radius r using the formula
r = np.exp(10 * (np.abs(2*theta) - np.abs(np.abs(2*theta) - 1) - 1) / np.abs(2*theta))

# Fill the area under the curve with yellow
ax.fill(theta, r, color='yellow')

# Draw the curve outline in yellow
ax.plot(theta, r, color='yellow')

# Remove radial and angular ticks
ax.set_rticks([])
ax.set_xticks([])

# Set the background to black for both the polar axes and the figure
ax.set_facecolor('black')
plt.gcf().patch.set_facecolor('black')

# Display the plot
plt.show()
