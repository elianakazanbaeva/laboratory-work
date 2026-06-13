'''
Ден текстовый файл в первой строке которого хранится число N, а во второй
строке N целых чисел. Необходимо создать упорядоченный по убыванию список, в который
поместить все эти элементы, при этом очередной элемент вставлять в список так, чтобы не
нарушалась его упорядоченность
'''

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def add_sorted(self, val):
        new_node = Node(val)

        if self.head is None or self.head.value < val:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        while (current.next is not None) and (current.next.value) >= val:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def display(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.value))
            current = current.next
        print(' '.join(result))


def load_data_from_file(filepath):
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()

        if len(lines) < 2:
            raise ValueError('Файл должен содержать минимум две строки.')

        n_str = lines[0].strip()
        data_str = lines[1].strip()

        if not n_str.isdigit():
            raise ValueError('Первая строка должна содержать число N.')

        n = int(n_str)
        numbers = list(map(int, data_str.split()))

        if len(numbers) != n:
            raise ValueError(f'Ожидается {n} чисел, но найдено'
                             f' {len(numbers)}.')

        return numbers

    except FileNotFoundError:
        print(f'Ошибка: Файл "{filepath}" не найден.')
        return None


def main():
    numbers = load_data_from_file('input.txt')

    if numbers is None:
        return

    sorted_list = LinkedList()

    for num in numbers:
        sorted_list.add_sorted(num)

    print('Результат (упорядоченный по убыванию):')
    sorted_list.display()


if __name__ == '__main__':
    main()