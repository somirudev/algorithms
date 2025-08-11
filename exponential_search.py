import random


def exponential_search(sorted_list, target):
    if not sorted_list:
        return -1
    if sorted_list[0] == target:
        return 0

    index = 1
    # make exponential jumps through list to decide in which block target could be
    while index < len(sorted_list) and sorted_list[index] < target:
        index *= 2

    # binary search the target block
    low = index // 2
    high = min(index, len(sorted_list) - 1)
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    random_list = sorted([random.randrange(0, 200) for i in range(100)])
    random_target = random.randint(0, 200)
    print(f"searching for {random_target} in {random_list}")
    print(
        f"found at index {exponential_search(random_list, random_target)} (if -1: not found)"
    )
