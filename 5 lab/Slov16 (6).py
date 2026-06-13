#Получить фамилии детей данного детского сада, которые родились в указанном
# месяце; вывести также их возраст и группу.
def main_simple(children):
    print('Детский сад "Золотой ключик":')
    for surname in children:
        age = children[surname]['возраст']
        group = children[surname]['группа']
        birthmonth = children[surname]['месяц_рождения']
        print('Фамилия:', surname,', возраст:', age,', месяц рождения:', birthmonth,', группа:', group)
    try:
        month = int(input('Введите месяц рождения (1-12): '))
        if month >= 1 or month <= 12:
            print('Дети, родившиеся в', month, 'месяце:')
            count = 0
            for surname in children:
                month_child = children[surname]['месяц_рождения']
                group = children[surname]['группа']
                age = children[surname]['возраст']
                if month_child == month:
                    print('Фамилия:', surname,', возраст:', age,', группа:', group)
                    count=1
            if count == 0:
                print('Таких детей нет')
        else:
            print('Такого месяца не существует')
    except ValueError:
        print('Такого месяца не существует')

kindergarden = {
        'Иванов': {'возраст': 6, 'месяц_рождения': 5, 'группа': 'Солнышко'},
        'Петров': {'возраст': 5, 'месяц_рождения': 3, 'группа': 'Ромашка'},
        'Сидорова': {'возраст': 6, 'месяц_рождения': 12, 'группа': 'Солнышко'},
        'Кузнецов': {'возраст': 5, 'месяц_рождения': 5, 'группа': 'Ромашка'},
        'Смирнова': {'возраст': 4, 'месяц_рождения': 8, 'группа': 'Капелька'},
}
main_simple(kindergarden)