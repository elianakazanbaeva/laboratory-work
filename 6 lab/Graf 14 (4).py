'''
Сформировать данные для функции своего варианта (с использованием
пакета NumPy) и отобразить эти данные на экране в виде обычного графика в
декартовых координатных осях с использованием пакета Matplotlib.

y(x) = sin(x) * x ** 2, x in [0; 20; 0.01]
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 20, 0.01)
y = np.sin(x) * x**2
plt.plot(x, y, label=r'y(x) = \sin(x) \cdot x^2')
plt.title(r'График функции $y(x) = \sin(x) \cdot x^2$', fontsize=10)
plt.show()