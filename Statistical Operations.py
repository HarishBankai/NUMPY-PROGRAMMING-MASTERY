import numpy as np  

#Creating a numpy array
arr1 = np.array([1, 2, 4, 9, 7, 3 , 5, 15, 3, 7, 6, 1, 9])

mean = np.mean(arr1)
print("Mean : ", mean)

median = np.median(arr1)
print("Median : ", median)

standard_deviation = np.std(arr1)
print("Standard Deviation : ", standard_deviation)

variance = np.var(arr1)
print("Variance: ", variance)

