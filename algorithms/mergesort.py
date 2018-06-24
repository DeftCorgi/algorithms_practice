def mergesort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = mergesort(items[:mid])
    right = mergesort(items[mid:])

    i, j, k = [0] * 3
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            items[k] = left[i]
            i += 1
        else:
            items[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        items[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        items[k] = right[j]
        j += 1
        k += 1

    return items


print(mergesort([5, 4, 6, 2, 1, 2, 3, 4]))
