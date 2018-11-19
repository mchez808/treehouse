import json

```
with open('148.json') as artfile:
    art = json.load(artfile)
    print(art['description'])

nums = json.loads("[1, 3, 5]")
nums[2]

json.dumps([5, 4, 3, 2, 1])
# >>> '[5, 4, 3, 2, 1]'

me = {'first_name': 'Mark', 'last_name': 'Chesney', 'topic': 'Python'}
str(me)
json.dumps(me)
```

*Note: the difference between using single- and double-quotations*

