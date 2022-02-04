"""
Реализации контейнера:
5. Объектная реализация контейнера на основе комбинированной
структуры «Стек-массив динамических списков»

Варианты информационного наполнения контейнера

1.	Задача «Студенческие группы»
	информационные объекты: студенты (свойства – Фамилия, Возраст)
	студенты объединяются в рамках объекта Группа (свойство – Номер)
	группы объединяются в рамках объекта-контейнера Факультет
(свойство – НазваниеФакультета)

"""

from university.structure import Student, GroupOfStudent, Faculty


def passage_from_faculty_to_deposit(group_name):
    if faculty.is_empty():
        print("Факультет пуст")
        return
    while faculty.is_empty():
        cur_group = faculty.pop()
        if cur_group.group_name == group_name:
            faculty.push(cur_group)
            return cur_group
        save_deposit.push(cur_group)
    print(f"Группа {group_name} не найдена")
    return


def passage_from_deposit_to_faculty(group_name):
    if save_deposit.is_empty():
        print("Депозит пуст")
        return
    while save_deposit.is_empty():
        cur_group = save_deposit.pop()
        if cur_group.group_name == group_name:
            faculty.push(cur_group)
            return cur_group
        faculty.push(cur_group)
    print(f"Группа {group_name} не найдена")
    return


def add_student_in_group(student_name, student_age, some_group: GroupOfStudent):
    for students in some_group:
        if students.last_name == student_name:
            ans = input(f"Студент {student_name} уже есть в группе, добавить (y/n)")
            if ans == "y":
                student = Student(student_name, student_age)
                some_group.add(student)
                print(f"Студент {student_name} добавлен в группу \n")
            elif ans == "n":
                return


def search_student(student_name, some_group: GroupOfStudent):
    for inx, students in enumerate(some_group):
        if students.last_name == student_name:
            return inx, students
    return


def action():
    act = input("Добавить - 1\n"
                "Удалить - 2\n"
                "Изменение данных - 3\n")
    return act


def faculty_act(act):  # Взаимодейстие с факльтетом
    if act == "1":
        print(f"\n{faculty.faculty_name}\n")
    elif act == "2":
        faculty.faculty_name = input("Введите новое название факультета: ")


def group_act(act):  # Взаимодейстие с группой
    new_group = input("Введите номер группы: ")
    cur_group = passage_from_deposit_to_faculty(new_group) or passage_from_faculty_to_deposit(new_group)
    if act == "1":
        if cur_group:
            print(f"\nГруппа {new_group} уже есть\n")
            return
        group = GroupOfStudent(new_group)
        faculty.push(group)
        print(f"\nГруппа {new_group} добавлена\n")
        return
    if cur_group:
        if act == "2":
            faculty.pop()
            print(f"\nГруппа {new_group} была удалена\n")
            return
        elif act == "3":
            new_group_number = input("Введите новый номер группы: ")
            cur_group.group_number = new_group_number
            print("Номер группы был изменен")
            return
        return
    return
    # else:
    #     print(f"\nГруппа {new_group} не найдена\n")


def student_act(act):
    student_name = input("Введите фамилию студета: ")

    if act == "1":
        student_age = input("Введите возраст студента: ")
        student_group = input("Введите номер группы для добавления студента: ")
        cur_group = passage_from_faculty_to_deposit(student_group) or passage_from_faculty_to_deposit(student_name)
        if cur_group:
            add_student_in_group(student_name, student_age, cur_group)
        else:
            cur_group = GroupOfStudent(student_group)
            student = Student(student_name, student_age)
            cur_group.add(student)
            faculty.push(cur_group)

    elif act == "2":
        student_group = input("Введите номер группы студента для удаления: ")
        cur_group = passage_from_faculty_to_deposit(student_group) or passage_from_faculty_to_deposit(student_name)
        if cur_group:
            cur_student = search_student(student_name, cur_group)[0]
            if cur_student:
                cur_group.pop(cur_student)
                print(f"\nСтудент {student_name} был удален\n")
            else:
                print(f"\nСтудент {student_name} не найден\n")
        else:
            print(f"\nГруппа {student_group} не найдена\n")

    elif act == "3":
        student_group = input("Введите номер группы студента: ")
        cur_group = passage_from_faculty_to_deposit(student_group) or passage_from_faculty_to_deposit(student_name)
        if cur_group:
            cur_student = search_student(student_name, cur_group)[1]
            if cur_student:
                ans = input("\nИзменить фамилию - 1\n"
                            "\nИзменить возраст - 2\n"
                            "\nИзменить все данные -3 \n")
                if ans == "1":
                    new_student_name = input("Введите фамилию для изменения: ")
                    cur_student.last_name = new_student_name
                elif ans == "2":
                    new_age = input("Введите возраст студента для изменения: ")
                    cur_student.age = new_age
                elif ans == "3":
                    new_student_name = input("Введите фамилию для изменения: ")
                    new_age = input("Введите возраст студента для изменения: ")
                    cur_student.last_name = new_student_name
                    cur_student.age = new_age
            else:
                print(f"\nСтудент {student_name} не найден\n")
        else:
            print(f"\nГруппа {student_group} не найдена\n")


def display_faculty():
    while save_deposit:
        group = save_deposit.pop()
        faculty.push(group)
    while faculty:
        cur_group = faculty.pop()
        print(f"\n{cur_group.group_namber}\n")
        for students in cur_group:
            print(f"[{students.last_name}: {students}]", end=' ')
        save_deposit.push(cur_group)


def download():
    pass


def save():
    pass


def choice(user_choice):
    if user_choice == "1":
        print("\nФакультет: ")
        faculty_act(input("Вывести название факультета - 1\n"
                          "Изменить название факультета - 2\n"))

    elif user_choice == "2":
        print("Группа: ")
        group_act(action())

    elif user_choice == "3":
        print("Студент: ")
        student_act(action())

    elif user_choice == "4":
        display_faculty()


def main():
    while True:
        user_choice = input("Факультет - 1\n"
                            "Группа - 2\n"
                            "Студент - 3\n"
                            "Вывод всей структуры - 4\n"
                            "Сохранение в файл - 5\n"
                            "Завершение работы - 6\n")
        if user_choice == "6":
            exit()
        choice(user_choice)


if __name__ == "__main__":
    if "json файл пуст":
        faculty = Faculty("К.Т")
        save_deposit = Faculty("Save Deposit")
    # else подгрузка с json файла
    main()
