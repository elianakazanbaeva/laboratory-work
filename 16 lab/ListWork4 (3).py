'''
Дан односвязный линейный список и указатель на голову списка P1.
Необходимо вывести указатель на пятый элемент этого списка P5.
Известно, что в исходном списке не менее 5 элементов.
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

    def get_fifth(self):
        current = self.head
        for i in range(4):
            if current is None:
                return None
            current = current.next
        return current


elements = input('Введите элементы списка через пробел: ').strip().split()
if len(elements) < 5:
    print('Ошибка: в списке должно быть не менее 5 элементов.')
else:
    lst = LinkedList()
    for item in elements:
        lst.append(item)

    fifth = lst.get_fifth()

    print('\nУказатель на пятый элемент (P5):', fifth)
    if fifth:
        print('Значение пятого элемента:', fifth.data)