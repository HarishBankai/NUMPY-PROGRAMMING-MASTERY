import numpy as np  

#Creating a numpy array
arr1 = np.array([1, 2, 4, 9, 7, 3])

copied_array = arr1.copy()                  # Create a copy of the original array
print("Original array : ", arr1)            # Print the original array
print("Copied array : ", copied_array)      # Print the copied array

arr2 = np.array([11, 7, 24, 19, 8, 5])

view_array = arr2.view()                  # Create a view of the original array

print("Original array : ", arr2)          # Print the original array
print("View of the array : ", view_array)  # Print the view of the array

view_array[4] = 29874628  # Modify an element in the view
print("Modified view of the array : ", view_array)  # Print the modified view of the array