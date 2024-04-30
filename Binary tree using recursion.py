class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None


class Tree:
    def __init__(self):
        self.root=None
        self.temp=None

    def create(self, data):
        newnode=data
        self.root = self.insert(self.root,newnode)

    def insert(self,root,newnode):
        if root is None:
            root = Node(data)
        elif root.data > newnode:
            root.left = self.insert(root.left, newnode)
        elif root.data < data:
            root.right = self.insert(root.right, newnode)

        return root

    def print(self):
        preorder(self.root)

def preorder(root):
    if root is not None:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)


obj = Tree()
a = [1, 2, 3, 4, 5, 6]
for i in a:
    obj.create(i)
# n=int(input("enter no of datas:"))
# for i in range(n):
#     data= int(input("enter data:"))
#     b.create(data)
obj.print()
