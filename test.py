import numpy as np

a = np.array([[1,2,3],[4,5,6]])

b = np.repeat(a,2,axis=(0,1))

# c = np.repeat(b,2,axis=0)

print(a)
print(b)
print(c)