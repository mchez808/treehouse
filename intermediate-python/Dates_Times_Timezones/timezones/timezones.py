import pytz
import datetime

# write a script that takes a datetime object in my timezone,
# and then returns it in 6 other timezones,
# using this format string:
tz_format = '%Y-%m-%d %H:%M%:%S %Z%z'


starter = pytz.utc.localize(datetime.datetime(2015, 10, 21, 23, 29))

# take a timezone name as a string
# tz_name = "US/Hawaii"
# Convert starter to that timezone using pytz's timezones
# and return the new datetime.
# by convert, they mean adjust the time from one timezone to another!

# Create a function named to_timezone
def to_timezone(tz_name):
    tz_target = pytz.timezone(tz_name)
    return starter.astimezone(tz_target)


# Code Challenge
import datetime

naive = datetime.datetime(2015, 10, 21, 4, 29)

pacific_tz = datetime.timezone(datetime.timedelta(hours=-8))
hill_valley = naive.replace(tzinfo=pacific_tz)
# Great, but replace just sets the timezone, it doesn't move the datetime to the new timezone.

# Let's move one into the new timezone.
paris_tz = datetime.timezone(datetime.timedelta(hours=1))
paris = datetime.datetime(2015, 10, 21, 13, 29, tzinfo=paris_tz)

hill_valley.astimezone(tz=pacific_tz)
