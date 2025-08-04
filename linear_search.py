import random


def linear_search(unsorted_list, target):
    for index, element in enumerate(unsorted_list):
        if element == target:
            return index
    return -1


if __name__ == "__main__":
    random_list = [random.randrange(0, 10) for i in range(10)]
    random_target = random.randint(0, 9)
    print(f"searching for {random_target} in {random_list}")
    print(
        f"found at index {linear_search(random_list, random_target)} (if -1: not found)"
    )
