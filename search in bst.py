global a
a = []
class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newnode = Node(data)
        if self.root is None:
            self.root = newnode
        else:
            temp = self.root
            while 1:
                if data < temp.data:
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

    def searchSubtree(self, key):
        temp = self.root
        while 1:
            if temp is None:
                return []
            if temp.data == key:
                root = temp
                res = preorder(root)
                return res
            else:
                if temp.data > key:
                    temp = temp.left
                else:
                    temp = temp.right


def preorder(root):
    if root is not None:
        a.append(root.data)
        preorder(root.left)
        preorder(root.right)
    return a


tree = Tree()
b = [4, 2, 7, 1, 3]
for i in b:
    tree.insert(i)
ans = tree.searchSubtree(7)
print(ans)
