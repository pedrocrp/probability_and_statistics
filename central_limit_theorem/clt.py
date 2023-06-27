# Import required libraries: numpy for numerical computations, 
# matplotlib for basic plotting and seaborn for advanced plotting
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def central_limit_theorem(population_size, sample_size, num_samples):
    """
    Demonstrates the Central Limit Theorem.
    
    Args:
    population_size (int): Size of the population to be generated.
    sample_size (int): Size of each sample.
    num_samples (int): Number of samples to be drawn.
    """

    # Generate a population from an exponential distribution
    population = np.random.exponential(scale=1.0, size=population_size)

    # Draw 'num_samples' samples of size 'sample_size' from the population and calculate their means
    means = [np.mean(np.random.choice(population, size=sample_size)) for _ in range(num_samples)]

    # Plot the distribution of sample means
    sns.histplot(means, kde=True)
    
    # Title for the plot
    plt.title('Sample Means')
    
    # Save the plot as 'distribution_graph' in the current directory
    plt.savefig('distribution_graph')


# Use of the function:
central_limit_theorem(100000, 40, 10000)
