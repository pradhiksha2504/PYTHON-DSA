class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.next = None
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

    def display(self):
        temp = self.head
        if self.head is None:
            print("None")
            return
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        # print(temp.data)

    def reverse(self, k):
        self.temp = self.head
        count = 0
        while count < k:
            # print("temp:", self.temp.data)
            self.temp = self.temp.next
            count += 1
        # print(self.temp.data)
        current = self.temp
        # print("current: ", current.data)

        self.prev = None
        self.curr = self.head
        self.next = None
        count = 0
        while self.curr and count<k:
            a = self.curr.next
            self.next = self.curr.next
            self.curr.next = self.prev
            self.prev = self.curr
            self.curr = self.next
            count+=1
        self.head = self.prev
        print("next:", self.next.data)
        # self.prev.next.next= current
        # self.prev = current/
        print("a:", a.data)
        self.display()

        temp = self.curr
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        temp = a


ll = LinkedList()
a = [1, 2, 3, 4, 5]
k = 3
for i in a:
    ll.create(i)
ll.reverse(k)
# ll.display()












