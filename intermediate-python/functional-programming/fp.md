# sorting

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
