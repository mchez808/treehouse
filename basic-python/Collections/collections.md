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
