import numpy as np 

# Create 1D array A 
A = np.array([1, 2, 3]) 

# Create 2D column vector B
B = np.array([[23], [25], [29]]) 

# Perform element-wise addition between A and each column of B
result_add = A + B 

# Perform element-wise multiplication between A and B
result_multi = A * B 

# Print arrays with comments explaining their shapes and values
print("Array A (shape 1D):")
print(A)

print("\nArray B (shape 2D column vector):")
print(B)

print("\nResult of BROADCAST ADDITION (A + B):")
print(result_add)

print("\nResult of BROADCAST MULTIPLCATION (A * B):")
print(result_multi)     

#Vectorization 
squared_data = A ** 2
print("\nSquared Array :", squared_data)