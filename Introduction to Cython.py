import numpy as np
import time
from sum_of_squares_cython import sum_of_squares_cython

x = np.random.rand(1000000)

start = time.time()
result = sum_of_squares_cython(x)
end = time.time()

print(f"Result: {result}")
print(f"Time taken with Cython: {end - start} seconds")