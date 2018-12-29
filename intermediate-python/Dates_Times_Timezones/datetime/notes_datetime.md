
# datetime

```Py
import datetime

date1 = datetime.datetime(2011, 12, 25)
date2 = datetime.date(2011, 12, 25)

time = datetime.time(8, 15)

time.hour
date1.year
```

## basics methods in datetime.datetime:

```Py
.now()
.replace()
```

### .now()

`now = datetime.datetime.now()`

Create a new variable called two that holds the value of now with the hour set to 14.

### .replace()

`two = now.replace(hour=14)`

## datetime.timedelta

timedelta objects represent gaps in time. They are returned when you subtract one datetime from another. They can also be assigned to a variable and then used to augment datetime objects.

`timedelta` objects represent **durations of time**. You can make them directly, or get them by subtracting one datetime from another.

Create a timedelta that goes back 5 minutes.

`datetime.timedelta(minutes=-5)`

Add 30 days to a datetime.

```Py
y2k = datetime.datetime(2000, 1, 1)
y2k + datetime.timedelta(30)
y2k + datetime.timedelta(hours=5)
```

Q: Which attribute is not available on a timedelta?  Answer: years

### challenge

Write a function called far_away that takes one argument, a timedelta.
Add that timedelta to datetime.datetime.now() and return the resulting datetime object.

```Py
def far_away(timedelta):
    return datetime.datetime.now() + timedelta
```

## .now() and .today() methods

These are seemingly equal.
`datetime.datetime.now().second == datetime.datetime.today().second`

### challenge

Write a function named minutes that takes two datetimes and, using `timedelta.total_seconds()` to get the number of seconds, returns the number of minutes, rounded, between them. The first will always be older and the second newer. You'll need to subtract the first from the second.

```Py
def minutes(dt1, dt2):
    return int(round(datetime.timedelta.total_seconds(dt2 - dt1) / 60, 0))

t1 = datetime.datetime(2018, 5, 15, 7, 15)
t2 = datetime.datetime(2018, 5, 15, 8, 45)
```

### Advanced Challenge

(Step 1 of 3) Create a function named is_over_13 that takes a datetime and returns whether or not the difference between that datetime and today is 4745 days or more.

```Py
import datetime
today = datetime.datetime.today()

def is_over_13(datetime):
    return (today - datetime).days > 4745

# to test this: create a datetime 20 years before today
dt1998 = today.replace(year=1998)
is_over_13(dt1998)
```


# strftime and strptime

turning your `datetime` objects into specific strings, or creating `datetime` objects from strings

strftime - Method to create a string from a datetime

strptime - Method to create a datetime from a string according to a format string

### Links:

* [strftime/strptime guide](https://docs.python.org/3/library/datetime.html?highlight=datetime#strftime-and-strptime-behavior)

* [strftime reference sheet](http://strftime.org/)

### challenge

(1/2) [Create a function named to_string that takes a datetime and gives back a string in the format "24 September 2012".](https://teamtreehouse.com/library/dates-and-times-in-python/dates-and-times/strftime-strptime)

```Py
## Examples
# to_string(datetime_object) => "24 September 2012"

def to_string(datetime):
    return datetime.strftime("%d %B %Y")
```

(2/2) Create a new function named from_string that takes two arguments: a date as a string and an strftime-compatible format string, and returns a datetime created from them.

```Py
## Examples
# from_string("09/24/12 18:30", "%m/%d/%y %H:%M") => datetime

def from_string(date_string, strftime_string):
    return datetime.datetime.strptime(date_string, strftime_string)
```

### challenge

Write a function named time_tango that takes a date and a time.
It should combine them into a datetime and return it.

```Py
def time_tango(date, time):
    return datetime.datetime.combine(date, time)

# .combine() is more compact, but otherwise functionally equivalent to this:
    # return datetime.datetime(date.year, date.month, date.day, time.hour, time.minute)
```

### Advanced Challenge

(Step 2 of 3) Now create a function named date_string that takes a datetime and returns a string like "May 20" using strftime. The format string is "%B %d".

```Py
def date_string(datetime):
    return datetime.strftime("%B %d")
```

(Step 3 of 3) Finally, make a variable named birth_dates. Use map() and filter(), along with your two functions, to create date strings for every datetime in birthdays so long as the datetime is more than 13 years old.

```Py
birthdays = [
    datetime.datetime(2012, 4, 29),
    datetime.datetime(2006, 8, 9),
    datetime.datetime(1978, 5, 16),
    datetime.datetime(1981, 8, 15),
    datetime.datetime(2001, 7, 4),
    datetime.datetime(1999, 12, 30)
]

x = filter(is_over_13, birthdays)
birth_dates = map(date_string, x)
print(list(birth_dates))
```
========================
# timezones

naive datetime vs aware datetime (aware of timezone)

this only works on an AWARE datetime object, NOT a naive one
datetime.datetime.astimezone(datetime.datetime.timezone())

pytz package

`import pytz`
