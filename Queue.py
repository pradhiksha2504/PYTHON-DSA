class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if len(self.queue) <1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.display()
q.dequeue()
q.display()