def bayes_theorem(P_A, P_B, P_B_given_A):
    """
    Function to calculate and return the posterior probability of event A given event B, 
    using Bayes' theorem.

    Parameters:
    P_A (float): Prior probability of event A
    P_B (float): Probability of event B
    P_B_given_A (float): Probability of event B given event A

    Returns:
    float: Posterior probability of event A given event B
    """
    # Application of Bayes' theorem
    P_A_given_B = (P_B_given_A * P_A) / P_B
    
    return P_A_given_B

# Probabilities
P_D = 1/1000   # Probability of having the disease (event A)
P_TP = (0.99 * P_D) + (0.02 * (1-P_D)) # Probability of getting a positive test result (event B)
P_TP_given_D = 0.99 # Probability of getting a positive test result if the person has the disease (B given A)

# Calculating the probability of having the disease given a positive test result (A given B)
P_D_given_TP = bayes_theorem(P_D, P_TP, P_TP_given_D)

print(f"The probability of having the disease given a positive test result is {P_D_given_TP*100:.2f}%")
