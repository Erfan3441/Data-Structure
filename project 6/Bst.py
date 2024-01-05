class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Inorder traversal
    def inorder(self, root):
        if root is not None:
            # Traverse left
            self.inorder(root.left)

            # Traverse root
            print(str(root.value) + "->", end=' ')

            # Traverse right
            self.inorder(root.right)

    # Insert a node
    def insert(self, node, value):
        # Return a new node if the tree is empty
        if node is None:
            return Node(value)

        # Traverse to the right place and insert the node
        if value < node.value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

        return node

    # Find the inorder successor
    def minValueNode(self, node):
        current = node

        # Find the leftmost leaf
        while current.left is not None:
            current = current.left

        return current

    # Deleting a node
    def deleteNode(self, root, value):
        # Return if the tree is empty
        if root is None:
            return root

        # Find the node to be deleted
        if value < root.value:
            root.left = self.deleteNode(root.left, value)
        elif value > root.value:
            root.right = self.deleteNode(root.right, value)
        else:
            # If the node is with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # If the node has two children,
            # place the inorder successor in position of the node to be deleted
            temp = self.minValueNode(root.right)

            root.value = temp.value

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.value)

        return root

    # Search for a value in the tree
    def search(self, root, value):
        if root is None or root.value == value:
            return root
        elif value < root.value:
            return self.search(root.left, value)
        else:
            return self.search(root.right, value)

    # Preorder traversal
    def preorder(self, root):
        if root is not None:
            # Traverse root
            print(str(root.value) + "->", end=' ')

            # Traverse left
            self.preorder(root.left)

            # Traverse right
            self.preorder(root.right)

    # Postorder traversal
    def postorder(self, root):
        if root is not None:
            # Traverse left
            self.postorder(root.left)

            # Traverse right
            self.postorder(root.right)

            # Traverse root
            print(str(root.value) + "->", end=' ')


# bst = BinarySearchTree()
# bst.root = bst.insert(bst.root, 8)
# bst.root = bst.insert(bst.root, 3)
# bst.root = bst.insert(bst.root, 1)
# bst.root = bst.insert(bst.root, 6)
# bst.root = bst.insert(bst.root, 7)
# bst.root = bst.insert(bst.root, 10)
# bst.root = bst.insert(bst.root, 14)
# bst.root = bst.insert(bst.root, 4)

# print("Inorder traversal: ", end=' ')
# bst.inorder(bst.root)

# print("\nSearch for value 6:")
# result = bst.search(bst.root, 6)
# if result:
#     print(f"Found: {result.value}")
# else:
#     print("Not found")

# print("Preorder traversal: ", end=' ')
# bst.preorder(bst.root)

# print("\nPostorder traversal: ", end=' ')
# bst.postorder(bst.root)

# print("\nDeleting the node with value 6")
# bst.root = bst.deleteNode(bst.root, 6)

# print("\nInorder traversal after deleting 6: ", end=' ')
# bst.inorder(bst.root)
