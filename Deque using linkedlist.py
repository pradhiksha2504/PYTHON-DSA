class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def underflow(self):
        temp = self.front
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def insertionatrear(self, data):
        newnode = Node(data)
        if self.front is None:
            self.front = self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode
        print("QUEUE ELEMENTS AFTER INSERTION")
        self.print()

    def insertionatfront(self, data):
        newnode = Node(data)
        if self.front is None:
            self.front = self.rear = newnode
        else:
            newnode.next = self.front
            self.front = newnode
        print("QUEUE ELEMENTS AFTER INSERTION")
        self.print()

    def deletionatrear(self):
        if self.underflow() == 0:
            print("UNDERFLOW")
        elif self.front is self.rear:
            self.front=None
            self.rear=None

        else:
            temp = self.front
            prev = temp
            while temp.next:
                prev = temp
                temp = temp.next
            self.rear = prev
            prev.next = None
            temp = None
        print("QUEUE ELEMENTS AFTER DELETION")
        self.print()

    def deletionatfront(self):
        if self.underflow() == 0:
            print("UNDERFLOW")
        else:
            self.front = self.front.next
        print("QUEUE ELEMENTS AFTER DELETION")
        self.print()

    def print(self):
        temp = self.front
        if self.front is None:
            print("No elements in the queue")
        else:
            # print("QUEUE ELEMENTS")
            while temp.next:
                print(temp.data, end=" ")
                temp = temp.next
            print(temp.data)


q = Queue()
print("QUEUE USING SINGLY LINKED LIST IMPLEMENTATION")
while 1:
    print("""
1. Insertion at Front
2. Insertion at Rear
3. Deletion at Front
4. Deletion at Rear
5. Display
6. Exit
""")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        n = int(input("Enter data to insert: "))
        q.insertionatfront(n)
    elif ch == 2:
        n = int(input("Enter data to insert: "))
        q.insertionatrear(n)
    elif ch == 3:
        q.deletionatfront()
    elif ch == 4:
        q.deletionatrear()
    elif ch == 5:
        q.print()
    elif ch == 6:
        exit()
    else:
        print("ENTER VALID INPUT")
