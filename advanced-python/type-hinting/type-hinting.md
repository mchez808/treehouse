# Type Hinting: Built-In Types

PyCharm allows for variable annotations

```Py
# either int or float
def add1(a: complex, b: complex) -> complex:
    return a + b

# int or float, but not imaginary numbers
from numbers import Real
def add2(a: Real, b: Real) -> Real:
    return a + b

# return None (aka void, in other languages)
def hello() -> None:
    print("Hello world!")
```

# Type Hinting: Generics

### `typing.List` type

```Py
from typing import List

class Recipe:
    def __init__(self, title: str):
	self.title: str = title
	self.ingredients: List[RecipeIngredient] = []
	self.steps: List[RecipeStep] = []
```

If we don't want to define a default value for the variable, 
we can just name it and hint it.

`	self.order: int  # not followed by equals sign`

^ This is 100% semantic sugar; it does not create the variable in Python

### `typing.Union` type

`Union` lets you specify 2+ valid types

```Py
from typing import Union

class RecipeIngredient:
    def __init__(self, ingredient: Union[Ingredient, str])
        pass
```

### `typing.Optional` type

it can include `None`

It's great for places where you have arguments that can be left out.

```
from typing import Optional

class RecipeIngredient:
    def __init__(self, ingredient: Union[Ingredient, str], 
        measurement: Optional[str]=None)
```

### others

```
typing.Mapping
typing.Sequence
```

# More Resources 

## PEPs related to type-hinting:

* PEP 3107

* PEP 484

* PEP 526

## Other resources

* [ `typing` module docs](https://docs.python.org/3/library/typing.html)

* * [generics in typing module](https://docs.python.org/3/library/typing.html#generics)

* [mypy](http://mypy-lang.org/), the Python static type checker

