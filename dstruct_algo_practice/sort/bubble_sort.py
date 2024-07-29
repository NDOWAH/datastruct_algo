
def buble_sort(arr):
    n = len(arr)
    """sort a list of items

    Args:
        arr array: list of numbers to be sorted
        n integer: number of elements in the list.
    """
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print("The sorted array is:", buble_sort([8, 4, 7, 3, 7, 1]))

