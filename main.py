import json

from university.structure import Student, GroupOfStudent, Faculty
from university.serializer import FacultySerializer
import os


def passage_from_faculty_to_deposit(group_name):
    if faculty.is_empty():
        return
    while faculty.size() != 0:
        cur_group = faculty.pop()
        if cur_group.group_number == group_name:
            faculty.push(cur_group)
            return cur_group
        save_deposit.push(cur_group)
    # print(f"Группа {group_name} не найдена")
    # return


def passage_from_deposit_to_faculty(group_name):
    if save_deposit.is_empty():
        return
    while save_deposit.size() != 0:
        cur_group = save_deposit.pop()
        if cur_group.group_number == group_name:
            faculty.push(cur_group)
            return cur_group
        faculty.push(cur_group)
    # print(f"Группа {group_name} не найдена")
    # return


def add_student_in_group(student_name, student_age, some_group: GroupOfStudent):
    """Добавление студента в группу"""
    for students in some_group:
        if students.last_name == student_name:
            ans = input(f"\nСтудент {student_name} уже есть в группе, добавить (y/n) ")
            if ans == "y" or "н":
                student = Student(student_name, student_age)
                some_group.add(student)
                print(f"\nСтудент {student_name} добавлен в группу \n")
                return
            elif ans == "n" or "т":
                return
    new_student = Student(student_name, student_age)
    some_group.add(new_student)
    print(f"\nСтудент {student_name} добавлен в группу {some_group.group_number}")


def search_student(student_name, some_group: GroupOfStudent):
    """Поиск студента в группе"""
    for inx, students in enumerate(some_group):
        if students.last_name == student_name:
            return inx, students
    return


def action():
    act = input("Добавить - 1\n"
                "Удалить - 2\n"
                "Изменение данных - 3\n"
                "Назад - 4\n")
    return act


def faculty_act(act):  # Взаимодейстие с факльтетом
    if act == "1":
        print(f"\n{faculty.faculty_name}\n")
    elif act == "2":
        faculty.faculty_name = input("Введите новое название факультета: ").title()
    elif act == "3":
        return


def group_act(act):  # Взаимодейстие с группой
    if act == "4":
        return
    new_group = input("Введите номер группы: ")
    cur_group = passage_from_deposit_to_faculty(new_group) or passage_from_faculty_to_deposit(new_group)
    if act == "1":
        if cur_group:
            print(f"\nГруппа {new_group} уже есть")
            return
        group = GroupOfStudent(new_group)
        faculty.push(group)
        print(f"\nГруппа {new_group} добавлена")
        return
    elif cur_group:
        if act == "2":
            faculty.pop()
            print(f"\nГруппа {new_group} была удалена")
            return
        elif act == "3":
            new_group_number = input("Введите новый номер группы: ")
            cur_group.group_number = new_group_number
            print("Номер группы был изменен")
            return
    else:
        print(f"\nГруппа {new_group} не найдена")


def student_act(act):
    if act == "4":
        return

    student_name = input("Введите фамилию студета: ").title()

    if act == "1":
        student_age = input("Введите возраст студента: ")
        student_group = input("Введите номер группы для добавления студента: ")
        cur_group = passage_from_faculty_to_deposit(student_group) or passage_from_deposit_to_faculty(student_group)
        if cur_group:
            add_student_in_group(student_name, student_age, cur_group)
        else:
            ans = input("Такой группы нет, хотите создать ? (y/n) ")
            if ans == "y" or "н":
                cur_group = GroupOfStudent(student_group)
                student = Student(student_name, student_age)
                cur_group.add(student)
                faculty.push(cur_group)
                print(f"Студент {student_name} добавлен в группу {cur_group.group_number}\n")
            elif ans == "n" or "т":
                return

    elif act == "2":
        student_group = input("Введите номер группы студента для удаления: ")
        cur_group = passage_from_faculty_to_deposit(student_group) or passage_from_deposit_to_faculty(student_group)
        if cur_group:
            cur_student = search_student(student_name, cur_group)
            if cur_student:
                cur_group.pop(cur_student[0])
                print(f"\nСтудент {student_name} был удален\n")
            else:
                print(f"\nСтудент {student_name} не найден\n")
        else:
            print(f"\nГруппа {student_group} не найдена")

    elif act == "3":
        student_group = input("Введите номер группы студента: ")
        cur_group = passage_from_faculty_to_deposit(student_group) or passage_from_deposit_to_faculty(student_group)
        if cur_group:
            cur_student = search_student(student_name, cur_group)[1]
            if cur_student:
                ans = input("\nИзменить фамилию - 1\n"
                            "\nИзменить возраст - 2\n"
                            "\nИзменить все данные - 3 \n")
                if ans == "1":
                    new_student_name = input("Введите фамилию для изменения: ").title()
                    cur_student.last_name = new_student_name
                elif ans == "2":
                    new_age = input("Введите возраст студента для изменения: ")
                    cur_student.age = new_age
                elif ans == "3":
                    new_student_name = input("Введите фамилию для изменения: ").title()
                    new_age = input("Введите возраст студента для изменения: ")
                    cur_student.last_name = new_student_name
                    cur_student.age = new_age
                    print("Данные успешно изменены")
            else:
                print(f"\nСтудент {student_name} не найден\n")
        else:
            print(f"\nГруппа {student_group} не найдена\n")


def display_faculty():
    """Вывод всей структуры"""
    if not save_deposit.size() and not faculty.size():
        print("\nВ факультете пока нет групп\n")
    while save_deposit.size() != 0:
        group = save_deposit.pop()
        faculty.push(group)
    while faculty.size() != 0:
        cur_group = faculty.pop()
        print(f"\nНомер группы: {cur_group.group_number}")
        if not cur_group.is_empty():
            for students in cur_group:
                print(f"[{students.last_name}: {students.age}]", sep=', ', end=' ')
            print()
        else:
            print("В группе пока нет студентов")
        save_deposit.push(cur_group)


def download():
    pass


def save():
    passage_from_deposit_to_faculty(None)
    serializer = FacultySerializer()
    faculty_serialize = serializer.serialize(faculty)
    with open("faculty_data.json", "w", encoding="utf-8") as inf:
        json.dump(faculty_serialize, inf, ensure_ascii=False, indent=3)
    print("\nСохранение завершено успешно")


def choice(user_choice):
    if user_choice == "1":
        print("\nФакультет: ")
        faculty_act(input("Вывести название факультета - 1\n"
                          "Изменить название факультета - 2\n"
                          "Назад - 3\n"))

    elif user_choice == "2":
        print("\nГруппа: ")
        group_act(action())

    elif user_choice == "3":
        print("\nСтудент: ")
        student_act(action())

    elif user_choice == "4":
        display_faculty()

    elif user_choice == "5":
        save()


def main():
    while True:
        user_choice = input("\nФакультет - 1\n"
                            "Группа - 2\n"
                            "Студент - 3\n"
                            "Вывод всей структуры - 4\n"
                            "Сохранение в файл - 5\n"
                            "Завершение работы - 6\n")
        if user_choice == "6":
            ans = input("Сохранить изменения ? (y/n) ")
            if ans == "y" or "н":
                save()
            exit()
        choice(user_choice)


if __name__ == "__main__":
    if os.stat("faculty_data.json").st_size == 0:
        faculty = Faculty(input("Введите название факультета ").title())
    else:
        faculty_serializer = FacultySerializer()
        with open("faculty_data.json") as ouf:
            download_data = json.load(ouf)
        faculty = faculty_serializer.deserialize(download_data)

    save_deposit = Faculty("Save Deposit")
    main()

# TODO описание функций
