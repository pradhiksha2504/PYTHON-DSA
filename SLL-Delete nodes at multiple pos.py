"""Given a position x delete the nodes present in the position of multiples
of x. if x = 2 and length of list is 8, delete the nodes at position 2,4,6,8"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.temp = None

    def create(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.temp = self.head
        else:
            self.temp.next = newnode
            self.temp = newnode

    def length(self):
        self.temp = self.head
        count = 0
        while self.temp:
            count += 1
            self.temp = self.temp.next
        return count

    def multiple(self, y):
        if y == 1:
            self.head = None
            return
        length = self.length()
        lst = []
        for num in range(1, length + 1):
            if num % y == 0:
                lst.append(num)
        b = []
        self.temp = self.head
        count = 1
        for num in lst:
            while self.temp:
                if count == num:
                    b.append(self.temp.data)
                    self.temp = self.temp.next
                    count += 1
                    break
                else:
                    self.temp = self.temp.next
                    count += 1
        for j in b:
            self.deleteData(j)

    def deleteData(self, b):
        self.temp = self.head
        while self.temp.next:
            if self.head.data == b:
                self.head = self.head.next
            if self.temp.next.data == b:
                delete = self.temp.next
                self.temp.next = delete.next
                delete.next = None
                del delete
                break
            else:
                self.temp = self.temp.next

    def display(self):
        temp = self.head
        if self.head is None:
            print("None")
            return
        while temp.next:
            print(temp.data, end=" ")
            temp = temp.next
        print(temp.data)


ll = LinkedList()
# n = int(input("Enter size: "))
# a = list(map(int, input("Enter data: ").split()))
a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in a:
    ll.create(i)
x = int(input("Enter position: "))
print("LINKED LIST BEFORE DELETION")
ll.display()
ll.multiple(x)
print("LINKED LIST AFTER DELETION")
ll.display()
