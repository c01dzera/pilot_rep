class LinkedList:
    """ Модель связного спика. """

    class LinkedListElement:
        """ Модель узла связного списка. """
        def __init__(self, value, next_node=None) -> None:
            """ Инициализация атрибутов класса: значение и ссылка на следующий узел """
            self.value = value
            self.next_node = next_node

    class LinkedListIterator:
        """ Модель итератора для связного списка. """
        __current_element = None

        def __init__(self, first_element):
            """ Инициализирутся атрибут итератора, а именно первый элемент списка """
            self.__current_element = first_element

        def __next__(self):
            """ Возвращает слудующий элемент списка если он не пуст, иначе исключение. """
            if self.__current_element is None:
                raise StopIteration

            element = self.__current_element.value
            self.__current_element = self.__current_element.next_node
            return element

    def __init__(self) -> None:
        """ Инициализация первой ссылки (головы) связного списка. """
        self.__head = None

    def clear(self) -> None:
        """ Полное очищение связного списка. """
        self.__head = None

    def is_empty(self) -> bool:
        """ Проверка связного списка на пустоту. """
        return self.__head is None

    def __iter__(self):
        return LinkedList.LinkedListIterator(self.__head)

    def add(self, value):
        """ Добавление элемента в связный список. """
        if self.__head is None:
            self.__head = LinkedList.LinkedListElement(value)

        else:
            current = self.__head
            while current.next_node:
                current = current.next_node
            current.next_node = LinkedList.LinkedListElement(value)

    def insert(self, idx: int, value) -> None:
        """ Добавлние элемента в связный список согласно индексу """
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

    def pop(self, idx=0) -> None or LinkedListElement:
        """ Удаление элемента согласно индесу """
        if self.__head is None:
            return None

        if idx == 0:
            element = self.__head
            self.__head = self.__head.next_node
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
