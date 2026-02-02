import numpy as np

# Load data from CSV file with comma delimiter and handle any potential Unicode characters
data1 = np.genfromtxt(
    'C:\\Users\\haris\\OneDrive\\Documents\\VSC\\DATASET CSV\\Iris.csv',
    delimiter=',',
    encoding='utf-8'
)

top_5_rows = data1[:5]

print("Successfully loaded Iris dataset : ", top_5_rows)

data2 = np.random.rand(1, 10)
print("Generated data : ", data2)

data3 = np.array([[1,8,9], [2,4,6], [3,5,7]])
np.savetxt('C:\\Users\\haris\\OneDrive\\Documents\\VSC\\DATASET CSV\\Iris.csv', data3, delimiter=',')
print("Save data in CSV")