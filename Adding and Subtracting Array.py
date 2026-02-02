import numpy as np  

#Creating a numpy array
arr1 = np.array([1, 2, 4, 9, 7, 3])
arr2 = np.array([8, 68, 5, 2, 15, 23])

print("First Array :")
print(arr1)
print("Second Array :")
print(arr2)

arr3 = np.add(arr1,arr2)

print("Array after Addition :")
print(arr3)

arr4 = np.subtract(arr1,arr2)
print("Array after Subtracting :")
print(arr4)