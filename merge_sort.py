import random


def merge_sort(to_sort_list):
    print(to_sort_list)
    if len(to_sort_list) > 1:
        middle = len(to_sort_list) // 2
        first_half = to_sort_list[:middle]
        second_half = to_sort_list[middle:]

        merge_sort(first_half)
        merge_sort(second_half)

        i = j = k = 0
        while i < len(first_half) and j < len(second_half):
            if first_half[i] < second_half[j]:
                to_sort_list[k] = first_half[i]
                i += 1
            else:
                to_sort_list[k] = second_half[j]
                j += 1
            k += 1

        while i < len(first_half):
            to_sort_list[k] = first_half[i]
            i += 1
            k += 1

        while j < len(second_half):
            to_sort_list[k] = second_half[j]
            j += 1
            k += 1

    return to_sort_list


if __name__ == "__main__":
    random_list = [random.randrange(0, 100) for i in range(10)]
    print(merge_sort(random_list))
