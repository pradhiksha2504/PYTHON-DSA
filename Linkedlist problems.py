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

    def evenOdd(self):
        temp = self.head
        while temp:
            if temp.data % 2 == 0:
                print(temp.data, end=" ")
            temp = temp.next

    def length(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def middleElement(self):
        l = self.length()
        print(l)
        mid = l // 2
        print(mid)
        temp = self.head
        for _ in range(mid):
            while temp:
                temp = temp.next
                break
        # print(temp.data)

    def display(self):
        temp = self.head
        while temp.next:
            print(temp.data, end=" ")
            temp = temp.next
        print(temp.data)


ll = Linkedlist()
a = [1, 2, 3, 4, 5, 6, 7]
for i in a:
    ll.create(i)
ll.display()
# ll.evenOdd()
ll.middleElement()
