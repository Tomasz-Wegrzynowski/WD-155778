import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 21, 1)

plt.plot(x, 1/x, 'g>:', label='funkcja 1/x' )
plt.xticks(x)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Wykres liniowy funkcji f(x) = 1/x dla x ϵ [1, 20]")
plt.legend()
plt.text(3,0.4,'Punkt (3,0.4)')
plt.show()