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


    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    # def reverseEven(self, k):


ll = Linkedlist()
a = [1, 2, 3, 4, 5]
for i in a:
    ll.create(i)
ll.display()