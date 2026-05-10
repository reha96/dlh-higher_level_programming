#!/usr/bin/python3


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
            return

        if new_node.data <= self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        prev = None
        while current is not None and new_node.data > current.data:
            prev = current
            current = current.next_node

        prev.next_node = new_node
        new_node.next_node = current

    def __str__(self):
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(1)
    sll.sorted_insert(0)
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    sll.sorted_insert(90)
    print(sll)