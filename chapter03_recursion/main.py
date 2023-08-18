def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


def greet2(name):
    print("how are you, ", name, "?")


def bye():
    print("ok bye!")


def greet(name):
    print("hello, ", name, "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()


def binary_search(arr, target):
    if not arr:
        return -1

    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2

    if arr[mid] == target:
        return target
    elif arr[mid] > target:
        return binary_search(arr[:mid], target)
    else:
        return binary_search(arr[mid + 1:], target)
