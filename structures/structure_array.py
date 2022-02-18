class StackArray:
    """ Модель стэк массива. """
    def __init__(self):
        """ Инициализация пустого стэк массива. """
        self.__lst = []

    def is_empty(self) -> bool:
        """ Проверка стэк массива на пустоту. """
        return not self.__lst

    def push(self, obj) -> None:
        """ Добавление элемента в стэк массив. """
        self.__lst.append(obj)

    def pop(self):
        """ Возвращается элемет с вершины стэк массива если он не пуст, иначе None """
        if self.is_empty():
            return None

        result = self.__lst[-1]
        self.__lst = self.__lst[:-1]
        return result

    def size(self) -> int:
        """ Возвращает количество элементав в стэк массиве """
        return len(self.__lst)
