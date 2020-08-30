```Py
even_numbers = [x for x in range(5) if x % 2 == 0]
squares = [x**2 for x in range(0,5)]
even_squares = [x**2 for x in range(5) if x % 2 == 0]
```

turn lists into dictionaries or sets
```Py
square_dict = { x : x*x for x in range(5) }
square_set = {x * x for x in [-1, 1, 3, -3, -5, 5]}

zeroes = [0 for _ in even_numbers]  # same length as even_numbers
```

list comprehensions can include more than one "for"
```Py
pairs = [(x, y)
         for x in range(10)
         for y in range(10)]   # 100 pairs (0,0), (0,1), ... (9,8), (9,9)

increasing_pairs = [(x, y)
                    for x in range(10)
                    for y in range(x + 1, 10)]
```

## enumerate

```Py
list(enumerate("abc"))

for i, document in enumerate(documents):
    do_something(i, document)

for i, _ in enumerate(documents): do_something(i)  # Pythonic way of coding
```

## generators

Two ways to create a generator: 

using `yield`:

```Py
def lazy_range(n):
    """a lazy version of range()"""
    i = 0
    while i < n:
        yield i
        i += 1
```

(In Python 3, `range` is lazy, but the point was to demonstrate an example of creating a generator.)

another way is using a `for` comprehension *wrapped in parentheses*:

```Py
lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)
```

### zip

```Py
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zippy = zip(list1, list2)
list(zippy)  # returns [('a', 1), ('b', 2), ('c', 3)]
list(zippy)  # returns []
# if you repeat a function call on a generator, often you'll find that the generator has been emptied.
zippys = zip(list1, [1, 2, 3, 4, 5, 6, 7])
list(map(lambda x: x*2, zippys))  # [('a', 1, 'a', 1), ('b', 2, 'b', 2), ('c', 3, 'c', 3)]
# note: the shorter list length becomes the zip-list length
```

"unzip" (strange trick)

```Py
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
```

### argument unpacking

The asterisk performs *argument unpacking*, which uses the elements of `pairs` as 
individual arguments to `zip`. It ends up the same as this:

```Py
zip(('a', 1), ('b', 2), ('c', 3))
# returns [('a', 'b', 'c'), (1, 2, 3)]
```

def add(a, b): return a + b

add(1, 2)     # returns 3
add(*[1, 2])  # returns 3
add([1, 2])  # ERROR

# args and kwargs

```Py
def magic(*args, **kwargs):
    print("unnamed args: ", args)
    print("keyword args: ", kwargs)

magic(1, 2, key="word", key2="word2")
magic(3, 4, brick="house", mortal="kombat")
```

It works the other way too:

```Py
def reverse_magic(x, y, z):
    return x + y + z

x_y_list = [1, 2]
z_dict = {"z": 3}

reverse_magic(*x_y_list, **z_dict)

```
