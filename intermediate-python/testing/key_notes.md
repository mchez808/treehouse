## Using Coverage.py with unittest

`pip install coverage`

Make sure your test file contains `unittest.main()` 
(i.e., that it can be run from the command line without the -m unittest argument.)

`coverage run tests.py`

Generate a report (in command line) 

`coverage report`

 or 

`coverage report -m`

(if you want the missed lines.)

Reference: [coverage.py documentation](http://nedbatchelder.com/code/coverage/)

*note: the command line switch -m*

e.g.  `python -m unittest`

In the case and context of Python:

> This allows modules to be located using the Python module namespace for execution as scripts. 
> So you can specify any module in Python's search path this way, not just files in the current directory.
> A module located using -m is executed just as if its filename had been provided on the command line

### HTML Coverage Reports

`coverage html`

This will generate the HTML report. By default, it'll live in the htmlcov/ directory.
To serve HTML files (and CSS, JS, etc) directly from Python, we used the http.server module by typing (in cmd) 

`python -m http.server`

[http.server documentation](http://nedbatchelder.com/code/coverage/)

# unittest - Advanced Topics

## Error Testing

```
assertRaises()
assertLogs()
assertWarns()
```

assertRaises(x) - Make sure the following code raises the x exception.

For these advanced topics, you want to refer to the [unittest documentation](https://docs.python.org/3/library/unittest.html)

### @unittest.expectedFailure

You can use @unittest.expectedFailure on tests that you know will fail. 

```Python
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
```


# unittest - Intermediate Topics


### with 

`with` is a context manager.  It will execute something within a limited pre-defined context.
> The "with" statement makes try/finally statements a whole lot easier.

Structure: 

```Python
with EXPRESSION as NAME:
    BLOCK
```

Example:

```Python
with assertRaises(ValueError):
    int('a')
```

Another Example:

```Python
def opened(filename, mode = 'r'):
    f = open(filename, mode):
        try:
             Do some code
        finally:
             f.close()
```

### setUp()

`setUp()` - Method that is run before each test. Use this to set up state for the tests

```Python
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')
```

### unittest notes from code challenge

```Python
import unittest
from string_fun import get_anagrams
class AnagramTestCase(unittest.TestCase):
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            get_anagrams("")
```

### setUp(): a challenging real example (for unittest)

taken from tests.py, which tests dice.py

```Python
class RollTests(unittest.TestCase):
    def setUp(self):
        self.hand1 = dice.Roll('1d2')
        self.hand3 = dice.Roll('3d6')

    def test_adding(self):
        self.assertEqual(self.hand1+self.hand3,
                         sum(self.hand1.results)+sum(self.hand3.results))
```
# unittest - novice topics

### New Terms (topic: unittest)

```
assertIn(x, y)
assertNotIn(x, y)
assertIsInstance(x, y)
assertGreaterEqual(x, y)
assertLessEqual(x, y)
```

assertIn(x, y) - Make sure x is a member of y (this is like the in keyword)

assertNotIn(x, y) - example: `self.assertNotIn("code", get_anagrams("treehouse"))`

assertIsInstance(x, y) - Make sure x is an instance of the y class

assertGreaterEqual(x, y) - Make sure x is greater than or equal to y

assertLessEqual(x, y) - Make sure x is less than or equal to y

```Python
from string_fun import get_anagrams

class AnagramTests(unittest.TestCase):
    def test_in_anagrams(self):
        all_anagrams = get_anagrams("treehouse")
        self.assertIn("house", all_anagrams)

    def test_not_in_anagrams(self):
        self.assertNotIn("code", all_anagrams)

import unittest

from string_fun import is_palindrome

class PalindromeTestCase(unittest.TestCase):
    def test_good_palindrome(self):
        self.assertTrue(is_palindrome("tacocat"))

    def test_bad_palindrome(self):
        self.assertFalse(is_palindrome("asdf"))
```

# unittest - very basics

```Python
assertEqual(x, y)
assertNotEqual(x, y)
assertGreater(x, y)
assertLess(x, y)
```

assertEqual(x, y) - Make sure x and y are equal.  (*note: assert_equals # also appears, maybe Python 2?*)

assertNotEqual(x, y) - Make sure x and y are not equal

assertGreater(x, y) - Make sure x is greater than y

assertLess(x, y) - Make sure x is less than y


### Your First unittest Test Case

Most of the power of testing in Python comes from the `unittest` framework and its `TestCase` class.

```Python
import unittest
class SimpleTestCase(unittest.TestCase):
    def test_ten_minus_ten(self):
        assert 10 - 10 == 0
```

### New Terms

`unittest` - Python's library for writing tests

`TestCase` - A collection of tests

Running tests

* Running tests in Command Line: `python -m unittest tests.py`

* Running tests in a Script: `unittest.main()`
 
Remember, all tests in a TestCase have to start with the word `test_` to be run.

You can have methods that don't start with test_ for other purposes if you need them.

Reference: [unittest docs](https://docs.python.org/3/library/unittest.html)

## Writing and Running Doctests

Doctests are the simplest tests to write in Python since they're written in plain text in the docstrings you're already writing for your code.

### New terms

`doctest` - A test written in a docstring.

`doctest library` - The built-in Python library for running doctests.

### example

```Python
def average(num_list):
    """Return the average for a list of numbers
    >>> average([1, 2])
    1.5
    
    """
    return sum(num_list) / len(num_list)
Running doctests
From the command line
python -m doctest your_script.py
From inside a script
if __name__ == '__main__':
    import doctest
    doctest.testmod()
doctest documentation
```

Reference: [URL to Evernotes](https://www.evernote.com/client/web?login=true#?anb=true&b=3a6bccbd-06a7-49d5-9cb3-ce0eb89f0680&n=c2481594-341f-4e00-b728-832e968a8f69&s=s516&)
