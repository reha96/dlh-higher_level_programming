#!/usr/bin/python3
"""Write a class Node that defines a node of a singly linked list

Raises:
    TypeError: _description_
    TypeError: _description_

Returns:
    _type_: _description_
"""


class Node:
    """class Node"""

    def __init__(self, data, next_node=None):
        """initialization

        Args:
            data (_type_): _description_
            next_node (_type_, optional): _description_. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """property def data(self): to retrieve it

        Returns:
            _type_: _description_
        """
        return self.__data

    @data.setter
    def data(self, data):
        """property setter def data(self, value): to set it

        Args:
            data (_type_): _description_

        Raises:
            TypeError: _description_
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """property def next_node(self): to retrieve it

        Returns:
            _type_: _description_
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """property setter def next_node(self, value): to set it

        Args:
            value (_type_): _description_

        Raises:
            TypeError: _description_
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """class SinglyLinkedList that defines a singly linked list"""

    def __init__(self):
        """initialization"""
        self.__head = None

    def sorted_insert(self, value):
        """Public instance method: def sorted_insert(self, value):
        that inserts a new Node into the correct sorted position
        in the list (increasing order)

        Args:
            value (_type_): _description_
        """
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
        if prev is not None:
            prev.next_node = new_node
        new_node.next_node = current

    def __str__(self):
        """printable string

        Returns:
            _type_: _description_
        """
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
