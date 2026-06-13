# Для заданной квадратной матрицы найти след матрицы, суммируя элементы,
# стоящие на главной диагонали. Преобразовать исходную матрицу по правилу:
# четные строки разделить на полученное значение, нечетные оставить без
# изменения. След матрицы — это сумма элементов, находящихся
# на главной диагонали
from random import randint
try:
    matrix_size = int(input('Введите размер матрицы: '))
    matrix = []
    sum_main = 0

    if matrix_size > 0:

        for i in range(matrix_size):
            line = []
            for j in range(matrix_size):
                line.append(float(input('введите элемент матрицы: ')))
                #line.append(randint(0, 9))
            matrix.append(line)
        print('Исходная матрица:')
        for i in range(matrix_size):
            for j in range(matrix_size):
                print('{:3f}'.format(matrix[i][j]), end=' ')
            print()
    for i in range(matrix_size):
        sum_main += matrix[i][i]
    print('След матрицы:', sum_main)
    if sum_main == 0:
        print('Ошибка: деление на ноль невозможно!')
    else:
        matrix1 = []
        for i in range(matrix_size):
            line = []
            for j in range(matrix_size):
                if i % 2 == 0:
                    line.append(matrix[i][j] / sum_main)
                else:
                    line.append(matrix[i][j])
            matrix1.append(line)

        print('Измененная матрица:')
        for i in range(matrix_size):
            for j in range(matrix_size):

                print('{:7.3f}'.format(matrix1[i][j]), end=' ')
            print()

except ValueError:
    print('При вводе была допущена ошибка!')
