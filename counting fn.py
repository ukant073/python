import numpy as np
a= np.arange(9).reshape(3,3)
print(a)
condition = np.mod(a,2)==0
print("element wise value of condition:")
print(condition)
print(np.extract(condition,a))
