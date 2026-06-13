'''
Даны ссылки A1 и A2 на барьерные элементы двух двусвязных списков (о списке
с барьерным элементом см. задание Dynamic70). Объединить исходные списки, связав конец
первого и начало второго списка (барьерным элементом объединенного списка должен
остаться барьерный элемент второго списка). Вывести ссылки на первый и последний
элементы объединенного списка (если объединенный список является пустым, то дважды
вывести ссылку на его барьерный элемент). После удаления лишнего барьерного элемента
вызвать для него метод Dispose.
'''

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    def Dispose(self):
        self.data = None
        self.next = None
        self.prev = None


class BarrierList:
    def __init__(self):
        self.barrier = Node(0)
        self.barrier.next = self.barrier
        self.barrier.prev = self.barrier

    def append(self, data):
        new_node = Node(data)
        last = self.barrier.prev

        new_node.prev = last
        new_node.next = self.barrier

        last.next = new_node
        self.barrier.prev = new_node

    def get_first(self):
        if self.barrier.next == self.barrier:
            return None
        return self.barrier.next

    def get_last(self):
        if self.barrier.prev == self.barrier:
            return None
        return self.barrier.prev

    def get_barrier(self):
        return self.barrier

    def is_empty(self):
        return self.barrier.next == self.barrier

    def merge_with(self, other_list):
        if self.is_empty():
            self.barrier.Dispose()
            return other_list

        if other_list.is_empty():
            other_list.barrier.prev = self.barrier.prev
            other_list.barrier.next = self.barrier.next
            self.barrier.Dispose()
            return other_list

        last1 = self.barrier.prev
        first1 = self.barrier.next
        first2 = other_list.barrier.next
        last2 = other_list.barrier.prev

        last1.next = first2
        first2.prev = last1

        other_list.barrier.next = first1
        other_list.barrier.prev = last2

        self.barrier.Dispose()

        return other_list

    def display(self):
        elements = []
        current = self.barrier.next
        while current != self.barrier:
            elements.append(str(current.data))
            current = current.next
        print(' <-> '.join(elements) if elements else 'Пусто')

    def print_references(self):
        first = self.get_first()
        last = self.get_last()
        barrier = self.get_barrier()

        if first is None and last is None:
            print(f'Первый элемент: {barrier}')
            print(f'Последний элемент: {barrier}')
        else:
            print(f'Первый элемент: {first}')
            print(f'Последний элемент: {last}')
        print(f'Барьерный элемент: {barrier}')

vals1 = input('Элементы первого списка (через пробел): ').strip().split()
list1 = BarrierList()
for v in vals1:
    list1.append(v)
print('Содержимое:')
list1.display()

vals2 = input('Элементы второго списка (через пробел): ').strip().split()
list2 = BarrierList()
for v in vals2:
    list2.append(v)
print('Содержимое:')
list2.display()

result_list = list1.merge_with(list2)

print('Объединённый список:')
result_list.display()
print('\nСсылки на элементы:')
result_list.print_references()