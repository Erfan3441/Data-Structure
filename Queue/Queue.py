class QueueReplica:
    counter = -1
    queue = list()

    def __init__(self, size):
        for i in range(size):
            self.queue.append(None)
            self.size = size

    def Enqueue(self, value):
        if(self.counter == -1):
            self.counter += 1
            self.queue[self.counter] = value
        elif self.counter == self.size:
            self.Is_full()
        else:
            self.counter += 1
            self.queue[self.counter] = value


    def Dequeue(self):
        if self.counter != -1:
            for i in range(self.size - 1):
                self.queue[i] = self.queue[i + 1]
        else:
            self.Is_empty()

    def Peek(self):
        return self.queue[0]


    def Is_empty(self):
        if self.counter == -1:
            return True
        else:
            return False


    def Is_full(self):
        if self.counter == self.size:
            return True
        else:
            return False

    def Reverse(self):
        return self.queue[::-1]


