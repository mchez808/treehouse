Functional Utilities

Contents
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

## filter()

Filters are a very useful utility in programming, letting you refine a group of items into just the ones that meet your criteria. It's a "must be this tall to ride" sign for your data!

`filter()` takes a **function and an iterable**. The function, like with `map()`, takes only a single argument and is applied to each item in the iterable. If the function returns a truthy value for the item, the item is sent back to `filter()` which, ultimately, returns a new iterable of the filtered items.

You can achieve the same effect with `[item for item in iterable if func(item)]`. Again, like with `map()`, this can be more quickly readable for small applications.

I mentioned `filterfalse()`. This function works just like `filter()` but only returns things where the filter function gives back a `False` or non-truthy value. You can read more in the [documentation](https://docs.python.org/3/library/itertools.html#itertools.filterfalse).

```Python
def is_long_book(book):
    return book.number_of_pages >= 600

long_books = list(filter(is_long_book, BOOKS))
long_books2 = [book for book in BOOKS if book.number_of_pages >= 600]
```

# import functools

Contents
```Python
functools
    functools.partial()
    functools.reduce()
```

## functools.partial()

# Functional Tools

```Python
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

## functools.reduce()

```Python
from functools import reduce
x_product = reduce(multiply, xs)
list_product = partial(reduce, multiply)
x_product2 = list_product(xs)

def double(x):
    return x*2

list_doubler = partial(map, double)
print(list(list_doubler(a)))
```
