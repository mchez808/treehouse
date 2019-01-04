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


# Using c_to_f and a list comprehension, create a variable named good_temps.
# Convert each Celsius temperature into Fahrenheit,
# but only if the Celsius temperature is between 9 and 32.6.

temperatures = [
    37,
    0,
    25,
    100,
    13.2,
    29.9,
    18.6,
    32.8
]


def c_to_f(temp):
    """Returns Celsius temperature as Fahrenheit"""
    return temp * (9/5) + 32

def is_in_domain(temp_celsius):
    """but only if the Celsius temperature is between 9 and 32.6"""
    return 9 <= temp_celsius and temp_celsius <= 32.6

good_temps = [c_to_f(temp) for temp in temperatures if is_in_domain(temp)]


#########
from functools import reduce
from operator import add

prices = [
    (6.99, 5),
    (2.94, 15),
    (156.99, 2),
    (99.99, 4),
    (1.82, 102)
]

# Let's start by writing a function named product_sales that takes a single two-member tuple made up of a price and a number of units sold. product_sales should return the product of the price and the number of units.

def product_sales(tuple_value):
    price, units = tuple_value
    return price * units

print(product_sales((10.5, 2)))

total = list(map(product_sales, prices))
product_sum = reduce(add, total)
# Use map() to find the per-product totals for each item in prices,
# then use reduce (and add) to find the total value.

if product_sum != (6.99*5) + (2.94*15) + (156.99*2) + (99.99*4) + (1.82*102):
    raise ValueError("sum is incorrect")
#########
