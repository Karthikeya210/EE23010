import numpy as np

# Given data
data = np.array([0.13, 0.12, 0.78, 0.51])

# Define the hypothesized cumulative distribution function F0(x)
def F0(x):
    if x < 0:
        return 0
    elif 0 <= x < 1:
        return x
    else:
        return 1

# Sort the data in ascending order
sorted_data = np.sort(data)

# Calculate the EDF (Empirical Distribution Function) values
n = len(sorted_data)
edf_values = np.arange(1, n + 1) / n

# Calculate the absolute differences between EDF and F0
differences = np.abs(edf_values - np.vectorize(F0)(sorted_data))

# Find the maximum absolute difference (Kolmogorov-Smirnov test statistic D)
D = np.max(differences)

# Given significance level and critical value
alpha = 0.01
critical_value = 0.669

# Perform the hypothesis test
psi = 1 if D <= critical_value else 0

# Calculate the observed value of D + ψ
observed_value = D + psi

# Print the results
print("Kolmogorov-Smirnov test statistic D:", D)
print("ψ:", psi)
print("Observed value of D + ψ:", observed_value)

