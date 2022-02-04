import abc

from university.structure import Student, GroupOfStudent, Faculty


class Serializer(abc.ABC):

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
            "name": obj.name,
            "student_list": []
        }
        for el in obj:
            result["student_list"].append(student_serializer.serialize(el))
        return result

    def deserialize(self, obj):
        student_serializer = StudentSerializer()
        result = GroupOfStudent(obj["name"])
        for el in obj["student_list"]:
            result.add(student_serializer.deserialize(el))
        return result


class FacultySerializer(Serializer):
    def serialize(self, obj):
        group_serializer = GroupSerializer()
        result = {
            "name": obj.name,
            "groups": []
        }
        new_faculty = Faculty(obj.name)
        while not obj.is_empty():
            group = obj.pop()
            result["group"].append(group_serializer.serialize(group))
            new_faculty.push(group)
        while not new_faculty.is_empty():
            obj.push(new_faculty.pop())
        return result

    def deserialize(self, obj):
        group_serializer = GroupSerializer()
        result = Faculty(obj["name"])
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
