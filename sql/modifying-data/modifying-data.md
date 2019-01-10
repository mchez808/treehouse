
See all of the SQL used in *Modifying Data With SQL*
in the [Modifying Data With SQL Cheatsheet. ](https://github.com/treehouse/cheatsheets/blob/master/modifying_data_with_sql/cheatsheet.md)

CRUD review:

CRUD    |  SQL
------------------
CREATE  |  INSERT
READ    |  SELECT
UPDATE  |  *
DELETE  |  *

* (same)

database seed file: name of file with many `add` commands

You don't have to add in values for all columns. Just specify those columns.
If you're doing all columns, then you don't need to.


# Handling Errors When Manipulating Data

## Transactions, Commits, Rollbacks

**Definitions**
* Autocommit - every statement you write gets saved to disk.
* Seeding - populating a database for the first time.
* Script file - a file containing SQL statements.

```SQL
-- Switch autocommit off and begin a transaction:
BEGIN TRANSACTION;

-- Or simply:
BEGIN;

-- To save all results of the statements after the start of the transaction to disk:
COMMIT;

-- To reset the state of the database to before the beginning of the transaction:
ROLLBACK;
```

Q: The BEGIN; or the BEGIN TRANSACTION; statement does what?

ANS: Transactions switch autocommit mode off.

## Databases with Frameworks

**Definitions**
DML - **Data Manipulation Language** - the subset of the SQL programming language that deals with CRUD operations.
ORM - Object-Relational Mapping – used to perform CRUD operations with a language other than SQL.

### Examples of ORMs
* Hibernate for Java
* CoreData for Objective-C or Swift
* Django ORM for Python
* ActiveRecord for Ruby


# Challenges

## [Adding Data to a Database](https://teamtreehouse.com/library/modifying-data-with-sql/adding-data-to-a-database/adding-data-with-sql)

## [Updating Data in a Database](https://teamtreehouse.com/library/modifying-data-with-sql/updating-data-in-a-database/updating-data-with-sql)

## [Deleting Data From a Database](https://teamtreehouse.com/library/modifying-data-with-sql/deleting-data-from-a-database/deleting-data-with-sql)

## [Handling Errors When Manipulating Data](https://teamtreehouse.com/library/modifying-data-with-sql/handling-errors-when-manipulating-data/transactions-review)
