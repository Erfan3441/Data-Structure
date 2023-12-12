class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.last = None
        self.size = 0

    def AddToEmpty(self, data):
        if self.last is not None:
            return self.last
        self.last = Node(data)
        self.last.next = self.last
        self.size = 1

    def AddAtBegin(self, data):
        if self.last is None:
            return self.AddToEmpty(data)
        new_node = Node(data)
        new_node.next = self.last.next
        self.last.next = new_node
        self.size += 1
        return self.last

    def AddAtEnd(self, data):
        if self.last is None:
            return self.AddToEmpty(data)
        new_node = Node(data)
        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node
        self.size += 1
        return self.last

    def AddAtIndex(self, data, index):
        if index not in range(self.size + 1):
            return False
        if index == 0:
            self.AddAtBegin(data)
        else:
            current = self.last.next
            for _ in range(index - 1):
                current = current.next
            new_node = Node(data)
            new_node.next = current.next
            current.next = new_node
            if current == self.last:
                self.last = new_node
            self.size += 1
        return True

    def DeleteAtFirst(self):
        if self.last is None:
            return None
        
        removed_data = self.last.next.data
        if self.last.next == self.last:
            self.last = None
        else:
            self.last.next = self.last.next.next
        self.size -= 1
        return removed_data

    def DeleteAtEnd(self):
     if self.last is None:
        return None

     if self.last.next == self.last:
        removed_data = self.last.data
        self.last = None
     else:
        current = self.last.next
        while current.next != self.last:
            current = current.next

        removed_data = self.last.data
        current.next = self.last.next
        self.last = current

     self.size -= 1
     return removed_data

    def DeleteAtIndex(self, index):
        if index not in range(self.size):
            return  None
        if index == 0:
            return self.DeleteAtFirst()
        current = self.last.next
        for _ in range(index - 1):
            current = current.next

        removed_data = current.next.data    
        current.next = current.next.next
        #         اگر عنصر اخر هم حذف بشه اون رو درست میکنه
        if current.next == self.last.next:
            self.last = current
        self.size -= 1
        return removed_data

    def sizeoflist(self):
        return self.size

    def updateNode(self, data, index):
        if index not in range(self.size):
            return False
        current = self.last.next
        for _ in range(index):
            current = current.next
        current.data = data
        return True

    

    def concatenate(self, LinkedList):
     if self.last is None and LinkedList.last is None:
        return None

     if LinkedList.last is None:
        return self.last

     if self.last is None:
        self.last = LinkedList.last
        self.size = LinkedList.size
     else:
        self_last_next, LinkedList_last_next = self.last.next, LinkedList.last.next
        self.last.next = LinkedList_last_next
        LinkedList.last.next = self_last_next
        self.last = LinkedList.last
        self.size += LinkedList.size
     return self.last
    

    def print_list(self):
     if self.last is None:
        print("List is empty.")
        return

     current = self.last.next
     while True:
        print(current.data, end=' ')
        current = current.next
        if current == self.last.next:
            break
    print()  # برای افزودن خط جدید پس از چاپ لیست


