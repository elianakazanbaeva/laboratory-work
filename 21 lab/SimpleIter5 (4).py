'''
Написать класс, реализующий интерфейс итератора. Класс должен принимать в
конструкторе список элементов произвольного типа и позволять просмотреть его следующим
образом: сначала — все элементы с четными номерами в прямом порядке, затем — все
элементы с нечетными номерами в обратном порядке.
'''
class CustomIterator:
    def __init__(self, items):
        self._items = items
        self._n = len(items)
        self._phase = 0
        self._even_idx = 1
        self._odd_idx = self._n - 1 if self._n % 2 != 0 else self._n - 2

    def __iter__(self):
        return self

    def __next__(self):
        if self._phase == 0:
            if self._even_idx < self._n:
                val = self._items[self._even_idx]
                self._even_idx += 2
                return val
            self._phase = 1

        if self._odd_idx >= 0:
            val = self._items[self._odd_idx]
            self._odd_idx -= 2
            return val

        raise StopIteration

def get_input():
    while True:
        raw = input('Введите элементы через пробел: ').strip()
        if not raw:
            print('Ошибка: ввод не может быть пустым.')
            continue
        return raw.split()

if __name__ == '__main__':
    data = get_input()
    iterator = CustomIterator(data)
    print('Результат:')
    try:
        while True:
            print(next(iterator), end=' ')
    except StopIteration:
        print('\nГотово.')