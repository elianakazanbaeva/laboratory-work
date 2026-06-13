#Дан список из чисел и индекс элемента в списке k.
# Удалите из списка элемент с индексом k, сдвинув влево все элементы,
# стоящие правее элемента с индексом k.
from random import *
try:
    len_list = int(input('введите длину списка (натуральное число): '))
    list_numbers = []
    for i in range(len_list):
        list_numbers.append(randint(-100, 100))
    print('исходный список:', *list_numbers)
    del_index = int(input('введите индекс элемента, который хотите удалить '
                          '(отсчет элементов начинается с 0): '))
    for i in range(del_index, len_list - 1):
        list_numbers[i] = list_numbers[i + 1]
    list_numbers.pop()
    print('Измененный список:', *list_numbers)
except ValueError:
    print('при вводе была допущена ошибка!')