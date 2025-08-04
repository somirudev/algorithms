import random


def selection_sort(to_sort_list):
    for i in range(len(to_sort_list)):
        print(to_sort_list)
        smallest_index = i
        for j in range(i, len(to_sort_list)):
            if to_sort_list[j] < to_sort_list[smallest_index]:
                smallest_index = j
        to_sort_list[i], to_sort_list[smallest_index] = (
            to_sort_list[smallest_index],
            to_sort_list[i],
        )
    return to_sort_list


if __name__ == "__main__":
    random_list = [random.randrange(0, 100) for i in range(10)]
    print(selection_sort(random_list))
