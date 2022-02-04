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
