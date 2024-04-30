global size
size = 4


class CircularQueue:
    def __init__(self):
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % size == self.front:
            print(" Queue is Full\n")
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("QUEUE UNDERFLOW")
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1
        else:
            temp = self.queue[self.front]
            self.front += 1

    def display(self):
        if self.front == -1:
            print("QUEUE IS EMPTY")
        elif self.rear > self.front:
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
        else:
            for i in range(self.front,size):
                print(self.queue[i],end=" ")
            for j in  range(0,self.rear+1):
                print(self.queue[j],end=" ")


ob = CircularQueue()
a = [10, 20, 30, 40]
for i in a:
    ob.enqueue(i)
# ob.display()
ob.dequeue()
# ob.dequeue()
# ob.display()
ob.enqueue(90)
ob.display()
