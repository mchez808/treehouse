# Python III at Free Geek

## OOP

attributes of a "bed" object:

- is_made (boolean)

methods:

- make()

- sleep()


see bedroom.py


preview to OOP; memory address pointing
====


## pass by value
  passing a copy of the object
## pass by reference
  not passing a copy of the object, but the object itself

```Python
a = 5
print(a)
print(id(a))  # where the variable 'sits in memory'

l = [1,2,3]
print(id(l))  # the ID of a list looks no different from that of an int

a = 5
print(a)
print(id(a))  # does the assignment operator create a new object and change the references?
a = 10
print(a)
print(id(a))  # check and see...
```

...
Yes it does.

BUT in the case of an int.

```Py
l = [1,2,3]
print(id(l))
l[1] = 7
print(id(l))
```

Here Python does not demolish the house at the old address; it modifies it

```Py
l = [1,2,3]
l.append(4)  # this modifies the old address; doesn't construct a new one

def printer(num):
  num = num[:]  # makes a copy

print(l)
print(id(l))
```
