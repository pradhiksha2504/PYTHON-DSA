class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.prev = None
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
        # print("Length = ", count)
        return count

    # def remove(self, n):
    #     self.temp = self.head
    #     count = 1
    #     print(n)
    #     while count < n-1:
    #         print(n)
    #         self.temp = self.temp.next
    #         count += 1
    #     self.delete = self.temp.next
    #     self.delete.next = None
    #     del self.delete
    #     if self.temp.next is None:
    #         return head
    #     else:
    #         while self.temp.next:
    #             temp.next = temp.next.next
    #             break

    def middle(self, size):
        mid = size // 2
        count = 0
        self.temp = self.head
        while self.temp.next:
            if count == mid:
                print("middle element: ", self.temp.data)
                break
            else:
                count += 1
                self.temp = self.temp.next

    def nth(self, n):
        self.temp = self.head
        count = 0
        while self.temp:
            if count == n-1:
                print("Nth element: ", self.temp.data)
                break
            else:
                self.temp = self.temp.next
                count += 1


    def reverse(self):
        self.prev = None
        self.curr = self.head
        self.next = None
        while self.curr.next:
            self.next = self.curr.next
            self.curr.next = self.prev
            self.prev = self.curr
            self.curr = self.next
        self.head = self.prev
        # print("next:",self.curr.data)

    def print(self):
        self.temp = self.head
        while self.temp:
            print(self.temp.data, end=" ")
            self.temp = self.temp.next


ll = LinkedList()
a = [1,2,3,4,5]
n = len(a)
# m = int(input("Enter nth position: "))
for i in a:
    ll.create(i)
# ele = n - m + 1
# # print(ele)
# ll.nth(ele)
ll.print()
print()
# l = ll.length()
# # print(l)
ll.middle(n)
# ll.reverse()
# print("reverse")
# ll.print()

# ll.remove(ele)
ll.print()
