class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size

    def __hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.__hash(key)
        node = self.table[index]
        if node is None:
            self.table[index] = Node(key, value)
        else:
            while node.next:
                node = node.next
            node.next = Node(key, value)

    def find(self, key):
        index = self.__hash(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def delete(self, key):
        index = self.__hash(key)
        node = self.table[index]
        if node is None:
            return None
        if node.key == key:
            self.table[index] = node.next
            return node.value
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return key
            node = node.next
        return None
    


# hash_table = HashTable(size=10)

# # افزودن اطلاعات به هشترا
# hash_table.insert("name", "John")
# hash_table.insert("age", 25)
# hash_table.insert("city", "New York")

# # جستجو بر اساس کلید
# print("Name:", hash_table.find("name"))  # خروجی: John
# print("Age:", hash_table.find("age"))    # خروجی: 25
# print("City:", hash_table.find("city"))  # خروجی: New York

# # حذف اطلاعات بر اساس کلید
# # deleted_value = hash_table.delete("age")
# # print("Deleted Age:", deleted_value)  # خروجی: 25
