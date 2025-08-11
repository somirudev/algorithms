import random


class Heap:
    def __init__(self, max=True):
        self.heap_list = [0]
        self.heap_size = 0
        self.max = max
        if self.max:
            print("Created new Max-Heap")
        else:
            print("Created new Min-Heap")

    # insert a list and make sure it abides by heap rules
    def heapify(self, list):
        self.heap_list.extend(list)
        self.heap_size += len(list)
        for index in range(self.heap_size // 2, 0, -1):
            self._sink_down(index)

    # insert a single value according to heap rules
    def push(self, value):
        self.heap_list.append(value)
        self.heap_size += 1
        self._bubble_up()

    # remove the root value and re-sort the tree
    def pop(self, delete=True):
        self.heap_list[1], self.heap_list[self.heap_size] = (
            self.heap_list[self.heap_size],
            self.heap_list[1],
        )
        self.heap_size -= 1
        self._sink_down()
        if delete:
            return self.heap_list.pop(self.heap_size + 1)
        else:
            return self.heap_list[self.heap_size + 1]

    # "pops" the root value until heap is empty without deleting the values and returns the sorted list
    def heapsort(self):
        for i in range(self.heap_size):
            self.pop(False)
        return self.heap_list[1:]

    # returns the root value without changing the heap
    def peek(self):
        return self.heap_list[1]

    # print heap like a tree but sideways for simplicity
    def print_heap(self, index=1, indent=""):
        if indent == "":
            print()
        if index * 2 + 1 <= self.heap_size:
            self.print_heap(index * 2 + 1, indent + "    ")
        print(f"{indent}|{self.heap_list[index]}<")
        if index * 2 <= self.heap_size:
            self.print_heap(index * 2, indent + "    ")
        if indent == "":
            print()

    # helper function that makes a node rise towards the root to satisfy heap rules (eg bigger than a parent in max heap -> swap with parent)
    def _bubble_up(self, index=None):
        if index is None:
            index = self.heap_size
        while index // 2 > 0:
            if self.max and self.heap_list[index] > self.heap_list[index // 2]:
                self.heap_list[index], self.heap_list[index // 2] = (
                    self.heap_list[index // 2],
                    self.heap_list[index],
                )
                index = index // 2
            elif not self.max and self.heap_list[index] < self.heap_list[index // 2]:
                self.heap_list[index], self.heap_list[index // 2] = (
                    self.heap_list[index // 2],
                    self.heap_list[index],
                )
                index = index // 2
            else:
                break

    # helper function that makes a node sink towards the leafs to satisfy heap rules (eg smaller than a child in max heap -> swap with biggest child)
    def _sink_down(self, index=1):
        while index * 2 <= self.heap_size:
            if index * 2 == self.heap_size:
                maxindex = minindex = index * 2
            elif self.heap_list[index * 2] > self.heap_list[index * 2 + 1]:
                maxindex = index * 2
                minindex = index * 2 + 1
            else:
                maxindex = index * 2 + 1
                minindex = index * 2
            if self.max and self.heap_list[index] < self.heap_list[maxindex]:
                self.heap_list[index], self.heap_list[maxindex] = (
                    self.heap_list[maxindex],
                    self.heap_list[index],
                )
                index = maxindex
            elif not self.max and self.heap_list[index] > self.heap_list[minindex]:
                self.heap_list[index], self.heap_list[minindex] = (
                    self.heap_list[minindex],
                    self.heap_list[index],
                )
                index = minindex
            else:
                break


if __name__ == "__main__":
    random_list = [random.randint(0, 10) for x in range(10)]
    print(random_list)
    maxheapify = Heap()
    maxheapify.heapify(random_list)
    maxheapify.print_heap()

    minheap = Heap(False)
    for i in range(15):
        value = random.randint(0, 20)
        minheap.push(value)
        minheap.print_heap()
    for i in range(5):
        min = minheap.pop()
        print(f"min was {min}")
        minheap.print_heap()

    maxheap = Heap()
    for i in range(15):
        value = random.randint(0, 20)
        maxheap.push(value)
        maxheap.print_heap()
    for i in range(5):
        max = maxheap.pop()
        print(f"max was {max}")
        maxheap.print_heap()

    print(random_list)
    maxheap.heapify(random_list)
    maxheap.print_heap()
    print(maxheap.heapsort())
