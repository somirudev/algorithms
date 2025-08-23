import random


class Node:
    def __init__(self, value, data):
        self.value = value
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # method to insert a value into the BST, no balancing
    def insert(self, value, data=None):
        if self.root is None:  # no root, create it
            self.root = Node(value, data)
            return

        current = self.root
        parent = None
        while current is not None:  # first None pointer
            parent = current  # keep track of parent
            if value < current.value:  # smaller, move left
                current = current.left
            elif value > current.value:  # bigger, move right
                current = current.right
            else:  # found duplicate, ignore
                return

        if value < parent.value:  # create new node at correct position below parent
            parent.left = Node(value, data)
        else:
            parent.right = Node(value, data)

    # deletes a value, returns True if value was found and deleted,
    # returns False if value wasn't in the tree
    def delete(self, value):
        parent = None
        current = self.root

        while (
            current is not None and current.value != value
        ):  # search for value or None
            parent = current

            if value < current.value:  # smaller, move left
                current = current.left
            else:  # bigger, move right
                current = current.right

        if current is None:  # not found
            return False

        if (
            current.left is None or current.right is None
        ):  # at most one child, easy replacement
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
            successor_parent = current
            successor = current.right
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
            current.value = successor.value

            if successor_parent == current:
                successor_parent.right = successor.right
            else:
                successor_parent.left = successor.right
        return True

    # searches for the value in root, returns the nodes data if found, False if value is not in the tree
    def search(self, value):
        current = self.root

        while current is not None:
            if value < current.value:  # smaller, move left
                current = current.left
            elif value > current.value:  # bigger, move right
                current = current.right
            else:  # value found
                return current.value

        return False

    # prints the current layout of the tree sideways, (recursively)
    def print_tree(self):
        print()

        def draw(node, indent=""):
            if node is None:
                return
            if node.right:
                draw(node.right, indent + "    ")
            print(indent + "|" + str(node.value) + "<")
            if node.left:
                draw(node.left, indent + "    ")

        if self.root:
            draw(self.root)
        print()


if __name__ == "__main__":
    binary = BinarySearchTree()
    for i in range(10):
        value = random.randint(0, 20)
        print(f"inserting {value}")
        binary.insert(value, value)
        binary.print_tree()
    for i in range(5):
        target = random.randint(0, 20)
        print(f"searching for {target}")
        print(f"found: {binary.search(target)}")
    for i in range(5):
        to_delete = random.randint(0, 20)
        print(f"deleting {to_delete}")
        print(f"deleted: {binary.delete(to_delete)}")
        binary.print_tree()
