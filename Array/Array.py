class Array:

    array = []

    def __init__(self, Maxsize):
        for i in range(Maxsize):
            self.array.append(None)
            self.size = Maxsize


    def Insert(self, value, index):
        if index < self.size:
            self.array[index] = value
            return index
        else:
            return -1

    def Delete(self,index):
        if index < self.size:
            obj =self.array[index]
            self.array[index]=None
            return obj
        else:
            return  None

    def find(self, value):
        for i in range(self.size):
            if self.array[i]==value:
               return i
        return -1