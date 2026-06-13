'''
Дядя Андрей и девочка Маша играют в игру. У них имеются две упаковки сока по 24
литра: один грушевый, другой вишнёвый. Кроме того, у Андрея есть кружка в 500 мл, а у
Маши — две кружки по 240 мл. Игроки пьют сок по очереди по следующим правилам: они
наполняют все свои кружки до краёв, а затем выпивают налитое до дна. При этом запрещается
смешивать два вида сока в одной ёмкости. Если кто-то не может сделать ход, то ходит его
соперник. Игра заканчивается, когда никто не может сделать ход. Побеждает тот, кто выпил
больше сока.
'''

class JuicePool:
    def __init__(self):
        self.pear = INITIAL_JUICE
        self.cherry = INITIAL_JUICE

    def has_enough(self, pear_need, cherry_need):
        return self.pear >= pear_need and self.cherry >= cherry_need

    def consume(self, pear_need, cherry_need):
        self.pear -= pear_need
        self.cherry -= cherry_need

    def __str__(self):
        return "Остаток сока -> Грушевый: {} мл, Вишнёвый: {} мл".format(
            self.pear, self.cherry
        )


class Player:
    def __init__(self, name, is_human=True):
        self.name = name
        self.is_human = is_human
        self.total_drunk = 0

    def make_move(self, pool, move):
        pear_need, cherry_need = move[1], move[2]
        if pool.has_enough(pear_need, cherry_need):
            pool.consume(pear_need, cherry_need)
            self.total_drunk += (pear_need + cherry_need)
            return True
        return False

    def __str__(self):
        return "{} (Выпито: {} мл)".format(self.name, self.total_drunk)


class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__(name, is_human=True)

    def choose_move(self, possible_moves):
        if not possible_moves:
            return None

        print("\n--- Ход игрока {} ---".format(self.name))
        print("Доступные варианты наполнения кружек:")
        for i, move in enumerate(possible_moves):
            print("{}. {}".format(i + 1, move[0]))

        while True:
            try:
                choice_str = input("Выберите номер хода: ")
                choice = int(choice_str)
                if 1 <= choice <= len(possible_moves):
                    return possible_moves[choice - 1]
                else:
                    print("Неверный номер. Попробуйте снова.")
            except ValueError:
                print("Введите число.")


class AIPlayer(Player):
    def __init__(self, name):
        super().__init__(name, is_human=False)

    def choose_move(self, possible_moves):
        if not possible_moves:
            return None

        print("\n--- Ход компьютера ({}) ---".format(self.name))
        best_move = possible_moves[0]
        for move in possible_moves[1:]:
            if move[1] + move[2] > best_move[1] + best_move[2]:
                best_move = move
        print("Компьютер выбирает: {}".format(best_move[0]))
        return best_move

class Game:
    def __init__(self, player1, player2):
        self.pool = JuicePool()
        self.players = [player1, player2]
        self.current_player_idx = 0
        self.consecutive_passes = 0
        self.is_game_over = False

    def get_andrey_moves(self, pool):
        moves = []
        if pool.has_enough(ANDREY_MUG, 0):
            moves.append(("Выпить 500 мл грушевого сока", ANDREY_MUG, 0))
        if pool.has_enough(0, ANDREY_MUG):
            moves.append(("Выпить 500 мл вишнёвого сока", 0, ANDREY_MUG))
        return moves

    def get_masha_moves(self, pool):
        moves = []
        if pool.has_enough(MASHA_MUG, 0):
            moves.append(("1 кружка грушевого (240 мл)", MASHA_MUG, 0))
        if pool.has_enough(0, MASHA_MUG):
            moves.append(("1 кружка вишнёвого (240 мл)", 0, MASHA_MUG))
        if pool.has_enough(MASHA_MUG * 2, 0):
            moves.append(("2 кружки грушевого (480 мл)", MASHA_MUG * 2, 0))
        if pool.has_enough(0, MASHA_MUG * 2):
            moves.append(("2 кружки вишнёвого (480 мл)", 0, MASHA_MUG * 2))
        if pool.has_enough(MASHA_MUG, MASHA_MUG):
            moves.append(("1 грушевый + 1 вишнёвый (480 мл)", MASHA_MUG, MASHA_MUG))
        return moves

    def display_status(self):
        print("\n" + "=" * 50)
        print("{}".format(self.pool))
        for p in self.players:
            print("{}".format(p))
        print("=" * 50)

    def play_turn(self):
        player = self.players[self.current_player_idx]

        if player.name == "Дядя Андрей":
            possible_moves = self.get_andrey_moves(self.pool)
        else:
            possible_moves = self.get_masha_moves(self.pool)

        if not possible_moves:
            print("-> {} не может сделать ход (не хватает сока)!".format(player.name))
            self.consecutive_passes += 1
            if self.consecutive_passes >= 2:
                self.is_game_over = True
            self.current_player_idx = (self.current_player_idx + 1) % len(self.players)
            return

        self.consecutive_passes = 0
        move = player.choose_move(possible_moves)

        if move:
            player.make_move(self.pool, move)
            print("-> {} выпил {} мл.".format(player.name, move[1] + move[2]))

        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)

    def determine_winner(self):
        print("\n" + "#" * 50)
        print("ИГРА ОКОНЧЕНА!")
        print("Финальное состояние: {}".format(self.pool))
        for p in self.players:
            print("{}".format(p))

        if self.players[0].total_drunk > self.players[1].total_drunk:
            print("ПОБЕДИЛ: {}!".format(self.players[0].name))
        elif self.players[1].total_drunk > self.players[0].total_drunk:
            print("ПОБЕДИЛ: {}!".format(self.players[1].name))
        else:
            print("НИЧЬЯ!")
        print("#" * 50)

    def start(self):
        while not self.is_game_over:
            self.display_status()
            self.play_turn()

        self.determine_winner()


def get_game_mode():
    print("\n" + "=" * 50)
    print("ВЫБОР РЕЖИМА ИГРЫ")
    print("=" * 50)
    print("1. Одиночная игра (против компьютера)")
    print("2. Игра вдвоём (два человека)")

    while True:
        try:
            choice = int(input("\nВыберите режим (1 или 2): "))
            if choice in [1, 2]:
                return choice
            else:
                print("Введите 1 или 2.")
        except ValueError:
            print("Введите число.")


def get_character_choice():
    print("\n" + "=" * 50)
    print("ВЫБОР ПЕРСОНАЖА")
    print("=" * 50)
    print("1. Дядя Андрей (1 кружка 500 мл)")
    print("2. Девочка Маша (1-2 кружки по 240 мл)")

    while True:
        try:
            choice = int(input("\nЗа кого будете играть? (1 или 2): "))
            if choice in [1, 2]:
                return choice
            else:
                print("Введите 1 или 2.")
        except ValueError:
            print("Введите число.")


def create_players():
    mode = get_game_mode()

    if mode == 1:
        char_choice = get_character_choice()
        if char_choice == 1:
            player1 = HumanPlayer("Дядя Андрей")
            player2 = AIPlayer("Девочка Маша")
            print("\nВы играете за Дядю Андрея. Компьютер играет за Машу.")
        else:
            player1 = AIPlayer("Дядя Андрей")
            player2 = HumanPlayer("Девочка Маша")
            print("\nВы играете за Девочку Машу. Компьютер играет за Андрея.")
    else:
        player1 = HumanPlayer("Дядя Андрей")
        player2 = HumanPlayer("Девочка Маша")
        print("\nИгра вдвоём: Андрей vs Маша")

    return player1, player2


def main():
    print("=" * 50)
    print("'СОК ДЯДИ АНДРЕЯ И ДЕВОЧКИ МАШИ'")
    print("=" * 50)
    print("\nПравила:")
    print("- Наполняйте кружки до краёв перед употреблением")
    print("- Запрещено смешивать два вида сока в одной кружке")
    print("- Дядя Андрей: 1 кружка 500 мл (грушевый или вишнёвый)")
    print("- Девочка Маша: 1 или 2 кружки по 240 мл")
    print("- Если игрок не может сделать ход, ход переходит сопернику")
    print("- Игра заканчивается, когда оба не могут сделать ход")
    print("- Побеждает тот, кто выпил больше сока")

    player1, player2 = create_players()
    game = Game(player1, player2)
    game.start()


if __name__ == "__main__":
    INITIAL_JUICE = 24000
    ANDREY_MUG = 500
    MASHA_MUG = 240
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nИгра прервана пользователем.")
    except EOFError:
        print("\n\nИгра завершена.")