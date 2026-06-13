'''
Преобразовать двусвязный список в бинарное дерево поиска без использования
дополнительной памяти (создания новых объектов). Корнем дерева должен стать элемент
списка, находящийся в его середине, а само дерево должно иметь наименьшую возможную
высоту. При преобразовании поля left и right узлов бинарного дерева рассматриваются
эквивалентными полям prev и next узлов двусвязного списка. Вывести исходный список и
получившееся дерево
'''
class DLLToBSTConverter:
    def convert(self, head):
        if not head:
            return None

        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        self._current = head
        return self._build_bst(0, count - 1)

    def _build_bst(self, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        left_node = self._build_bst(start, mid - 1)

        root = self._current
        root.prev = left_node
        self._current = self._current.next

        root.next = self._build_bst(mid + 1, end)
        return root
#1 2 3 4 5 6 7