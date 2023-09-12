import random
import numpy as np

def theoretical_probability(n, p):
    return (p - 1) / (n - 1)

def simulate_probability(n, p, num_simulations=10000):
    selected_numbers = np.random.choice(np.arange(1, n + 1), size=(num_simulations, 2))
    s_values, r_values = selected_numbers[:, 0], selected_numbers[:, 1]
    
    favorable_outcomes = np.sum((r_values <= p) & (s_values <= p))
    favorable_outcomes2 = np.sum(s_values <= p)
    
    A = favorable_outcomes / num_simulations
    B = favorable_outcomes2 / num_simulations
    
    return (A / B)

n = 100  # Change n to any desired value
p = 50   # Change p to any desired value

theoretical_prob = theoretical_probability(n, p)
simulated_prob = simulate_probability(n, p, num_simulations=10000)

print(f"Theoretical Probability: {theoretical_prob:.4f}")
print(f"Simulated Probability: {simulated_prob:.4f}")

