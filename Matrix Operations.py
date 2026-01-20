import numpy as np

# Create two 2x2 matrices for demonstration of matrix operations
# A and B are used in various engineering/physics applications like solving systems of equations or transformations
A = np.array([[2, 6],  
              [3, 4]])
B = np.array([[9, 7],  
              [6, 5]])

# Add the matrices element-wise (same dimensions required)
# The resulting matrix C will also be 2x2 where each element is sum of corresponding elements in A and B
print("Matrix A : \n", A)  # Print original Matrix A for reference
print("Matrix B : \n", B)  # Print original Matrix B for reference

# Add the two matrices using matrix addition operation
C = A + B  
print("Result of adding Matrix A and B (A + B): \n", C)

# Multiply Matrix A by scalar value 3 - each element in the matrix is multiplied by 3
D = A * 3  
print("Result of multiplying Matrix A by 3 (3 * A): \n", D)

# Add explanation comments at top
# This code demonstrates basic matrix operations which are fundamental in linear algebra applications such as:
# - Solving systems of linear equations
# - Transformations in computer graphics
# - Engineering and physics calculations involving vectors and matrices