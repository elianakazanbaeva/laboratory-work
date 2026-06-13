'''
Юный путешественник решил изучить схему авиационного сообщения Схема
авиационного сообщения задана в текстовом файле с именем FileName. в виде матрицы
смежности. Первая строка файла содержит количество городов (n) n<=15, связанных
авиационным сообщением, а следующие n строк хранят матрицу (m), m[i][j]=0, если не
имеется возможности перелета из города i в город j, иначе m[i][j]=1. Определить номера
городов, в которые из города K можно долететь не менее чем с L пересадками и более
коротких путей к таким городам не существует. Перечислите номера таких городов в
порядке возрастания. Нумерация городов начинается с 1. Если таких городов нет,
выведите число (-1).
'''


class Graph:
    def __init__(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            raise ValueError('файл не найден')

        if not lines:
            raise ValueError('файл пуст')

        try:
            self.n = int(lines[0])
        except ValueError:
            raise ValueError('неверное число городов')
        if not (1 <= self.n <= 15):
            raise ValueError('n должно быть от 1 до 15')

        if len(lines) < self.n + 1:
            raise ValueError('недостаточно строк для матрицы')

        self.adj = []
        for i in range(1, self.n + 1):
            parts = lines[i].split()
            if len(parts) != self.n:
                raise ValueError(f'строка {i}: ожидается {self.n} чисел')

            row = []
            for x in parts:
                try:
                    val = int(x)
                except ValueError:
                    raise ValueError(f'строка {i}: обнаружено нечисло "{x}"')
                if val not in (0, 1):
                    raise ValueError(f'строка {i}: значение должно быть 0 или 1')
                row.append(val)
            self.adj.append(row)

        remaining_tokens = []
        for line in lines[self.n + 1:]:
            remaining_tokens.extend(line.split())

        if len(remaining_tokens) < 2:
            raise ValueError('отсутствуют параметры k и l')
        try:
            self.k = int(remaining_tokens[0])
            self.l = int(remaining_tokens[1])
        except ValueError:
            raise ValueError('неверный формат k или l')

        if not (1 <= self.k <= self.n):
            raise ValueError('номер города k вне диапазона')
        if self.l < 0:
            raise ValueError('параметр l не может быть отрицательным')

    def solve(self):
        dist = [-1] * self.n
        dist[self.k - 1] = 0
        queue = [self.k - 1]
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            for v in range(self.n):
                if self.adj[u][v] == 1 and dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)

        res = [i + 1 for i in range(self.n) if dist[i] >= self.l + 1 and dist[i] != -1]
        return res if res else [-1]


if __name__ == '__main__':
    try:
        g = Graph('FileName')
        print('Города, до которых можно долететь: ', ' '.join(map(str, g.solve())))
    except ValueError as e:
        print('ошибка ввода: ' + str(e))