'''
Дана вершина A1 стека, содержащего не менее десяти элементов. Извлечь из стека
первые девять элементов и вывести их значения. Вывести также ссылку на новую вершину
стека. После извлечения элементов из стека освобождать ресурсы, которые они использовали,
вызывая для этих элементов метод Dispose.
'''

class Node:
    def __init__(self, Data=None, Next=None):
        self.Data = Data
        self.Next = Next

    def Dispose(self):
        print(f'Освобождение ресурсов узла со значением = {self.Data}')
        self.Data = None
        self.Next = None

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.Next = self.head
        self.head = new_node

    def pop(self):
        if self.isEmpty():
            return None
        popped = self.head
        self.head = self.head.Next
        popped.Next = None
        return popped

    def peek(self):
        return self.head


values = input('Введите элементы стека через пробел (не менее 10): ').strip().split()
if len(values) < 10:
    print('Ошибка: в стеке должно быть не менее 10 элементов.')
else:
    stack = Stack()
    for value in reversed(values):
        stack.push(value)

    print('Извлечение первых девяти элементов:')
    for i in range(9):
        node = stack.pop()
        if node:
            print(f'Значение: {node.Data}')
            node.Dispose()

    new_top = stack.peek()
    print('\nСсылка на новую вершину стека:', repr(new_top))
    if new_top:
        print('Значение новой вершины:', new_top.Data)
    else:
        print('Стек пуст')