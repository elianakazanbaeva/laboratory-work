'''
Изначально на доске написано число n. Игрок в свой ход может прибавить к числу на
доске любой его натуральный делитель, стереть старое число и записать новое. (Например,
если на доске написано число 12, то можно его стереть и написать одно из чисел 13, 14, 15, 16,
18, 24.). Побеждает тот, кто получит после своего хода число, не меньшее 60.
'''
import random

class Player:
    def __init__(self, name):
        self.name = name

    def choose_move(self, valid_moves):
        print(f'\nХод игрока: {self.name}')
        print('Доступные варианты:', ', '.join(map(str, valid_moves)))

        while True:
            try:
                choice = int(input('Введите число для записи: '))
                if choice in valid_moves:
                    return choice
                else:
                    print('Ошибка: Недопустимый ход.')
            except ValueError:
                print('Ошибка: Введите целое число.')


class Computer:
    def __init__(self, name):
        self.name = name

    def choose_move(self, valid_moves, target_number):
        print(f'\nХод игрока: {self.name}')
        print('Доступные варианты:', ', '.join(map(str, valid_moves)))

        for move in valid_moves:
            if move >= target_number:
                print(f'Компьютер выбирает: {move}')
                return move

        for move in reversed(valid_moves):
            if move < target_number:
                print(f'Компьютер выбирает: {move}')
                return move

        choice = valid_moves[-1]
        print(f'Компьютер выбирает: {choice}')
        return choice


class Game:
    def __init__(self, start_number, target_number=60):
        self.current_number = start_number
        self.target_number = target_number
        self.players = []
        self.current_player_index = 0
        self.is_game_over = False
        self.winner = None

    def add_player(self, player):
        self.players.append(player)

    def get_divisors(self, n):
        divisors = []
        for i in range(1, n + 1):
            if n % i == 0:
                divisors.append(i)
        return divisors

    def get_valid_moves(self):
        divisors = self.get_divisors(self.current_number)
        return sorted([self.current_number + d for d in divisors])

    def make_move(self, new_number):
        print(f'Записано число: {new_number}')
        self.current_number = new_number

    def check_win_condition(self):
        if self.current_number >= self.target_number:
            self.is_game_over = True
            self.winner = self.players[self.current_player_index]
            return True
        return False

    def switch_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play(self):
        print(f'\nСтарт. Число на доске: {self.current_number}. Цель: >= {self.target_number}')

        while not self.is_game_over:
            current_player = self.players[self.current_player_index]
            valid_moves = self.get_valid_moves()

            if isinstance(current_player, Computer):
                chosen_number = current_player.choose_move(valid_moves, self.target_number)
            else:
                chosen_number = current_player.choose_move(valid_moves)

            self.make_move(chosen_number)

            if self.check_win_condition():
                print(f'\nПобеда! {self.winner.name} выиграл с числом {self.current_number}')
                break

            self.switch_turn()
            print(f'\nТекущее число на доске: {self.current_number}')


if __name__ == '__main__':
    print('=== ПРАВИЛА ИГРЫ ===')
    print('1. Изначально на доске написано число n.')
    print('2. Игрок в свой ход может прибавить к числу на доске любой его натуральный делитель.')
    print('3. Старое число стирается, записывается новое.')
    print('4. Побеждает тот, кто получит после своего хода число, не меньшее 60.')
    print('====================\n')

    print('Выберите режим игры:')
    print('1. Игрок против Компьютера')
    print('2. Игрок против Игрока')

    mode = input('Введите номер режима (1 или 2): ')

    start_num = random.randint(5, 30)
    target_num = 60

    print(f'\nСлучайное начальное число: {start_num}')

    game = Game(start_number=start_num, target_number=target_num)

    p1 = Player('Игрок 1')
    game.add_player(p1)

    if mode == '1':
        computer = Computer('Компьютер')
        game.add_player(computer)
    else:
        p2 = Player('Игрок 2')
        game.add_player(p2)

    game.play()