class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.delete = None
        self.head = None
        self.temp = None

    def insertbeg(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.head.next = self.head
            self.temp = self.head
        else:
            self.temp = self.head.next
            while self.temp.next != self.head:
                self.temp = self.temp.next
            self.temp.next = newnode
            newnode.next = self.head
            self.head = newnode

    def insertend(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.head.next = self.head
            self.temp = self.head
        else:
            self.temp.next = newnode
            self.temp = newnode
            newnode.next = self.head

    def deleteend(self):
        if self.head is None:
            return "LINKED LIST  IS  EMPTY"
        else:
            length = self.length()
            if length == 1:
                self.head = None
            else:
                self.temp = self.head.next
                while self.temp.next != self.head:
                    self.temp = self.temp.next
                self.delete = self.temp
                print("delete: ", self.delete.data)



    def length(self):
        count = 1
        self.temp = self.head.next
        while self.temp != self.head:
            count += 1
            self.temp = self.temp.next
        return count

    def print(self):
        if self.head is None:
            return "LINKED LIST IS EMPTY"
        else:
            self.temp = self.head
            print(self.temp.data, end=' ')
            self.temp = self.head.next
            while self.temp != self.head:
                print(self.temp.data, end=' ')
                self.temp = self.temp.next


ll = Linkedlist()
# a = [1, 2, 3, 4, 5]
a = [1, 2, 3]
for i in a:
    ll.insertend(i)
# ll.insertbeg(8)
ll.deleteend()
ll.print()
