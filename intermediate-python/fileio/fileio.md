# Python File I/O

(Reference: [see File I/O docs](https://docs.python.org/3/library/functions.html#open))

## Writing to Files

```
open(filename, mode="r")

# write "hello world" to whatever file the file variable points at.

file.write("hello world")

# close the pointer to the file file.

file.close()
```

The two most common modes or flags for writing are "w", for truncating and then writing, and "a" for appending to the file.

The context manager pattern for dealing with files is:

```
with open("my_file.txt", "a") as file:

    file.write("Hello world")
```

## Reading from Files

`open("my_file.txt", mode="r")`


Read the entire contents of the file.

`file.read(bytes=-1)`

You can control the number of bytes read by passing in an integer.


Move the read/write pointer to another part of the file.

`file.seek() `


Read the entire file into a list, with each line as a list item.

`file.readlines()`

### The context manager pattern

```
with open("my_file.txt", "r") as file:
    file.read(10)
```

For more on [sys.argv, check out the docs](https://docs.python.org/3/library/sys.html#sys.argv)

