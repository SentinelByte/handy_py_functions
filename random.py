import random

# Generating random samples
population = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sample = random.sample(population, k=4)
print(sample)

'''
This code generates a random sample of elements from the population list 
using the random.sample() function from the random module in Python. 
random.sample() function selects a specified number of unique elements from a population without replacement.
The K-<number> defines how many element to randomly select.
'''
