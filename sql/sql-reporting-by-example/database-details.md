
The database at Jefferson Middle School contains the following seven tables.

```
STUDENTS
TEACHERS
SUBJECTS
ROOMS
PERIODS
CLASSES
SCHEDULE
```

### Full table descriptions

The first table you'll need to know about is the STUDENTS table.
Which contains an ID primary key, and then the first and
last names of the student, followed by the student's grade.

Next is the TEACHERS table, which contains an ID primary key and
then the teacher's first and last names.

After that, we've got the SUBJECTS table,
which contains the different subjects, like math and science.
This table contains an ID primary key,
followed by the subject's name, what grade the subject is intended for, and
then a quick description of what that subject teaches.

There's also a ROOMS table, which contains one row for each room in the school.
In here, there's an ID primary key, as well as an integer
identifying the maximum number of students the room can hold.

A school day at Jefferson Middle School is made up of 7 periods,
summarized in the PERIODS table.
It's got an ID primary key, followed by the start time and duration of the period.
Also, the ID of each period represents which period it is.
So the period with an ID of one is going to represent the first period of the day.

Getting to something a bit more complicated, we've got the CLASSES table.
Each row in the CLASSES table represents one individual class.
So for each class, we've got an ID primary key followed by four foreign keys.
Telling us which subject is being taught, which period it is,
which teacher teaches it, and which room it's in.

Finally, we've got the SCHEDULE table, which contains scheduling information for
all of the students. Each row is a pairing between a student and a class.
Each student should have seven rows in this table.
