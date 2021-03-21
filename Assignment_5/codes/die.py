import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import random

simlen=int(1e6)

w=1/6
l=5/6
exp_amt=0
amt = 0
#Simulations using Bernoulli r.v.
win = bernoulli.rvs(size=simlen,p=w)
loss= bernoulli.rvs(size=simlen,p=l)
prob_win = np.sum(win)/simlen
prob_loss = np.sum(loss)/simlen
#print(prob_loss)

def recur(y):
  if y==6:
    return prob_win*(amt+1)
  else:
    return prob_loss*(amt-1)

for i in range (simlen):
  amt = 0
  for j in range (3):
    y = random.randint(1,6)
    amt = amt+ recur(y)
    #print(amt/(3))
  exp_amt +=amt/(3)
print('Simulated results :')
print (exp_amt/simlen)


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

amnt = (pr1*1)+(pr2*0)-(pr3*1)-(pr4*3)
print(amnt)
