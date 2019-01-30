# Let's play with the *args pattern.
# Create a function named multiply that takes any number of arguments. Return the product (multiplied value) of all of the supplied arguments. The type of argument shouldn't matter.
# Slices might come in handy for this one.

xs = 3,4,5

# (arguably / according to Guido) BEST!
from operator import mul

def multiply(*args):
    pass

# better
# from functools import reduce
# from operator import mul
#
# def multiply(*args):
#     return reduce(mul, args)


# good enough
# def multiply(*args):
#     product = 1
#     for i in args:
#         product *= i
#     return product


# ======================================================
# SOLUTION: moving asterisk into function call
# DON'T DO:  multiply(xs)  tuple PACKING is NOT done here
# DO THIS:  multiply(*xs)  tuple PACKING is done here!
# ======================================================

''' the additive equivalent
'''
# BEST!
sum(xs)

# better
from functools import reduce
from operator import add

# good enough
# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

sum = reduce(add, xs)
