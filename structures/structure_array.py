class StackArray:

    def __init__(self, elements=None):
        if isinstance(elements, list):
            self.__lst = elements.copy()
        else:
            self.__lst = []

    def is_empty(self):
        return not self.__lst

    def push(self, obj):
        self.__lst.append(obj)

    def pop(self):
        if self.is_empty():
            return None

        result = self.__lst[-1]
        self.__lst = self.__lst[:-1]
        return result
