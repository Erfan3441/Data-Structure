class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, data, index):
        if index == 0:
            self.insert_at_begin(data)
            return

        new_node = Node(data)
        current_node = self.head
        pos = 0

        while current_node is not None and pos < (index - 1):
            pos += 1
            current_node = current_node.next

        if current_node is None:
            raise Exception("Index not present.")
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def update_node(self, data, index):
        current_node = self.head
        pos = 0

        while current_node is not None and pos != index:
            pos += 1
            current_node = current_node.next

        if current_node is not None:
            current_node.data = data
        else:
            raise Exception("Index not present.")

    def remove_node_at_begin(self):
        if self.head is None:
            return None

        removed_data = self.head.data
        self.head = self.head.next
        return removed_data

    def remove_node_at_end(self):
        if self.head is None:
            return None

        if self.head.next is None:
            removed_data = self.head.data
            self.head = None
            return removed_data

        current_node = self.head
        prev_node = None

        while current_node.next:
            prev_node = current_node
            current_node = current_node.next

        removed_data = current_node.data
        prev_node.next = None
        return removed_data

    def remove_node_at_index(self, index):
        if self.head is None:
            return None

        if index == 0:
            return self.remove_node_at_begin()

        current_node = self.head
        prev_node = None
        pos = 0

        while current_node is not None and pos < index:
            prev_node = current_node
            current_node = current_node.next
            pos += 1

        if current_node is None:
            raise Exception("Index out of bounds.")
            return None

        prev_node.next = current_node.next
        removed_data = current_node.data
        return removed_data

    def size_of_list(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def invert(self):
        current_node = self.head
        prev = None
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
        self.head = prev

    def concatenate(self, linkedlist):
        if self.head is None:
            self.head = linkedlist.head
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = linkedlist.head


    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()    
