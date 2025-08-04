import random


def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        middle = (low + high) // 2

        if sorted_list[middle] == target:
            return middle
        elif sorted_list[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    return -1


if __name__ == "__main__":
    random_list = [random.randrange(0, 10) for i in range(10)]
    random_list = sorted(random_list)
    random_target = random.randint(0, 9)
    print(f"searching for {random_target} in {random_list}")
    print(
        f"found at index {binary_search(random_list, random_target)} (if -1: not found)"
    )
