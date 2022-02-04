class LinkedList:

    class LinkedListElement:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next_node = next_node

    class LinkedListIterator:
        __current_element = None

        def __init__(self, first_element):
            self.__current_element = first_element

        def __next__(self):
            if self.__current_element is None:
                raise StopIteration

            element = self.__current_element.value
            self.__current_element = self.__current_element.next_node
            return element

    def __init__(self):
        self.__head = None

    def clear(self):
        self.__head = None

    def __iter__(self):
        return LinkedList.LinkedListIterator(self.__head)

    def add(self, value):
        if self.__head is None:
            self.__head = LinkedList.LinkedListElement(value)

        else:
            current = self.__head
            while current.next_node:
                current = current.next_node
            current.next_node = LinkedList.LinkedListElement(value)

    def insert(self, idx, value):
        if self.__head is None:
            self.__head = LinkedList.LinkedListElement(value)
            return

        if idx == 0:
            self.__head = LinkedList.LinkedListElement(value, self.__head)
            return

        i = 1
        current = self.__head
        while i != idx and current.next_node:
            current = current.next_node
            i += 1
        prev_next = current.next_node
        current.next_node = LinkedList.LinkedListElement(value, prev_next)

    def pop(self, idx=0):
        if self.__head is None:
            return None

        if idx == 0:
            element = self.__head
            self.__head == self.__head.next_node
            return element.value

        i = 1
        current = self.__head
        while i != idx and current.next_node:
            current = current.next_node
        element = current.next_node
        if element:
            current.next_node = current.next_node.next_node
            return element.value

        return None


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


# class StudentSerializer:
#
#     def serialize(self, obj):
#         return {
#             "last_name": obj.last_name,
#             "age": obj.age
#         }
#
#     def deserialize(self, obj):
#         return Student(obj["last_name"], obj["age"])
#
#
# class GroupOfStudent():
#     def serialize(self, obj):
#         student_serializer = StudentSerializer()
#         result = {
#             "last_name": obj.last_name,
#             "student_list": []
#         }
#         for el in obj:
#             result["student_list"].append(student_serializer.serialize(el))
#         return result
#
# student1 = Student("Van", 14)
# group = GroupOfStudent()
#
# group.serialize(LinkedList)