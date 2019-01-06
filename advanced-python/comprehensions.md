Examples

list comprehension

```Py
>>> [num * 2 for num in range(1, 6)]
[2, 4, 6, 8, 10, 12]
```

dict comprehension

```Py
>>> {letter: num for letter, num in zip('abcdef', range(1, 7))}
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
```

set comprehension

```Py
>>> {num * 2 for num in [5, 2, 18, 2, 42, 2, 2]}
{84, 10, 4, 36}
```

[Some docs about comprehensions](https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions)

More examples!

```Py
factors_of_3 = [n for n in range(1, 101) if n % 3 == 0]

rows = range(3)
columns = range(5)
[(x, y) for y in rows for x in columns]
```
`>>> [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (1, 1), ...`

> The inner iterable is looped through first, and then the outer iterable.
> So the inner one goes all the way through for each trip that the outer one takes.

In my words: in this example above, first, one column is completely looped through.
And then Python moves on to the next row, and then proceeds with another column.

```Py
[(letter, number) for number in range(1, 5) for letter in 'abc']
```

`>>> [(a, 1), (b, 1), (c, 1), (a, 2), (b, 2), ..., (b, 4), (c, 4)]`

```Py
{student: points for student, points in zip(['Mark', 'Bob', 'Sam'], [123, 211, 9000])}


total_nums = range(1, 101)
fizzbuzzes = {
    'fizz': [n for n in total_nums if n % 3 == 0],
    'buzz': [n for n in total_nums if n % 7 == 0]
}


{round(x/y) for y in range(1, 11) for x in range(2, 21)}  # set: unique values
[round(x/y) for y in range(1, 11) for x in range(2, 21)]  # list: repeated values


fizzbuzzes = {key: set(value) for key, value in fizzbuzzes.items()}
fizzbuzzes['fizzbuzz'] = {n for n in fizzbuzzes['fizz'].intersection(fizzbuzzes['buzz'])}
fizzbuzzes['fizzbuzz']
```
