# Даны три файла вещественных чисел с именами S1, S2 и S3, элементы которых
# упорядочены по убыванию. Объединить эти файлы в новый файл с именем S4 так,
# чтобы его элементы также оказались упорядоченными по убыванию.

import struct

try:
    txt_files = ['S1.txt', 'S2.txt', 'S3.txt']
    bin_files = ['S1.bin', 'S2.bin', 'S3.bin']
    all_numbers = []
    for txt_name, bin_name in zip(txt_files, bin_files):
        with open(txt_name, 'r') as file:
            with open(bin_name, 'wb') as file_bin:
                content = file.read().replace(',', '.')
                numbers = [float(x) for x in content.split()]
                numbers.sort()
                numbers.reverse()
                print(bin_name,':', *numbers)
                for number in numbers:
                    file_bin.write(struct.pack('d', number))

    for filename in bin_files:
        with open(filename, 'rb') as file_bin:
            data = file_bin.read()
            for i in range(0, len(data), 8):
                num = data[i:i + 8]
                if len(num) == 8:
                    num = struct.unpack('d', num)[0]
                    all_numbers.append(num)
    all_numbers.sort()
    all_numbers.reverse()
    with open('S4.bin', 'wb') as file_out:
        for number in all_numbers:
            file_out.write(struct.pack('d', number))
    print('S4.bin:', *all_numbers)

except FileNotFoundError:
    print('Ошибка: один из файлов отсутствует или отсутствую данные')
except ValueError:
    print('Ошибка: в файлах с данными есть ошибка (некорректное число)')