'''
 Расширить класс двусвязного циклического списка из лабораторной работы №16
интерфейсом итератора. Итератор должен возвращать все элементы списка в обратном
порядке без остановки.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node
        self.size += 1

    def __iter__(self):
        return ReverseIterator(self)


class ReverseIterator:
    def __init__(self, linked_list):
        self._current = linked_list.head.prev if linked_list.head else None
        self._is_empty = linked_list.head is None

    def __iter__(self):
        return self

    def __next__(self):
        if self._is_empty:
            raise StopIteration
        value = self._current.value
        self._current = self._current.prev
        return value


def get_user_input():
    while True:
        raw = input('Введите элементы через пробел: ').strip()
        if not raw:
            print('Ошибка: ввод не может быть пустым.')
            continue
        return raw.split()


if __name__ == '__main__':
    data = get_user_input()

    cdl = CircularDoublyLinkedList()
    for item in data:
        cdl.append(item)

    if cdl.size == 0:
        print('Список пуст.')
    else:
        try:
            count = int(input('Сколько строк нужно вывести: '))
            iterator = iter(cdl)
            count_now = 0
            while count_now < count :
                print(f'\n{count_now+1}: {next(iterator)}', end=' ')
                count_now += 1
        except ValueError:
            print('Вы ввели не целое число')