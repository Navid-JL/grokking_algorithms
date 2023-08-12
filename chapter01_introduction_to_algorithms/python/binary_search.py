from array import array

numbers_list = array('i', [4, 5, 7, 2, 1, 3, 6, 8, 10, 9])


def binary_search(sorted_array: list, element: int) -> int:
    """Searches an element in a sorted array

    Args:
        sorted_array (array): [1,2,3,4,...]
        element (int): 2

    Returns:
        int: The index of the element in the sorted array
    """
    low = 0
    high = len(sorted_array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_array[mid]
        if guess == element:
            return mid
        elif guess > element:
            high = mid - 1
        else:
            low = mid + 1
    return None
