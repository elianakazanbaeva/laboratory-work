#Тип поиска: целочисленный
#Границы: left (нижняя), right (верхняя)
#Условие монотонности: существует x0, такое что
#   ∀ x < x0: feasible(x) == False
#   ∀ x ≥ x0: feasible(x) == True

def binary_search(feasible, left, right):
    """
        Бинарный поиск минимального x, где feasible(x) = True.

        Аргументы:
            feasible: Монотонная функция int -> bool
            left: Левая граница (feasible(left-1) = False)
            right: Правая граница (feasible(right) = True)

        Вывод:
            Минимальный x, удовлетворяющий условию.
    """
    while left < right:
        # Вычисление средней точки
        middle_value = (left + right) // 2
        if feasible(middle_value):
            # Если feasible(middle) = True, то ответ где-то в [left, middle]
            right = middle_value
        else:
            left = middle_value + 1
    return left


def min_max_partition_sum(numbers, subarray_count):
    """
        Находит минимальную максимальную сумму при разбиении массива на k частей.

        Аргументы:
            numbers: Массив чисел
            subarray_count: Количество подмассивов

        Вывод:
            Минимальное значение S, при котором разбиение возможно.
    """
    def feasible(S):
        """Можно ли разбить на ≤k подмассивов с суммой ≤ S?"""
        current_count = 1
        current_sum = 0
        for number in numbers:
            if number > S:
                return False
            if current_sum + number > S:
                current_count += 1
                current_sum = number
                if current_count > subarray_count:
                    return False
            else:
                current_sum += number
        return True
    total_sum = sum(numbers)
    left = (total_sum + subarray_count - 1) // subarray_count
    right = total_sum
    return binary_search(feasible, left, right)

if __name__ == "__main__":
    # Тест
    test_numbers = [7, 2, 5, 10, 8]
    k = 2
    result = min_max_partition_sum(test_numbers, k)
    print('Минимальное S для массива (',*test_numbers,') и k=',k,':', result)

    test_numbers2 = [1, 2, 3, 4, 5]
    k2 = 3
    result2 = min_max_partition_sum(test_numbers2, k2)
    print('Минимальное S для массива (',*test_numbers2,') и k=',k2,':', result2)