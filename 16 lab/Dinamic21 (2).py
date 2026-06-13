'''
Даны две очереди; начало и конец первой равны A1 и A2, а второй — A3 и A4
(если очередь пуста, соответствующие объекты равны None). Переместить все
элементы первой очереди (в порядке от начала к концу) в конец второй очереди
и вывести ссылки на начало и конец преобразованной второй очереди.
Новые объекты типа Node не создавать.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def merge(self, other):
        if other.head is None:
            return
        if self.head is None:
            self.head = other.head
            self.tail = other.tail
        else:
            self.tail.next = other.head
            self.tail = other.tail
        other.head = None
        other.tail = None

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return ' -> '.join(values) if values else 'null'


elems1 = input('Введите элементы первой очереди через пробел: ').strip().split()
elems2 = input('Введите элементы второй очереди через пробел: ').strip().split()
q1 = Queue()
for val in elems1:
    q1.enqueue(val)

q2 = Queue()
for val in elems2:
    q2.enqueue(val)

q2.merge(q1)
print('\nПосле перемещения:')
print('Вторая очередь (преобразованная):', q2)
print('Ссылка на начало второй очереди:', q2.head)
print('Ссылка на конец второй очереди:', q2.tail)

if q2.head:
    print('Значение начала:', q2.head.value)
    print('Значение конца:', q2.tail.value)
else:
    print('Вторая очередь пуста.')