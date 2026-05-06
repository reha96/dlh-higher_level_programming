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
        else:
            self.__data = data
    
    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        if (
            not isinstance(value, Node) or
            value is not None
            ):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value
            
class SinglyLinkedList:
    def __init__(self):
        pass
    
    def sorted_insert(self, value):
        

# And, write a class SinglyLinkedList that defines a singly linked list by:

#     Private instance attribute: head (no setter or getter)
#     Simple instantiation: def __init__(self):
#     Should be printable:
#     print the entire list in stdout
#     one node number by line
#     Public instance method: def sorted_insert(self, value): that inserts a new Node into the correct sorted position in the list (increasing order)
#     You are not allowed to import any module
