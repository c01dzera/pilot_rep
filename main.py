import json
from university.structure import Student, GroupOfStudent, Faculty
from university.serializer import FacultySerializer
import os


def passage_from_faculty_to_deposit(group_name: str, faculty: Faculty, save_deposit: Faculty) -> None or GroupOfStudent:
    """
    Поиск группы, перемещая группы из стэка 'faculty' в стэк 'save_deposit',
    возвращает искомую группу, иначе перемещает все группы в стэк 'save_deposit'.
    """
    if faculty.is_empty():
        return
    while faculty.size() != 0:
        cur_group = faculty.pop()
        if cur_group.group_number == group_name:
            faculty.push(cur_group)
            return cur_group
        save_deposit.push(cur_group)


def passage_from_deposit_to_faculty(group_name: str, faculty: Faculty, save_deposit: Faculty) -> None or GroupOfStudent:
    """
    Поиск группы, перемещая группы из стэка 'save_deposit' в стэк 'faculty',
    возвращает искомую группу, иначе перемещает все группы в стэк 'faculty'.
    """
    if save_deposit.is_empty():
        return
    while save_deposit.size() != 0:
        cur_group = save_deposit.pop()
        if cur_group.group_number == group_name:
            faculty.push(cur_group)
            return cur_group
        faculty.push(cur_group)


def add_student_in_group(student_name: str, student_age: str, some_group: GroupOfStudent) -> None:
    """ Добавление студента в группу. """
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


def search_student(student_name: str, some_group: GroupOfStudent) -> (int, Student) or None:
    """ Поиск студента в группе. """
    for inx, students in enumerate(some_group):
        if students.last_name == student_name:
            return inx, students
    return


def action() -> str:
    """ Передает выбор пользователя. """
    act = input("Добавить - 1\n"
                "Удалить - 2\n"
                "Изменение данных - 3\n"
                "Назад - 4\n")
    return act


def faculty_act(act: str, faculty: Faculty) -> None:
    """ Производит взаимодействие со стэком 'faculty'. """
    if act == "1":
        print(f"\n{faculty.faculty_name}\n")
    elif act == "2":
        faculty.faculty_name = input("Введите новое название факультета: ").title()
    elif act == "3":
        return


def group_act(act: str, faculty: Faculty, save_deposit: Faculty):
    """ Производит взаимодействие с группой студентов. """
    if act == "4":
        return
    new_group = input("Введите номер группы: ")
    cur_group = passage_from_deposit_to_faculty(new_group, faculty, save_deposit) \
        or passage_from_faculty_to_deposit(new_group, faculty, save_deposit)

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


def student_act(act: str, faculty: Faculty, save_deposit: Faculty) -> None:
    """ Производит взаимодействие со студентом. """

    student_name = input("Введите фамилию студета: ").title()

    if act == "1":
        student_age = input("Введите возраст студента: ")
        student_group = input("Введите номер группы для добавления студента: ")

        cur_group = passage_from_faculty_to_deposit(student_group, faculty, save_deposit) \
            or passage_from_deposit_to_faculty(student_group, faculty, save_deposit)

        if cur_group:
            add_student_in_group(student_name, student_age, cur_group)
            return
        else:
            ans = input("Такой группы нет, хотите создать ? (y/n) ")
            if ans == "y" or "н":
                cur_group = GroupOfStudent(student_group)
                student = Student(student_name, student_age)
                cur_group.add(student)
                faculty.push(cur_group)
                print(f"\nСтудент {student_name} добавлен в группу {cur_group.group_number}")
                return
            elif ans == "n" or "т":
                return

    student_group = input(f"Введите номер группы {'для удаления' if act == '2' else 'для поиска'} студента: ")
    cur_group = passage_from_faculty_to_deposit(student_group, faculty, save_deposit) \
        or passage_from_deposit_to_faculty(student_group, faculty, save_deposit)

    if act == "2" or act == "3":
        if cur_group:
            if act == "2":
                cur_student = search_student(student_name, cur_group)
                if cur_student:
                    cur_group.pop(cur_student[0])
                    print(f"\nСтудент {student_name} был удален")
                else:
                    print(f"\nСтудент {student_name} не найден")

            else:
                cur_student = search_student(student_name, cur_group)[1]
                if cur_student:
                    ans = input("Изменить фамилию - 1\n"
                                "Изменить возраст - 2\n"
                                "Изменить все данные - 3 \n")
                    if ans == "1":
                        new_student_name = input("Введите фамилию для изменения: ").title()
                        cur_student.last_name = new_student_name
                        print("\n")
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
                    print(f"\nСтудент {student_name} не найден")
        else:
            print(f"\nГруппа {student_group} не найдена")


def display_faculty(faculty: Faculty, save_deposit: Faculty) -> None:
    """ Вывод всей структуры. """
    if not save_deposit.size() and not faculty.size():
        print("\nВ факультете пока нет групп")
        return
    passage_from_deposit_to_faculty("-1", faculty, save_deposit)
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


def download() -> (Faculty, Faculty, FacultySerializer):
    """ Загрузка данных с файла .json. """
    save_deposit = Faculty("Save Deposit")
    serializer = FacultySerializer()
    if os.stat("faculty_data.json").st_size == 0:
        faculty = Faculty(input("Введите название факультета ").title())
    else:
        with open("faculty_data.json") as ouf:
            download_data = json.load(ouf)
        faculty = serializer.deserialize(download_data)
    return faculty, save_deposit, serializer


def save(serializer: FacultySerializer, faculty: Faculty, save_deposit: Faculty) -> None:
    """ Сохранение данных в файл .json. """
    passage_from_deposit_to_faculty("-1", faculty, save_deposit)
    faculty_serialize = serializer.serialize(faculty)
    with open("faculty_data.json", "w", encoding="utf-8") as inf:
        json.dump(faculty_serialize, inf, ensure_ascii=False, indent=3)
    print("\nСохранение завершено успешно")


def choice(user_choice: str, faculty: Faculty, save_deposit: Faculty, serializer: FacultySerializer):
    """ Реализуется выбор пользователя. """
    if user_choice == "1":
        print("\nФакультет: ")
        faculty_act(input("Вывести название факультета - 1\n"
                          "Изменить название факультета - 2\n"
                          "Назад - 3\n"), faculty)

    elif user_choice == "2":
        print("\nГруппа: ")
        group_act(action(), faculty, save_deposit)

    elif user_choice == "3":
        print("\nСтудент: ")
        student_act(action(), faculty, save_deposit)

    elif user_choice == "4":
        display_faculty(faculty, save_deposit)

    elif user_choice == "5":
        save(serializer, faculty, save_deposit)


def main():
    """
    Запускает пользовательский интерфейс, в зависимости от выбора
    пользователяб передает данные следющим функциям.
    """
    faculty, save_deposit, serializer = download()
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
                save(serializer, faculty, save_deposit)
            exit()
        choice(user_choice, faculty, save_deposit, serializer)


if __name__ == "__main__":
    main()
