Python has [great documentation](https://docs.python.org/3/library/csv.html) for the csv module.

Sometimes you might have issues with the csv module and files that contain a lot of Unicode, especially if you're using Python 2. If you run into that issue, check out [unicodecsv](https://pypi.python.org/pypi/unicodecsv/0.14.1).

For both CSV and JSON files, and others, the amazing [tablib](http://docs.python-tablib.org/en/latest/) library is a great thing to check out.

```
import csv

with open('museum.csv', newline='') as csvfile:
    artreader = csv.reader(csvfile, delimiter='|')
    rows = list(artreader)
    for row in rows[:2]:
        print(', '.join(row)]


with open('museum.csv', newline='') as csvfile:
    artreader = csv.DictReader(csvfile, delimiter='|')
    rows = list(artreader)
    for row in rows[1:3]:
        print(row['group1'])


with open('teachers.csv', 'a') as csvfile:
    fieldnames = ['first_name', 'last_name', 'topic']
    teachwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    teachwriter.writeheader()
    teachwriter.writerow({
        'first_name': 'Kenneth',
        'last_name': 'Love',
        'topic': 'Python'
    })
    teachwriter.writerow({
        'first_name': 'Alena',
        'last_name': 'Holligan',
        'topic': 'PHP'
    })

```

