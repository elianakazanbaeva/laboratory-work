#Напишите программу, которая подсчитывает количество единиц товаров,
# приобретенных покупателями онлайн-магазина. На вход программе подается
# число n – количество записей о покупках, а затем n строк вида
# «Покупатель Товар Количество». Для каждого покупателя программа
#должна выводить список покупок.
n = int(input('Введите количество записей: '))
main_list = []
for i in range(n):
    try:
        customer, product, quantity = input('введите запись в формате "покупатель товар количество" ').split()
        quantity = int(quantity)
        main_list.append([customer, product, quantity])
    except:
        print('Ошибка в записи. Пропускаем...')

# Получаем список всех покупателей
all_customers = []
for record in main_list:
    if record[0] not in all_customers:
        all_customers.append(record[0])
all_customers.sort()
print('Список покупок:')
for customer in all_customers:
    print(customer,':')
    products_sum = []
    for record in main_list:
        if record[0] == customer:
            found = False
            for i in range(len(products_sum)):
                if products_sum[i][0] == record[1]:
                    products_sum[i][1] += record[2]
                    found = True
                    break
            if not found:
                products_sum.append([record[1], record[2]])
    products_sum.sort(key=lambda x: x[0])
    for i in products_sum:
        print(i[0], '-', i[1], 'шт.')

#норм ввод
'''
Иван Хлеб 3
Мария Молоко 2
Иван Сыр 1
Петр Яйца 12
'''

#не норм ввод
'''
Иван Хлеб 0.3
Мария Молоко vfn
Иван Сыр 7
Петр Яйца -10
'''