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

#Generating random variables 
p=0.7
a=0
r = bernoulli.rvs(p, size=1000)
#print(r)
for i in range(1000):
  if(r[i]==1):
    a+=1
a= a/1000
print(a)
#Mean
mean=bernoulli.mean(a)
print("Generated samples ")
print ("Mean =", mean)

#Variance
var=bernoulli.var(a)
print ("Variance =", var)
