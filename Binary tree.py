class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
    def height(self):
        h = tree_height(self.root)
        return h
        # print(h)

    def insert(self, data):
        newnode = Node(data)
        if self.root is None:
            self.root = newnode
        else:
            temp = temp1 = self.root
            flag = 0
            while 1:
                if temp.left is None:
                    temp.left = newnode
                    break
                elif temp.right is None:
                    temp.right = newnode
                    break
                elif flag == 0:
                    #to move the temp to the next level on the left side
                    temp = temp1.left
                    flag = 1
                else:
                    temp = temp1.right
                    flag = 0
                    temp1 = temp1.left

    def print(self):
        print("Pre-Order:", end=" ")
        preorder(self.root)
        print("\nIn-Order:",end=" ")
        inorder(self.root)
        print("\nPost-Order:", end=" ")
        postorder(self.root)

    def deleteChild(self, key):
        deleteNode(self.root, key)


def deleteNode(root, key):
    if root is None:
        return root
    else:
        if key > root.data:
            root.left = deleteNode(root.left, key)
            return root
        elif key < root.data:
            root.right = deleteNode(root.right, key)
            return root
    if root.left is None:
        temp = root.right
        del root
        return temp
    elif root.right is None:
        temp = root.left
        del root
        return temp


def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


def tree_height(root):
    if root is None:
        return 0
    else:
        left_height = tree_height(root.left)
        right_height = tree_height(root.right)
        return 1 + max(left_height, right_height)


tree = Tree()
a = [1, 2, 3, 4, 5, 6]
for i in a:
    tree.insert(i)
# h = tree.height()
# print(h)
tree.print()
tree.deleteChild(4)
print("\n")
tree.print()
