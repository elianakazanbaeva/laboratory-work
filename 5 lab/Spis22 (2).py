#Напишите программу, которая вычисляет арифметическое выражение,
# введённое в виде символьной строки. Выражение содержит только целые числа,
# знаки арифметических действий (сложения, вычитания, умножения и деления)
# и круглые скобки правильной вложенности.
def plus_minus_multiplication_division(expr):
    # Сначала выполняем умножение и деление
    numbers = []
    signs = []

    # Разбиваем на числа и операторы
    number = ''
    for i in expr:
        if i in '0123456789':
            number += i
        elif i in '+/*-':
            if expr.rfind(i) != len(expr) - 1:
                numbers.append(int(number))
                signs.append(i)
                number = ''
            else:
                return 'ошибка ввода'
        else:
            return 'ошибка ввода'
    numbers.append(int(number))  #последнее число

    #умножение и деление
    i = 0
    while i < len(signs):
        if signs[i] == '*':
            numbers[i] = numbers[i] * numbers[i + 1]
            numbers.pop(i + 1)
            signs.pop(i)
        elif signs[i] == '/':
            numbers[i] = numbers[i] // numbers[i + 1]
            numbers.pop(i + 1)
            signs.pop(i)
        else:
            i += 1
    #сложение и вычитание
    result = numbers[0]
    for i in range(len(signs)):
        if signs[i] == '+':
            result += numbers[i + 1]
        else:
            result -= numbers[i + 1]
    return result

expression = input('Введите выражение с целыми числами: ').replace(' ', '')
if '.' not in expression:
    while '(' in expression:
        #внутренние скобки
        start = expression.rfind('(')
        end = expression.find(')', start)
        actions_in_staples = expression[start + 1 : end]
        result = plus_minus_multiplication_division(actions_in_staples)
        #скобки -> результат
        expression = expression[:start] + str(result) + expression[end + 1:]
    #выражение без скобок
    final_result = plus_minus_multiplication_division(expression)
    print('Результат:', final_result)
else:
    print('Ошибка ввода!')

#1+2*(1*(1+3))
#=9
#1+2)(()
#vnjknbkfj
#1+2+
#1/0
#0.75*3