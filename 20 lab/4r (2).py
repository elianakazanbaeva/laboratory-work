
class PartitionSolver:
    def __init__(self):
        self.res = []

    def solve(self, in_file, out_file):
        try:
            with open(in_file, 'r', encoding='utf-8') as f:
                n = int(f.read().strip())
            if not (1 <= n < 15):
                raise ValueError
        except Exception:
            raise ValueError('Требуется натуральное n < 15')

        self.res.clear()
        self._gen(n, n, [])

        with open(out_file, 'w', encoding='utf-8') as f:
            for p in self.res:
                f.write('+'.join(map(str, p)) + '\n')

    def _gen(self, rem, mx, cur):
        if rem == 0:
            self.res.append(cur[:])
            return
        for i in range(min(rem, mx), 0, -1):
            cur.append(i)
            self._gen(rem - i, i, cur)
            cur.pop()

if __name__ == '__main__':
    try:
        PartitionSolver().solve('input.txt', 'output.txt')
    except ValueError as e:
        print(e)