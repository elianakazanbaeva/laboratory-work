'''
Две корпорации хотят разделить сферы влияния, выбрав два разных города для
размещения своих штаб-квартир так, чтобы все города, в некоторой округе от штаб
квартиры не были доступны для конкурентов. Схема автомобильного сообщения между
городами задана в текстовом файле с именем FileName в виде матрицы смежности. Первая
строка файла содержит количество городов (n, n<=25), связанных дорогами, а следующие
n строк хранят матрицу (m), m[i][j]=0, если нет дороги из города i в город j, иначе m[i][j]=1.
Даны два города-кандидата с номерами K1 и K2 для этих двух штаб-квартир. Определить
есть ли города, в которые можно попасть из обоих штаб-квартир, если двигаться от
каждой штаб-квартиры не более чем через L промежуточных городов. Перечислите
номера таких городов в порядке возрастания. Нумерация городов начинается с 1. Если
таких городов нет, выведите число (-1).
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
            raise ValueError('неверное число вершин')

        if self.n <= 0:
            raise ValueError('число вершин должно быть положительным')

        if len(lines) < self.n + 1:
            raise ValueError('недостаточно строк для матрицы')

        self.adj = []
        for i in range(1, self.n + 1):
            parts = lines[i].split()
            if len(parts) != self.n:
                raise ValueError('матрица не квадратная или неверное количество столбцов')

            row = []
            for x in parts:
                try:
                    val = int(x)
                except ValueError:
                    raise ValueError('обнаружено нечисло в матрице')
                if val not in (0, 1):
                    raise ValueError('матрица содержит не 0 или 1')
                row.append(val)
            self.adj.append(row)

        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.adj[i][j] != self.adj[j][i]:
                    raise ValueError('матрица не симметрична')

        remaining_tokens = []
        for line in lines[self.n + 1:]:
            remaining_tokens.extend(line.split())

        if len(remaining_tokens) < 3:
            raise ValueError('недостаточно данных для k1, k2, l')

        try:
            self.k1 = int(remaining_tokens[0])
            self.k2 = int(remaining_tokens[1])
            self.l = int(remaining_tokens[2])
        except ValueError:
            raise ValueError('неверный формат k1, k2, l')

        if not (1 <= self.k1 <= self.n and 1 <= self.k2 <= self.n):
            raise ValueError('номера городов вне диапазона')
        if self.k1 == self.k2:
            raise ValueError('города штаб-квартир должны различаться')
        if self.l < 0:
            raise ValueError('параметр l должен быть неотрицательным')

    def _bfs(self, start):
        max_dist = self.l + 1
        dist = [-1] * self.n
        dist[start-1] = 0
        queue = [start-1]
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            if dist[u] >= max_dist:
                continue
            for v in range(self.n):
                if self.adj[u][v] == 1 and dist[v] == -1:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        res = set()
        for i in range(self.n):
            if 0 < dist[i] <= max_dist:
                res.add(i+1)
        return res

    def find_common(self):
        s1 = self._bfs(self.k1)
        s2 = self._bfs(self.k2)
        common = sorted(s1 & s2)
        return common if common else [-1]

if __name__ == '__main__':
    try:
        g = Graph('FileName')
        print('Количество общих городов:', ' '.join(map(str, g.find_common())))
    except ValueError as e:
        print('ошибка: ' + str(e))