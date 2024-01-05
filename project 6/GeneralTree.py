class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class GeneralTree:
    def __init__(self):
        self.root = None

    def insert(self, parent, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            newNode = TreeNode(value)
            parent.children.append(newNode)

    def remove(self, value):
        if self.root is not None:
            self.root = self._remove(self.root, value)

    def _remove(self, node, value):
        if node is None:
            return None
        if node.value == value:
            # A simple way to "remove" the node is to wipe out its children,
            # which effectively removes that sub-tree from the general tree. 
            node.children = []
            return None
        new_children = []
        for child in node.children:
            child_result = self._remove(child, value)
            if child_result is not None:
                new_children.append(child_result)
        node.children = new_children
        return node

    # Helper method to find a node with a given value
    def find(self, value):
        return self._find(self.root, value)

    def _find(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        for child in node.children:
            result = self._find(child, value)
            if result is not None:
                return result
        return None


# gt = GeneralTree()
# gt.insert(None, 'R')  # ایجاد ریشه
# root = gt.find('R')
# gt.insert(root, 'A')
# gt.insert(root, 'B')
# gt.insert(root, 'C')

# A = gt.find('A')
# B = gt.find('B')
# gt.insert(A, 'D')
# gt.insert(A, 'E')
# gt.insert(A, 'F')
# gt.insert(B, 'G')

# gt.remove('A')  # حذف یک گره

# def print_tree(node, level=0):
#     if node is not None:
#         print(' ' * level + str(node.value))
#         for child in node.children:
#             print_tree(child, level + 1)


# print_tree(gt.root)  # چاپ درخت
