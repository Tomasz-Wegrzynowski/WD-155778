import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 30.1, 0.1)
s1 = (np.sin(x)*(-1))+2
s2 = np.sin(x)
plt.plot(x, s1, label='sin(x)')
plt.plot(x, s2, label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title("Wykres sin(x)")
plt.legend()

plt.show()