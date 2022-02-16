import abc
from university.structure import Student, GroupOfStudent, Faculty


class Serializer(abc.ABC):  # Todo описание методов класса

    @abc.abstractmethod
    def serialize(self, obj):  # превращаем питоновский объект в словарь
        pass

    @abc.abstractmethod
    def deserialize(self, obj):  # превращаем словарь в питоновский объект
        pass


class StudentSerializer(Serializer):

    def serialize(self, obj):
        return {
            "last_name": obj.last_name,
            "age": obj.age
        }

    def deserialize(self, obj):
        return Student(obj["last_name"], obj["age"])


class GroupSerializer(Serializer):
    def serialize(self, obj):
        student_serializer = StudentSerializer()
        result = {
            "group_number": obj.group_number,
            "student_list": []
        }
        for el in obj:
            result["student_list"].append(student_serializer.serialize(el))
        return result

    def deserialize(self, obj):
        student_serializer = StudentSerializer()
        result = GroupOfStudent(obj["group_number"])
        for el in obj["student_list"]:
            result.add(student_serializer.deserialize(el))
        return result


class FacultySerializer(Serializer):
    def serialize(self, obj):
        group_serializer = GroupSerializer()
        result = {
            "faculty_name": obj.faculty_name,
            "groups": []
        }
        new_faculty = Faculty(obj.faculty_name)
        while not obj.is_empty():
            group = obj.pop()
            result["groups"].append(group_serializer.serialize(group))
            new_faculty.push(group)
        while not new_faculty.is_empty():
            obj.push(new_faculty.pop())
        return result

    def deserialize(self, obj):
        group_serializer = GroupSerializer()
        result = Faculty(obj["faculty_name"])
        obj["groups"].reverse()
        for group in obj["groups"]:
            result.push(group_serializer.deserialize(group))
        return result


class FacultyListSerializer(Serializer):
    def serialize(self, obj):
        faculty_serializer = FacultySerializer()
        result = []
        for element in obj:
            result.append(faculty_serializer.serialize(element))
        return result

    def deserialize(self, obj):
        faculty_serializer = FacultySerializer()
        result = []
        for element in obj:
            result.append(faculty_serializer.deserialize(element))
        return result
