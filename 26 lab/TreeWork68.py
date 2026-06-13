'''
В первой строке текстового файла записаны целые числа, разделенные
пробелами. Создать дерево поиска, последовательно включая в него перечисленные в файле
числа. После этого необходимо, привести дерево к АВЛ-сбалансированному виду, выполнив
для RR-поворот. Известно, что требуется не более одного такого поворота. Вывести корень
полученного дерева.
'''
class TreeWork68:
    def __init__(self, errors):
        self.errors = errors

    def balanceTree(self, node):
        if node is None:
            return None
        node.left = self.balanceTree(node.left)
        node.right = self.balanceTree(node.right)
        if self.getHeight(node.right) - self.getHeight(node.left) == 2:
            if self.getHeight(node.right.right) >= self.getHeight(node.right.left):
                print('RR-поворот для узла ' + str(node.val))
                return self.rotateRR(node)
        return node

    def getHeight(self, node):
        if node is None:
            return 0
        l = self.getHeight(node.left)
        r = self.getHeight(node.right)
        if l > r:
            return l + 1
        return r + 1

    def rotateRR(self, node):
        y = node.right
        t2 = y.left
        y.left = node
        node.right = t2
        return y