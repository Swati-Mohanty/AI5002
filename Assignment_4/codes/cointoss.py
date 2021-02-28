import numpy as np
import random
import matplotlib.pyplot as plt 
from scipy.stats import bernoulli

sample_size = 10000

#Bernoulli simulation
x1 = bernoulli.rvs(size=sample_size,p=0.5)
x2 = bernoulli.rvs(size=sample_size,p=0.5)
x3 = bernoulli.rvs(size=sample_size,p=0.5)
x4 = bernoulli.rvs(size=sample_size,p=0.5)

y1 = x1+x2
y2 = x1+x2+x3
y3 = x1+x2+x3+x4

#print(y1)
#print(y2)
#print(y3)

#2 toss
prob_y1 = [np.equal(y1,i).mean() for i in range(3)]
print(prob_y1)
#3 toss
prob_y2 = [np.equal(y2,i).mean() for i in range(4)]
print(prob_y2)
#4 toss#
prob_y3 = [np.equal(y3,i).mean() for i in range(5)]
print(prob_y3)

#Binomial simulation
print('Binomial simulation')
y11=np.random.binomial(n=2, p=0.5, size=sample_size)
#print (y11)
prob_y11 = [np.equal(y11,i).mean() for i in range(3)]
print(prob_y11)

y12=np.random.binomial(n=3, p=0.5, size=sample_size)
#print (y12)
prob_y12 = [np.equal(y12,i).mean() for i in range(4)]
print(prob_y12)

y13=np.random.binomial(n=4, p=0.5, size=sample_size)
#print (y13)
prob_y13 = [np.equal(y13,i).mean() for i in range(5)]
print(prob_y13)
