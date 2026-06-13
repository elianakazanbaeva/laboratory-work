#Даны имена четырех файлов. Найти количество файлов с указанными именами,
#которые имеются в текущем каталоге.

user_file = []
count = 0
for i in range(4):
    user_file.append(input('введите имя файла: '))
for name in user_file:
    try:
        with open(name, 'rb') as file:
            count += 1
    except FileNotFoundError:
        pass
    except PermissionError:
        pass
print(count)

#file[1,3,4].bin
#file2.png