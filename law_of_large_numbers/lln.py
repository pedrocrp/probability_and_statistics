# Import the required libraries: numpy for numerical computations 
# and matplotlib for basic plotting
import numpy as np
import matplotlib.pyplot as plt

def LLN(interactions = 1000):
    """
    Demonstrates the Law of Large Numbers by simulating coin tosses.

    Args:
    interactions (int): Number of games or iterations to simulate.
    """

    # Setting up the random seed for reproducibility
    np.random.seed(42)
    
    # Number of trials per game
    n_trials = 10
    
    # The expected value for a fair coin toss is 0.5
    expected_value = 0.5

    # List to store the mean outcomes for each game
    mean_outcomes_all = []

    # Simulate the games
    for n in range(1, interactions + 1):
        # Simulate 'n_trials' coin tosses for each game, 
        # where 0 represents "tails" and 1 represents "heads"
        print(n)
        trials = np.random.randint(2, size=(n_trials, n))
        
        # Calculate the mean outcome for each game
        mean_outcomes = trials.mean(axis=1).mean()
        
        # Store the mean outcomes
        mean_outcomes_all.append(mean_outcomes)

    # Create a figure for the plot
    plt.figure(figsize=(10, 6))

    # Plot the mean outcomes for each game
    plt.plot(list(range(1, interactions + 1)), mean_outcomes_all, 'X', markersize=5)

    # Set the labels for the x and y axes and the plot title
    plt.xlabel('Number of Experiments', fontsize=13)
    plt.ylabel('Average of Outcomes', fontsize=13)
    plt.title('Average of Outcomes vs Number of Experiments', fontsize=15)

    # Plot the expected value line
    plt.axhline(expected_value, color='red', linestyle='dashed', linewidth=2, label='Expectation')

    # Add a legend
    plt.legend()

    # Save the plot as 'distribution_graph' in the current directory
    plt.savefig('distribution_graph')

# Use of the function:
# Simulate 100000 games, calculate the average outcome for each game, and plot these averages versus the number of games
LLN(interactions = 100000)
