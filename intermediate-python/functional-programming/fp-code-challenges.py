# Code challenges

# itemgetter

from operator import itemgetter

fruit_list = [
    ('apple', 2),
    ('banana', 5),
    ('coconut', 1),
    ('durian', 3),
    ('elderberries', 4)
]

sorted_fruit = sorted(fruit_list, key=itemgetter(1))

# attrgetter

import datetime
from operator import attrgetter

# Use sorted() and attrgetter() to sort date_list
# by the day attribute of each datetime object.
# Save this sorting into a variable named sorted_dates.

date_list = [
    datetime.datetime(2015, 4, 29, 10, 15, 39),
    datetime.datetime(2006, 8, 15, 14, 59, 2),
    datetime.datetime(1981, 5, 16, 2, 10, 42),
    datetime.datetime(2012, 8, 9, 14, 59, 2),
]

# Use sorted() and attrgetter() to sort date_list by the day attribute of each
# datetime object.

# Save this sorting into a variable named sorted_dates.
sorted_dates = sorted(date_list, key=attrgetter('day'))
