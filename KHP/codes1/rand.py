import numpy as np
import matplotlib.pyplot as plt

# Read data from the "uni.dat" file
data = np.genfromtxt("uni.dat")

x = data[:, 0]  # Use correct index for columns (0 for x)
pdf = data[:, 1]  # Use correct index for columns (1 for pdf)
cdf = data[:, 2]

# Create a histogram plot of the PDF
plt.figure()
plt.plot(x, pdf)
plt.xlabel('x (Standard Normal Random Variable)')
plt.ylabel('PDF Value')
plt.title('PDF of Standard Normal Distribution')
plt.savefig('/home/mayank/EE23010/KHP/figs/figure2.png')
plt.show()

plt.figure()
plt.plot(x, cdf)
plt.xlabel('x (Standard Normal Random Variable)')
plt.ylabel('PDF Value')
plt.title('PDF of Standard Normal Distribution')
plt.savefig('/home/mayank/EE23010/KHP/figs/figure3.png')
plt.show()

