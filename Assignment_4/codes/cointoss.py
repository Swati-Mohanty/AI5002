import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

#Simlen
simlen=1000

#Number of toss
n =  3

#Probability of getting H/T
p = 0.5
k=1

#Simulating the probability using  the bernoulli random variable
data_bern_mat = bernoulli.rvs(p,size=(n,simlen))
data_binom=np.sum(data_bern_mat, axis=0)
#print(data_bern_mat)
#print(data_binom)

probs_100 = [np.equal(data_binom,i).mean() for i in range(n+1)]
print(probs_100)
plt.xticks(range(n+1))
plt.plot(list(range(n+1)), probs_100, color='blue', marker='o')
plt.xlabel('Number of Heads',fontsize=14)
plt.ylabel('Probability',fontsize=14)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.grid()
