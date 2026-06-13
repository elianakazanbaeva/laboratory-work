'''
 Реализовать для бинарного дерева интерфейс итератора, который будет возвращать
значения элементов, находящихся в узлах дерева, в порядке "корень-право-лево".
Преобразовывать дерево в список или иную структуру данных нельзя, рекурсию использовать
запрещается.
'''
class RootRightLeftIterator:
    def __init__(self, root):
        self.stack = [root] if root else []

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration

        node = self.stack.pop()
        if node.prev:
            self.stack.append(node.prev)
        if node.next:
            self.stack.append(node.next)

        return node.val
#1 2 3 4 5 6 7
#10 5 15 None 7 12 20