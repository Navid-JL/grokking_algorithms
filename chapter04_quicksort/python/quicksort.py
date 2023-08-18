def quicksort(arr: list[int]):
    arr_length = len(arr)

    if arr_length < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


# test = [4, 2, 1, 5, 3]
print(quicksort([4, 2, 1, 5, 3]))
# print(test[:])
