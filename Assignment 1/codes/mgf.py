# Moment  
from scipy import stats 
import matplotlib.pyplot as plt
import numpy as np  
  
arr1 = [[1, 3, 27],  
        [3, 4, 6],  
        [7, 6, 3],  
        [3, 6, 8]]   
arr2 = []
arr2.append(stats.moment(arr1, moment = 0)) 
arr2.append(stats.moment(arr1, moment = 2)) 

print (arr2)
plt.plot(arr2)
print("Oth moment : \n", stats.moment(arr1, moment = 0)) 
  
print("\n6th moment : \n", stats.moment(arr1, moment = 6)) 
  
print("\n9th moment : \n", stats.moment(arr1, moment = 9, axis = None)) 
  
print("\n12th moment : \n", stats.moment(arr1, moment = 12, axis = 1)) 
  
print("\n10th moment : \n", stats.moment(arr1, moment = 10, axis = 1)) 
#1-Dimensional Data:

#Import required libraries:
from scipy import stats

#Dataset:
d = [1,2,3,4,5]

#Finding 0th moment:
print("0th Moment = ",stats.moment(d,moment=0))

#Finding 1st moment:
print("1st Moment = ",stats.moment(d,moment=1))

#Finding 2nd moment:
print("2nd Moment = ",stats.moment(d,moment=2))

#Finding 3nd moment:
print("3nd Moment = ",stats.moment(d,moment=3))

#Finding 4th moment:
print("4th Moment = ",stats.moment(d,moment=4))


#============================================================


#2-Dimensional Data:

#Import required libraries:
from scipy import stats

#Dataset:
d = [[5,6,9,11,3],[21,4,8,15,2]]

#Finding 0th moment:
print("0th Moment = ",stats.moment(d,moment=0))

#Finding 1st moment:
print("1st Moment = ",stats.moment(d,moment=1))

#Finding 2nd moment:
print("2nd Moment = ",stats.moment(d,moment=2))

#Finding 3nd moment:
print("3nd Moment = ",stats.moment(d,moment=3))

#Finding 4th moment:
print("4th Moment = ",stats.moment(d,moment=4))
