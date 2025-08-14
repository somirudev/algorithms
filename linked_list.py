class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_list:
    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.length = 0

    def append(self, value):
        if self.last_node is None:
            self.first_node = self.last_node = Node(value)
        else:
            self.last_node.next = Node(value)
            self.last_node = self.last_node.next
        self.length += 1

    def insert(self, value, index):
        if not 0 <= index <= self.length:
            raise IndexError("Index out of bounds")

        if index == self.length:
            self.append(value)
            return

        if index == 0:
            self.push(value)
            return

        node = self.first_node
        for _ in range(index - 1):
            node = node.next
        temp_node = node.next
        node.next = Node(value)
        node.next.next = temp_node
        self.length += 1

    def search(self, target):
        node = self.first_node
        index = 0
        while node is not None:
            if node.value == target:
                return index
            node = node.next
            index += 1
        return -1

    def delete(self, target):
        node = self.first_node
        index = 0
        prev_node = None
        while node is not None:
            if node.value == target:
                self.length -= 1

                # Target value is at first node
                if prev_node is None:
                    self.first_node = node.next
                    if self.first_node is None:
                        self.last_node = None
                    return index

                # Target value is at last node
                if node.next is None:
                    prev_node.next = None
                    self.last_node = prev_node
                    return index

                # Target value is in the middle
                prev_node.next = node.next
                return index

            prev_node = node
            node = node.next
            index += 1
        return -1

    def push(self, value):
        current_first_node = self.first_node
        self.first_node = Node(value)
        self.length += 1
        self.first_node.next = current_first_node

    def pop(self):
        popped_node = self.first_node
        self.first_node = popped_node.next
        self.length -= 1
        return popped_node.value

    def reverse(self):
        self.last_node = self.first_node
        prev_node = None
        current_node = self.first_node
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.first_node = prev_node

    def print_ll(self):
        print("[", end="")
        node = self.first_node
        while node is not self.last_node:
            print(node.value, end=", ")
            node = node.next
        print(str(node.value) + "]")


if __name__ == "__main__":
    ll = Linked_list()
    string_1 = "Hello"
    print(f"Appending '{string_1}'")
    ll.append(string_1)
    string_2 = "World"
    print(f"Appending '{string_2}'")
    ll.append(string_2)
    ll.print_ll()

    print(f"deleting '{string_2}'- deleted at index: {ll.delete(string_2)}")
    ll.print_ll()

    value = 6
    index = 1
    print(f"inserting '{value}' at index {index}")
    ll.insert(value, index)
    ll.print_ll()
    value = (True, False)
    index = 0
    print(f"pushing {value}")
    ll.push(value)
    ll.print_ll()

    char = "!"
    index = -3
    try:
        print(f"inserting '{char}' at index {index}")
        ll.insert(char, index)
        ll.print_ll()
    except Exception as e:
        print(e)
    index = 30
    try:
        print(f"inserting '{char}' at index {index}")
        ll.insert(char, index)
        ll.print_ll()
    except Exception as e:
        print(e)
    index = ll.length
    print(f"inserting '{char}' at index {index}")
    ll.insert(char, index)
    ll.print_ll()

    print("Reversing list")
    ll.reverse()
    ll.print_ll()
    print(f"searching for '{string_1}': found at index: {ll.search(string_1)}")
    string_3 = "Pancake"
    print(f"searching for '{string_3}': found at index: {ll.search(string_3)}")
    print(f"linked_list.pop() returns: {ll.pop()}")
    ll.print_ll()
    print(f"list length is {ll.length}")
