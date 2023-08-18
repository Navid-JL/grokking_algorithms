def sum(arr: list[int]) -> int:
    arr_length = len(arr)
    if arr_length == 1:
        return arr[0]
    else:
        last_element = arr.pop()
        return last_element + sum(arr)


def count(arr: list[int]) -> int:
    arr_length = len(arr)
    if arr_length == 1:
        return 1
    else:
        arr.pop()
        return 1 + count(arr)


def max(arr: list[int]) -> int:
    arr_length = len(arr)

    if arr_length == 1:
        return arr[0]
    else:
        m = max(arr[1:])
        return m if m > arr[0] else arr[0]


# list1 = [[1, 2, 3], [4, 5, 6]]
# flattened_list = [element for sublist in list1 for element in sublist]
# print(flat_list)

# print(max([4, 3, 10, 2]))
squares = (x * x for x in range(1000))
for i in squares:
    print(i)
