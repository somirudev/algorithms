import random


class Node:
    def __init__(self, parent, value, data):
        self.value = value
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent
        self.height = 1


class AVL_BST:
    def __init__(self):
        self.root = None

    # helper function returns height of node, 0 if node doesn't exit
    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    # helper function, returns difference in height between left and right subtrees
    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    # helper function to rebalance the tree from node up parent by parent until root
    def _rebalance(self, node):
        while node:
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right) # update height

            if self._get_balance(node) > 1:  # left side is higher
                if node.left and self._get_balance(node.left) < 0:
                    node.left = self._left_rotation(node.left)
                node = self._right_rotation(node)

            elif self._get_balance(node) < -1:  # right side is higher
                if node.right and self._get_balance(node.right) > 0:
                    node.right = self._right_rotation(node.right)
                node = self._left_rotation(node)

            node = node.parent  # continue up the tree

    # performs right rotation on node
    # returns new root of subtree
    def _right_rotation(self, node):
        grandparent = node.parent
        C = node  # node becomes the child of parent P
        P = node.left  # node.left becomes parent of node C

        # pointer changes
        C.left = P.right
        P.right = C

        # update parent pointers
        C.parent = P
        P.parent = grandparent
        if C.left is not None:
            C.left.parent = C

        # update grandparent pointing to P (or self.root if no grandparent)
        if grandparent is not None:
            if grandparent.left == C:
                grandparent.left = P
            else:
                grandparent.right = P
        else:
            self.root = P

        # update heights and balances of changed nodes
        C.height = 1 + max(self._get_height(C.left), self._get_height(C.right)) 
        P.height = 1 + max(self._get_height(P.left), self._get_height(P.right)) 
        # return new root of this subtree
        return P

    # performs left rotation on node
    # returns new root of subtree
    def _left_rotation(self, node):
        grandparent = node.parent
        C = node  # node becomes the child of parent P
        P = node.right  # node.right becomes parent of node C

        # update pointers
        C.right = P.left
        P.left = C

        # update parent pointers
        C.parent = P
        P.parent = grandparent
        if C.right is not None:
            C.right.parent = C

        # update grandparent pointing to P (or self.root if no grandparent)
        if grandparent is not None:
            if grandparent.left == C:
                grandparent.left = P
            else:
                grandparent.right = P
        else:
            self.root = P

        # update heights and balances of changed nodes
        C.height = 1 + max(self._get_height(C.left), self._get_height(C.right)) 
        P.height = 1 + max(self._get_height(P.left), self._get_height(P.right)) 
        # return new root of this subtree
        return P

    # method to insert a value into the BST, calls rebalance on the parent of the placed node after insertion
    def insert(self, value, data=None):
        if self.root is None:  # no root, create it
            self.root = Node(None, value, data)
            return

        current = self.root
        parent = None
        while current is not None:  # continue until there's no more nodes
            if value < current.value:  # smaller, move left
                parent = current
                current = current.left
            elif value > current.value:  # bigger, move right
                parent = current
                current = current.right
            else:  # found duplicate, ignore
                return

        if value < parent.value:  # create new node at correct position below parent
            parent.left = Node(parent, value, data)
        else:
            parent.right = Node(parent, value, data)

        self._rebalance(parent)

    # method to delete a vlue into the BST, calls rebalance on the removed node (if there was one) after deletion
    def delete(self, value):
        parent = None
        current = self.root

        # search for value or None
        while current is not None and current.value != value:
            parent = current  # keep track of parent

            if value < current.value:  # smaller, move left
                current = current.left
            else:  # bigger, move right
                current = current.right

        if current is None:  # not found
            return False

        # at most one child, easy replacement
        if current.left is None or current.right is None:
            to_balance = current.parent
            child = None
            if current.left is not None:
                child = current.left
            else:
                child = current.right

            if parent is None:  # if self.root is the value
                self.root = child  # fix self.root to new root
            elif parent.left == current:
                parent.left = child  # fix parent pointer to new child
            else:
                parent.right = child

        else:  # two children
            successor = current.right
            while (
                successor.left is not None
            ):  # move left as far as possible in right subtree
                successor = successor.left

            # update current value to successor's value
            current.value = successor.value
            to_balance = successor.parent
            if successor.parent == current:
                current.right = successor.right
            else:
                successor.parent.left = successor.right

        self._rebalance(to_balance)
        return True

    # searches for the value in root, returns Data stored in the node if found, or False if value is not in the tree
    def search(self, value):
        current = self.root

        while current is not None:
            if value < current.value:  # smaller, move left
                current = current.left
            elif value > current.value:  # bigger, move right
                current = current.right
            else:  # value found
                return current.data

        return False

    # prints the current layout of the tree sideways, (recursively)
    def print_tree(self):
        print()

        def draw(node, indent=""):
            if node is None:
                return
            if node.left:
                draw(node.left, indent + "    ")
            print(f"{indent}|{str(node.value)}<")
            if node.right:
                draw(node.right, indent + "    ")

        if self.root:
            draw(self.root)
        print()


if __name__ == "__main__":
    avl = AVL_BST()
    for i in range(20):
        value = random.randint(0, 20)
        print(f"inserting {value}")
        avl.insert(value, value)
        avl.print_tree()
    for i in range(5):
        target = random.randint(0, 20)
        print(f"searching for {target}")
        print(f"found: {avl.search(target)}")
    for i in range(10):
        to_delete = random.randint(0, 20)
        print(f"deleting {to_delete}")
        print(f"deleted: {avl.delete(to_delete)}")
        avl.print_tree()
