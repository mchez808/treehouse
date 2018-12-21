# Code challenges

from operator import itemgetter

fruit_list = [
    ('apple', 2),
    ('banana', 5),
    ('coconut', 1),
    ('durian', 3),
    ('elderberries', 4)
]

sorted_fruit = sorted(fruit_list, key=itemgetter(1))
