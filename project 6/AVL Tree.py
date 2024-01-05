class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree(object):
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)
    
    def inorder_traversal(self, root):
        if root is not None:
            self.inorder_traversal(root.left)
            print(root.key, end=' ')
            self.inorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root is not None:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.key, end=' ')

    def preOrder(self, root):
        if not root:
            return

        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)






# myTree = AVLTree()
# root = None

# # Constructing tree given in the above figure
# nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]

# for num in nums:
#     root = myTree.insert(root, num)

# # The constructed AVL Tree would be
# #        9
# #       /  \
# #      1    10
# #     / \     \
# #    0   5     11
# #   /   / \
# # -1   2   6

# print("Inorder traversal of the constructed AVL tree is")
# myTree.inorder_traversal(root)
# print()

# print("Postorder traversal of the constructed AVL tree is")
# myTree.postorder_traversal(root)
# print()

# print("Preorder traversal of the constructed AVL tree is")
# myTree.preOrder(root)
# print()

# # Deleting node 10
# root = myTree.delete(root, 10)

# print("Inorder Traversal after deletion of 10:")
# myTree.inorder_traversal(root)
# print()

# print("Postorder Traversal after deletion of 10:")
# myTree.postorder_traversal(root)
# print()

# print("Preorder Traversal after deletion of 10:")
# myTree.preOrder(root)
# print()