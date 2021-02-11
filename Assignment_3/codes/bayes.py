import numpy as np
from scipy.stats import bernoulli

sample_size=1000

prob_A=0.6
prob_B=0.4
prob_D_A= 0.02
prob_D_B = 0.01

#Simulations of random samples
sample_A= bernoulli.rvs(size= sample_size, p = prob_A)
sample_B= bernoulli.rvs(size= sample_size, p = prob_B)
sample_D_A= bernoulli.rvs(size= sample_size, p = prob_D_A)
sample_D_B= bernoulli.rvs(size= sample_size, p = prob_D_B)

#Calculating the number of favourable outcomes

a=(np.sum(sample_A))/1000
b=(np.sum(sample_B))/1000
d_a=(np.sum(sample_D_A))/1000
d_b=(np.sum(sample_D_B))/1000

#calculating the probability using Bayes Theorem

val = ((b*d_b)/((b*d_b)+(a*d_a)))
print ("Probability that the defected item was produced by machine B",val)
