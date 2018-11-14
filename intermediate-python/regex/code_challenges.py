# https://teamtreehouse.com/library/regular-expressions-in-python/introduction-to-regular-expressions/players-dictionary-and-class
# Challenge Task 1 of 2
# Create a variable named players that is an re.search() or re.match() to capture three groups:
# last_name, first_name, and score. It should include re.MULTILINE.


import re

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''


z = re.search(r',\s[\w]+[\s]?[\w]*:', string, re.MULTILINE | re.IGNORECASE)
print(z)
