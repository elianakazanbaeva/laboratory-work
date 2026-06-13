'''
На окружности отмечено 9 точек, делящих эту окружность на 9 равных дуг. Петя и
Вася играют в игру, делая ходы по очереди. Первым ходит Петя; своим первым ходом он
окрашивает в красный или синий цвет любую отмеченную точку. Затем каждый из игроков
своим ходом может окрасить в красный или синий цвет любую неокрашенную отмеченную
точку, соседнюю с уже окрашенной. Вася выигрывает, если после окрашивания всех точек
найдётся равносторонний треугольник, все три вершины которого окрашены, причём в один и
тот же цвет.
(0,3,6)(1,4,7)(2,5,8)
'''
import random

class Board:
    def __init__(self):
        self.points = ['.'] * 9
        self.point_colors = [None] * 9
        self.point_players = [None] * 9
        self.moves = 0

    def show(self):
        print('\n        ● 0')
        print('      ●   ●')
        print('    8       1')
        print('   ●         ●')
        print('  7           2')
        print('  ●           ●')
        print('  6           3')
        print('   ●         ●')
        print('    5       4')
        print('      ●   ●')
        print('        ●')
        print()

        print('Состояние точек:')
        for i in range(9):
            if self.points[i] == '.':
                status = '○ пустая'
            else:
                color_name = '🔴 Красная' if self.point_colors[i] == 'R' else '🔵 Синяя'
                player = self.point_players[i]
                status = f'{color_name} ({player})'
            print(f'  Точка {i}: {status}')
        print()

    def valid_moves(self):
        if self.moves == 0:
            return list(range(9))
        colored = [i for i, c in enumerate(self.points) if c != '.']
        valid = set()
        for i in colored:
            valid.add((i - 1) % 9)
            valid.add((i + 1) % 9)
        return [i for i in valid if self.points[i] == '.']

    def make_move(self, idx, color, player_letter):
        if idx not in self.valid_moves() or self.points[idx] != '.':
            return False
        self.points[idx] = color
        self.point_colors[idx] = color
        self.point_players[idx] = player_letter
        self.moves += 1
        return True

    def vasya_wins(self):
        if self.moves < 9:
            return False
        return any(self.points[a] == self.points[b] == self.points[c] != '.'
                   for a, b, c in TRIANGLES)

    def full(self):
        return self.moves == 9


class Player:
    def __init__(self, name, is_human=True):
        self.name = name
        self.is_human = is_human
        self.letter = name[0]

    def get_move(self, board):
        raise NotImplementedError


class Human(Player):
    def get_move(self, board):
        valid = board.valid_moves()
        while True:
            try:
                idx = int(input(f'{self.name}, точка (из {', '.join(map(str, valid))}): '))
                if idx not in valid:
                    print('Недопустимая точка!')
                    continue
                color = input('Цвет (R/B): ').upper()
                if color not in COLORS:
                    print('Недопустимый цвет!')
                    continue
                return idx, color
            except ValueError:
                print('Введите число!')


class AI(Player):
    def get_move(self, board):
        valid = board.valid_moves()
        if not valid:
            return None, None

        for a, b, c in TRIANGLES:
            vals = [board.points[a], board.points[b], board.points[c]]
            empty = [i for i, v in zip((a, b, c), vals) if v == '.']
            filled = [v for v in vals if v != '.']

            if len(empty) == 1 and len(filled) == 2 and filled[0] == filled[1]:
                if empty[0] in valid:
                    return empty[0], filled[0]

        return random.choice(valid), random.choice(COLORS)


class Game:
    def __init__(self):
        self.board = Board()
        self.mode = None

    def show_menu(self):
        print('=== ПРАВИЛА ИГРЫ ===')
        print('1. На окружности отмечено 9 точек, делящих её на 9 равных дуг.')
        print('2. Петя и Вася играют, делая ходы по очереди. Первым ходит Петя.')
        print('3. Первым ходом окрашивается любая точка в красный или синий цвет.')
        print('4. Затем можно окрашивать только неокрашенную точку, соседнюю с окрашенной.')
        print('5. Вася выигрывает, если после окрашивания всех 9 точек найдётся')
        print('   равносторонний треугольник, все вершины которого одного цвета.')
        print('6. Петя выигрывает, если после окрашивания всех 9 точек')
        print('   НЕ найдётся ни одного одноцветного равностороннего треугольника.')
        print('====================\n')

        print('Выберите режим игры:')
        print('1. Игрок против Компьютера')
        print('2. Игрок против Игрока')

        while True:
            choice = input('Введите номер режима (1 или 2): ').strip()
            if choice in ['1', '2']:
                self.mode = choice
                break
            print('Неверный ввод! Введите 1 или 2.')

    def setup_players(self):
        if self.mode == '1':
            print('\nВыберите сторону:')
            print('1. Играть за Петю (первый ход)')
            print('2. Играть за Васю (второй ход)')
            while True:
                choice = input('Ваш выбор (1 или 2): ').strip()
                if choice in ['1', '2']:
                    break
                print('Неверный ввод!')

            if choice == '1':
                self.petya = Human('Петя')
                self.vasya = AI('Вася')
            else:
                self.petya = AI('Петя')
                self.vasya = Human('Вася')
        else:
            self.petya = Human('Петя')
            self.vasya = Human('Вася')

        self.current = self.petya

    def switch(self):
        self.current = self.vasya if self.current == self.petya else self.petya

    def play(self):
        self.show_menu()
        self.setup_players()

        print('\n=== НАЧАЛО ИГРЫ ===')
        print('🔴 = Красная точка, 🔵 = Синяя точка')
        print('П = Петя, В = Вася')

        while not self.board.full():
            self.board.show()
            print(f'Ход: {self.current.name} ({self.current.letter})')

            if self.current.is_human:
                idx, color = self.current.get_move(self.board)
            else:
                idx, color = self.current.get_move(self.board)
                print(f'{self.current.name}: точка {idx}, цвет {color}')

            if not self.board.make_move(idx, color, self.current.letter):
                print('Ошибка хода!')
                continue

            self.switch()

        self.board.show()
        print('\n=== РЕЗУЛЬТАТ ===')
        if self.board.vasya_wins():
            print('ВАСЯ ВЫИГРАЛ! (найден одноцветный треугольник)')
        else:
            print('ПЕТЯ ВЫИГРАЛ! (нет одноцветных треугольников)')


if __name__ == '__main__':
    COLORS = ['R', 'B']
    TRIANGLES = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
    Game().play()