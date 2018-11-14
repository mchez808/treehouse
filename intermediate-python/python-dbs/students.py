'''Creates SQLite db file when run from terminal console.'''

from peewee import *

db = SqliteDatabase('students.db')

class Student(Model):
     username = CharField(max_length=255, unique=True)
     points = IntegerField(default=0)

     class Meta:
         database = db


# list of dictionaries
students = [
    {'username': 'mchez808',
    'points': 3600},
    {'username': 'kennethlove',
    'points': 4888}
]


def add_students():
    for student in students:
        try:
            Student.create(username = student['username'],
                           points = student['points'])
        except IntegrityError:
            student_record = Student.get(username = student['username'])
            student_record.points = student['points']
            student_record.save()


def top_student():
    # ONE-LINE: student = Student.select().order_by(Student.points.desc()).get()
    select_all = Student.select()
    descending_option = Student.points.desc()
    sorted_query = select_all.order_by(descending_option)
    the_top_student = sorted_query.get()
    return the_top_student


# Review: This code format evaluates to True if our file is run directly, and not imported:
if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    print("Our top student right now is: {0.username}.".format(top_student()))

