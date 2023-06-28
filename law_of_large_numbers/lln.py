import numpy as np
import matplotlib.pyplot as plt

def LLN(interactions = 1000, fair=True):
    """
    Demonstrates the Law of Large Numbers by simulating coin tosses.

    Args:
    interactions (int): Number of games or iterations to simulate.
    fair (bool): Indicate whether the coin is fair or not.
    """

    np.random.seed(42)
    n_trials = 10
    
    if fair:
        p = [0.5, 0.5]
        expected_value = 0.5
    else:
        p = [0.3, 0.7]
        expected_value = 0.7

    mean_outcomes_all = []

    for n in range(1, interactions + 1):
        print(n)
        trials = np.random.choice([0, 1], size=(n_trials, n), p=p)
        mean_outcomes = trials.mean(axis=1).mean()
        mean_outcomes_all.append(mean_outcomes)

    plt.figure(figsize=(10, 6))
    plt.plot(list(range(1, interactions + 1)), mean_outcomes_all, 'X', markersize=5)
    plt.xlabel('Number of Experiments', fontsize=13)
    plt.ylabel('Average of Outcomes', fontsize=13)
    plt.title('Average of Outcomes vs Number of Experiments', fontsize=15)
    plt.axhline(expected_value, color='red', linestyle='dashed', linewidth=2, label='Expectation')
    plt.legend()
    plt.savefig('distribution_graph')

LLN(interactions = 100000, fair=True)
