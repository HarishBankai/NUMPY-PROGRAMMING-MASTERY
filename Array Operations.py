import numpy as np  

#Creating a numpy array
arr1 = np.array([1, 2, 4, 9, 7, 3])
arr2 = np.array([11, 7, 24, 19, 8, 5])

#Printing the array
print(arr1)
print(arr2)

# Accessing Elements:
# - Indexing starts from 0
# - First element: position 0 in Python arrays
# - Fourth element: position 3 (since indexing starts at 0)
# Print and show the result of accessing elements

print("First elements : ", arr1[0])

#Accessing the fourth element
print("Fourth elements : ",arr1[3])         

zeros_array = np.zeros(6)                    # Create an array filled with zeros
print("Array of zeros : ", zeros_array)     # Add explanation comment about zero arrays:

ones_array = np.ones(6)                     # Create an array filled with ones
print("Array of ones : ", ones_array)       # Add explanation comment about one arrays:

arr3 = arr1 + arr2                             # Element-wise addition of two arrays
print("Result of adding arr1 and arr2 : ", arr3)  # Print the result of addition

arr4 = arr1 * arr2                                      # Element-wise multiplication of two arrays
print("Result of multiplying arr1 and arr2 : ", arr4)  # Print the result of multiplication
