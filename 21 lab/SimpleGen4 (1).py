'''
Написать функцию-генератор, которая принимает на вход список целых чисел и
порождает последовательность квадратов этих чисел.
Реализовать через класс, использующий эту функцию-генератор.
'''
class SquareGenerator:
    def generate(self, lst):
        if not lst:
            return
        for x in lst:
            yield x ** 2


def main():
    while True:
        try:
            numbers_input = input('Введите целые числа через пробел: ').strip()
            if not numbers_input:
                print('Ошибка: строка не может быть пустой.')
                continue

            numbers = []
            for token in numbers_input.split():
                numbers.append(int(token))
            break
        except ValueError:
            print('Ошибка: введите только целые числа, разделённые пробелами.')

    generator = SquareGenerator()

    print('Исходный список:', ', '.join(map(str, numbers)))
    print('Квадраты:')

    for val in generator.generate(numbers):
        print(val)


if __name__ == '__main__':
    main()