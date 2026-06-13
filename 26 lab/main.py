from errors import ErrorHandler
from CalcTree4 import CalcTree4
from CalcTree26 import CalcTree26
from TreeWork68 import TreeWork68

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class MainController:
    def __init__(self):
        self.errors = ErrorHandler()
        self.taskFour = CalcTree4(self.errors)
        self.taskTwentySix = CalcTree26(self.errors)
        self.taskSixtyEight = TreeWork68(self.errors)
        print('система готова')

    def run(self):
        self.executeTaskFour()
        self.executeTaskTwentySix()
        self.executeTaskSixtyEight()

    def executeTaskFour(self):
        print('--- задача CalcTree4 ---')
        fname = 'filename.txt'
        if self.errors.checkFile(fname):
            data = self.readFile(fname)
            if data is not None:
                root = self.buildRpnTree(data)
                if root is not None:
                    self.taskFour.transformTree(root)
                    print('корень: ' + str(root.val))
                    print('адрес: ' + str(id(root)))
                else:
                    self.errors.showError('ошибка построения')
            else:
                self.errors.showError('ошибка чтения')
        else:
            self.errors.showError('пропуск задачи')

    def executeTaskTwentySix(self):
        print('--- задача CalcTree26 ---')
        fname = 'FN1.txt'
        outname = 'FN2.txt'
        if self.errors.checkFile(fname):
            data = self.readFile(fname)
            if data is not None:
                root = self.buildInfixTree(data)
                if root is not None:
                    xval = self.taskTwentySix.inputX()
                    res = self.taskTwentySix.evalTree(root, xval)
                    print('результат: ' + str(res))
                    self.writeToFile(outname, str(res))
                    self.taskTwentySix.replaceVar(root, xval)
                    self.printTreeSideways(outname, root)
                    print('дерево записано в ' + outname)
                else:
                    self.errors.showError('ошибка построения')
            else:
                self.errors.showError('ошибка чтения')
        else:
            self.errors.showError('пропуск задачи')

    def executeTaskSixtyEight(self):
        print('--- задача TreeWork68 ---')
        fname = 'numbers.txt'
        if self.errors.checkFile(fname):
            nums = self.readNumbers(fname)
            if nums is not None:
                root = self.buildBst(nums)
                if root is not None:
                    root = self.taskSixtyEight.balanceTree(root)
                    print('корень: ' + str(root.val))
                    print('адрес: ' + str(id(root)))
                else:
                    self.errors.showError('ошибка построения')
            else:
                self.errors.showError('ошибка чтения чисел')
        else:
            self.errors.showError('пропуск задачи')

    def readFile(self, fname):
        try:
            f = open(fname, 'r')
            line = f.read().strip()
            f.close()
            return line
        except Exception:
            return None

    def readNumbers(self, fname):
        try:
            f = open(fname, 'r')
            line = f.readline().strip()
            f.close()
            parts = line.split()
            res = []
            for p in parts:
                val = self.errors.checkNumber(p)
                if val is not None:
                    res.append(val)
            return res
        except Exception:
            return None

    def writeToFile(self, fname, data):
        try:
            f = open(fname, 'w')
            f.write(data + '\n')
            f.close()
        except Exception:
            self.errors.showError('ошибка записи')

    def printTreeSideways(self, fname, root):
        lines = []
        self.collectLines(root, lines, 0)
        try:
            f = open(fname, 'a')
            for line in lines:
                f.write(line + '\n')
            f.close()
        except Exception:
            self.errors.showError('ошибка вывода')

    def collectLines(self, node, lines, level):
        if node is None:
            return
        self.collectLines(node.right, lines, level + 1)
        txt = str(node.val)
        indent = ' ' * (level * 8)
        lines.append(indent + txt.rjust(4))
        self.collectLines(node.left, lines, level + 1)

    def buildRpnTree(self, tokens):
        opmap = {'+': -1, '-': -2, '*': -3, '/': -4, '%': -5, '^': -6}
        stack = []
        parts = tokens.split()
        for token in parts:
            cur = TreeNode(token)
            if token in opmap:
                if len(stack) < 2:
                    self.errors.showError('ошибка стека')
                    return None
                right = stack.pop()
                left = stack.pop()
                cur.val = opmap[token]
                cur.left = left
                cur.right = right
            else:
                num = self.errors.checkNumber(token)
                if num is None:
                    return None
                cur.val = num
            stack.append(cur)
        if len(stack) > 0:
            return stack.pop()
        return None

    def buildInfixTree(self, expr):
        priority = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3, '(': 0}
        vals = []
        ops = []
        i = 0
        while i < len(expr):
            ch = expr[i]
            if ch == ' ':
                i = i + 1
                continue
            if ch.isdigit():
                num = ''
                while i < len(expr) and expr[i].isdigit():
                    num = num + expr[i]
                    i = i + 1
                nval = self.errors.checkNumber(num)
                if nval is None:
                    return None
                vals.append(TreeNode(nval))
                continue
            if ch == 'x':
                vals.append(TreeNode('x'))
                i = i + 1
                continue
            if ch == '(':
                ops.append(ch)
            elif ch == ')':
                while len(ops) > 0 and ops[-1] != '(':
                    self.makeNode(vals, ops)
                if len(ops) > 0:
                    ops.pop()
            else:
                if not self.errors.checkOperation(ch):
                    i = i + 1
                    continue
                while len(ops) > 0 and ops[-1] != '(' and priority.get(ops[-1], 0) >= priority.get(ch, 0):
                    self.makeNode(vals, ops)
                ops.append(ch)
            i = i + 1
        while len(ops) > 0:
            self.makeNode(vals, ops)
        if len(vals) > 0:
            return vals.pop()
        return None

    def makeNode(self, vals, ops):
        if len(vals) < 2:
            self.errors.showError('ошибка стека')
            return
        op = ops.pop()
        right = vals.pop()
        left = vals.pop()
        n = TreeNode(op)
        n.left = left
        n.right = right
        vals.append(n)

    def buildBst(self, nums):
        root = None
        for val in nums:
            if root is None:
                root = TreeNode(val)
            else:
                cur = root
                while True:
                    if val < cur.val:
                        if cur.left is None:
                            cur.left = TreeNode(val)
                            break
                        cur = cur.left
                    else:
                        if cur.right is None:
                            cur.right = TreeNode(val)
                            break
                        cur = cur.right
        return root

boot = MainController()
boot.run()