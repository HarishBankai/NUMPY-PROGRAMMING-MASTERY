import numpy as np  

A = np.array([1, 2, 3])
B = np.array([[23], [25], [29]])

result_add = A + B
result_multi = A * B


print("A :\n", A)
print("B :\n", B)
print("BROADCAST ADDITION :\n", result_add)
print("BROADCAST MULTIPLCATION :\n", result_multi)