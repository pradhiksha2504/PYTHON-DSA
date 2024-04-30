global size
size = 4


class Queue:
    def __init__(self):
        self.queue = []

    def insertRear(self, data):
        if len(self.queue) > size:
            print("OVERFLOW")
        else:
            self.queue.append(data)

    def insertFront(self, data):
        if len(self.queue) == size:
            print("OVERFLOW")
        else:
            self.queue.insert(0, data)

    def deleteRear(self):
        if len(self.queue) == 0:
            print("UNDERFLOW")
        else:
            key = self.queue.pop()
            print("DELETED ELEMENT: ", key)

    def deleteFront(self):
        if len(self.queue) == 0:
            print("UNDERFLOW")
        else:
            key = self.queue.pop(0)
            print("DELETED ELEMENT: ", key)

    def display(self):
        if len(self.queue) == 0:
            print("QUEUE IS EMPTY")
        else:
            print(*self.queue)


q = Queue()
a = [10, 20, 5, 15, 30]
for i in a:
    q.insertRear(i)
q.display()
q.insertFront(40)
q.display()
q.deleteFront()
q.display()
q.deleteRear()
q.display()
