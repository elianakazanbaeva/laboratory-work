"""
Имеется информация об учениках младшей школы. Для всех учеников известны:
фамилия, имя и класс. Для учеников 1-х классов дополнительно известна их скорость чтения
(слов в минуту, тип int). Для учеников 4-х классов известны баллы итоговой аттестации
(единый муниципальный тест от 1 до 100 баллов, тип float). Для учеников 2-х и 3-х классов
известны данные итоговой школьной контрольной по математике (оценки от 1 до 10 баллов,
тип float). Написать функцию, позволяющую ввести с клавиатуры данные для одного ученика.
Используя эту функцию, ввести сведения об N учениках и сохранить их в бинарном файле.
Распечатать на экране содержимое данного файла в виде таблицы
"""

import struct

class student_base:
    def __init__(self, last_name, first_name, class_number):
        if not last_name or not first_name:
            raise ValueError("Фамилия и имя не могут быть пустыми")
        if class_number not in (1, 2, 3, 4):
            raise ValueError("Класс должен быть 1, 2, 3 или 4")

        self.last_name = last_name
        self.first_name = first_name
        self.class_number = class_number

    def __str__(self):
        return f"{self.last_name:15} {self.first_name:15} {self.class_number:2}"


class first_grade_student(student_base):
    def __init__(self, last_name, first_name, reading_speed):
        student_base.__init__(self, last_name, first_name, 1)
        if reading_speed <= 0:
            raise ValueError("Скорость чтения должна быть положительным"
                             " числом")
        self.reading_speed = reading_speed

    def __str__(self):
        return (student_base.__str__(self) +
                10 * " " +
                f"Чтение = {self.reading_speed:3} сл/мин")

    def get_value(self):
        return self.reading_speed


class second_third_grade(student_base):

    def __init__(self, last_name, first_name, class_number, math_score):
        student_base.__init__(self, last_name, first_name, class_number)
        if not (1 <= math_score <= 10):
            raise ValueError("Оценка по математике должна быть от 1 до 10")
        self.math_score = math_score

    def __str__(self):
        return (student_base.__str__(self) + 10 * " " +
                f" Математика ={self.math_score:4.1f}")

    def get_value(self):
        return self.math_score

class fourth_grade(student_base):
    def __init__(self, last_name, first_name, final_exam_score):
        student_base.__init__(self, last_name, first_name, 4)
        if not (1 <= final_exam_score <= 100):
            raise ValueError("Баллы итоговой аттестации должны быть"
                             " от 1 до 100")
        self.final_exam_score = final_exam_score

    def __str__(self):
        return (student_base.__str__(self) + 10 * " " +
                f" Аттестация ={self.final_exam_score:5.1f}")

    def get_value(self):
        return self.final_exam_score


class binary_file:
    formats = "25s25sif"

    def __init__(self, file_name):
        self.file_name = file_name
        self.struct_handler = struct.Struct(self.formats)

    def encode_string(self, text):
        # строка в байты (25)
        return text.encode("utf-8")[:25].ljust(25, b"\x00")


    def decode_string(self, raw_bytes):
        return raw_bytes.decode("utf-8").rstrip("\x00")

    def save_students(self, students):
        with open(self.file_name, "wb") as binary_file:
            for student in students:
                additional_value = float(student.get_value())
                packed_data = self.struct_handler.pack(
                    self.encode_string(student.last_name),
                    self.encode_string(student.first_name),
                    student.class_number,
                    additional_value)
                binary_file.write(packed_data)

    def load_students(self):
        loaded_students = []
        with open(self.file_name, "rb") as binary_file:
            while True:
                raw_bytes = binary_file.read(self.struct_handler.size)
                if not raw_bytes:
                    break

                (last_name_bytes, first_name_bytes,
                 class_number, additional_value) = \
                    self.struct_handler.unpack(raw_bytes)

                last_name = self.decode_string(last_name_bytes)
                first_name = self.decode_string(first_name_bytes)

                if class_number == 1:
                    loaded_students.append(
                        first_grade_student(
                            last_name, first_name, int(additional_value)))
                elif class_number in (2, 3):
                    loaded_students.append(
                        second_third_grade(
                            last_name, first_name,
                            class_number, additional_value))

                else:
                    loaded_students.append(fourth_grade(
                        last_name, first_name, additional_value))
        return loaded_students

def input_student():
    last_name = input("Введите фамилию: ").strip()
    first_name = input("Введите имя: ").strip()
    class_number = int(input("Введите номер класса (1-4): "))

    if class_number == 1:
        reading_speed = int(input("Введите скорость чтения (сл/мин): "))
        return first_grade_student(last_name, first_name, reading_speed)

    if class_number in (2, 3):
        math_score = float(input("Введите оценку по математике (1-10): "))
        return second_third_grade(last_name, first_name,
                                  class_number, math_score)

    if class_number == 4:
        final_score = float(input("Введите баллы итоговой аттестации"
                                  " (1-100): "))
        return fourth_grade(last_name, first_name, final_score)
    raise ValueError("Некорректный класс")

def print_table(students):
    print(f"{'-' * 80}")
    print(f"{'Фамилия':15} {'Имя':15} {'Кл':10} {'Доп. информация':40}")
    print(f"{'-' * 80}")

    for student in students:
        print(student)

    print(f"{'-' * 80}")
    print(f"Всего учеников: {len(students)}")
    print()


def run():
    try:
        students_count = int(input("Введите желаемое количество "
                                   "учеников: "))
        if students_count <= 0:
            raise ValueError("Количество учеников должно быть "
                                 "положительным")

        students = []
        for index in range(students_count):
            print(f"Ученик {index + 1} из {students_count}")
            while True:
                try:
                    student = input_student()
                    students.append(student)
                    break
                except ValueError:
                    print(f"Ошибка ввода")
                    print("Повторите ввод для этого ученика")
        file_manager = binary_file("c4.bin")
        file_manager.save_students(students)
        loaded_students = file_manager.load_students()
        print_table(loaded_students)
    except ValueError:
        print(f"Ошибка ввода")
    except FileNotFoundError:
        print("Ошибка: файл не найден")

if __name__ == "__main__":
    run()