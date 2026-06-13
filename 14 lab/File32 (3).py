#Дан файл целых чисел, содержащий четное количество элементов.
#Удалить из данного файла первую половину элементов.
#файлы: user1.txt (user1.bin)

import struct
try:
    with open('user1.txt', 'r') as file:
        with open('user1.bin', 'wb') as file1:
            numbers = [int(x) for x in file.readline().replace(',', '').split(' ')]
            for num in numbers:
                file1.write(struct.pack('i', num))

    with open('user1.bin', 'rb') as file:
        data = file.read()

    if len(data) % 4 != 0:
        print('Ошибка: файл повреждён (размер не кратен 4 байтам)')
    else:
        num_elements = len(data) // 4
        if num_elements % 2 == 0:
            all_numbers = struct.unpack(f'{num_elements}i', data)
            second_half = all_numbers[num_elements // 2:]
            with open('user1.bin', 'wb') as file:
                for i in range(len(second_half)):
                    file.write(struct.pack('i', second_half[i]))

            print(f"Первая половина удалена")
            print(f"Оставшиеся числа:", *second_half)
        else:
            print("Ошибка: количество элементов нечётное (нарушено условие задачи)")
except ValueError:
    print('при вводе была допущена ошибка')
'''
1, 2, 3, 4, 5, 6, 7, 8, 9, 10
1, 2, 3
1.4, 1.5, 1.6, 1.7

fbhdth htht ethjrs hteshjr
'''
