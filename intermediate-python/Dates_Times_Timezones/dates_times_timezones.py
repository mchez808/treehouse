import datetime
import pytz

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
