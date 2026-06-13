'''
 Дан файл  titanic.csv с данными о пассажирах Титаника:
PassengerId — Идентификатор пассажира
Survived — Выжил
Pclass — Класс пассажира
Name — Имя
Sex — Пол
Age — Возраст
SibSp — Число братьев, сестёр или супругов на борту
Parch — Число родителей или детей на борту
Ticket — Номер билета
Fare — Стоимость билета
Cabin — Номер каюты
Embarked — Порт посадки
Считать файл и выполнить следующие действия:
определить и вывести на печать количество выживших пассажиров, средний возраст
выживших, среднюю стоимость билетов выживших пассажиров.
Вывести на печать любые 6 строк этой выборки.
'''

import pandas as pd

# Считываем файл с данными
try:
    # Пытаемся считать файл с разными кодировками, если нужно
    df = pd.read_csv('titanic.csv')
except UnicodeDecodeError:
    # Если возникает ошибка с кодировкой, пробуем другие
    try:
        df = pd.read_csv('titanic.csv', encoding='ISO-8859-1')
    except:
        df = pd.read_csv('titanic.csv', encoding='cp1251')

# Выводим информацию о структуре данных
print("=" * 70)
print("АНАЛИЗ ДАННЫХ О ПАССАЖИРАХ ТИТАНИКА")
print("=" * 70)
print(f"\nВсего записей в файле: {len(df)}")
print(f"Колонки в данных: {list(df.columns)}")

# 1. Количество выживших пассажиров
survived_count = df['Survived'].sum()
print("\n" + "=" * 70)
print("СТАТИСТИКА ПО ВЫЖИВШИМ ПАССАЖИРАМ")
print("=" * 70)
print(f"Количество выживших пассажиров: {survived_count}")
print(f"Общее количество пассажиров: {len(df)}")
print(f"Процент выживших: {survived_count/len(df)*100:.2f}%")

# 2. Средний возраст выживших пассажиров
# Игнорируем пропущенные значения (NaN) при расчете среднего
survived_df = df[df['Survived'] == 1]
average_age_survived = survived_df['Age'].mean()
print(f"\nСредний возраст выживших пассажиров: {average_age_survived:.2f} лет")

# 3. Средняя стоимость билетов выживших пассажиров
average_fare_survived = survived_df['Fare'].mean()
print(f"Средняя стоимость билетов выживших пассажиров: {average_fare_survived:.2f}")

# Выводим дополнительную статистику для контекста
print("\n" + "-" * 70)
print("ДОПОЛНИТЕЛЬНАЯ СТАТИСТИКА:")
print(f"Средний возраст всех пассажиров: {df['Age'].mean():.2f} лет")
print(f"Средняя стоимость билетов всех пассажиров: {df['Fare'].mean():.2f}")
print(f"Минимальный возраст выжившего: {survived_df['Age'].min():.0f} лет")
print(f"Максимальный возраст выжившего: {survived_df['Age'].max():.0f} лет")

# 4. Выводим любые 6 строк выборки выживших пассажиров
print("\n" + "=" * 70)
print("6 СЛУЧАЙНЫХ СТРОК ИЗ ВЫБОРКИ ВЫЖИВШИХ ПАССАЖИРОВ")
print("=" * 70)

# Выбираем 6 случайных строк из выживших
random_survived = survived_df.sample(n=min(6, len(survived_df)), random_state=42)

# Настраиваем отображение pandas для красивого вывода
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 20)

# Выводим выбранные строки с наиболее важными колонками
columns_to_show = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Fare', 'Embarked']
print(random_survived[columns_to_show].to_string(index=False))

# Также покажем первые 6 строк полного датафрейма для сравнения
print("\n" + "=" * 70)
print("ПЕРВЫЕ 6 СТРОК ПОЛНОГО НАБОРА ДАННЫХ")
print("=" * 70)
print(df.head(6).to_string(index=False))

# Дополнительно: аналитика по классам пассажиров
print("\n" + "=" * 70)
print("СТАТИСТИКА ВЫЖИВАЕМОСТИ ПО КЛАССАМ")
print("=" * 70)

for pclass in sorted(df['Pclass'].unique()):
    class_df = df[df['Pclass'] == pclass]
    class_survived = class_df['Survived'].sum()
    class_total = len(class_df)
    print(f"\nКласс {pclass}:")
    print(f"  Всего пассажиров: {class_total}")
    print(f"  Выжило: {class_survived}")
    print(f"  Процент выживших: {class_survived/class_total*100:.2f}%")
    print(f"  Средний возраст: {class_df['Age'].mean():.2f} лет")
    print(f"  Средняя стоимость билета: {class_df['Fare'].mean():.2f}")

# Дополнительно: аналитика по полу
print("\n" + "=" * 70)
print("СТАТИСТИКА ВЫЖИВАЕМОСТИ ПО ПОЛУ")
print("=" * 70)

for sex in df['Sex'].unique():
    sex_df = df[df['Sex'] == sex]
    sex_survived = sex_df['Survived'].sum()
    sex_total = len(sex_df)
    print(f"\n{sex}:")
    print(f"  Всего пассажиров: {sex_total}")
    print(f"  Выжило: {sex_survived}")
    print(f"  Процент выживших: {sex_survived/sex_total*100:.2f}%")

# Информация о пропущенных значениях
print("\n" + "=" * 70)
print("ИНФОРМАЦИЯ О ПРОПУЩЕННЫХ ЗНАЧЕНИЯХ")
print("=" * 70)
print(df.isnull().sum())