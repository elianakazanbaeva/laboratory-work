'''
Дан первый элемент A1 непустого двусвязного списка. Перегруппировать
элементы списка, переместив все элементы с нечетными номерами в конец списка (в том же
порядке) и вывести ссылку на первый элемент преобразованного списка. Новые объекты типа
Node не создавать, свойства Data не изменять.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(' <-> '.join(elements) if elements else 'Список пуст')

    def rearrange_odd_positions_to_end(self):
        if not self.head or not self.head.next:
            return

        even_head = None
        even_tail = None
        odd_head = None
        odd_tail = None

        current = self.head
        position = 1

        while current:
            next_node = current.next
            current.next = None
            current.prev = None

            if position % 2 == 1:
                if not odd_head:
                    odd_head = current
                    odd_tail = current
                else:
                    odd_tail.next = current
                    current.prev = odd_tail
                    odd_tail = current
            else:
                if not even_head:
                    even_head = current
                    even_tail = current
                else:
                    even_tail.next = current
                    current.prev = even_tail
                    even_tail = current

            current = next_node
            position += 1
        if not even_head:
            self.head = odd_head
            self.tail = odd_tail
        elif not odd_head:
            self.head = even_head
            self.tail = even_tail
        else:
            self.head = even_head
            even_tail.next = odd_head
            odd_head.prev = even_tail
            self.tail = odd_tail

dll = DoublyLinkedList()
user_input = input('Введите элементы списка через пробел: ').strip().split()
for i in user_input:
    dll.append(i)
if dll.head is None:
    print('Список пуст. Операция невозможна.')
else:
    print('Исходный список:')
    dll.print_list()
    dll.rearrange_odd_positions_to_end()
    print('Преобразованный список (нечетные позиции перемещены в конец):')
    dll.print_list()
    print(f'Ссылка на первый элемент преобразованного списка (объект): {dll.head}')
    print(f'Значение первого элемента: {dll.head.data if dll.head else None}')