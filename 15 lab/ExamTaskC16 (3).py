"""
На вход подаются сведения о клиентах фитнес-центра. В первой строке
указывается код K одного из клиентов, во второй строке — целое число N, а каждая из
последующих N строк имеет формат
<Продолжительность занятий (в часах)> <Код клиента> <Год> <Номер месяца>
Все данные целочисленные. Значение года лежит в диапазоне от 2000 до 2010, код клиента —
в диапазоне 10–99, продолжительность занятий — в диапазоне 1–30. Для каждого года, в
котором клиент с кодом K посещал центр, определить месяц, в котором продолжительность
занятий данного клиента была наименьшей для данного года (если таких месяцев несколько,
то выбирать месяц с наибольшим номером; месяцы с нулевой продолжительностью занятий не
учитывать). Сведения о каждом годе выводить на новой строке в следующем порядке:
наименьшая продолжительность занятий, год, номер месяца. Упорядочивать сведения по
возрастанию продолжительности занятий, а при равной продолжительности — по
возрастанию номера года. Если данные о клиенте с кодом K отсутствуют, то вывести строку
«Нет данных»
"""
import struct

def validate_visit_data(duration, client_code, year, month):
    if not (1 <= duration <= 30):
        raise ValueError(f"Длительность {duration} вне диапазона 1-30")
    if not (10 <= client_code <= 99):
        raise ValueError(f"Код клиента {client_code} вне диапазона 10-99")
    if not (2000 <= year <= 2010):
        raise ValueError(f"Год {year} вне диапазона 2000-2010")
    if not (1 <= month <= 12):
        raise ValueError(f"Месяц {month} вне диапазона 1-12")


class client_visit:
    def __init__(self, duration, client_code, year, month):
        validate_visit_data(duration, client_code, year, month)
        self.duration = duration
        self.client_code = client_code
        self.year = year
        self.month = month

    def matches(self, client_code):
        return self.client_code == client_code

    def is_better_than(self, other):
        if self.duration < other.duration:
            return True
        if self.duration == other.duration and self.month > other.month:
            return True
        return False

    def __str__(self):
        return f"Продолжительность: {self.duration}, Год: {self.year}, Месяц: {self.month}"

    def to_binary(self, format_string="iiii"):
        return struct.pack(format_string, self.duration, self.client_code, self.year, self.month)

    def from_binary(data, format_string="iiii"):
        if isinstance(data, bytes):
            data = struct.unpack(format_string, data)
        duration, client_code, year, month = data
        return client_visit(duration, client_code, year, month)


def main():
    try:
        with open(input_txt, "r", encoding="utf-8") as text_file:
            lines = [line.strip() for line in text_file.readlines() if line.strip()]

        if len(lines) < 2:
            raise ValueError("Файл должен содержать минимум 2 строки (код клиента и количество)")

        try:
            target_client_code = int(lines[0])
        except ValueError:
            raise ValueError(f"Неверный формат кода клиента: '{lines[0]}'")

        try:
            visits_count = int(lines[1])
        except ValueError:
            raise ValueError(f"Неверный формат количества записей: '{lines[1]}'")

        actual_data_lines = len(lines) - 2
        if actual_data_lines != visits_count:
            raise ValueError(f"Количество строк с данными ({actual_data_lines}) не совпадает с N ({visits_count})")

        visits_list = []
        for line_index, line_content in enumerate(lines[2:], start=3):
            parts = line_content.split()
            if len(parts) != 4:
                raise ValueError(f"Ошибка в строке: ожидалось 4 числа, найдено {len(parts)}")

            try:
                duration = int(parts[0])
                client_code = int(parts[1])
                year = int(parts[2])
                month = int(parts[3])
            except ValueError:
                raise ValueError(f"Ошибка в строке: нечисловое значение")
        try:
            visit = client_visit(duration, client_code, year, month)
            visits_list.append(visit)
        except ValueError:
            raise ValueError(f"Ошибка в строке")

        with open(output, "wb") as binary_file:
            for visit in visits_list:
                binary_file.write(visit.to_binary())

        del visits_list
        loaded_visits_list = []

        with open(output, "rb") as binary_file:
            while True:
                chunk = binary_file.read(data_form.size)
                if len(chunk) < data_form.size:
                    break
                loaded_visits_list.append(client_visit.from_binary(chunk))

        best_visits_by_year = {}
        for visit in loaded_visits_list:
            if not visit.matches(target_client_code):
                continue
            if visit.year not in best_visits_by_year:
                best_visits_by_year[visit.year] = visit
            else:
                current_best = best_visits_by_year[visit.year]
                if visit.is_better_than(current_best):
                    best_visits_by_year[visit.year] = visit

        if not best_visits_by_year:
            print("Нет данных")
        else:
            sorted_results = sorted(best_visits_by_year.values(), key=lambda v: (v.duration, v.year))
            for visit in sorted_results:
                print(visit)

    except FileNotFoundError:
        print("Файл не найден.")
    except ValueError as e:
        print(f"Ошибка данных: {e}")

if __name__ == "__main__":
    input_txt = "input1.txt"
    output = "data.bin"
    data_form = struct.Struct("iiii")
    main()