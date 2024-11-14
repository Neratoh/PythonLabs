import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = x ** np.cos(x)

plt.plot(x, y, label=r'$y = x^{\cos(x)}$', color='blue', linewidth=2, linestyle='-')

# Додаємо заголовок та підписи до осей
plt.title('Графік функції $y = x^{\cos(x)}$')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()

plt.grid(True)
plt.show()

