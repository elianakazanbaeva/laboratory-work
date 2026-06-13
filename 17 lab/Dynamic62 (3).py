'''
Даны ссылки A1, A2 и A3 на первый, последний и текущий элементы непустого
двусвязного списка. Также даны пять чисел. Включить в класс IntList (
• три закрытых поля first, last, current типа Node (первый, последний и текущий элементы
списка);
• конструктор с параметрами aFirst, aLast, aCurrent — первым, последним и текущим
элементами существующего списка;
• процедура InsertLast(D), которая добавляет новый элемент со значением D в конец списка
(D —входной параметр целого типа, добавленный элемент становится текущим);
• процедура Put (без параметров), которая выводит ссылки на поля first, last и current,
используя метод Put класса PT.)
процедуру InsertAfter(D), которая вставляет новый элемент со значением D после текущего
элемента списка (D — входной параметр целого типа). Вставленный элемент становится
текущим. С помощью метода InsertAfter вставить пять данных чисел в исходный список и
вывести ссылки на первый, последний и текущий элементы полученного списка.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class PT:
    def Put(obj):
        if obj is None:
            print('None', end=' ')
        else:
            print(obj, end=' ')


class IntList:
    def __init__(self, aFirst, aLast, aCurrent):
        self.first = aFirst
        self.last = aLast
        self.current = aCurrent

    def InsertLast(self, D):
        new_node = Node(D)
        if self.first is None:
            self.first = self.last = self.current = new_node
        else:
            self.last.next = new_node
            new_node.prev = self.last
            self.last = self.current = new_node

    def InsertAfter(self, D):
        if self.current is None:
            self.InsertLast(D)
            return
        new_node = Node(D)
        new_node.prev = self.current
        new_node.next = self.current.next
        if self.current.next:
            self.current.next.prev = new_node
        else:
            self.last = new_node
        self.current.next = new_node
        self.current = new_node

    def Put(self):
        print('first:', end=' ')
        PT.Put(self.first)
        print()
        print('last:', end=' ')
        PT.Put(self.last)
        print()
        print('current:', end=' ')
        PT.Put(self.current)
        print()


vals = input('Элементы списка: ').strip().split()
head = tail = prev = None
for v in vals:
    node = Node(v)
    if not head:
        head = node
    else:
        prev.next = node
        node.prev = prev
    prev = tail = node

A1, A2, A3 = head, tail, head
int_list = IntList(A1, A2, A3)

print('\nВведите 5 чисел:')
for i in range(5):
    int_list.InsertAfter(input(f'{i+1}: '))

print('\nРезультат:')
int_list.Put()

print('\nЗначения:', end=' ')
curr = int_list.first
res = []
while curr:
    res.append(str(curr.data))
    curr = curr.next
print(' -> '.join(res) if res else 'Пусто')