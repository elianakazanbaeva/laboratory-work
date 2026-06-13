'''
Дано бинарное дерево и корень дерева P1. Необходимо вывести содержимое
листьев дерева, перечисляя их слева направо.
'''
class TreeWork4:
    def get_leaves(root):
        if root is None: return []
        if root.left is None and root.right is None: return [root.val]
        return TreeWork4.get_leaves(root.left) + TreeWork4.get_leaves(root.right)
#1 2 3 4 null 5 6