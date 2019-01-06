
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

intermediate = map(product_sales, prices)
total = reduce(add, intermediate)
# Use map() to find the per-product totals for each item in prices,
# then use reduce (and add) to find the total value.

if total != (6.99*5) + (2.94*15) + (156.99*2) + (99.99*4) + (1.82*102):
    raise ValueError("sum is incorrect")
#########


# Finish the prereqs function so that it recursively finds all of the prerequisite
# course titles in courses (like "Object-Oriented Python" is a prerequisite for
# "Django Basics"). You should add() the title of the prerequisite to the pres set
#  and then call prereqs again with the child courses.
#
# In the end, return the prereqs set.
#
courses = {'count': 2,
           'title': 'Django Basics',
           'prereqs': [{'count': 3,
                     'title': 'Object-Oriented Python',
                     'prereqs': [{'count': 1,
                               'title': 'Python Collections',
                               'prereqs': [{'count':0,
                                         'title': 'Python Basics',
                                         'prereqs': []}]},
                              {'count': 0,
                               'title': 'Python Basics',
                               'prereqs': []},
                              {'count': 0,
                               'title': 'Setting Up a Local Python Environment',
                               'prereqs': []}]},
                     {'count': 0,
                      'title': 'Flask Basics',
                      'prereqs': []}]}

def prereqs(data, pres=None):
    pres = pres or set()
    list_of_dicts = data['prereqs']
    if list_of_dicts:
        for dict in list_of_dicts:
            pres.add(dict['title'])
            if dict['prereqs']:
                prereqs(dict, pres)
    return pres

required_courses = prereqs(courses)

# correct contents
{'Object-Oriented Python', 'Python Collections',
'Setting Up a Local Python Environment', 'Python Basics', 'Flask Basics'}

# incorrect contents
{'Django Basics'}

####################

# Use a lambda and filter() to create a variable named high_cal with only the items in meals where the "calories" value is greater than 1000.

meals = [
    {'name': 'cheeseburger',
     'calories': 750},
    {'name': 'cobb salad',
     'calories': 250},
    {'name': 'large pizza',
     'calories': 1500},
    {'name': 'burrito',
     'calories': 1050},
    {'name': 'stir fry',
     'calories': 625}
]

high_cal = filter(lambda dict: dict['calories'] > 1000, meals)

####################

# Use reduce() and a lambda to find the longest string in strings. Save this value in the variable longest.
# Remember, reduce() takes two arguments and
# you can write an if statement like: give_me_this if this_thing > that_thing else give_me_that.

from functools import reduce

strings = [
    "Do not take life too seriously. You will never get out of it alive.",
    "My fake plants died because I did not pretend to water them.",
    "A day without sunshine is like, you know, night.",
    "Get your facts first, then you can distort them as you please.",
    "My grandmother started walking five miles a day when she was sixty. She's ninety-seven now and we don't know where she is.",
    "Life is hard. After all, it kills you.",
    "All my life, I always wanted to be somebody. Now I see that I should have been more specific.",
    "Everyone's like, 'overnight sensation.' It's not overnight. It's years of hard work.",
]

reduce(lambda x, y: x if len(x) > len(y) else y, strings)
# equivalent to this lambda expression
def longer(s1, s2):
    return s1 if len(s1) > len(s2) else s2
reduce(longer, strings)

####################

from functools import partial

prices = [
    10.50,
    9.99,
    0.25,
    1.50,
    8.79,
    101.25,
    8.00
]

def discount(price, amount):
    return price - price * (amount/100)

discount_10 = partial(discount, amount=10)
