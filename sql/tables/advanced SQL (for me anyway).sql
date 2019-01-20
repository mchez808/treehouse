-- links to cloud database
-- https://teamtreehouse.com/sql_playgrounds/402#/queries/a46e8d4e-eacc-4ba9-b6dd-f870203553e2
-- https://teamtreehouse.com/library/getting-the-grand-total

-- HAVING
SELECT SUM(cost) as Total, user_id FROM orders
GROUP BY user_id HAVING Total > 250
ORDER BY Total DESC;

-- try a join?
-- https://teamtreehouse.com/sql_playgrounds/442#/queries/05246454-1311-40ab-a0f9-76e748ba2d09
-- Calculate the average rating for each movie and round it to one decimal place
SELECT AVG(reviews.rating), movies.title FROM reviews, movies
WHERE movie_id = movies.id
GROUP BY movie_id;

-- Calculate the minimum and maximum rating for every movie
SELECT MIN(reviews.rating) AS worst, MAX(reviews.rating) AS best, movies.title AS best, COUNT(reviews.id) AS "# of ratings" FROM reviews, movies
WHERE movies.id = reviews.movie_id
GROUP BY movie_id;

SELECT * FROM reviews ORDER BY movie_id ASC;

-- SUBQUERYING

-- Can I figure out his challenge?
-- https://teamtreehouse.com/community/confused-with-subqueries-challenges-please-help

-- successful subquery!
SELECT SUM(cost) AS Total, user_id FROM orders
WHERE user_id = (SELECT user_id FROM orders
GROUP BY user_id ORDER BY SUM(cost) DESC LIMIT 1);
