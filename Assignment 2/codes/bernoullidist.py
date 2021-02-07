from scipy.stats import bernoulli
import matplotlib.pyplot as plt
import numpy as np

#probability of sucess
p=0.7

#Mean
mean=bernoulli.mean(p)
print ("Mean =", mean)

#Variance
var=bernoulli.var(p)
print ("Variance =", var)

#Generating random variables 
p=0.7
r = np.array(bernoulli.rvs(p, size=1000))
a=(np.sum(r))/1000

print(a)
#Mean
mean=bernoulli.mean(a)
print("Generated samples ")
print ("Mean =", mean)

#Variance
var=bernoulli.var(a)
print ("Variance =", var)
