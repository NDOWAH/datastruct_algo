"""
algorithm
=========
REVERSE_INSERTION(arr, n)
    for i <-- 2 to n
        j <-- i - 1
        key <-- arr[i]
        while j > 0 and arr[j] < key
            arr[j+1] <--arr[j]
            j = j -1
        arr[j+1] <-- key
"""


def reverse_insertion_sort(arr, n):
    for i in range(1, n):
        j = i - 1
        key = arr[i]
        while j >= 0 and arr[j] < key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return arr


print(reverse_insertion_sort([5, 2, 4, 6, 1, 3], 6))
print(reverse_insertion_sort([31, 41, 59, 26, 41, 58], 6))
print(reverse_insertion_sort([2, 4, 6, 8, 3], 5))
