class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        self.temp = None

    def create(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = self.temp = newnode
        else:
            self.temp.next = newnode
            self.temp = newnode

    def swap(self, num1, num2):
        prevX = None
        tempX = self.head
        while tempX.data != num1 and tempX != None:
            prevX = tempX
            tempX = tempX.next
        print("previous x: ", prevX)
        print("Temp x: ", tempX.data)
        prevY = None
        tempY = self.head
        while tempY.data != num2 and tempY!=None:
            prevY = tempY
            tempY = tempY.next
        print("previous y: ", prevY.data)
        print("temp y: ", tempY.data)
        if tempY is None or tempX is None:
            return
        if prevX is not None:
            prevX.next = tempY
        else:
            self.head = tempY
        if prevY is not None:
            prevY.next = tempX
        else:
            self.head = tempX
        temp = tempX.next
        tempX.next = tempY.next
        tempY.next = temp
        self.print()

    def print(self):
        self.temp = self.head
        while self.temp:
            print(self.temp.data, end=" ")
            self.temp = self.temp.next


ll = Linkedlist()
a = [1, 2, 3, 4, 5]
x = 1
y = 6
for i in a:
    ll.create(i)
ll.print()
print()
ll.swap(x, y)
