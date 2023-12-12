class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def remove_at_first(self):
        if self.head is None:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        return removed_data

    def remove_at_end(self):
        if self.head is None:
            return None
        current = self.head
        while current.next:
            current = current.next
        removed_data = current.data
        if current.prev:
            current.prev.next = None
        else:
            self.head = None
        return removed_data

    def remove_at_index(self, index):
        if self.head is None or index < 0:
            return None
        if index == 0:
            return self.remove_at_first()
        current = self.head
        for _ in range(index):
            current = current.next
            if current is None:
                return None
        removed_data  = current.data
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        return removed_data

    def update_node(self, data, index):
        if self.head is None or index < 0:
            return False
        current = self.head
        for _ in range(index):
            current = current.next
            if current is None:
                return False
        current.data = data
        return True

    def size_of_list(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def concatenate(self, other_list):
        if self.head is None:
            self.head = other_list.head
        elif other_list.head is None:
            current = self.head
            while current.next:
                current = current.next
            current.next = other_list.head
            other_list.head.prev = current

        other_list = None    

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Usage:
# Create two lists
list1 = LinkedList()
list2 = LinkedList()

# Add some elements
list1.insert_at_end(1)
list1.insert_at_end(2)
list1.insert_at_end(3)

list2.insert_at_end(4)
list2.insert_at_end(5)
list2.insert_at_end(6)

# Print both lists
print("List 1 before concatenation:")
list1.print_list()

print("List 2 before concatenation:")
list2.print_list()

# Concatenate list2 at the end of list1
list1.concatenate(list2)

# Print the concatenated list
print("List 1 after concatenation:")
list1.print_list()