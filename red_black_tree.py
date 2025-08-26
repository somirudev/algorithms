class Node:
    def __init__(self, value):
        self.red = False
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


class Red_Black_BST:
    def __init__(self):
        self.nil = Node(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.nil.parent = None
        self.root = self.nil

    # method to insert a value into the BST, calling balancing according to Red/Black BST afterwards
    def insert(self, value):
        new_node = Node(value)
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.value < current.value:
                current = current.left
            elif new_node.value > current.value:
                current = current.right
            else:
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        current_node = new_node
        while current_node is not self.root and current_node.parent.red:
            parent = current_node.parent
            grandparent = parent.parent
            if grandparent.right is parent:
                uncle = grandparent.left
                if uncle.red:  # both parent and uncle are red, recolor them to black, set grandparent to red and check from there
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    current_node = grandparent

                else:  # parent is red, but uncle is not, rotations needed to solve
                    if (
                        parent.left is current_node
                    ):  # zig-zag case, rotate child & parent to make it a straight line
                        self._right_rotation(parent)
                        current_node = parent
                        parent = current_node.parent
                    parent.red = False  # straight line case, rotate parent & grandparent and fix colors
                    grandparent.red = True
                    self._left_rotation(grandparent)
            else:
                uncle = grandparent.right
                if uncle.red:  # both aprent and uncle are red, recolor them to black, set grandparent to red and check from there
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    current_node = grandparent

                else:  # parent is red, but uncle is not, rotations needed to solve
                    if (
                        parent.right is current_node
                    ):  # zig-zag case, rotate child & parent to make it a straight line
                        self._left_rotation(parent)
                        current_node = parent
                        parent = current_node.parent
                    parent.red = False  # straight line case, rotate parent & granddparent and fix colors
                    grandparent.red = True
                    self._right_rotation(grandparent)
        self.root.red = False

    def _right_rotation(self, node):
        if node is self.nil or node.left is self.nil:
            return

        grandparent = node.parent
        C = node  # node becomes the [C]hild of [P]arent P
        P = node.left  # node.left becomes [P]arent of [C]hild C

        # pointer changes
        C.left = P.right
        P.right = C

        # update parent pointers
        C.parent = P
        P.parent = grandparent
        if C.left is not self.nil:
            C.left.parent = C

        # update grandparent pointing to P (or self.root if no grandparent)
        if grandparent is not None:
            if grandparent.left is C:
                grandparent.left = P
            else:
                grandparent.right = P
        else:
            self.root = P

    def _left_rotation(self, node):
        if node is self.nil or node.right is self.nil:
            return

        grandparent = node.parent
        C = node  # node becomes the [C]hild of [P]arent P
        P = node.right  # node.left becomes [P]arent of [C]hild C

        # pointer changes
        C.right = P.left
        P.left = C

        # update parent pointers
        C.parent = P
        P.parent = grandparent
        if C.right is not self.nil:
            C.right.parent = C

        # update grandparent pointing to P (or self.root if no grandparent)
        if grandparent is not None:
            if grandparent.right == C:
                grandparent.right = P
            else:
                grandparent.left = P
        else:
            self.root = P

    # deletes a value, returns True if value was found and deleted,
    # returns False if value wasn't in the tree
    def delete(self, value):
        current = self.root

        # search for value
        while current is not self.nil and current.value != value:
            if value < current.value:  # smaller, move left
                current = current.left
            else:  # bigger, move right
                current = current.right

        if current is self.nil:  # not found
            return False

        deleted_node_red = current.red
        node_to_fix = self.nil

        # case 1: at max 1 child:
        if current.left is self.nil:
            node_to_fix = current.right
            self._transplant(current, current.right)
        elif current.right is self.nil:
            node_to_fix = current.left
            self._transplant(current, current.left)

        # case 2: 2 children:
        else:
            # find smallest successor
            successor = current.right
            while successor.left is not self.nil:
                successor = successor.left
            # remember deleted node color
            deleted_node_red = successor.red
            node_to_fix = successor.right

            if successor.parent is current:
                node_to_fix.parent = successor
            else:
                self._transplant(successor, successor.right)
                successor.right = current.right
                successor.right.parent = successor
            self._transplant(current, successor)
            successor.left = current.left
            successor.left.parent = successor
            successor.red = current.red

        if not deleted_node_red:
            self.fix_delete(node_to_fix)

        return True

    # replaces old subtree with new subtree
    def _transplant(self, old, new):
        if old.parent is None:
            self.root = new
        elif old.parent.left is old:
            old.parent.left = new
        else:
            old.parent.right = new
        new.parent = old.parent

    def fix_delete(self, node_to_fix):
        while node_to_fix is not self.root and not node_to_fix.red:
            parent = node_to_fix.parent
            if parent is None:
                break

            if node_to_fix is parent.left:
                sibling = parent.right

                # case 1: sibling is red - recolor and rotate to transform to another case and solve in next loops
                if sibling.red:
                    sibling.red = False
                    parent.red = True
                    self._left_rotation(parent)
                    sibling = parent.right

                # case 2: sibling is black, and both of its children are also black - recolor sibling and move up the tree
                if not sibling.left.red and not sibling.right.red:
                    sibling.red = True
                    node_to_fix = parent

                else:
                    # case 3: sibling is black, left child is red, right child is black - recolor and rotate to transform into case 4
                    if not sibling.right.red:
                        sibling.left.red = False
                        sibling.red = True
                        self._right_rotation(sibling)
                        sibling = parent.right

                    # case 4: sibling is black, left child is black, right child is red - recolor and rotate to fix tree, then break the loop
                    sibling.red = parent.red
                    parent.red = False
                    sibling.right.red = False
                    self._left_rotation(parent)
                    node_to_fix = self.root

            else:
                sibling = parent.left

                # case 5: sibling is red - recolor and rotate to transform to another case and solve in next loops
                if sibling.red:
                    sibling.red = False
                    parent.red = True
                    self._right_rotation(parent)
                    sibling = parent.left

                # case 6: sibling is black, and both of its children are also black - recolor sibling and move up the tree
                if not sibling.left.red and not sibling.right.red:
                    sibling.red = True
                    node_to_fix = parent

                else:
                    # case 7: sibling is black, left child is black, right child is red - recolor and rotate to transform into case 4
                    if not sibling.left.red:
                        sibling.right.red = False
                        sibling.red = True
                        self._left_rotation(sibling)
                        sibling = parent.left

                    # case 8: sibling is black, left child is red, right child is black - recolor and rotate to fix tree, then break the loop
                    sibling.red = parent.red
                    parent.red = False
                    sibling.left.red = False
                    self._right_rotation(parent)
                    node_to_fix = self.root
        node_to_fix.red = False

    # searches for the value in root, returns the nodes value if found, False if value is not in the tree
    def search(self, value):
        current = self.root
        while current != self.nil and value != current.value:
            if value < current.value:
                current = current.left
            else:
                current = current.right
        if current == self.nil:
            return False
        else:
            return current.value

    # prints the current layout of the tree sideways, (recursively)
    def print_tree(self):
        print()

        def draw(node, indent=""):
            if node is None:
                return
            if node.right:
                draw(node.right, indent + "      ")
            print(f"{indent}|{str(node.value)}, {'R' if node.red else 'B'}<")
            if node.left:
                draw(node.left, indent + "      ")

        if self.root:
            draw(self.root)
        print()


def print_test(name, tree):
    print(f"TEST: {name}")
    tree.print_tree()


if __name__ == "__main__":
    rbt = Red_Black_BST()
    rbt.insert(10)
    print_test("insert root (10), should be black", rbt)
    rbt.delete(10)
    print_test("delete root (10), should be empty", rbt)
    rbt.insert(10)
    rbt.insert(5)
    print_test("re-insert root 10 and insert left child (5), should be red", rbt)
    rbt.insert(15)
    print_test("insert right child (15), should be red", rbt)
    rbt.delete(10)
    print_test("delete root (10) with children, replace with child", rbt)
    rbt.delete(5)
    rbt.delete(15)
    rbt.insert(10)
    rbt.insert(5)
    rbt.insert(15)
    rbt.insert(3)
    print_test(
        "remake 10/5/15 tree & insert 3, should trigger recolor because parent and uncle are red",
        rbt,
    )
    rbt.insert(1)
    print_test("insert 1, should trigger left-left case, right rotation", rbt)
    rbt.insert(20)
    rbt.insert(25)
    print_test("insert 20 & 25, should trigger right-right case, left rotation", rbt)
    rbt_lr = Red_Black_BST()
    for val in [10, 5, 15, 3]:
        rbt_lr.insert(val)
    rbt_lr.print_tree()
    rbt_lr.insert(4)
    print_test("insert 4, should trigger left-right case, double rotation", rbt_lr)
    rbt_rl = Red_Black_BST()
    for val in [10, 5, 15, 17]:
        rbt_rl.insert(val)
    rbt_rl.print_tree()
    rbt_rl.insert(16)
    print_test("insert 16, should trigger right-left case, double rotation", rbt_rl)
    rbt_del = Red_Black_BST()
    for val in [10, 5, 15, 3, 12, 17, 1, 20, 25, 6, 8, 11, 14, 16, 18, 22]:
        rbt_del.insert(val)
    print_test("new tree for deletion tests", rbt_del)
    rbt_del.delete(22)
    print_test("deleting 22, red leaf, no actions needed", rbt_del)
    rbt_del.insert(22)
    rbt_del.delete(25)
    print_test(
        "reinsert 22 and delete 25, black node with red child, replace & recolor",
        rbt_del,
    )
    rbt_del.delete(15)
    print_test("delete 15, successor replacement (16)", rbt_del)
    rbt_del.delete(1)
    print_test(
        "delete 1, imbalance in black nodes in path from root, sibling black, nephews black, rotation and recolor",
        rbt_del,
    )
    # red sibling fix_delete
    rbt_del2 = Red_Black_BST()
    for val in [10, 5, 15, 12, 18, 11, 13]:
        rbt_del2.insert(val)
    rbt_del2.print_tree()
    rbt_del2.delete(5)
    print_test("delete 5, red sibling case", rbt_del2)

    rbt_del3 = Red_Black_BST()
    for val in [10, 5, 20, 15, 30]:
        rbt_del3.insert(val)
    rbt_del3.root.left.red = False
    rbt_del3.root.right.red = True
    rbt_del3.root.right.right.red = False
    rbt_del3.root.right.left.red = False
    rbt_del3.print_tree()
    rbt_del3.delete(15)
    print_test("delete 15, black sibling case, single recolor", rbt_del3)

    rbt_del4 = Red_Black_BST()
    for val in [10, 5, 20, 1, 7, 15, 30]:
        rbt_del4.insert(val)
    rbt_del4.root.right.right.red = False
    rbt_del4.root.right.left.red = False
    rbt_del4.root.left.right.red = False
    rbt_del4.root.left.left.red = False
    rbt_del4.print_tree()
    rbt_del4.delete(15)
    print_test(
        "delete 15, black sibling, black nephews, moving up the tree multiple times case",
        rbt_del4,
    )

    rbt_del5 = Red_Black_BST()
    for val in [10, 5, 20, 1, 7, 15, 30, 25, 40]:
        rbt_del5.insert(val)
    rbt_del5.root.right.right.right.red = False
    rbt_del5.root.right.right.left.red = False
    rbt_del5.root.right.right.red = True
    rbt_del5.root.right.left.red = False
    rbt_del5.root.left.right.red = False
    rbt_del5.root.left.left.red = False
    rbt_del5.print_tree()
    rbt_del5.delete(15)
    print_test(
        "delete 15, red sibling, black nephews, rotate and recolor until 25 is the only red node",
        rbt_del5,
    )
    rbt_del5.insert(20)
    rbt_del5.insert(28)
    rbt_del5.root.right.left.red = True
    rbt_del5.root.right.left.right.red = False
    rbt_del5.root.right.left.left.red = False
    rbt_del5.print_tree()
    rbt_del5.delete(1)
    print_test(
        "delete 1, multiple rotations and recoloring, finishing with only node 7 as red",
        rbt_del5,
    )
