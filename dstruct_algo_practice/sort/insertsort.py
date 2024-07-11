#implementation of insertion sort
def insertion_sort(arr, n):
    """
    Sorts items in increasing order
    :param arr: items to be sorted
    :param n: number of items
    :return: sorted items
    """
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr


print(insertion_sort([5, 2, 4, 6, 1, 3], 6))
print(insertion_sort([4, 5, 1, 3, 3, 6, 2], 7))

