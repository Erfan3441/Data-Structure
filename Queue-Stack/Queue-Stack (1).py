class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, value):
        self.enqueue_stack.append(value)


    def dequeue(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                last_element1 = self.enqueue_stack[-1]
                del self.enqueue_stack[-1]
                self.dequeue_stack.append(last_element1)
        if self.dequeue_stack:
            last_element2 = self.dequeue_stack[-1]
            del self.dequeue_stack[-1]
            return last_element2
        else:
            raise IndexError("Queue is empty")



