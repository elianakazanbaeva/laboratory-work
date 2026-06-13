try:
    def parse_number(pos):
        """ возвращает (число, новая позиция)"""
        number = 0
        while pos < expr_length and expression[pos].isdigit():
            number = number * 10 + int(expression[pos])
            pos += 1
        return number, pos


    def parse_term(pos):
        """
        <терм> ::= <цифра> | <терм> * <цифра>
        Рекурсивная обработка умножения
        Возвращает (результат, новая позиция)
        """
        result, pos = parse_number(pos)
        if pos < expr_length and expression[pos] == '*':
            pos += 1
            right_result, pos = parse_term(pos)
            result *= right_result
        return result, pos


    def parse_expression(pos):
        """
        <выражение> ::= <терм> | <выражение> + <терм> | <выражение> − <терм>
        Рекурсивная обработка сложения и вычитания
        Возвращает (результат, новая позиция)
        """
        result, pos = parse_term(pos)
        if pos < expr_length and expression[pos] in '+-':
            operator = expression[pos]
            pos += 1
            right_result, pos = parse_expression(pos)
            if operator == '+':
                result += right_result
            else:
                result -= right_result
        return result, pos

    with open('input.txt', 'r') as file:
        expression = file.read().strip()
    expr_length = len(expression)
    if not expression:
        print("вы ничего не ввели")
    else:
        result, _ = parse_expression(0)
        print("Результат:", result)

except FileNotFoundError:
    print("Ошибка: файл не найден")
except ValueError:
    print("Ошибка: некорректный формат числа")

'''
5*3*4   =60
5+3*4   =17
10-4   =6
2*3+4*5   =26
0   =0
0*5+3    =3
9*8*7-6*5*4+3*2*1    =390
'''