'''
Дан односвязный линейный список и указатель на голову списка P1. Необходимо
вставить значение M перед каждым вторым элементом списка, и вывести ссылку на последний
элемент полученного списка P2. При нечетном числе элементов исходного списка в конец
списка вставлять не надо.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before_even(self, M):
        if not self.head:
            return None

        prev = None
        curr = self.head
        position = 1

        while curr:
            if position % 2 == 0:
                new_node = Node(M)
                new_node.next = curr
                if prev:
                    prev.next = new_node
                else:
                    self.head = new_node
                prev = curr
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
            position += 1
        return prev

    def display(self):
        values = []
        curr = self.head
        while curr:
            values.append(str(curr.data))
            curr = curr.next
        print(' -> '.join(values) if values else 'None')

elements = input('Введите элементы списка через пробел: ').strip().split()
if not elements:
    print('Список пуст. Нет элементов.')
else:
    try:
        M = input('Введите значение M для вставки: ').strip()
    except EOFError:
        M = ''

    lst = LinkedList()
    for item in elements:
        lst.append(item)

    print('\nИсходный список:')
    lst.display()

    last_node = lst.insert_before_even(M)

    print('Список после вставки:')
    lst.display()

    print('\nСсылка на последний элемент (P2):', last_node)
    if last_node:
        print('Значение последнего элемента:', last_node.data)
    else:
        print('Последний элемент отсутствует (список пуст).')