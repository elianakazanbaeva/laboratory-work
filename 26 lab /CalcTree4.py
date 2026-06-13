'''
 В текстовом файле с именем filename дано арифметическое выражение в
обратной польской записи. Операндами в выражении являются целые числа из промежутка
от 0 до 9. Используемые операции: сложение (+), вычитание (-), умножение (*), деление
нацело (/) и целочисленный остаток от деления (%) и возведение в степень (^). Постройте
дерево, соответствующее данному выражению. Знаки операций кодируйте числами: сложение
(-1), вычитание (-2), умножение (-3), деление нацело (-4), целочисленный остаток от деления (
5), возведение в степень (-6). Преобразуйте дерево так, чтобы в нем не было операции деления
Иными словами, замените поддеревья, в которых есть операции / или %, значением данного
поддерева. Выведите указатель на корень полученного дерева.
'''
class CalcTree4:
    def __init__(self, errors):
        self.errors = errors

    def transformTree(self, node):
        if node is None:
            return None
        node.left = self.transformTree(node.left)
        node.right = self.transformTree(node.right)
        if node.left is None and node.right is None:
            return node
        leftVal = node.left.val
        rightVal = node.right.val
        if node.val == -4 or node.val == -5:
            if not self.errors.checkDivision(int(rightVal)):
                return node
            newVal = self.compute(int(leftVal), int(rightVal), node.val)
            print('замена операции ' + str(node.val) + ' на ' + str(newVal))
            node.val = newVal
            node.left = None
            node.right = None
            return node
        return node

    def compute(self, a, b, op):
        if op == -1: return a + b
        if op == -2: return a - b
        if op == -3: return a * b
        if op == -4: return a // b
        if op == -5: return a % b
        if op == -6: return a ** b
        return 0
