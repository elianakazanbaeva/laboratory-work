'''
 Дан корень P1 непустого дерева. Листом дерева называется его вершина, не
имеющая дочерних вершин. Вывести количество листьев для данного дерева.
'''
class TreeWork13:
    def count_leaves(root):
        if root is None: return 0
        if root.left is None and root.right is None: return 1
        return TreeWork13.count_leaves(root.left) + TreeWork13.count_leaves(root.right)
#1 2 3 null 4 null 5