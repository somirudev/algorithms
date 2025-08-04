import random


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:  # no root, create it
            self.root = Node(value)
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
            parent.left = Node(value)
        else:
            parent.right = Node(value)

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

    def search(self, value):
        current = self.root

        while current is not None:
            if value < current.value:  # smaller, move left
                current = current.left
            elif value > current.value:  # bigger, move right
                current = current.right
            else:  # value found
                return True

        return False

    def print_tree(self):
        print()

        def draw(node, indent=""):
            if node is None:
                return
            if node.left:
                draw(node.left, indent + "    ")
            print(indent + "|" + str(node.value) + "<")
            if node.right:
                draw(node.right, indent + "    ")

        if self.root:
            draw(self.root)
        print()

    def _get_max_depth(self, node):
        if node is None:
            return 0
        else:
            left_depth = self._get_max_depth(node.left)
            right_depth = self._get_max_depth(node.right)
            return 1 + max(left_depth, right_depth)


if __name__ == "__main__":
    binary = Binary_search_tree()
    for i in range(10):
        value = random.randint(0, 20)
        print(f"inserting {value}")
        binary.insert(value)
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
