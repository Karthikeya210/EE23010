import numpy as np
import matplotlib.pyplot as plt
import math  # Import the math module

# Sample size
simlen = 10000
# Possible outcomes
n = np.arange(0, 7)

# Generate X1 and X2 without explicit loops
y = np.random.randint(0, 2, size=(6, simlen))

# Calculate X without loops
X = np.sum(y, axis=0)
# Find the frequency of each outcome
unique, counts = np.unique(X, return_counts=True)
# Simulated probability
psim = counts / simlen

# Theoretical probability
p = 0.5
k_values = np.arange(0, 7)

#Instead of for/while loops we use vectorize to create list combinations..
def calculate_combinations(k):
    return math.factorial(6) // (math.factorial(k) * math.factorial(6 - k)) * (p ** k) * ((1 - p) ** (6 - k))

vectorized_combinations = np.vectorize(calculate_combinations)

combinations = vectorized_combinations(k_values)

# Now find the max and its index to find the most likely outcome
most_likely_outcome = np.argmax(combinations)

print(f"Therefore the most likely outcome is for X = {most_likely_outcome}")

# Plotting
plt.stem(n, psim, markerfmt='o', linefmt='C0-', use_line_collection=True, label='Simulation')
plt.stem(n, combinations, markerfmt='o', linefmt='C1-', use_line_collection=True, label='Analysis')
plt.xlabel('$n$')
plt.ylabel('$p_{X}(n)$')
plt.legend()
plt.grid()

# Save or display the plot
plt.savefig('/home/karthikeya/Desktop/Probability/New_assignment1/figs/figure1.png')
plt.show()

