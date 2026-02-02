# Import the NumPy library
import numpy as np

# 1. Define the dtype with explicit types:
# - 'i4' = 32-bit integer
# - 'U10' = Unicode string of maximum length 10
# - 'f4' = 32-bit float
columns = [('ID', 'i4'), ('name', 'U10'), ('marks', 'f4')]

# 2. Use TUPLES () for the individual records:
# Creating a sample 2D array with structured data types
data = np.array([
    (1, 'Atharva', 25),
    (2, 'Harish', 30),
    (4, 'Aditya', 35), 
    (5, 'Rutik', 35), 
    (6, 'Abhinav', 35), 
    (7, 'Prashant', 35), 
    (8, 'Anita', 35) 
], dtype=columns)

# Print the structured data
print("Structured Data:")
print(data)

# Access and print individual columns by their names
print('Name : ', data['name'])
print('ID : ', data['ID'])
print('Marks : ', data['marks'])
