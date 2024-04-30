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

    def print(self):
        print("Pre-Order:", end=" ")
        preorder(self.root)
        print("\nIn-Order:",end=" ")
        inorder(self.root)
        print("\nPost-Order:", end=" ")
        postorder(self.root)

    def deleteChild(self, key):
        deleteNode(self.root, key)

    def search(self, key):
        temp = self.root
        while 1:
            if temp is None:
                return 0
            if temp.data == key:
                return 1
            else:
                if temp.data > key:
                    temp = temp.left
                else:
                    temp = temp.right

    def searchSubtree(self, key):
        temp = self.root
        while 1:
            if temp is None:
                return []
            if temp.data == key:
                root = temp
                preorder(root)
                break
            else:
                if temp.data > key:
                    temp = temp.left
                else:
                    temp = temp.right

    def height(self, root):
        if root is None:
            return 0
        else:
            lheight = self.height(root.left)
            rheight = self.height(root.right)
        return max(lheight, rheight) + 1

    def printNode(self,  root, level):
        if root is None:
            return
        if level == 1:
            print(root.data, end=" ")
        elif level > 1:
            self.printNode(root.left, level-1)
            # print()
            self.printNode(root.right, level-1)
            # print()

    def levelOrder(self):
        h = self.height(self.root)
        for i in range(1, h+1):
            self.printNode(self.root, i)


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
    else:
        succParent = root
        succ = root.right
        while succ.left:
            succParent = succ
            succ = succ.left
        if succParent != root:
            succParent.left = succ.right
        else:
            succParent.right = succ.left
        # root.data =


def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


tree = Tree()
# a = [10, 11, 9, 8, 91, 20, 7]
a = [4, 2, 7, 1, 3, 5, 8]
for i in a:
    tree.insert(i)
# res = tree.search(9)
# print(res)
tree.searchSubtree(5)
# tree.print()
tree.levelOrder()
