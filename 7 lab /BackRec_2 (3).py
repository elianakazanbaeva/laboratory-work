def compute_solution():
    # Чтение входных данных из input.txt с проверкой
    try:
        with open('input.txt', 'r') as f:
            line1 = f.readline().split()
            if len(line1) != 2:
                raise ValueError("Первая строка должна содержать два числа:"
                                 " N и E")
            n = int(line1[0])
            E = int(line1[1])

            if n < 0 or E < 0:
                raise ValueError("N и E должны быть неотрицательными")

            energies = list(map(int, f.readline().split()))
            prices = list(map(int, f.readline().split()))

            if len(energies) != n or len(prices) != n:
                raise ValueError("Количество значений не совпадает с N")

            if any(x < 0 for x in energies) or any(x < 0 for x in prices):
                raise ValueError("Энергии и цены должны быть"
                                 " неотрицательными")

    except Exception as e:
        # Запись ошибки в output.txt
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write("Ошибка ввода: " + str(e) + '\n')
        return

    # Особый случай: E = 0 → пустой набор
    if E == 0:
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write('\n0\n0\n')
        return

    # DP: dp[i][e] — минимальная стоимость для первых i предметов
    # и энергии ровно e
    INF = 10**18
    dp = [[INF] * (E + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    # Заполнение таблицы
    for i in range(1, n + 1):
        e_i = energies[i - 1]
        p_i = prices[i - 1]
        for e in range(E + 1):
            # 1. Не берём предмет i
            dp[i][e] = dp[i - 1][e]

            # 2. Берём предмет i, если хватает энергии
            if e >= e_i and dp[i - 1][e - e_i] != INF:
                new_cost = dp[i - 1][e - e_i] + p_i
                if new_cost < dp[i][e]:
                    dp[i][e] = new_cost

    # Проверка, достижима ли энергия E
    if dp[n][E] == INF:
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write("Решение невозможно\n")
        return

    # Восстановление решения
    chosen = []
    i, e = n, E
    while i > 0 and e >= 0:
        if dp[i][e] != dp[i - 1][e]:
            chosen.append(i)  # номер предмета (1-индексированный)
            e -= energies[i - 1]
        i -= 1

    chosen.reverse()
    total_energy = sum(energies[i - 1] for i in chosen)
    total_price = dp[n][E]

    # Запись результата в output.txt
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(' '.join(map(str, chosen)) + '\n')
        f.write(str(total_energy) + '\n')
        f.write(str(total_price) + '\n')
    print('Ответ записан в файл output.txt')


if __name__ == "__main__":
    compute_solution()
