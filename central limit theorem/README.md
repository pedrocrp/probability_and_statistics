# Central Limit Theorem Simulation Project
## Project Description
This project aims to provide a practical demonstration of the Central Limit Theorem (CLT) through a simulation. The Central Limit Theorem is a fundamental statistical theory that states that the distribution of the sum (or average) of a large number of independent, identically distributed variables tends towards a normal distribution, regardless of the shape of the original distribution.

Our simulation generates a large population following an exponential distribution. We then draw multiple samples of a fixed size from this population and calculate their means. According to the CLT, the distribution of these sample means should approximate a normal distribution.

## Code
The code for this project is written in Python and uses the NumPy, Matplotlib, and seaborn libraries. NumPy is used for random number generation and numerical computations, Matplotlib for basic plotting, and seaborn for advanced plotting and creating a kernel density estimate.

The function central_limit_theorem demonstrates the Central Limit Theorem as follows:

1. It generates a population from an exponential distribution using np.random.exponential().
2. Draws a fixed number (num_samples) of samples, each of a fixed size (sample_size), from this population and calculates their means.
3. Uses seaborn's histplot() function to create a histogram of the sample means, along with a kernel density estimate.
4. The plot is titled 'Sample Means' and saved as 'distribution_graph' in the current directory.

The function is then called with a population size of 100,000, sample size of 40, and 10,000 samples to be drawn.

## Requirements
The following Python packages are required to run this project:

- NumPy
- Matplotlib
- seaborn
These packages can be installed using Python's pip package manager:

```
pip install -r requirements.txt
```

## Usage
To use this project, follow these steps:

1. Clone the repository.
2. Ensure that the NumPy, Matplotlib, and seaborn packages are installed.
3. Run the Python script. This will generate an image of the resulting histogram.
4. Open the image of the histogram to view the Central Limit Theorem visualization.

This project serves as a simple demonstration of the Central Limit Theorem and can be extended or adapted for other purposes, such as part of a statistics or probability course, or as a teaching tool.













