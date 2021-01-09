Functional Utilities

# Section 1 Contents

```Python
sorted()
    operator.itemgetter()
    operator.attrgetter()
map()
    [func(item) for item in iterable]  # list comprehension
filter()
    [item for item in iterable if func(item)] # list comprehension
any()
all()
```

# Section 2 Contents
```Python
functools
    functools.partial()
    functools.reduce()
        (recursion)
lambda
```


# sorted()

How to sort lists without changing the list.

`sorted()` takes an iterable to sort and returns a new list from it.

If you need to customize the sorting, pass a function in as the `key` argument. There's an optional `reverse` argument that will cause the results to be reversed before they're returned.

`key` is a `kwarg` to `sorted`

`from operator import attrgetter, itemgetter`

## itemgetter
`operator.itemgetter()` gets items from an object that supports that operation. We use it to get keys from dicts but it has other uses too.

```Python
# dict named RAW_BOOKS
RAW_BOOKS = get_books('books.json', raw=True)
pub_sort = sorted(RAW_BOOKS, key=itemgetter('publish_date'))
print(pub_sort[0]['publish_date'], pub_sort[-1]['publish_date'])
```

## attrgetter
`operator.attrgetter()` gets attributes from an object.

```Python
BOOKS = get_books('books.json')
pages_sort = sorted(BOOKS, key=attrgetter('number_of_pages'))
print(pages_sort[0].number_of_pages, pages_sort[-1].number_of_pages)
```

# map() and filter()

## map()
`map()` lets us apply transformations to each item in an iterable.

`map()` takes a function and an iterable. The function should take a single argument. This function will be applied, in order, to each item in the iterable and the result of that function will be returned to `map()`. In the end, `map()` will return a new iterable with the mutated values.

`[func(item) for item in iterable]` achieves the same result, plus turns the results into a list. For simple, single-serving applications, this is often a better choice since it's often more readable at a glance.

```Python
def sales_price(book):
    """Apply a 20% discount to the book's price"""
    book = copy(book)
    book.price = round(book.price*0.8, 2)
    return book
```

`map()` is effectively a list comprehension.

### equivalent expressions
using `map()`

sales_books = list(map(sales_price, BOOKS))

using a list comprehension

sales_books2 = [sales_price(book) for book in BOOKS]

Treehouse [comprehensions workshop](http://teamtreehouse.com/library/python-comprehensions)

### more on map()

from *DS From Scratch*: You can use `map` with multiple-argument functions
if you provide multiple lists:

```Python
def multiply(x, y):
    return x*y

products = list(map(multiply, [1, 2], [4, 5]))   # [1*4, 2*5] = [4, 10]
```
Note:
`map()` produces a generator which offers up one item at a time,
and `list(map())` simply unrolls the generator into a complete list.
The unrolling is necessary in this case, but not when `map` is used with `reduce`,
since `reduce` takes an iterable

[generators](http://anandology.com/python-practice-book/iterators.html)


## filter()

Filters are a very useful utility in programming, letting you refine a group of items into just the ones that meet your criteria. It's a "must be this tall to ride" sign for your data!

`filter()` takes a **function and an iterable**. The function, like with `map()`, takes only a single argument and is applied to each item in the iterable. If the function returns a truthy value for the item, the item is sent back to `filter()` which, ultimately, returns a new iterable of the filtered items.

You can achieve the same effect with `[item for item in iterable if func(item)]`. Again, like with `map()`, this can be more quickly readable for small applications.

### any() and all()

These work on lists, sets, and tuples.
(They may not work on dictionaries though, at least not as expected.)

`any(iterable)`

`all(iterable)`

Side note: `filterfalse()` is a function that works just like `filter()` but only returns things where the filter function gives back a `False` or non-truthy value. You can read more in the [documentation](https://docs.python.org/3/library/itertools.html#itertools.filterfalse).

```Python
def is_long_book(book):
    return book.number_of_pages >= 600

long_books = list(filter(is_long_book, BOOKS))
long_books2 = [book for book in BOOKS if book.number_of_pages >= 600]
```

# Functional Tools

## functools.reduce()

Think of it as a for-loop that has an outside value.

`functools.reduce()` will return whatever the function returns last, when it runs out of items in the iterable.

functools.reduce() takes a function and an iterable. The function, though, takes **two** arguments. The first time it runs, the two arguments will be the first two items in the iterable. Every time after that, the first argument will be the result of the last time the function was run. The second argument will be the next value from the iterable. When the iterable is out of items, reduce() will return whatever the function returned last.

Calling a function over again from within itself is known as recursion and it's what makes reduce() able to do its job.

```Python
from functools import reduce

def product(x, y):
    return x*y

print(reduce(product, [2, 3, 4, 5]))
# equivalent lambda expression
print(reduce(lambda x, y: x*y, [2, 3, 4, 5]))

# Think of it as a for-loop that has an outside value.
# because of reduce(), we don't have to write the following:
    total = 1
    for x in [1, 2, 3, 4, 5]
        total *= x
    print(total)
```

### A recursion example

It's handy to know that recursion is how `reduce()` operates.

```Python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
```

```Python
x_product = reduce(multiply, xs)
list_product = partial(reduce, multiply)
x_product2 = list_product(xs)
```

Another `reduce` example, from code challenge:

```Py
from functools import reduce
from operator import add

prices = [
    (6.99, 5),
    (2.94, 15),
    (156.99, 2),
    (99.99, 4),
    (1.82, 102)
]

# product_sales takes a single two-member tuple (price and units sold).
# product_sales returns the product.

def product_sales(tuple_value):
    price, units = tuple_value
    return price * units

print(product_sales((10.5, 2)))

map_of_products = map(product_sales, prices)
total = reduce(add, map_of_products)
```

note: `map_of_products` is a generator object
`type(map_of_products)  # <class 'map'>`
if you execute `list(map_of_products)`, then `map_of_products` gets emptied out.

```Py
>>> list(generator_of_products)
[34.95, 44.1, 313.98, 399.96, 185.64000000000001]
>>> list(generator_of_products)
[]
```

## Lambdas

Lambdas can't contain new lines (outside of containers) or assignments.
Lambdas have an implicit return.

### An example that's (hopefully) easy to understand 

Prerequisite: use of `map(function, iterable)`

Lambda is the *anonymous function*, a function without a name.
One would create a nameless function if you only use it once.

```Py
# add 1 to an iterable, WITHOUT a lambda
def add1(x):
    """add 1 to each element (broadcast addition)
    x : iterable
    return : iterable
    
    >>> add1([1, 2, 3])
    [2, 3, 4]
    """
    for i, _ in enumerate(x):
        x[i] += 1
    return x
```

Let's do this with a lambda function (add 1 to each element):

```Py
map1 = map(lambda x: x + 1, [1, 2, 3])
list(map1)

>>> [2, 3, 4]
```

That's lambda for you!

```Py
total = reduce(lambda x, y: x + y, [b.price for b in BOOKS])

long_books = list(filter(is_long_book, BOOKS))
# lambda equivalent
long_books = filter(lambda book: book.number_of_pages >= 600, BOOKS)
good_deals = filter(lambda book: book.price <= 6, BOOKS)
```


## functools.partial()

`functools.partial` lets you preset some arguments to a function. You can then call the new function with the remaining arguments as needed. This often ends up being really handy when used with map() and filter().

```Python
import functools

def exp(base, power):
    return base ** power

from functools import partial
two_to_the = partial(exp, 2)
print(two_to_the(3))

square_of = partial(exp, power=2)
print(square_of(5))
```

```Python
xs = [1, 2, 3, 4]

def double(x):
    return x*2

list_doubler = partial(map, double)
print(list(list_doubler(xs)))

def is_even(x):
    return x % 2 == 0

list_evener = partial(filter, is_even)
print(list(list_evener(xs)))
```

```Python
def double(x):
    return x*2

list_doubler = partial(map, double)
print(list(list_doubler(a)))
```

### Currying

> It starts to get messy if you curry arguments in the middle of functions, so we'll avoid this.
- Data Science From Scratch

> Currying is handy if you have to wait on future input.
> Currying is a technique you don't come across in Python very often. But, thanks to lambdas, we can implement it pretty easily.
- Kenneth Love, Treehouse
