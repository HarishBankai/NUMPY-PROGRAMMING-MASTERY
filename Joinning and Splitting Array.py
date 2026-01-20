import numpy as np  

#Creating a numpy array
arr1 = np.array([1, 2, 4, 9, 7, 3])
arr2 = np.array([11, 7, 24, 19, 8, 5])

#Printing the array
print(arr1)
print(arr2)

array_hstack = np.hstack((arr1, arr2))          # Join two arrays horizontally
print("Horzontally stacked array : ", array_hstack)  # Print the horizontally stacked array

array_vstack = np.vstack((arr1, arr2))          # Join two arrays vertically
print("Vertically stacked array : \n", array_vstack)  # Print the vertically

arr3 = array_hstack
array_hsplit = np.hsplit(arr3, 12)                # Split the horizontally stacked array into 12 parts
print("Horizontally split arrays : ", array_hsplit)  # Print the horizontally split arrays

arr3 = array_vstack
array_vsplit = np.vsplit(arr3, 2)                # Split the vertically stacked array into 2 parts
print("Vertically split arrays : ", array_vsplit)  # Print the vertically split arrays