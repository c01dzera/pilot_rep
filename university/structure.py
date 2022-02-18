from structures.structure_array import StackArray
from structures.structure_linked_list import LinkedList


class Student:
    """ Модель студента университета. """

    def __init__(self, last_name: str, age: str) -> None:
        """ Инициализируются атрибуты класса 'Student':
        фамилия и возраст. """
        self.__last_name = last_name
        self.__age = age

    @property
    def last_name(self) -> str:
        """ Возвращает фамилию студента. """
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        """ Изменяет фамилию студента. """
        self.__last_name = value

    @property
    def age(self) -> str:
        """ Возвращает возраст стуента. """
        return self.__age

    @age.setter
    def age(self, value: str) -> None:
        """ Изменяет возраст студента. """
        self.__age = value


class GroupOfStudent(LinkedList):
    """ Модель группы студентов университета,
     созданной на основе класса 'LinkedList'. """

    def __init__(self, group_number) -> None:
        """ Инициализирум атрибуты группы: номер группы. """
        super().__init__()
        self.__group_number = group_number

    @property
    def group_number(self) -> str:
        """ Возвращает номер группы. """
        return self.__group_number

    @group_number.setter
    def group_number(self, value: str) -> None:
        """ Изменяет номер группы. """
        self.__group_number = value


class Faculty(StackArray):
    """ Модель факультета университета,
     созданной на основе класса 'StackArray' """

    def __init__(self, faculty_name):
        """ Инициализируем артибуты факультета: название факультета. """
        super().__init__()
        self.__faculty_name = faculty_name

    @property
    def faculty_name(self) -> str:
        """ Возвращает название факультета. """
        return self.__faculty_name

    @faculty_name.setter
    def faculty_name(self, value):
        """ Изменяет название факультета. """
        self.__faculty_name = value
