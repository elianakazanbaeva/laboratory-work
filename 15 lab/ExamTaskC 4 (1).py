# <номер месяца> <год> <код клиента> <продолжительность занятий (в часах)>
# найти строку исходных данных с максимальной продолжительностью занятий.
# вывести эту продолжительность, а также соответствующие ей год и номер месяца (в указанном порядке).
# если имеется несколько строк с максимальной продолжительностью, то вывести данные, соответствующие самой поздней дате.
import struct

class fitness_record:
    struct_format = "iiii"
    struct_size = struct.calcsize(struct_format)

    def __init__(self, month, year, client, duration):
        if not (1 <= month <= 12):
            raise ValueError(f"месяц {month} вне диапазона 1..12")
        if not (2000 <= year <= 2010):
            raise ValueError(f"год {year} вне диапазона 2000..2010")
        if not (10 <= client <= 99):
            raise ValueError(f"код клиента {client} вне диапазона 10..99")
        if not (1 <= duration <= 30):
            raise ValueError(f"продолжительность {duration} вне диапазона 1..30")

        self.month = month
        self.year = year
        self.client = client
        self.duration = duration

    def pack(self):
        return struct.pack(self.struct_format, self.month, self.year, self.client, self.duration)

    def unpack(data):
        m, y, c, d = struct.unpack(fitness_record.struct_format, data)
        return fitness_record(m, y, c, d)

    def date_tuple(self):
        return (self.year, self.month)


class binary_file:
    def __init__(self, filename):
        self.filename = filename

    def save(self, records):
        with open(self.filename, "wb") as file:
            for rec in records:
                file.write(rec.pack())

    def load(self):
        records = []
        with open(self.filename, "rb") as file:
            while True:
                data = file.read(fitness_record.struct_size)
                if not data:
                    break
                records.append(fitness_record.unpack(data))
        return records


def find_best(records):
    if not records:
        raise ValueError("список записей пуст")
    best = records[0]
    for rec in records[1:]:
        if rec.duration > best.duration:
            best = rec
        elif rec.duration == best.duration:
            if rec.date_tuple() > best.date_tuple():
                best = rec
    return best


def read_from_txt(filename):
    records = []
    with open(filename, "r") as file:
        lines = file.readlines()

    if not lines:
        raise ValueError("файл input.txt пуст")

    try:
        count = int(lines[0].strip())
    except ValueError:
        raise ValueError("некорректное количество записей")

    if count <= 0:
        raise ValueError("количество записей должно быть > 0")

    if len(lines) < count + 1:
        raise ValueError(f"недостаточно строк в файле (ожидалось {count}, есть {len(lines) - 1})")

    for i in range(1, count + 1):
        parts = lines[i].strip().split()
        if len(parts) != 4:
            raise ValueError(f"строка {i}: ожидалось 4 числа, получено {len(parts)}")
        try:
            m, y, c, d = map(int, parts)
        except ValueError:
            raise ValueError(f"строка {i}: некорректный формат числа")
        records.append(fitness_record(m, y, c, d))

    return records


def main():
    try:
        records = read_from_txt("input.txt")
        fm = binary_file("c4.bin")
        fm.save(records)
        loaded = fm.load()
        result = find_best(loaded)
        print(f"продолжительность занятий: {result.duration} ч.")
        print(f"год: {result.year}")
        print(f"месяц: {result.month}")

    except FileNotFoundError:
        print("ошибка файла")
    except ValueError as e:
        print("ошибка данных:", e)


if __name__ == "__main__":
    main()