# generator objects

This is a special kind of object that has a value, a pointer to the current index, and a __next__ method (ooh, special method!) that knows how to get the next item from the iterable.

# generator objects, vs generators unrolled into list
products = list(map(multiply, [1, 2], [4, 5]))   # [1*4, 2*5] = [4, 10]
```
Note:
`map()` produces a generator which offers up one item at a time,
and `list(map())` simply unrolls the generator into a complete list.
The unrolling is necessary in this case, but not when `map` is used with `reduce`,
since `reduce` takes an iterable

[generators](http://anandology.com/python-practice-book/iterators.html)

```Py
def get_numbers():
    numbers = [4, 8, 15, 16, 23, 42]
    for number in numbers:
        yield number
```
### yield

Briefly, `yield` lets you send data back out of a function without ending the execution of the function.
If we call this function, `get_numbers()`, we'd have a generator object.

`numbers = get_numbers`

We can do next(numbers) and we'd get 4, then 8, then 15, and so on.

### yield from

Since we're just returning values from an iterable, we can use `yield from` to skip the entire for loop:

def get_numbers():
    numbers = [4, 8, 15, 16, 23, 42]
    yield from numbers
