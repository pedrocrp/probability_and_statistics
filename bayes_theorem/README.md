# Bayes' Theorem Calculator Project
## Project Description
This project aims to illustrate the practical application of Bayes' theorem, a fundamental concept in probability theory and statistics that describes how to update the probability of a hypothesis based on evidence.

The specific scenario in this project is a medical test for a disease. Given the probability of having the disease (prior), the probability of testing positive, and the probability of testing positive given that a person has the disease, the code calculates the probability of having the disease given a positive test result (posterior).

## Code
The code for this project is written in Python and consists of a single function, bayes_theorem, that implements Bayes' theorem. This function takes three arguments: the prior probability of an event A (having the disease), the probability of an event B (testing positive), and the probability of B given A. It returns the posterior probability of A given B.

The probability values are defined for a hypothetical disease scenario and the bayes_theorem function is used to calculate the posterior probability of having the disease given a positive test result. This value is then printed.

## Requirements
This project requires Python 3.6+ to run and does not depend on any third-party Python libraries.

## Usage
To use this project, follow these steps:

1. Clone the repository.
2. Ensure that you have Python 3.6 or newer installed.
3. Run the Python script.
4. The script will print the calculated probability to the console.

This project serves as a simple demonstration of the use of Bayes' theorem and can be extended or adapted for other purposes, such as part of a statistics or probability course, or as a teaching tool.