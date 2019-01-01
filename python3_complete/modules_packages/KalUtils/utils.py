def is_even(item):
    if (type(item) == int):
        return item % 2 == 0
    if (type(item) == str):
        return len(item) % 2 == 0
