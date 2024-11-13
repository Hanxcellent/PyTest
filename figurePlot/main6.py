import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon, poisson

# Parameters
lambda_rate = 1 / 15  # Rate (lambda) for the Poisson process (arrivals per minute)
simulation_time = 10000  # Total simulation time in minutes
interval_time = 20  # Time interval to check bus counts

# Step 1: Generate interarrival times using the inverse transform method
np.random.seed(42)  # For reproducibility
interarrival_times = -np.log(1 - np.random.rand(int(simulation_time * lambda_rate * 2))) / lambda_rate
arrival_times = np.cumsum(interarrival_times)  # Cumulative sum to get arrival times

# Truncate arrivals that exceed the total simulation time
arrival_times = arrival_times[arrival_times <= simulation_time]

# Step 2a: Plot histogram of interarrival times and theoretical exponential distribution
plt.figure(figsize=(12, 5))

# Histogram of simulated interarrival times
plt.hist(interarrival_times, bins=50, density=True, alpha=0.6, color='skyblue', label='Simulated Interarrival Times')

# Theoretical exponential distribution for comparison
x_vals = np.linspace(0, 100, 200)
plt.plot(x_vals, expon.pdf(x_vals, scale=1/lambda_rate), 'r-', lw=2, label='Theoretical Exponential PDF')

plt.xlabel('Interarrival Time (minutes)')
plt.ylabel('Probability Density')
plt.title('Histogram of Interarrival Times with Theoretical Exponential Distribution')
plt.legend()

# Step 2b: Count buses in 20-minute intervals and plot relative frequency
num_intervals = int(simulation_time / interval_time)
bus_counts = [np.sum((arrival_times >= i * interval_time) & (arrival_times < (i + 1) * interval_time))
              for i in range(num_intervals)]

# Plot histogram of bus counts and theoretical Poisson distribution
plt.figure(figsize=(12, 5))
plt.hist(bus_counts, bins=range(0, max(bus_counts) + 1), density=True, alpha=0.6, color='orange', align='left',
         label='Simulated Bus Counts per 20 Minutes')

# Theoretical Poisson distribution
poisson_mean = lambda_rate * interval_time
poisson_probs = [poisson.pmf(k, poisson_mean) for k in range(max(bus_counts) + 1)]
plt.plot(range(max(bus_counts) + 1), poisson_probs, 'bo-', lw=2, label='Theoretical Poisson PMF')

plt.xlabel('Number of Buses per 20 Minutes')
plt.ylabel('Relative Frequency')
plt.title('Bus Arrivals per 20 Minutes with Theoretical Poisson Distribution')
plt.legend()

plt.show()
