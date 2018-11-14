from peewee import *

db = sqliteDatabase('new_db_terms.db')


class NewDatabaseTerms(Model):
    term = CharField(max_length=255, unique=True)
    description = CharField(max_length=255)

    class Meta:
        database = db


if __name__ = '__main__':
    db.connect()
    db.create_tables([NewDatabaseTerms], safe=True)

'''
    New Terms
    model - A code object that represents a database table
    SqliteDatabase - The class from Peewee that lets us connect to an SQLite database
    Model - The Peewee class that we extend to make a model
    CharField - A Peewee field that holds onto characters. It's a varchar in SQL terms
    max_length - The maximum number of characters in a CharField
    IntegerField - A Peewee field that holds an integer
    default - A default value for the field if one isn't provided
    unique - Whether the value in the field can be repeated in the table
    .connect() - A database method that connects to the database
    .create_tables() - A database method to create the tables for the specified models.
    safe - Whether or not to throw errors if the table(s) you're attempting to create already exist

    SQLite commands:
    .tables
    .exit

    New Terms
    .create() - creates a new instance all at once
    .select() - finds records in a table
    .save() - updates an existing row in the database
    .get() - finds a single record in a table
    .delete_instance() - deletes a single record from the table
    .order_by() - specify how to sort the records
    if __name__ == '__main__' - a common pattern for making code only run when the script is run and not when it's imported
    db.close() - not a method we used, but often a good idea. Explicitly closes the connection to the database.
    .update() - also something we didn't use. Offers a way to update a record without .get() and .save(). Example: Student.update(points=student['points']).where(Student.username == student['username']).execute()
'''
