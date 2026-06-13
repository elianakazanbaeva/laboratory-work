#Задана квадратная матрица. Получить транспонированную матрицу и проверить,
# является ли исходная матрица симметричной относительно главной диагонали
from random import randint
try:
    matrix_size = int(input('Введите размер матрицы: '))
    matrix = []
    if matrix_size>0:
        for i in range(matrix_size):
            line = []
            for j in range(matrix_size):
                #line.append(randint(0, 9))
                line.append(float(input('Введите элeмент: ')))
            matrix.append(line)
        print(matrix)
        print('исходная матрица:')
        for i in range(matrix_size):
            for j in range(matrix_size):
                print('{:10f}'.format(matrix[i][j]), end=' ')
            print()
        print('Транспортированная матрица:')
        for i in range(matrix_size):
            for j in range(matrix_size):
                print('{:10f}'.format(matrix[j][i]), end=' ')
            print()
        result = 1
        for i in range(matrix_size):
            for j in range(i + 1, matrix_size):
                if matrix[i][j] != matrix[j][i]:
                    result = 0
        if result == 0:
            print('Матрица НЕ симметрична относительно главной диагонали')
        else:
            print('Матрица симметрична относительно главной диагонали')

except ValueError:
    print('При вводе была допущена ошибка!')

#1 7 3 7 4 5 3 5 2
