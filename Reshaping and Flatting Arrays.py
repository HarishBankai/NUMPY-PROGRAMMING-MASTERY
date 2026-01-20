import numpy as np  

#Creating a numpy array
arr1 = np.array([1, 2, 4, 9, 7, 3])
print
print(arr1)

array_reshaped = arr1.reshape(3, 2)
print("Reshaped Array :")
print(array_reshaped)

arr2 = np.array([[11, 7, 24], 
                 [19, 8, 5]])

print(arr2)

array_flattened = arr2.flatten()

print("Flattened Array :")
print(array_flattened)