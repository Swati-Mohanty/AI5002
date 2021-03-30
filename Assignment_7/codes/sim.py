import numpy as np
import random
import math
import matplotlib.pyplot as plt 
from scipy.stats import bernoulli

sample_space = 1000
max_size = 10 #k 
p_simul = []
p_theoretical =[]
n = np.array([1,2,3,4,5,6,7,8,9,10])

def psim(digit_size) :
  count = 0
  p_sim = 0
  for j in range(sample_space):
    flag = 0
    a = 0
    #generated k-digit number
    for i in range(digit_size):
      k = random.randint(0,9)
      #print (k)
      a = a*10 + k
      #print(a)
      if((k==0)|(k==5)|(k==9)):
        flag = 1
    if(flag==1):
      count+=1
    #print(a)
  return (1-(count/sample_space))


for d in range(max_size):
  digit_size = d+1
  #print(psim (digit_size))
  p_simul = np.append(p_simul,psim(digit_size))
  p_theoretical = np.append(p_theoretical , (0.7**digit_size))

#print(p_simul)
#print(p_theoretical)
#Plotting
plt.stem( n,p_simul, markerfmt='o', use_line_collection=True, label='Simulation')
plt.stem( n,p_theoretical,markerfmt='o', use_line_collection=True, label='Theoretical')
plt.xlabel('$No. of digits$')
plt.ylabel('$P(X)$')
plt.legend()
plt.grid()# minor

  
