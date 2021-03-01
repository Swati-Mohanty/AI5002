import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import random
simlen=int(1e6)
sample_size=6

w=1
l=5
prob_w=w/sample_size
prob_l=l/sample_size

#Simulations using Bernoulli r.v.
win = bernoulli.rvs(size=simlen,p=prob_w)
loss= bernoulli.rvs(size=simlen,p=prob_l)

#Event of getting 6 in throws
e1 = win
e2 = loss*win
e3 = loss*loss*win
e4 = loss*loss*loss
#Probability of each event
p1 = (np.sum(e1))/simlen
p2 = (np.sum(e2))/simlen
p3 = (np.sum(e3))/simlen
p4 = (np.sum(e4))/simlen

print('Simulated results')
print(p1)
print(p2)
print(p3)
print(p4)

amount = (p1*1) + (p2*0) - (p3*1) - (p4*3)
print(amount)

#Theoretical
r1=0
r2=0
r3=0
r4=0

for i in range(1000):
  roll1 = random.randint(1,6)
  roll2 = random.randint(1,6)
  roll3 = random.randint(1,6)
  if(roll1==6):
    r1=r1+1
  elif (roll2==6):
    r2+=1
  elif (roll3==6):
    r3+=1
  else:
    r4+=1
  

pr1=r1/1000
pr2=r2/1000
pr3=r3/1000
pr4=r4/1000

print('Theoretical results')
print(pr1)
print(pr2)
print(pr3)
print(pr4)

amnt = (pr1*1)+(pr2*0)-(pr3*1)-(pr4*3)
print(amnt)
