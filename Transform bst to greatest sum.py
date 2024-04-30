"""BST --> GREATEST SUM TREE
SEARCH IN BST
EVEN NODES IN BST"""

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

    def searchNode(self):
        return search(self.root, 2)

    def transform(self):
        transformBST(self.root)
        evenNode(self.root)

    def display(self):
        inorder(self.root)


def search(root, key):
    if root is None:
        return
    if root.data == key:
        return True
    else:
        if key > root.data:
            search(root.right, key)
        else:
            search(root.left, key)
    return False


def evenNode(root):
    if root is None:
        return
    if root.data % 2 == 0:
        global lst
        lst.append(root.data)
    evenNode(root.right)
    evenNode(root.left)


def transformBST(root):
    if root is None:
        return
    transformBST(root.right)
    global add
    add += root.data
    root.data = add - root.data
    transformBST(root.left)
    # return sum


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


tree = Tree()
add = 0
lst = []
# a = [10, 11, 9, 8, 91, 20, 7]
# a = [4, 2, 7, 1, 3, 5, 8]
a = [11, 2, 29, 1, 7, 15, 40, 35]
for i in a:
    tree.insert(i)
res = tree.searchNode()
print(res)
# tree.transform()
tree.display()
print()
# print(lst)
