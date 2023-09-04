import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Sample size
simlen = 10000

# Possible outcomes
string = "PROBABILITY"

# Generate X1 and X2 without explicit loops
X = np.random.choice(list(string), size=(simlen))

# Find the frequency of each outcome
unique, counts = np.unique(X, return_counts=True)

# Simulated probability
psim = counts / simlen

#Theoretical Probability
string_ = list(string)
sample_space = len(string_)

unique2, counts2 = np.unique(string_, return_counts=True)

prob = list(counts2 / sample_space)
print(unique2)
print(counts2)
probability_dict = dict(zip(unique2, prob))

print(f"Therefore the probability of choosing a vowel is {probability_dict['A'] + probability_dict['I'] + probability_dict['O']}")

# Plotting
plt.stem(unique, psim, markerfmt='o', linefmt='C0-', use_line_collection=True, label='Simulation')
plt.stem(unique2, prob, markerfmt='o', linefmt='C1-', use_line_collection=True, label='Analysis')
plt.xlabel('$k$')  # Use 'k' instead of 'n'
plt.ylabel('$p_{X}(k)$')  # Use 'k' instead of 'n'
plt.legend()
plt.grid()

# Save or display the plot
plt.savefig('/home/karthikeya/Desktop/Probability/New_assignment4/figs/figure1.png')
plt.show()

