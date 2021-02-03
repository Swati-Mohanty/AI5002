from scipy.stats import bernoulli
import matplotlib.pyplot as plt

#probability of sucess
p=0.7

#Mean
mean=bernoulli.mean(p)
print ("Mean =", mean)

#Variance
var=bernoulli.var(p)
print ("Variance =", var)
