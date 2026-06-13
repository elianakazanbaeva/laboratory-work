'''
Дано число D и ссылка A0 на один из элементов непустого двусвязного списка.
Вставить после данного элемента списка новый элемент со значением D и вывести ссылку на
добавленный элемент списка.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        return new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            raise ValueError('Значение элемента не должно быть пустым')
        new_node = Node(data)
        new_node.prev = prev_node
        new_node.next = prev_node.next

        if prev_node.next is not None:
            prev_node.next.prev = new_node
        else:
            self.tail = new_node

        prev_node.next = new_node
        return new_node

    def get_node_by_index(self, index):
        if index < 0:
            raise IndexError('Индекс не может быть отрицательным')
        current = self.head
        for i in range(index):
            if current is None:
                raise IndexError('Индекс выходит за границы списка')
            current = current.next
        if current is None:
            raise IndexError('Индекс выходит за границы списка')
        return current

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(' <-> '   .join(elements))


lst = DoublyLinkedList()
node = input('введите элементы через пробел: ').strip().split()
for element in node:
    lst.append(element)
print('Создан двусвязный список:')
lst.display()
try:
    d = int(input('Введите число D: '))
    index = int(input('Введите индекс элемента, после которого вставить: ')) - 1
    a0 = lst.get_node_by_index(index)
    new_node = lst.insert_after(a0, d)
    print(f'Добавлен новый элемент: значение {new_node.data}, ссылка {repr(new_node)}')
    print('Список после вставки:')
    lst.display()
except ValueError:
    print('Ошибка: введено некорректное число.')
except IndexError:
    print(f'Ошибка индекса')
