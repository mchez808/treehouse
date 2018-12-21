# Unit 1: Instant Objects

```
super()

instance.__class__.__name__
isinstance()
issubclass()
```

Methods and Method Args:

`self` is the very common convention for the instance argument.
The first argument has to represent the instance. 
You can use default values, `*args`, and `**kwargs` all you want!

# Unit 2: Inheritance

## Complex Relationships

Inheritance in Python is both easier and harder than in some other languages. 
Python's inheritance usually works exactly how you expect it to. 
But thanks to things like the "*method resolution order (MRO)*", 
sometimes it's not that simple.

## Super Duper

The `super()` function lets us call a bit of code from the parent class inside our own class.
This is really helpful when you need to override a method from the superclass, 
defining your own version, but keep the effects of the parent class's version of the code.

## Multiple Superclasses
We're not limited to a single parent class in Python. 
Make your code even more clean and clear.
When you're using multiple inheritance, `super()` calls become really important. 
They let things like `__init__` travel all the way up the chain to make sure the
class has all of the bits and pieces that it needs.

* `isinstance(<object>, <class>)` - This function will tell you whether or not <object> is an instance of <class>.

* If it could be an instance of several classes, you can use a tuple of classes: 

* * `isinstance(<object>, (<class1>, <class2>, <class3>))`

* `issubclass(<class>, <class>)` - This function will tell you whether or not one class is a descendant of another class. Just like isinstance(), you can use a tuple of classes to compare against.

```
instance.__class__

instance.__class__.__name__
```

# Unit 3: Advanced Objects

06 Sep 2018 Thursday

### Basic conversion between types:

```
class NumString:
     def __init__(self, value):
         self.value = str(value)
 
 def __str__(self):
     return str(self.value)
 
 def __int__(self):
     return int(self.value)
 
 def __float__(self):
     return float(self.value)
```

## Emulating Built-ins

```
yield

yield from
```

What if we want our classes to act like a list or a dict?

By emulating built-ins, you can make a class that's iterable but not searchable, or vice versa. This gives you a lot of control over how your classes are used.

### generator

```
def __iter__(self):
     for item in self.slots:
          yield item
```

`yield` sends items out of the method, as they're available, just like return
but unlike return, it keeps on working
This construct (function or method) is a generator

```
# Equivalent expression
def __iter__(self):
    yield from self.slots
```

example

```
class Double(int):
     def __new__(*args, **kwargs):
          self = int.__new__(*args, **kwargs)

          self = self*2
          return self
```

## Subclassing Built-ins

What if a built-in class has most of what you need? Here's how to customize them to fit exactly your needs.
Completely subclassing built-ins isn't the easiest skill in the world.
Just because immutable types expect you to override `__new__` doesn't mean you can't use `__init__` on them. 
They still call the method but you can't change the initialization of the object in them.

## Constructicons

What if we need something more complex than just a custom init or new method?

Constructors, as most classmethods would be considered, are a common sight in other languages.
They're less common in Python but still really useful. 
I highly recommend playing around with them outside of this course and getting comfortable with them.

As for `staticmethods`, they're...weird. 
A staticmethod is a method that doesn't require an instance (self) or a class (cls). 
So they belong to a class because, logically, they belong there. 
Most of the time, though, you're better served by just creating a function in the same module as your class.
Without being a `classmethod` , we could write the exact same method with a few differences,
like using `self` instead of `cls`, and then leave off the decorator. 
We'd have to create an instance of the class first, though. 
It'd look something like this ([Teacher's Notes](https://teamtreehouse.com/library/constructicons)).

We have to create the instance first, and then call the method. By using a class method, we move the instance creation into the method where it makes more sense. It's a small and fairly subtle design decision but it makes for a nicer interaction in the end.

## Special Methods

**Special Methods** (of access control): Most Python programmers see a method or attribute prefixed with _ and leave it alone. That goes doubly so for methods or attributes with a double underscore preceding but not trailing (__avoided, not __avoided__).

# Unit 4: Practice OOP Coding - Dice Game

## Comparisons using Magic Methods

Comparing and Combining Dice

If you want to get a lot of magic method goodies easily, [check out attrs](https://attrs.readthedocs.io/). It's a solid library and makes a lot of common usages much easier.

Or, to stick with the standard library, check out [the docs for functools.total_ordering](https://docs.python.org/3/library/functools.html#functools.total_ordering). You need to define __eq__ and then one of the other operations and Python will figure out the rest.

