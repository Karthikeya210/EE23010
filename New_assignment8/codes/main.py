import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

k_values = np.arange(0,7)

#Probability
p = 1/10 
n = 7    
#We can use binom to create binomial distribution
rv = binom(n, p)

#Make the list combinations with rv.pmf function
combinations = rv.pmf(k_values)

# Calculate the cumulative probabilities (CDF)
cdf = np.cumsum(combinations)

print(f"the probability that a transmitted codeword is decoded correctly is {cdf[1]}")
# Plot the CDF
plt.plot(k_values, cdf, marker='o', linestyle='-')
plt.title('CDF of (7, 4) Hamming Code with ε=0.1')
plt.xlabel('Number of Bit Errors (k)')
plt.ylabel('CDF')
plt.grid(True)
plt.show()







	
