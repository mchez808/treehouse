-- enter a query
SELECT * FROM Location;
SELECT * FROM Sale AS s LIMIT 2;
SELECT * FROM SalesRep AS sr

-- step 1: the inside subquery
SELECT s.SalesRepID, SUM(SaleAmount) AS StLouisAmount FROM Sale AS s
WHERE s.LocationID = 1
GROUP BY s.SalesRepID

-- step 2: staging placeholders for subqueries
SELECT sr.LastName FROM SalesRep AS sr
  LEFT OUTER JOIN () AS loc1
  LEFT OUTER JOIN () AS loc2

-- step 3: preparing the joins
SELECT sr.LastName FROM SalesRep AS sr
  LEFT OUTER JOIN (
    ...
  ) AS loc1 ON ...
  LEFT OUTER JOIN (
    ...
  ) AS loc2 ON ...
