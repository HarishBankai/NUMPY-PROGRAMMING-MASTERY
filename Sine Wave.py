import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(start=0, stop=10, num=100)
y = np.sin(x)

plt.plot(x, y, label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Wave')
plt.legend()
plt.show()