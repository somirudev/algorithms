import random


def bubble_sort(to_sort_list):
    n = len(to_sort_list)
    for i in range(n):
        swapped = False
        print(to_sort_list)
        for j in range(0, n - i - 1):
            if to_sort_list[j] > to_sort_list[j + 1]:
                swapped = True
                to_sort_list[j], to_sort_list[j + 1] = (
                    to_sort_list[j + 1],
                    to_sort_list[j],
                )
        if not swapped:
            break
    return to_sort_list


if __name__ == "__main__":
    random_list = [random.randrange(0, 100) for i in range(10)]
    print(bubble_sort(random_list))
