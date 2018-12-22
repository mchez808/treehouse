# sorting

How to sort lists without changing the list.

`sorted()` takes an iterable to sort and returns a new list from it.

If you need to customize the sorting, pass a function in as the `key` argument. There's an optional `reverse` argument that will cause the results to be reversed before they're returned.

`operator.itemgetter()` gets items from an object that supports that operation. We use it to get keys from dicts but it has other uses too.

`operator.attrgetter()` gets attributes from an object.

`from operator import attrgetter, itemgetter`

`key` is a `kwarg` to `sorted`

## itemgetter
`RAW_BOOKS` (below) is a dict
```
RAW_BOOKS = get_books('books.json', raw=True)
pub_sort = sorted(RAW_BOOKS, key=itemgetter('publish_date'))
print(pub_sort[0]['publish_date'], pub_sort[-1]['publish_date'])
```

## attrgetter
```
BOOKS = get_books('books.json')
pages_sort = sorted(BOOKS, key=attrgetter('number_of_pages'))
print(pages_sort[0].number_of_pages, pages_sort[-1].number_of_pages)
```

# map()
`map()` lets us apply transformations to each item in an iterable.

`map()` takes a function and an iterable. The function should take a single argument. This function will be applied, in order, to each item in the iterable and the result of that function will be returned to `map()`. In the end, `map()` will return a new iterable with the mutated values.

`[func(item) for item in iterable]` achieves the same result, plus turns the results into a list. For simple, single-serving applications, this is often a better choice since it's often more readable at a glance.

```
def sales_price(book):
    """Apply a 20% discount to the book's price"""
    book = copy(book)
    book.price = round(book.price*0.8, 2)
    return book
```
`map()` is effectively a list comprehension.

## equivalent expressions
### map()
sales_books = list(map(sales_price, BOOKS))
### list comprehension
sales_books2 = [sales_price(book) for book in BOOKS]

Treehouse [comprehensions workshop](http://teamtreehouse.com/library/python-comprehensions)
```
