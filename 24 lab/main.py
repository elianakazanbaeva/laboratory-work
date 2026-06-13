from error_handler import ErrorHandler
from TreeFun2 import DLLToBSTConverter
from TreeFun6 import RootRightLeftIterator
from TreeFun9 import CameraPlacer

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class ListBuilder:
    @staticmethod
    def build_dll(values):
        if not values:
            return None
        head = TreeNode(values[0])
        curr = head
        for v in values[1:]:
            node = TreeNode(v)
            curr.next = node
            node.prev = curr
            curr = node
        return head

class TreeBuilder:
    @staticmethod
    def build_tree(values):
        if not values or values[0] is None:
            return None
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        while queue and i < len(values):
            node = queue.pop(0)
            if i < len(values) and values[i] is not None:
                node.prev = TreeNode(values[i])
                queue.append(node.prev)
            i += 1
            if i < len(values) and values[i] is not None:
                node.next = TreeNode(values[i])
                queue.append(node.next)
            i += 1
        return root

class Printer:
    @staticmethod
    def print_dll(head):
        vals = []
        curr = head
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        print('Список:', ' <-> '.join(vals) if vals else 'Пусто')

    @staticmethod
    def print_tree(root):
        if not root:
            print('Дерево пустое.')
            return
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(str(node.val) if node else 'None')
            if node:
                queue.append(node.prev)
                queue.append(node.next)
        while result and result[-1] == 'None':
            result.pop()
        print('Дерево:', ', '.join(result))

    @staticmethod
    def print_iterator(iterator, label=''):
        vals = [str(v) for v in iterator]
        print(f'{label}: {" -> ".join(vals) if vals else "Пусто"}')

class LabRunner:
    def run(self):
        print('\nTreeFun2')
        raw_dll = input('Введите элементы списка: ')
        ErrorHandler.safe_execute('TreeFun2', self._task_dll_to_bst, raw_dll)

        print('\nTreeFun6')
        raw_tree6 = input('Введите уровни дерева: ')
        ErrorHandler.safe_execute('TreeFun6', self._task_iterator, raw_tree6)

        print('\nTreeFun9')
        raw_tree9 = input('Введите уровни дерева: ')
        ErrorHandler.safe_execute('TreeFun9', self._task_cameras, raw_tree9)


    def _task_dll_to_bst(self, raw):
        values = ErrorHandler.parse_dll_input(raw)
        if not values:
            print('Список пуст.')
            return
        head = ListBuilder.build_dll(values)
        Printer.print_dll(head)
        converter = DLLToBSTConverter()
        bst_root = converter.convert(head)
        Printer.print_tree(bst_root)

    def _task_iterator(self, raw):
        values = ErrorHandler.parse_tree_input(raw)
        if not values or values[0] is None:
            print('Дерево пустое.')
            return
        tree = TreeBuilder.build_tree(values)
        iterator = RootRightLeftIterator(tree)
        Printer.print_iterator(iterator, 'Обход')

    def _task_cameras(self, raw):
        values = ErrorHandler.parse_tree_input(raw)
        if not values or values[0] is None:
            print('Камер нужно: 0')
            return
        tree = TreeBuilder.build_tree(values)
        placer = CameraPlacer()
        count = placer.min_cameras(tree)
        print(f'Камер нужно: {count}')

if __name__ == '__main__':
    LabRunner().run()