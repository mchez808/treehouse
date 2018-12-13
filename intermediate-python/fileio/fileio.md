# Python File I/O

(Reference: [see File I/O docs](https://docs.python.org/3/library/functions.html#open))

# Writing to Files

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

# Reading from Files

## The context manager pattern

Read the entire contents of the file

### as one stream
```
with open("my_file.txt", "r") as file:
    file.read()
```

### line-by-line
```
with open("my_file.txt", "r") as file:
    for line in file:
        print(line)
```

### limiting characters read

```
file = open("my_file.txt", mode="r")`

file.read(5)`

```

Move the read/write pointer to another part of the file.

`file.seek(0)  # goes back to file start`

~~You can control the number of `bytes` read by passing in an integer.

~~file.read(bytes=-1)` is the same as `file.read()`

### `readline()`

Read one line

`a1 = file.readline()`

### `readlines()`

Read the entire file into a list, with each line as a list item.

`file.readlines()`


For more on [sys.argv, check out the docs](https://docs.python.org/3/library/sys.html#sys.argv)

