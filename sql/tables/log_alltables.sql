-- listed chronologically, for the most part

-- How many models of each make are there?
SELECT mk.MakeName, COUNT(md.ModelName) AS "Number of Models"
  FROM make AS mk
  LEFT OUTER JOIN model AS md ON mk.MakeID = md.MakeID
  GROUP BY mk.MakeName;

-- list out all makes and models
  SELECT mk.MakeName, md.ModelName FROM make AS mk
    INNER JOIN model AS md ON mk.MakeID = md.MakeID;

-- books
-- id, title, author, genre, first_published
SELECT title, LENGTH(title) AS longest_length FROM books ORDER BY LENGTH(title) DESC LIMIT 1;
SELECT LOWER(title) AS lowercase_title, UPPER(author) AS uppercase_author FROM books;

SELECT genre, COUNT(*) AS genre_count FROM books GROUP BY genre;
SELECT COUNT(DISTINCT genre) AS total_genres FROM books;


-- reviews
-- id, movie_id, username, review and rating
SELECT SUM(rating) AS starman_total_ratings FROM reviews WHERE movie_id = 6;
SELECT AVG(rating) AS average_rating FROM reviews WHERE movie_id = 6;
SELECT MIN(rating) AS star_min, MAX(rating) AS star_max FROM reviews WHERE movie_id = 6;


-- products
-- id, name, category, description, price, stock_count
SELECT name, ROUND(price / 1.4, 2) AS price_gbp FROM products;


-- customers
-- id, username, first_name, last_name, password, email, phone columns
SELECT SUBSTR(first_name, 1, 1) AS initial, last_name FROM customers;
SELECT REPLACE(email, '@', '<at>') AS obfuscated_email FROM customers;

-- orders
-- id, product_id, user_id, address_id, ordered_on, status, cost
SELECT COUNT(*) AS shipped_today FROM orders WHERE ordered_on = DATE("now") AND status = "shipped"
SELECT COUNT(*) FROM orders WHERE ordered_on
    BETWEEN DATE("now", "-7 days") AND DATE("now", "-1 day");

-- Count the total number of orders that were ordered yesterday and have the
-- status of 'shipped'. Alias it to ordered_yesterday_and_shipped.
SELECT COUNT(*) AS ordered_yesterday_and_shipped
FROM orders WHERE ordered_on = DATE("now", "-1 days") AND status = "shipped";

SELECT STRFTIME("%d-%m-%y", ordered_on), * AS UK_date FROM orders;


-- loans
-- id	book_id	patron_id	loaned_on	return_by	returned_on

-- Find all loans that are overdue.
SELECT * FROM loans
WHERE return_by < DATE("now")
AND returned_on IS NULL;

-- Find all loans that are due back this week.
SELECT * FROM loans
WHERE return_by BETWEEN DATE("now") AND DATE("now", "+7 days");
-- another student's
WHERE return_by BETWEEN DATE("now") AND DATE("now", "+6 days") AND returned_on IS NULL;

-- Format dates in all the loans table in the UK format without the year.
-- For example, April 1st is 01/04.
SELECT return_by, STRFTIME("%d/%m", return_by) AS "UK format" FROM loans;
SELECT loaned_on, STRFTIME("%d/%m", loaned_on) AS "UK format" FROM loans;


-- Use a JOIN to select all patrons with outstanding books. Select their first name and email address.
SELECT DISTINCT first_name, email FROM loans
INNER JOIN patrons ON loans.patron_id = patrons.id
WHERE returned_on IS NULL;


-- Use a JOIN to find out which patrons haven't had any loans. Select their first name and email address.
SELECT DISTINCT first_name, email FROM patrons
LEFT JOIN loans ON loans.patron_id = patrons.id
WHERE loaned_on IS NULL;
SELECT DISTINCT patron_id AS "patrons who have ever had a loan" FROM loans;
SELECT id, first_name FROM patrons ORDER BY id DESC;


SELECT title
, first_name || " " || last_name
, email
, loans.*
FROM loans
INNER JOIN books ON loans.book_id = books.id
INNER JOIN patrons ON loans.patron_id = patrons.id;


/******************************************
  Practice Simple WHERE Clauses with SQL

  https://teamtreehouse.com/library/introducing-the-practice-4

TABLES:
* customers
* products
* sales

*******************************************/
-- Create a list of mailing information for orders that took place on April 20th, 2017.
-- SELECT item, sale_date FROM sales
SELECT customer_name, delivery_address, sale_date FROM sales
WHERE sale_date = "2017-4-20";

-- LEARN FROM MY ERROR: 04 (for April)
  -- WHERE sale_date = "2017-04-20";


/******************************************/
-- Find all Playstation 4 products. Try and do this with 3 different queries.
SELECT "IN is case-SENSITIVE", name, short_description FROM products
WHERE name IN ("Playstation 4", "Playstation 4 Pro");

SELECT "IN is case-SENSITIVE", name, short_description FROM products
WHERE name IN ("playstation 4", "playstation 4 pro");

SELECT "IN is NOT case-sensitive", name, short_description FROM products
WHERE name LIKE "%playstation 4%";

-- LEARN FROM MY ERROR: %station% WITHOUT quotation marks
  -- WHERE name LIKE %station%;


/******************************************/
-- Create a list of names and mailing addresses of people without email addresses.
SELECT first_name	|| " " || last_name AS "Customer w/o email"
, email
FROM customers
WHERE email IS NULL;

/******************************************/
-- Create an email marketing list containing all people with an email address.
SELECT first_name	|| " " || last_name AS "email marketing list"
, email
FROM customers
WHERE email IS NOT NULL;


/******************************************/
-- Find all products with more than 250 units in stock. We need to put them on sale to sell them to make space for newer products.
SELECT name, units_in_stock FROM products
WHERE units_in_stock > 250;


/******************************************/
-- Find all orders that sold for between $225 and $245.
SELECT item, total_price FROM sales
WHERE total_price BETWEEN 225 AND 245;


/******************************************/
-- Create a list of products that support 4K. Include the product name and it's current price.
SELECT name, short_description FROM products
WHERE short_description LIKE "%4K%";
