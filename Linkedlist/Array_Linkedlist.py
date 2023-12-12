from singlelinkedlist2 import LinkedList
class Array:
    def __init__(self):
        self.linked_list = LinkedList()

    def insertatindex(self,data,index):
        self.linked_list.insert_at_index(data,index)

    def remove_at_index(self,index):
        self.linked_list.remove_node_at_index(index)

    def Size(self):
        return self.linked_list.size_of_list()
    
    def print_stack(self):
        self.linked_list.print_list()
