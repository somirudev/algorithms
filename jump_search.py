import random
import math


def jump_search(sorted_list, target):
    step = int(math.sqrt(len(sorted_list)))
    index = step
    prev_index = 0

    # jump search to select a block in which taget can be found
    while sorted_list[min(index, len(sorted_list) - 1)] < target:
        prev_index = index
        index += step
        if prev_index >= len(sorted_list):
            return -1

    # linear search selected block
    while sorted_list[prev_index] < target:
        prev_index += 1
        if prev_index == min(index, len(sorted_list)):
            return -1

    if sorted_list[prev_index] == target:
        return prev_index

    return -1


if __name__ == "__main__":
    random_list = sorted([random.randrange(0, 10) for i in range(10)])
    random_target = random.randint(0, 10)
    print(f"searching for {random_target} in {random_list}")
    print(
        f"found at index {jump_search(random_list, random_target)} (if -1: not found)"
    )
