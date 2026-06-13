'''
Дано описание неориентированного графа в текстовом файле с именем FileName1.
в виде матрицы смежности. Первая строка файла содержит количество вершин графа (n), а
следующие n строк содержат матрицу смежности (a), a[i][j]=0, если ребра между
вершинами i и j не существует. Построить матрицу инцидентности данного графа и
вывести ее в файл с именем FileName2. Для справки: матрица инцидентности (b) имеет
размер n x m, m- число ребер графа, b[i][j]=1, если ребро j инцидентно вершине i, в
противном случае b[i][j]=0. Нумерацию ребер осуществлять в следующем порядке:
сначала ребра, инцидентные вершине номер 1, потом ребра инцидентные вершине номер
2 и т.д. до вершины номер n. Ребра, инцидентные вершине с номером i перечислять в
порядке возрастания номера второй вершины, инцидентной данному ребру. При выводе в
первой строке указать размер матрицы инцидентности: числа n и m, а в следующих n
строках разместить матрицу инцидентности.
'''
class Graph:
    def __init__(self, input_file):
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            raise ValueError('файл не найден')

        if not lines:
            raise ValueError('файл пуст')

        try:
            self.n = int(lines[0])
        except ValueError:
            raise ValueError('первая строка должна содержать целое число N')

        if self.n <= 0:
            raise ValueError('число вершин должно быть положительным')

        if len(lines) < self.n + 1:
            raise ValueError(f'в файле недостаточно строк: ожидается {self.n + 1}, найдено {len(lines)}')

        self.adj = []
        for i in range(1, self.n + 1):
            parts = lines[i].split()

            if len(parts) != self.n:
                raise ValueError(f'строка {i}: ожидается {self.n} элементов, получено {len(parts)}')

            row = []
            for x in parts:
                try:
                    val = int(x)
                except ValueError:
                    raise ValueError(f'строка {i}: обнаружено нечисло "{x}"')

                if val not in (0, 1):
                    raise ValueError(f'строка {i}: элемент матрицы должен быть 0 или 1, получено {val}')
                row.append(val)
            self.adj.append(row)

        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.adj[i][j] != self.adj[j][i]:
                    raise ValueError('матрица не симметрична относительно главной диагонали')

    def build_incidence(self):
        self.edges = []
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.adj[i][j] == 1:
                    self.edges.append((i, j))

        self.m = len(self.edges)
        self.inc = [[0] * self.m for _ in range(self.n)]
        for idx, (u, v) in enumerate(self.edges):
            self.inc[u][idx] = 1
            self.inc[v][idx] = 1

    def save(self, output_file):
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f'{self.n} {self.m}\n')
            for row in self.inc:
                f.write(' '.join(str(x) for x in row) + '\n')

if __name__ == '__main__':
    try:
        g = Graph('FileName1')
        g.build_incidence()
        g.save('FileName2')
        print('Матрица инцидентности успешно построена и сохранена.')
    except ValueError as e:
        print('ошибка ввода: ' + str(e))
    except Exception as e:
        print('непредвиденная ошибка: ' + str(e))