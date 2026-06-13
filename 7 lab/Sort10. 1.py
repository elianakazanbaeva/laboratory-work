# Сортировка вставками
# Временная сложность:
#   -Средний случай: O(n^2)
#   -Худший случай: O(n^2)
# Дополнительная память: O(1)
# Так как сортировка происходит на месте (in-place)
# Является устойчивым алгоритмом

def get_user_input():
    """
    Читает целые числа из файла input.txt.

    Функция открывает файл input.txt в текущей директории и построчно
    считывает целые числа. Пустые строки игнорируются. Все числа добавляются 
    в список.

    Вывод:
        array: Список целых чисел, прочитанных из файла, или None в случае
               ошибки.

    Исключения:
        FileNotFoundError: Если файл input.txt не найден в текущей директории.
        ValueError: Если в файле содержатся данные, которые нельзя
                   преобразовать в целое число.
    """
    try:
        array = []
        with open('input.txt', 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:  # пропускаем пустые строки
                    number = int(line)
                    array.append(number)
        return array
    except FileNotFoundError:
        print('Файл input.txt не найден в текущей директории')
        return None
    except ValueError:
        print('Ошибка: файл input.txt содержит некорректные данные'
              ' (не целые числа)')
        return None


def insertion_sort_with_log(array):
    """
    Сортирует и записывает в файл output.txt массив целых чисел алгоритмом сортировки вставками.

    Алгоритм работает in-place, изменяя исходный массив. На каждой итерации
    берётся текущий элемент и вставляется в отсортированную часть массива
    слева от него, сдвигая большие элементы вправо.

    Аргументы:
        array: Список целых чисел для сортировки.

    Вывод:
        array: Отсортированный список целых чисел, или None если входной
              массив пустой или равен None.
    """
    if array is None or len(array) == 0:
        return None
    len_numbers = len(array)
    file_2 = open('output.txt', 'w', encoding='utf-8')
    with open('protocol.txt', 'w', encoding='utf-8') as file:
        file.write('Начинаем сортировку:\n')
        for i in range(1, len_numbers):
            current = array[i]
            j = i - 1
            while j >= 0 and array[j] > current:
                # Сдвигаем элементы больше текущего вправо
                array[j + 1] = array[j]
                j -= 1
            # Вставляем текущий элемент на правильную позицию
            array[j + 1] = current
            result_parts = []
            for k in range(i + 1): # отсортированная часть
                result_parts.append(str(array[k]))
            result_parts.append('|')
            if i + 1 < len_numbers: # неотсортированную часть (если есть)
                for k in range(i + 1, len_numbers):
                    result_parts.append(str(array[k]))
            file.write(' '.join(result_parts) + '\n')
    for i in range(len_numbers):
        file_2.write(str(array[i]) + '\n')
    file_2.close()
    return array

def main():
    """
    Основная функция программы для сортировки массива из файла input.txt.

    Функция выполняет последовательность действий:
    1. Читает числа из файла input.txt с помощью get_user_input()
    2. Если данные корректны и массив не пустой, сортирует массив с помощью
       insertion_sort_with_log()
    3. Записывает отсортированный массив в файл output.txt с помощью
       write_sorted_array_to_file()
    4. Выводит сообщения о статусе выполнения операции
    """
    user_array = get_user_input()
    if user_array:
        if len(user_array) == 0:
            print('Файл input.txt пуст')
            return

        if insertion_sort_with_log(user_array) is not None:
            print('Сортировка завершена успешно!')
            print('Отсортированные числа записаны в файл output.txt')
    else:
        print('Данные для сортировки не были получены,'
              ' проверьте файл input.txt')


if __name__ == '__main__':
    main()