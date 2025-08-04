import random


def insertion_sort(to_sort_list):
    for i in range(1, len(to_sort_list)):
        print(to_sort_list)
        key = to_sort_list[i]
        j = i - 1
        while j >= 0 and key < to_sort_list[j]:
            to_sort_list[j + 1] = to_sort_list[j]
            j -= 1
        to_sort_list[j + 1] = key
    return to_sort_list


if __name__ == "__main__":
    random_list = [random.randrange(0, 100) for i in range(10)]
    print(insertion_sort(random_list))
