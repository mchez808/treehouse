def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1


