'''
Напишите программу  для решения СЛАУ с использованием
библиотеки NumPy.   Результат решения вывести в виде вектора. Сделать
проверку
'''
import numpy as np

print('Введите матрицу коэффициентов A:')
print('Пример: 2 1 -1; -3 -1 2; -2 1 2')
A_input = input('A = ')

rows = A_input.split(';')
A = []
for row in rows:
    row_values = []
    for num in row.split():
        row_values.append(float(num))
    A.append(row_values)
A = np.array(A)

print('Введите вектор правых частей b:')
print('Пример: 8 -11 -3')
b_input = input('b = ')

b = []
for num in b_input.split():
    b.append(float(num))
b = np.array(b)

x = np.linalg.solve(A, b)

print('Решение системы: x =', *x)

print('Проверка (A*x):', *A @ x)
print('Должно быть:', *b)
print('Невязка:', *A @ x - b)