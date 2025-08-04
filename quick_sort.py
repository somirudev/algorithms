import random


def quick_sort(to_sort_list, low=0, high=-1):
    if high == -1:
        high = len(to_sort_list) - 1
    if low < high:
        print(to_sort_list[low : high + 1])
        middle = partition(to_sort_list, low, high)
        quick_sort(to_sort_list, low, middle - 1)
        quick_sort(to_sort_list, middle + 1, high)
    return to_sort_list


def partition(to_sort_list, low, high):
    random_pivot_index = random.randrange(low, high + 1)
    to_sort_list[high], to_sort_list[random_pivot_index] = (
        to_sort_list[random_pivot_index],
        to_sort_list[high],
    )
    pivot = to_sort_list[high]
    i = low - 1
    for j in range(low, high):
        if to_sort_list[j] <= pivot:
            i += 1
            to_sort_list[j], to_sort_list[i] = to_sort_list[i], to_sort_list[j]
    to_sort_list[high], to_sort_list[i + 1] = to_sort_list[i + 1], to_sort_list[high]
    return i + 1


if __name__ == "__main__":
    random_list = [random.randrange(0, 100) for i in range(10)]
    print(quick_sort(random_list))
