fruits = {
    "Apple": 2.99,
    "Orange": 3.00,
    "Banana": 5.24,
    "Grapes": 4.76,
}

user_input = input(
    f"Choose a fruit from {','.join([fruit for fruit in fruits])}\n:")

print(fruits[user_input.strip().lower().title()])
