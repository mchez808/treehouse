
```SQL
SELECT * FROM First 
UNION
SELECT * FROM Second;


UNION ALL
# This operation is similar to Union. But it also shows the duplicate rows.

SELECT * FROM First 
UNION ALL
SELECT * FROM Second;



SELECT * FROM First 
INTERSECT
SELECT * FROM Second;



SELECT * FROM First 
MINUS
SELECT * FROM Second;

```


## Primary Key Properties
* May never be null
* One primary key per table
* Cannot be modified to a new value


## Table Relationships

the trick about many-to-many relationships: they don't actually exist at all!
They're really two one-to-many relationships joined by a junction table (an associative entity table)
e.g.: orders and parts.  one order can have many parts; one part can have many orders.

one-to-one relationships: in practice, rather seldom

