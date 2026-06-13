'''
Ученые изучают поведение птиц, вьющих гнезда на бинарном дереве, и хотят
разместить в его узлах камеры. Каждая камера может обозревать узел, в котором она
расположена, а также непосредственного предка и непосредственных потомков этого узла. По
заданному бинарному дереву требуется определить, какое минимальное количество камер
потребуется ученым для того, чтобы полностью покрыть наблюдением все узлы дерева.
'''
class CameraPlacer:
    def min_cameras(self, root):
        if not root:
            return 0
        self.count = 0
        root_state = self._dfs(root)
        if root_state == 0:
            self.count += 1
        return self.count

    def _dfs(self, node):
        if not node:
            return 1

        left_state = self._dfs(node.prev)
        right_state = self._dfs(node.next)

        if left_state == 0 or right_state == 0:
            self.count += 1
            return 2
        elif left_state == 2 or right_state == 2:
            return 1
        else:
            return 0
#1 2 3 4 5 6 7