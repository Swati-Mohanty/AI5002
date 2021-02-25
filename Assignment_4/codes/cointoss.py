from scipy.stats import bernoulli
import matplotlib.pyplot as plt
import numpy as np

#Generating random variables 
p=0.5
sample_size = 10000
toss1 = bernoulli.rvs(size=sample_size,p=0.5)
toss2 = bernoulli.rvs(size=sample_size,p=0.5)

#print(toss1)
#print(toss2)
h0=0
h1=0
h2=0

for i in range (sample_size):
  if (toss1[i]!=toss2[i]):
    h1=h1+1
  elif ((toss1[i]==1)&(toss2[i]==1)):
    h2=h2+1
  else:
    h0=h0+1
print('Probability distribution of heads in two tosses of a coin')
print('0 Heads: ',h0/sample_size)
print('1 Head: ',h1/sample_size)
print('2 Heads: ',h2/sample_size)

#3toss
from scipy.stats import bernoulli
import matplotlib.pyplot as plt
import numpy as np

#Generating random variables 
p=0.5
sample_size = 10000
toss1 = bernoulli.rvs(size=sample_size,p=0.5)
toss2 = bernoulli.rvs(size=sample_size,p=0.5)
toss3 = bernoulli.rvs(size=sample_size,p=0.5)

#print(toss1)
#print(toss2)
h0=0
h1=0
h2=0
h3=0
for i in range (sample_size):
  if ((toss1[i]==0)&(toss2[i]==0)&(toss3[i]==0)):
    h0=h0+1
  elif ((toss1[i]==1)&(toss2[i]==1)&(toss3[i]==1)):
    h3=h3+1
  else:
    h1=h1+1
h2=h1/2
print('Probability distribution of tails in three tosses of a coin')
print('0 Tails: ',h0/sample_size)
print('1 Tail: ',h2/sample_size)
print('2 Tails: ',h2/sample_size)
print('3 Tails: ',h3/sample_size)


#4toss
from scipy.stats import bernoulli
import matplotlib.pyplot as plt
import numpy as np

#Generating random variables 
p=0.5
sample_size = 10000
toss1 = bernoulli.rvs(size=sample_size,p=0.5)
toss2 = bernoulli.rvs(size=sample_size,p=0.5)
toss3 = bernoulli.rvs(size=sample_size,p=0.5)
toss4 = bernoulli.rvs(size=sample_size,p=0.5)

#print(toss1)
#print(toss2)
h0=0
h1=0
h2=0
h3=0
h4=0
for i in range (sample_size):
  if ((toss1[i]==0)&(toss2[i]==0)&(toss3[i]==0)&(toss4[i]==0)):
    h0=h0+1
  elif ((toss1[i]==1)&(toss2[i]==1)&(toss3[i]==1)&(toss4[i]==1)):
    h4=h4+1
  elif ((toss1[i]==toss2[i])|(toss1[i]==toss3[i])|(toss1[i]==toss4[i])):
    h2=h2+1
  elif ((toss1[i]==1)|(toss2[i]==1)|(toss3[i]==1)|(toss4[i]==1)):
    h1=h1+1
  else :
    h3+=1
  
h3=h1
print('Probability distribution of heads in four tosses of a coin')
print('0 Heads: ',h0/sample_size)
print('1 Head: ',h1/sample_size)
print('2 Heads: ',h2/sample_size)
print('3 Heads: ',h3/sample_size)
print('4 Heads: ',h4/sample_size)
