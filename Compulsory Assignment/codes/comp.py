import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n1= 17
n2= 9
n_dash= n1+n2
p1= 0.5
p2=0.6
sample_size = 1000

x_a = np.random.binomial(n=n1, p=p1, size=sample_size)
x_b = np.random.binomial(n=n2, p=p2, size=sample_size)
y_dash = np.random.binomial(n= n_dash, p=p, size = sample_size)
#plt.plot(x_a, binom.pmf(x_a,n1,p))
#plt.plot(x_b, binom.pmf(x_b,n2,p))
y = (x_a - x_b)
plt.stem(y, binom.pmf(y,n_dash,p),markerfmt='o', use_line_collection=True,label='Simulated PMF')
plt.stem(y_dash, binom.pmf(y,n_dash,p),markerfmt='o', use_line_collection=True,label='Theoretical PMF')
plt.legend()
#print(y)
