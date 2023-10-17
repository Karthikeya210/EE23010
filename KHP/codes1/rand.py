import numpy as np
import matplotlib.pyplot as plt

# Read data from the "uni.dat" file
data = np.genfromtxt("uni.dat")

x = data[:, 0]  # Use correct index for columns (0 for x)
pdf = data[:, 1]  # Use correct index for columns (1 for pdf)

# Create a histogram plot of the PDF
plt.plot(x, pdf)
plt.xlabel('x (Standard Normal Random Variable)')
plt.ylabel('PDF Value')
plt.title('PDF of Standard Normal Distribution')
plt.savefig('/home/sayyam/KHP/figs/figure2.png')
plt.show()

