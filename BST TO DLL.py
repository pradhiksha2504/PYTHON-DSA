class TreeNode:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class ListNode:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None


class Tree:
    def __init__(self):
        self.root = None

    def createBST(self, data):
        newnode = TreeNode(data)
        if self.root is None:
            self.root = newnode
        else:
            temp = self.root
            while 1:
                if temp.data > data:
                    if temp.left is None:
                        temp.left = newnode
                        break
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = newnode
                        break
                    else:
                        temp = temp.right

    # def insertDll(self):
    #     lst = DLL()
    #     convertDLL(self.root, lst)

    def display(self):
        # print("PRINTING TREE ELEMENTS")
        inorder(self.root)


# def convertDLL(root, ll):
#     # print("hi")
#     if root is None:
#         return
#     # ll.display()
#     convertDLL(root.left, ll)
#     ll.createList(root.data)
#     convertDLL(root.right, ll)


class DLL:
    def __init__(self):
        self.head = self.temp = None

    def createList(self, data):
        newnode = ListNode(data)
        if self.head is None:
            self.head = self.temp = newnode
        else:
            self.temp.next = newnode
            newnode.prev = self.temp
            self.temp = newnode
            newnode.next = None

    def display(self):
        temp = self.head
        if temp is None:
            return
        print("PRINTING ELEMENTS IN LINKED LIST")
        while temp.next:
            print(temp.val, end=" ")
            temp = temp.next
        print(temp.val)


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    # print(root.data, end=" ")
    ll.createList(root.data)
    inorder(root.right)


t = Tree()
ll = DLL()
a = [11, 2, 29, 1, 7, 15, 40, 35]
for i in a:
    t.createBST(i)
    # ll.createList(i)
t.display()
# print()
# t.insertDll()
ll.display()
