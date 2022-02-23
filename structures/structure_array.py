class StackArray:
    """ Модель стэк массива. """
    def __init__(self):
        """ Инициализация пустого стэк массива. """
        self.__stack = []

    def is_empty(self) -> bool:
        """ Проверка стэк массива на пустоту. """
        return not self.__stack

    def push(self, obj) -> None:
        """ Добавление элемента в стэк массив. """
        self.__stack.append(obj)

    def pop(self):
        """ Возвращается элемет с вершины стэк массива если он не пуст, иначе None """
        if self.is_empty():
            return None

        result = self.__stack[-1]
        self.__stack = self.__stack[:-1]
        return result

    def size(self) -> int:
        """ Возвращает количество элементав в стэк массиве """
        return len(self.__stack)

    def clear(self) -> None:
        """ Полное очищение стэк массива. """
        self.__stack = []