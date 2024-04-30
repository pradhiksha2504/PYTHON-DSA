class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None


class Deque:
    def  __init__(self):
        self.front = self.rear = None

    def insertionatrear(self, data):
        newnode = Node(data)
        if self.front is None:
            self.front = self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode
            newnode.prev = self.rear
            self.rear.next = None

    def print(self):
        temp = self.front
        whil


q = Deque()
q.insertionatrear(10)

