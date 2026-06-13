'''
Сформировать и отобразить данные в виде трех разных графиков:
- из п. 1 – в виде столбчатой и круговой диаграммы (два графика);
- из п. 2 – в виде множества точек на плоскости (один график).
1. Распространенность полезных ископаемых (не менее пяти) в
России (данные сформировать самостоятельно).
2. Сгенерировать случайное распределение из 1000 точек с
координатами (x, y). Каждая координата – случайное вещественное
число в диапазоне [-100; -50] с равномерным распределением.
'''
import matplotlib.pyplot as plt
import numpy as np

print('Часть 1: Распространенность полезных ископаемых в России')

minerals = ['Нефть', 'Природный газ', 'Уголь', 'Железная руда', 'Золото']
percentages = [35, 25, 20, 12, 8]

if sum(percentages) != 100:
    print(f'Сумма процентов: {sum(percentages)}%. Нормализуем до 100%.')

    percentages = [i/sum(percentages)*100 for i in percentages]


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

#cтолбчатая диаграмма
bars = ax1.bar(minerals, percentages, color=['#FF6B6B', '#4ECDC4',
                                             '#45B7D1', '#96CEB4', '#FFEAA7'])
ax1.set_title('Распространенность полезных ископаемых в России', fontsize=14,
              fontweight='bold')
ax1.set_xlabel('Полезные ископаемые', fontsize=12)
ax1.set_ylabel('Доля, %', fontsize=12)
ax1.grid(axis='y', alpha=0.3)
ax1.set_ylim(0, 40)

# Добавляем подписи значений на столбцах
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{height:.1f}%', ha='center', va='bottom')

# 2. Круговая диаграмма
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
ax2.pie(percentages, labels=minerals, autopct='%1.1f%%', colors=colors,
        startangle=90, explode=[0.05]*len(minerals), shadow=True)
ax2.set_title('Доля полезных ископаемых в России', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()

# Выводим данные в консоль
print('Данные по полезным ископаемым:')
for mineral, percent in zip(minerals, percentages):
    print(f'{mineral}: {percent:.1f}%')

#Часть 2. случайные точки
print('Часть 2: Случайное распределение точек')

# Генерация 1000 случайных точек
np.random.seed(42)  # Для воспроизводимости результатов
n_points = 1000
x_coords = np.random.uniform(-100, -50, n_points)
y_coords = np.random.uniform(-100, -50, n_points)

# Создаем отдельный график для точек
plt.figure(figsize=(10, 8))
plt.scatter(x_coords, y_coords, alpha=0.6, c='blue', edgecolors='black', linewidth=0.5)
plt.title('Случайное распределение 1000 точек на плоскости', fontsize=14, fontweight='bold')
plt.xlabel('Координата X', fontsize=12)
plt.ylabel('Координата Y', fontsize=12)
plt.grid(True, alpha=0.3)
plt.axis('equal')  # Чтобы масштаб по осям был одинаковый

#линии, отмечающие диапазон
plt.axvline(x=-100, color='red', linestyle='--', alpha=0.5, label='Границы диапазона')
plt.axvline(x=-50, color='red', linestyle='--', alpha=0.5)
plt.axhline(y=-100, color='red', linestyle='--', alpha=0.5)
plt.axhline(y=-50, color='red', linestyle='--', alpha=0.5)

#прямоугольник, показывающий границы
from matplotlib.patches import Rectangle
rect = Rectangle((-100, -100), 50, 50, linewidth=1.5, edgecolor='red',
                 facecolor='none', linestyle='--', alpha=0.7)
plt.gca().add_patch(rect)

plt.legend()
plt.tight_layout()
plt.show()

# Статистика по точкам
print('Статистика по сгенерированным точкам:')
print('Количество точек:', n_points)
print(f'Диапазон X: [{x_coords.min():.2f}, {x_coords.max():.2f}]')
print(f'Диапазон Y: [{y_coords.min():.2f}, {y_coords.max():.2f}]')
print(f'Среднее X: {x_coords.mean():.2f}')
print(f'Среднее Y: {y_coords.mean():.2f}')
print(f'Стандартное отклонение X: {x_coords.std():.2f}')
print(f'Стандартное отклонение Y: {y_coords.std():.2f}')

# Показываем первые 5 точек в качестве примера
print('Первые 5 точек:')
for i in range(5):
    print(f'Точка {i+1}: ({x_coords[i]:.2f}, {y_coords[i]:.2f})')
