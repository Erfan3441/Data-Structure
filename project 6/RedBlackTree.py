Red = 'Red'
Black = 'Black'


class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data
        self.color = Red


class RedBlackTree:
    def __init__(self):
        nil_node = TreeNode(0)
        nil_node.color = Black
        self.NIL = nil_node
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:  # x is root
            self.root = y
        elif x == x.parent.left:  # x is left child
            x.parent.left = y
        else:  # x is right child
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:  # x is root
            self.root = y
        elif x == x.parent.right:  # x is right child
            x.parent.right = y
        else:  # x is left child
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert_fixup(self, z):
        while z.parent.color == Red:
            if z.parent == z.parent.parent.left:  # z.parent is the left child
                y = z.parent.parent.right  # uncle of z

                if y.color == Red:  # case 1
                    z.parent.color = Black
                    y.color = Black
                    z.parent.parent.color = Red
                    z = z.parent.parent

                else:  # case2 or case3
                    if z == z.parent.right:  # case2
                        z = z.parent  # marked z.parent as new z
                        self.left_rotate(z)

                    # case3
                    z.parent.color = Black  # made parent black
                    z.parent.parent.color = Red  # made parent red
                    self.right_rotate(z.parent.parent)

            else:  # z.parent is the right child
                y = z.parent.parent.left  # uncle of z

                if y.color == Red:
                    z.parent.color = Black
                    y.color = Black
                    z.parent.parent.color = Red
                    z = z.parent.parent

                else:
                    if z == z.parent.left:
                        z = z.parent  # marked z.parent as new z
                        self.right_rotate(z)

                    z.parent.color = Black  # made parent black
                    z.parent.parent.color = Red  # made parent red
                    self.left_rotate(z.parent.parent)

        self.root.color = Black

    def insert(self, data):
        z = TreeNode(data)
        y = self.NIL  # variable for the parent of the added node
        temp = self.root

        while temp != self.NIL:
            y = temp
            if z.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        z.parent = y

        if y == self.NIL:  # newly added node is root
            self.root = z

        elif z.data < y.data:  # data of child is less than its parent, left child
            y.left = z
        else:
            y.right = z

        z.right = self.NIL
        z.left = self.NIL

        self.insert_fixup(z)

    def rb_transplant(self, u, v):
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, x):
        while x.left != self.NIL:
            x = x.left
        return x

    def delete_fixup(self, x):
        while x != self.root and x.color == Black:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == Red:
                    w.color = Black
                    x.parent.color = Red
                    self.left_rotate(x.parent)
                    w = x.parent.right

                if w.left.color == Black and w.right.color == Black:
                    w.color = Red
                    x = x.parent

                else:
                    if w.right.color == Black:
                        w.left.color = Black
                        w.color = Red
                        self.right_rotate(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = Black
                    w.right.color = Black
                    self.left_rotate(x.parent)
                    x = self.root

            else:
                w = x.parent.left
                if w.color == Red:
                    w.color = Black
                    x.parent.color = Red
                    self.right_rotate(x.parent)
                    w = x.parent.left

                if w.right.color == Black and w.left.color == Black:
                    w.color = Red
                    x = x.parent

                else:
                    if w.left.color == Black:
                        w.right.color = Black
                        w.color = Red
                        self.left_rotate(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = Black
                    w.left.color = Black
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = Black

    def rb_delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.rb_transplant(z, z.right)

        elif z.right == self.NIL:
            x = z.left
            self.rb_transplant(z, z.left)

        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent != z:
                self.rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == Black:
            self.delete_fixup(x)

    def inorder(self, n):
        if n != self.NIL:
            self.inorder(n.left)
            print(f"Data: {n.data}, Color: {n.color}")
            self.inorder(n.right)

    def delete(self, data):
        z = self.search(self.root, data)
        if z != self.NIL:
            self.rb_delete(z)

    def search(self, node, data):
        while node != self.NIL and data != node.data:
            if data < node.data:
                node = node.left
            else:
                node = node.right
        return node


#t = RedBlackTree()
#values_to_insert = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35]
#for value in values_to_insert:
    #t.insert(value)



# rb_tree = RedBlackTree()
# rb_tree.insert(13)
# rb_tree.insert(8)
# rb_tree.insert(17)
# rb_tree.insert(1)
# rb_tree.insert(11)
# rb_tree.insert(15)
# rb_tree.insert(25)
# rb_tree.insert(6)
# rb_tree.insert(22)
# rb_tree.insert(27)


# print("Original Tree:")
# rb_tree.inorder(rb_tree.root)


# # rb_tree.delete(30)
# # rb_tree.delete(60)

# print("\nTree after deletion:")
# rb_tree.inorder(rb_tree.root)



