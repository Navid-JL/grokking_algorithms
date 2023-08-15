def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    arr_length = len(arr)
    for i in range(1, arr_length):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_array = []
    arr_length = len(arr)
    for i in range(arr_length):
        smallest = find_smallest(arr)
        new_array.append(arr.pop(smallest))
    return new_array


print(selection_sort([14, 2, 1, 5, 4]))
