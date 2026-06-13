'''
Дано бинарное дерево и корень дерева P1. Необходимо определить, является ли
дерево АВЛ-сбалансированным. В качестве результата вывести логическое значение: True или
False. Дерево называется АВЛ-сбалансированным, если для каждой его вершины выполнено
условие: высота ее левого и правого поддерева отличается не больше, чем на 1.
'''
class AVLChecker:
    def is_balanced(root):
        def check(node):
            if node is None: return 0, True
            hl, bl = check(node.left)
            hr, br = check(node.right)
            return 1 + max(hl, hr), bl and br and abs(hl - hr) <= 2
        _, res = check(root)
        return res
#10 5 15 null 7 null 20 null 25
#1 2 8 3 null null null 4 null 5