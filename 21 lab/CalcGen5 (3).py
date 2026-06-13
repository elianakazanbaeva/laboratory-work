'''
 Написать функцию-генератор, реализующую вычисление последовательности
значений арифметической прогрессии.
'''
class ArithmeticProgression:
    def generate(self, a1, d, n):
        if n <= 0:
            return
        current = a1
        for _ in range(n):
            yield current
            current += d


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Ошибка: введите целое число.')


def main():
    a1 = get_int('Введите первый член (a1): ')
    d = get_int('Введите разность (d): ')
    n = get_int('Введите количество членов (n): ')

    if n <= 0:
        print('Ошибка: количество членов должно быть положительным.')
        return

    generator = ArithmeticProgression()

    print('Результат:')
    for val in generator.generate(a1, d, n):
        print(val)


if __name__ == '__main__':
    main()
# 2 3 5
#100 -10 6
# -5 2 7