import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import rayleigh 
from scipy.stats import gengamma

	
x = np.linspace(0, 20, 100)
smr = []

#Rayleigh Distribution	
y1 = rayleigh.pdf(x, 0, 1 )
y2 = rayleigh.pdf(x, 1, 4)

#Generalized gamma Distribution
a, c = 1, 2
rv = gengamma(a, c)
#plt.plot(x, rv.pdf(x))
#plt.plot(gengamma.pdf(x,a,c))
z = gengamma.pdf(x,a,c)

#SMR Distribution
for i in range (0,30):
   smr.append( i/(2* pow((i*i)/2 +1,1.5)))
   #print(t)


print (smr)
#plt.plot(smr)

plt.plot(x, y1, "r", x,z,"b", smr,"g")
plt.legend(["Rayleigh", "Genralized Gamma", "SMR"])
