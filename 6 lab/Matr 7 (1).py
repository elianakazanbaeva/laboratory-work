'''
 Транспонирование матрицы.
1. Дано нечетное число n. Создайте двумерный массив из n×n элементов,
заполнив его символами "."; затем заполните символами "*" главную
диагональ и побочную диагональ.
2. Выведите полученный массив на экран, разделяя элементы массива
пробелами.
'''
try:
    array_size = int(input('Введите целую нечетную размерность двумерного массива: '))
    array = []
    if array_size % 2 != 0:

        for i in range (array_size):
            line = []
            for j in range (array_size):
                line.append('.')
            array.append(line)

        print('Исходный двумерный массив:')
        for i in range (array_size):
            for j in range (array_size):
                print('{:1}'.format(array[i][j]), end=' ')
            print()

        for i in range(array_size):
            array[i][array_size - 1 - i] = '*'
            array[i][i] = '*'

        print('Измененный двумерный массив:')
        for i in range (array_size):
            for j in range (array_size):
                print('{:1}'.format(array[i][j]), end=' ')
            print()

    else:
        print('введеное вами число не является нечетным')

except ValueError:
    print('Вы ввели не число или введенное вами число не является целым!')