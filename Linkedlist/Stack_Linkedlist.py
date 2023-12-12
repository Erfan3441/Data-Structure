from singlelinkedlist2 import LinkedList
class Stack:
    def __init__(self):
        self.linked_list = LinkedList()
    
    def push(self, data):
        self.linked_list.insert_at_begin(data)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.linked_list.remove_node_at_begin()

    def is_empty(self):
        return self.linked_list.head is None
    
    def peek(self):
        if self.is_empty():
            return None
        return self.linked_list.head.data
    
    def size(self):
        return self.linked_list.size_of_list()

    def print_stack(self):
        self.linked_list.print_list()

 