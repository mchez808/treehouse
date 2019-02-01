Dictionaries

* DON'T have a `remove` method; you would use `del dict[key]`

Tuples can serve as dict keys!

```Py
dict.update({'a':1, 'b':2})
dict1.update(dict2)

def word_count(string):
    list_of_keys = string.lower().split()
    dict = {key: 0 for key in list_of_keys}
    for word in list_of_keys:
        dict[word] += 1
    return dict
```

# 1
take a single argument, which will be a dictionary of Treehouse teachers and their courses.
function should return an integer for how many teachers are in the dict.

```Py
dd = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
 'Kenneth Love': ['Python Basics', 'Python Collections']}
# Each key will be a Teacher and the value will be a list of courses.

def num_teachers(dict):
    return len(dict.keys())
```

# 2
receive the same dictionary as its only argument.
The function should return the total number of courses for all of the teachers.

```Py
from operator import add
from functools import reduce

def num_courses(dict):
    return reduce(add, map(len, dict.values()))
```

# 3
function courses, should return a single list of all of the available courses in the dictionary. No teachers, just course names!def most_courses(dict):


```Py
# solution 1
def courses(dict):
    uglylist = [value for value in dict.values()]
    flat_list = sum(uglylist, [])
    return flat_list

# solution 2
def courses(dict):
    uglylist = [value for value in dict.values()]
    flat_list = [item for sublist in uglylist for item in sublist]
    return flat_list
```

# 4
most_courses should return the name of the teacher with the most courses. You might need to hold onto some sort of max count variable.


```Py
def most_courses(dict):
    dict_teacher_numcourses = {teacher: len(list_courses) for teacher, list_courses in dict.items()}
    for teacher in dict_teacher_numcourses.keys():
        if dict_teacher_numcourses[teacher] == max(dict_teacher_numcourses.values()):
            yield teacher

ddd = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'], 'Kenneth Love': ['Python Basics', 'Python Collections'], 'Bob Marley': ['One Love', 'Buffalo Soldier', 'Satisfy My Soul', 'Redemption Song']}

# a one-line solution, by Chris Freeman
def most_courses(dict):
    return max((len(list_courses), teacher) for teacher, list_courses in dict.items())[1]

def stats(dict):
    return [[teacher, len(list_courses)] for teacher, list_courses in dict.items()]

```


In the `random` library, there's a function named `sample` that takes two arguments: an iterable to sample from, and an integer of how many unique samples to return.

Finish the `get_locations` function so that it returns 3 unique values from the `cells` argument.

```Py
import random

def get_locations(cells):
    return random.sample(cells, 3)
```

Our game's `player` only has two attributes, x and y coordinates. Let's practice with a slightly different one, though. This one has x, y, and "hp", which stands for hit points.

Our `move` function takes this three-part tuple `player` and a `direction` tuple that's two parts, the x to move and the y (like (-1, 0) would move to the left but not up or down).

Finish the function so that if the player is being run into a wall, their `hp` is reduced by 5. Don't let them go past the wall. Consider the grid to be 0-9 in both directions. Don't worry about keeping their `hp` above 0 either.

```Py
# EXAMPLES:
# move((1, 1, 10), (-1, 0)) # (0, 1, 10)
# move((0, 1, 10), (-1, 0)) # (0, 1, 5)
# move((0, 9, 5), (0, 1)) # (0, 9, 0)

def move(coordinates, change):
    x, y, hp = coordinates
    dx, dy = change
    x += dx
    y += dy
    if x < 0 or x > 9:
        hp -= 5
        x -= dx
    elif y < 0 or y > 9:
        hp -= 5
        y -= dy
    return x, y, hp
```


OK, here's a...weird...set of tiles. I need you to loop through TILES and print out each item. Print each item on the same line unless the item is a double pipe (||). In that case, instead of printing the item, print a new line (\n). Use the end argument to print() to control whether things print on a new line or not.

```Py
TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)

for tile in TILES:
    if tile == '||':
        print('')
    else:
        print(tile, end='')
```
