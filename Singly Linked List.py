class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.delete = None
        self.forw = None
        self.head = None
        self.prev = None
        self.temp = None

    def insertbeg(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.temp = self.head
        else:
            newnode.next = self.head
            self.head = newnode
            self.temp = self.head

    def insertmid(self, data, pos):
            newnode = Node(data)
            self.temp = self.head
            count = 0
            while self.temp:
                # print(self.temp.data,count)
                self.temp = self.temp.next
                count += 1
            if count == 0:
                print("LINKED LIST IS EMPTY")
            else:
                self.temp = self.head
                count = 0
                while self.temp:
                    count += 1
                    if count == pos-1:
                        self.forw = self.temp.next
                        self.temp.next = newnode
                        self.temp = newnode
                        self.temp.next = self.forw
                    else:
                        self.temp = self.temp.next

    def insertend(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.temp = self.head
        else:
            self.temp = self.head
            while self.temp.next:
                self.temp = self.temp.next
            self.temp.next = newnode
            self.temp = newnode
            print(self.temp.data)

    def deletebeg(self):
        self.temp = self.head
        self.head = self.head.next
        self.temp = None

    def deletemid(self, pos):
        self.temp = self.head
        count = 0
        while self.temp:
            # print(self.temp.data,count)
            self.temp = self.temp.next
            count += 1
        if count == 0:
            print("LINKED LIST IS EMPTY")
        elif count == 1:
            self.head = None
        else:
            self.temp = self.head
            count = 1
            while count < pos-1:
                self.temp = self.temp.next
                count += 1
            # print(self.temp.data)
            self.delete = self.temp.next
            self.temp.next = self.temp.next.next
            # print(self.delete.data)
            self.delete.next = None
            del self.delete
            self.temp = self.temp.next.next

    def deleteEnd(self):
        self.temp = self.head
        while self.temp.next:
            # print("de", self.temp.data)
            self.prev = self.temp
            self.temp = self.temp.next
        self.prev.next = None
        self.temp = None
        # print(self.temp.data)

    def print(self):
        self.temp = self.head
        while self.temp:
            print(self.temp.data, end=' ')
            self.temp = self.temp.next


ll = LinkedList()
print("LINKED LIST IMPLEMENTATION")
while 1:
    print("""
1. Insertion at beg
2. Insertion at middle
3. Insertion at end
4. Delete at start
5. Delete at middle
6. Delete at end
7. Display
8. Exit
""")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        num = int(input("Enter data: "))
        ll.insertbeg(num)
    elif ch == 2:
        num = int(input("Enter data: "))
        x = int(input("Enter position to insert: "))
        ll.insertmid(num, x)
    elif ch == 3:
        num = int(input("Enter data: "))
        ll.insertend(num)
    elif ch == 4:
        ll.deletebeg()
    elif ch == 5:
        x = int(input("Enter position to delete: "))
        ll.deletemid(x)
    elif ch == 6:
        ll.deleteEnd()
    elif ch == 7:
        print("PRINTING LINKED LIST ELEMENTS")
        ll.print()
    elif ch == 8:
        exit()
    else:
        print("Invalid input")
    print()
