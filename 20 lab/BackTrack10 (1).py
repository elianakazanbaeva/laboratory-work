class MazeSolver:
    def __init__(self, filepath):
        self.n = 0
        self.grid = []
        self.start = self.end = (0, 0)
        self.visited = []
        self.count = 0
        self._load(filepath)

    def _load(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                lines = [line.rstrip('\n\r') for line in f.readlines()]
                lines = [l for l in lines if l.strip() != '']
        except FileNotFoundError:
            raise ValueError(f'Файл "{path}" не найден')

        if len(lines) < 4:
            raise ValueError('Недостаточно данных в файле')

        try:
            self.n = int(lines[0].strip())
        except ValueError:
            raise ValueError('Первая строка должна содержать целое число N')

        if not (1 <= self.n <= 15):
            raise ValueError(f'N должно быть от 1 до 15 (сейчас {self.n})')
        raw_rows = lines[1:self.n + 1]
        if len(raw_rows) < self.n:
            raise ValueError(f'Не хватает строк карты лабиринта. Ожидалось {self.n}, найдено {len(raw_rows)}')

        self.grid = []
        for i, row in enumerate(raw_rows):
            if len(row) < self.n:
                row = row.ljust(self.n)
            elif len(row) > self.n:

                row = row[:self.n]

            self.grid.append(list(row))
        if len(lines) < self.n + 3:
            raise ValueError('Не хватает строк с координатами мыши и сыра')

        try:
            sx, sy = map(int, lines[self.n + 1].split())
            ex, ey = map(int, lines[self.n + 2].split())
        except ValueError:
            raise ValueError('Координаты должны быть двумя целыми числами через пробел')

        self.start = (sx - 1, sy - 1)
        self.end = (ex - 1, ey - 1)
        for name, pos in [('мыши', self.start), ('сыра', self.end)]:
            x, y = pos
            if not (0 <= x < self.n and 0 <= y < self.n):
                raise ValueError(
                    f'Координаты {name} ({sx},{sy} или {ex},{ey}) выходят за границы лабиринта {self.n}x{self.n}')

            if self.grid[x][y] == 'М':
                raise ValueError(f'Позиция {name} ({x + 1},{y + 1}) попадает на стену "М"')

        self.visited = [[False] * self.n for _ in range(self.n)]

    def count_paths(self):
        self.count = 0
        self.visited = [[False] * self.n for _ in range(self.n)]
        self._dfs(*self.start)
        return self.count

    def _dfs(self, x, y):
        if (x, y) == self.end:
            self.count += 1
            return

        self.visited[x][y] = True

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                if self.grid[nx][ny] != 'М' and not self.visited[nx][ny]:
                    self._dfs(nx, ny)

        self.visited[x][y] = False


if __name__ == '__main__':
    try:
        solver = MazeSolver('maze.txt')
        result = solver.count_paths()
        print(f'Количество путей: {result}')
    except ValueError as e:
        print(f'Ошибка формата: {e}')
    except Exception as e:
        print(f'Неизвестная ошибка: {e}')