import numpy as np
import matplotlib.pyplot as plt

# Генерация данных
x = np.arange(0, 20, 0.01)  # Массив x от 0 до 20 с шагом 0.01
y = np.sin(x) * x**2        # Вычисление значений функции

# Настройка графика
plt.figure(figsize=(12, 6))
plt.plot(x, y, color='blue', linewidth=2, label=r'$y(x) = \sin(x) \cdot x^2$')

# Оформление
plt.title(r'График функции $y(x) = \sin(x) \cdot x^2$', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y(x)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.xlim(0, 20)

# Отображение
plt.tight_layout()
plt.show()