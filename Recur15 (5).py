'''
Вывести значение целочисленного выражения, заданного в виде строки S. Выражение
определяется следующим образом:
<выражение> ::= <терм> | <выражение> + <терм> | <выражение> − <терм>
<терм> ::= <цифра> | <терм> * <цифра>
'''

try:
    with open('input.txt', 'r') as file:
        expression = file.read().strip()

    position = 0
    expr_length = len(expression)

    if not expression:
        print(0)
    else:
        # первый терм
        result = 0
        while position < expr_length and expression[position].isdigit():
            result = result * 10 + int(expression[position])
            position += 1

        #умножения
        while position < expr_length and expression[position] == '*':
            position += 1
            number = 0
            while position < expr_length and expression[position].isdigit():
                number = number * 10 + int(expression[position])
                position += 1
            result *= number

        #сложения и вычитания
        while position < expr_length and expression[position] in '+-':
            operator = expression[position]
            position += 1

            #2 терм
            term = 0
            while position < expr_length and expression[position].isdigit():
                term = term * 10 + int(expression[position])
                position += 1

            #умножения
            while position < expr_length and expression[position] == '*':
                position += 1
                number = 0
                while position < expr_length and expression[position].isdigit():
                    number = number * 10 + int(expression[position])
                    position += 1
                term *= number

            # Применение операции
            if operator == '+':
                result += term
            else:
                result -= term

        print("Результат:", result)

except FileNotFoundError:
    print("Ошибка: файл не найден")
except ValueError:
    print("Ошибка: некорректный формат числа")
except IndexError:
    print("Ошибка: выход за границы строки")
except EOFError:
    print("Ошибка: пустой ввод")
except Exception:
    print("Ошибка: неверный формат выражения")

'''
5*3*4   =60
5+3*4   =17
10-4   =6
2*3+4*5   =26
0   =0
0*5+3    =3
9*8*7-6*5*4+3*2*1    =390
'''