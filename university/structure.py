from structures.structure_array import StackArray
from structures.structure_linked_list import LinkedList


class Student:

    def __init__(self, last_name, age):
        self.__last_name = last_name
        self.__age = age

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value


class GroupOfStudent(LinkedList):

    def __init__(self, group_number):
        super().__init__()
        self.__group_number = group_number

    @property
    def group_number(self):
        return self.__group_number

    @group_number.setter
    def group_number(self, value):
        self.__group_number = value


class Faculty(StackArray):

    def __init__(self, faculty_name):
        super().__init__()
        self.__faculty_name = faculty_name

    @property
    def faculty_name(self):
        return self.__faculty_name

    @faculty_name.setter
    def faculty_name(self, value):
        self.__faculty_name = value
