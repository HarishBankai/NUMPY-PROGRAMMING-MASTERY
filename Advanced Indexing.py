import numpy as np  

data = np.arange(50)

even_number = data[data % 2 == 0]
odd_number = data[data % 2 != 0]

print("OG ARRAY : ", data)
print("EVEN NUMBERS : ", even_number)
print("ODD NUMBERS : ", odd_number)