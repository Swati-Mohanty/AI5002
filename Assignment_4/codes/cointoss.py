import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt 
#np.random.seed(42)

n = 4   #no of tosses
p = 0.5
size=100
x=np.random.binomial(n=n, p=p, size=size)
#print (x)

probs_100 = [np.equal(x,i).mean() for i in range(n+1)]
print(probs_100)

plt.xticks(range(n+1))
plt.plot(list(range(n+1)), probs_100, color='blue', marker='o')
plt.xlabel('Number of Heads',fontsize=14)
plt.ylabel('Probability',fontsize=14)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.grid()
