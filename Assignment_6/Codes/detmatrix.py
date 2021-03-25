import numpy as np
import random
import matplotlib.pyplot as plt 
from scipy.stats import bernoulli

sample_size = 10000
c=0

#Bernoulli simulation
x1 = bernoulli.rvs(size=sample_size,p=0.5)
x2 = bernoulli.rvs(size=sample_size,p=0.5)
x3 = bernoulli.rvs(size=sample_size,p=0.5)
x4 = bernoulli.rvs(size=sample_size,p=0.5)

for i in range(sample_size):
  a = np.array([[x1[i],x2[i]], [x3[i],x4[i]]]) 
  #print(np.linalg.det(a))
  if(np.linalg.det(a)>0):
    c+=1
print('Probability of determinant being positive: ',c/sample_size)
