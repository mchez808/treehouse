
# datetime

## basics methods in datetime.datetime:

```
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

Q: Which attribute is not available on a timedelta?  Answer: years

### challenge

Write a function called far_away that takes one argument, a timedelta. Add that timedelta to datetime.datetime.now() and return the resulting datetime object.

```
def far_away(timedelta):
    return datetime.datetime.now() + timedelta
```

## .now() and .today() methods

### challenge

Write a function named minutes that takes two datetimes and, using `timedelta.total_seconds()` to get the number of seconds, returns the number of minutes, rounded, between them. The first will always be older and the second newer. You'll need to subtract the first from the second.

```
def minutes(dt1, dt2):
    return int(round(datetime.timedelta.total_seconds(dt2 - dt1) / 60, 0))

t1 = datetime.datetime(2018, 5, 15, 7, 15)
t2 = datetime.datetime(2018, 5, 15, 8, 45)
```

# strftime and strptime

turning your `datetime` objects into specific strings, or creating `datetime` objects from strings

strftime - Method to create a string from a datetime

strptime - Method to create a datetime from a string according to a format string

### Links:

* [strftime/strptime guide](https://docs.python.org/3/library/datetime.html?highlight=datetime#strftime-and-strptime-behavior)

* [strftime reference sheet](http://strftime.org/)

### challenge

[Create a function named to_string that takes a datetime and gives back a string in the format "24 September 2012".](https://teamtreehouse.com/library/dates-and-times-in-python/dates-and-times/strftime-strptime)

```
## Examples
# to_string(datetime_object) => "24 September 2012"
# from_string("09/24/12 18:30", "%m/%d/%y %H:%M") => datetime


```

========================
# timezones

naive datetime vs aware datetime (aware of timezone)

this only works on an AWARE datetime object, NOT a naive one
datetime.datetime.astimezone(datetime.datetime.timezone())

pytz package

`import pytz`
