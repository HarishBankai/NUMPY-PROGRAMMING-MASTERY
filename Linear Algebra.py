import numpy as np
# Create two 2x2 matrices A and B 
A = np.array([[1, 6],   # Matrix A values
              [9, 12]])
B = np.array([[2, 3],   # Matrix B values
              [8, 5]])

# Calculate matrix multiplication using numpy's dot function
C = np.dot(A, B)
print("MATRIX MULTIPLCATION : \n", C)

# Calculate matrix multiplication using @ operator (which is equivalent to np.dot for matrices)
result_set = A @ B 
print("Set Matrix : \n", result_set)

# Solve the linear system Ax = D using numpy.linalg.solve()
D = np.array([3, 7])
print("D : ", D)
solve_array = np.linalg.solve(A, D)  
print("Result : ", solve_array)

