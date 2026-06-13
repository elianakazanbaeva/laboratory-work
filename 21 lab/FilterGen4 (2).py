'''
Написать функцию-генератор, которая осуществляет фильтрацию входной
последовательности символов. На вход функции подается строка. Генератор должен
порождать последовательность символов, которые удовлетворяют следующему условию:
являются римскими цифрами.
'''


class RomanFilter:
    def generate(self, text):
        if not text:
            return
        roman_chars = set('IVXLCDMivxlcdm')
        for char in text:
            if char in roman_chars:
                yield char

def main():
    while True:
        user_input = input('Введите строку: ').strip()
        if not user_input:
            print('Ошибка: строка не может быть пустой.')
            continue
        break

    generator = RomanFilter()
    print('Результат (посимвольный вывод):')
    for char in generator.generate(user_input):
        print(char)

if __name__ == '__main__':
    main()
#XVII MLXVI 123 IV