import random


def interpolation_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high and sorted_list[low] <= target and target <= sorted_list[high]:
        # avoid divide by zero
        if sorted_list[high] - sorted_list[low] == 0:
            break

        # set middle according to the value difference between low and high and target
        middle = low + (target - sorted_list[low]) * (high - low) // (
            sorted_list[high] - sorted_list[low]
        )

        # same as binary search
        if sorted_list[middle] == target:
            return middle
        elif sorted_list[middle] < target:
            low = middle + 1
        else:
            high = middle - 1

    # extra check in case loop was terminated because divide by zero
    if low < len(sorted_list) and sorted_list[low] == target:
        return low
    else:
        return -1


if __name__ == "__main__":
    random_list = [random.randrange(0, 10) for _ in range(10)]
    random_list.sort()
    random_target = random.randint(0, 9)
    print(f"searching for {random_target} in {random_list}")
    print(
        f"found at index {interpolation_search(random_list, random_target)} (if -1: not found)"
    )
