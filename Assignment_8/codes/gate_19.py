import numpy as np
from scipy.stats import bernoulli

sample_size=10000

x_1 = 4/7
x_2 = 3/6

#Simulations of random samples
first_draw = bernoulli.rvs(size= sample_size, p = x_1)
second_draw = bernoulli.rvs(size= sample_size, p = x_2)

#Calculating the number of favourable outcomes

a=(np.sum(first_draw))/sample_size
b=(np.sum(second_draw))/sample_size


#calculating the probability using Conditional probability

c_prob = (x_1 * x_2)/x_1
print ("Probability that the second ball is red:",c_prob)
