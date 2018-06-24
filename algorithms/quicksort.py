# a = [20, 6, 4, 23, 8, 6, 10, 13, 4, 7, 12, 3, 78, 44]
a = [5, 4, 3, 2, 1, 0, -9, -8, -23, 21, 4]


def partition(arr, start, end):
    pindex = (start + end)//2
    pivot = arr[pindex]
    left = start

    # swap pivot with end
    swap(arr, pindex, end)
    for i in range(start, end):
        if arr[i] <= pivot:
            swap(arr, i, left)
            left += 1
    swap(arr, end, left)
    return left


def quicksort(arr, start=0, end=None):
    # base cases
    if end == None:
        end = len(arr) - 1

    if start < end:
        p_index = partition(arr, start, end)
        # quick sort both sides of arr
        quicksort(arr, start, p_index-1)  # first half
        quicksort(arr, p_index + 1, end)  # second half


def swap(arr, a, b):
    temp = arr[b]
    arr[b] = arr[a]
    arr[a] = temp


quicksort(a)
print(a)
