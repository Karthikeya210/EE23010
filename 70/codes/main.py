import numpy as np
from scipy.optimize import fsolve

# Define the values of X and their corresponding probabilities
# You should define A before using it in X_values
# You can change this value to your desired initial guess

X_values = np.array([1, 2, 4, 0,0,0])
P_X = np.array([1/2, 1/5, 3/25, 1/10, 1/25, 1/25])

# Define a function that represents E(X) 
def equation_to_solve(A):
    X_values[3] = 2 * A
    X_values[4] = 3 * A
    X_values[5] = 5 * A
    # Calculate E(X)
    E_X = np.sum(X_values * P_X)
    return E_X - 2.94


# Use fsolve to find the value of A that satisfies the equation E(X) - 2.94 = 0
A = fsolve(equation_to_solve, 1.0)[0]

# Calculate E(X^2) using the correct value of A
E_X_squared = np.sum((X_values ** 2) * P_X)

# Calculate the variance Var(X)
Var_X = E_X_squared - (2.94 ** 2)

print("Value of A:", A)
print("Variance of X:", Var_X)
