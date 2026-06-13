'''
В текстовом файле с именем FN1 дано арифметическое выражение в инфиксной
форме. В выражении используются: сложение(+), вычитание(-), умножение(*), деление
нацело(/), остаток от деления(%), возведение в степень(^), а так же целые числа из промежутка
[1; 30] и переменная x. При возведении в степень показатель степени неотрицательное целое
число. Постройте дерево выражения. После этого вычислите значение выражения при
заданном значении переменной x и выведите результат в текстовый файл с именем FN2.
Преобразуйте дерево, заменив все поддеревья, в которых использовалась переменная x, на их
значения при данном x. Не забудьте освободить память из-под удаленных вершин дерева.
Распечатайте дерево после преобразования в файл FN2 используя многострочный формат, в
котором дерево положено на бок. Каждый уровень дерева выводите в 8-и позициях,
используйте выравнивание по правому краю. При наличии нескольких подряд идущих
одинаковых операций дерево должно строиться по правилу: операции одинакового
приоритета вычисляются по порядку слева направо. Иными словами, выражение 2+3+4+5,
например, должно трактоваться как ((2+3)+4)+5, и не может трактоваться как (2+3)+(4+5) или
2+(3+(4+5)). Результаты всех вычислений, включая промежуточные, принадлежат типу int.
'''
class CalcTree26:
    def __init__(self, errors):
        self.errors = errors

    def inputX(self):
        print('введите значение x:')
        while True:
            val = input()
            xval = self.errors.checkInputNumber(val)
            if xval is not None:
                print('x = ' + str(xval))
                return xval
            print('повторите ввод:')

    def evalTree(self, node, x):
        if node is None:
            return 0
        if node.val == 'x':
            return x
        if node.left is None and node.right is None:
            return node.val
        l = self.evalTree(node.left, x)
        r = self.evalTree(node.right, x)
        return self.calcInt(l, r, node.val)

    def calcInt(self, a, b, op):
        if op == '+':
            return int(a) + int(b)
        if op == '-':
            return int(a) - int(b)
        if op == '*':
            return int(a) * int(b)
        if op == '/':
            if not self.errors.checkDivision(int(b)):
                return 0
            return int(a) // int(b)
        if op == '%':
            if not self.errors.checkDivision(int(b)):
                return 0
            return int(a) % int(b)
        if op == '^':
            return int(a) ** int(b)
        return 0

    def replaceVar(self, node, xval):
        if node is None:
            return None
        if node.val == 'x':
            v = self.evalTree(node, xval)
            print('замена x на ' + str(v))
            node.val = v
            node.left = None
            node.right = None
            return node
        node.left = self.replaceVar(node.left, xval)
        node.right = self.replaceVar(node.right, xval)
        if node.left is not None and node.right is not None:
            if node.left.left is None and node.left.right is None and node.right.left is None and node.right.right is None:
                v = self.calcInt(node.left.val, node.right.val, node.val)
                print('свертка ' + str(node.val) + ' в ' + str(v))
                node.val = v
                node.left = None
                node.right = None
                return node
        return node