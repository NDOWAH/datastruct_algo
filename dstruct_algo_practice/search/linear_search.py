"""
lin_search(arr, x)
    y = 0
    for i <---1 to n
        if arr[i] == x
            y = x
            index = i

"""

def lin_search(arr, x):
    y = 0
    for i in range(len(arr)):
        if arr[i] == x:
            y = x
            index = 1
    return x, index


print(lin_search([2, 4, 3, 5, 7, 2], 2))