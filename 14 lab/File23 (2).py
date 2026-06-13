#Дан файл вещественных чисел. Создать файл целых чисел, содержащий длины всех
#убывающих последовательностей элементов исходного файла. Например,
# для исходного файла с элементами 1.7, 4.5, 3.4, 2.2, 8.5, 1.2 содержимое
#результирующего файла должно быть следующим: 3, 2
#файлы: user.txt, result.bin

import struct
try:
    with open('user.txt','r') as file:
        with open('user.bin', 'wb') as file1:
            numbers = [float(x) for x in file.readline().replace(',', '').split(' ')]
            for number in numbers:
                file1.write(struct.pack('f', number))

    with open('user.bin', 'rb') as file:
        data = file.read()
    floats = []
    for i in range(0, len(data), 4):
        num = struct.unpack('f', data[i:i + 4])[0]
        floats.append(num)
    lengths = []
    if len(floats) >= 2:
        current_length = 1
        for i in range(1, len(floats)):
            if floats[i] < floats[i - 1]:
                current_length += 1
            else:
                if current_length >= 2:
                    lengths.append(current_length)
                current_length = 1
        if current_length >= 2:
            lengths.append(current_length)
    print('Длины убывающих последовательностей:', *lengths)
    with open('result.bin', 'wb') as file:
        for i in lengths:
            file.write(struct.pack('i', i))
except ValueError :
    print('в файле user.txt введены некорректные данные')
except FileNotFoundError :
    print('файл user.txt не найден')

#8.9, 3.4, 1.2, 1.2, 0.1, 8.9, 7.8, 5.6, 2.9