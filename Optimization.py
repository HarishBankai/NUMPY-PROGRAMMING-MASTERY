import numpy as np  

data = np.random.rand(1000000)  # Create an array of 100,000 random numbers using NumPy

def sum_with_loop(data):  
    """This function calculates the sum of elements in data using a Python loop."""
    total = 0  
    for num in data:  
        total += num  
    return total  

def sum_with_numpy(data):  
    """This function calculates the sum of elements in data using NumPy's optimized functions."""  
    return np.sum(data)  

print("SUM WITH LOOP : ", sum_with_loop(data))  
print("SUM WITH NUMPY : ", sum_with_numpy(data))  
