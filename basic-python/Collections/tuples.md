# tuples

(Kenneth Love pronounces them as "tuh-pulls")

You can use `del` to delete an entire tuple.
You cannot delete just a single item from the tuple, though, of course, since tuples are immutable.

You can change mutable members of tuples, such as lists.

### memory footprint

Tuples have a fixed size in memory, great for reducing the memory footprint of a script.

```Py
valid_tupple = (1, 2, 3)
valid_tupple = 1, 2, 3
valid_tupple = tuple([1, 2, 3])
```

## tuple swapping

### big advantage: simultaneous assignment

This allows us to swap values around, or assign many values at once.

```Py
a = 5
b = 20
a, b = b, a
```

# tuple packing

```Py
def add(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

def multiply(*args):
    product = 1
    for num in args:
        product *= num
    return product
```
