import numpy as np  

#Creating a numpy array
arr = np.array([1, 2, 4, 9, 7, 3])

#Printing the array
print(arr)

# Accessing Elements:
# - Indexing starts from 0
# - First element: position 0 in Python arrays
# - Fourth element: position 3 (since indexing starts at 0)
# Print and show the result of accessing elements

print("First elements : ", arr[0])

#Accessing the fourth element
print("Fourth elements : ",arr[3])         

zeros_array = np.zeros(6)                    # Create an array filled with zeros
print("Array of zeros : ", zeros_array)     # Add explanation comment about zero arrays:

ones_array = np.ones(6)                     # Create an array filled with ones
print("Array of ones : ", ones_array)       # Add explanation comment about one arrays:

