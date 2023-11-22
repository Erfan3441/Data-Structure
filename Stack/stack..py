class Stack:

    def _init_(self):
        self.values = []


        def push(self, value):
            self.values.append(value)


        def peek(self):
                if not self.Is_empty():
                    return self.values[-1]

                else:
                    return False

        def pop(self):
            if not self.Is_empty():
                element = self.values[-1]
                del self.values[-1]
                return element
            else:
                return False
                
        def Is_empty(self):
            return len(self.values) == 0
        














