# Project Overview

These exercises are done in SQLite, to demonstrate practice writing simple SQL
reports from the perspective of a business analyst at a fictional school,
Jefferson Middle School.

## Initializing the SQLite database

Please see the SQL commands to create this database in the file `school-system-db-setup.sql`,
or, alternatively, find it at [this AWS S3 URL](https://s3.amazonaws.com/treehouse-code-samples/sql_reporting_by_example.txt)

## Database Overview

The database at Jefferson Middle School contains the following seven related tables.

```
STUDENTS
TEACHERS
SUBJECTS
ROOMS
PERIODS
CLASSES
SCHEDULE
```

A detailed description can be viewed in the accompanied file `database-details.md`

# Grouping Exercises

## busiest teachers

There are 7 periods at Jefferson Middle School.
Which teachers teach a class during all 7 periods?

## query result

```SQL
WITH CLASSES_TEACHERS AS (
  SELECT * FROM TEACHERS
  JOIN CLASSES ON TEACHERS.ID = CLASSES.TEACHER_ID
)
SELECT TEACHER_ID,
FIRST_NAME, LAST_NAME,
COUNT(PERIOD_ID) AS NUM_PERIODS
FROM CLASSES_TEACHERS
GROUP BY TEACHER_ID
HAVING NUM_PERIODS = 7;
```

## report preview

TEACHER_ID	FIRST_NAME	LAST_NAME	NUM_PERIODS
373	Jeffrey	Bastion	7
374	Stanley	Petrovic	7
375	Idra	Patel	7
376	Jessica	Dillon	7
377	Patricia	Parker	7
