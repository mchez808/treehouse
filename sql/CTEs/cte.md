Things to remember about CTEs:

* an earlier CTE cannot reference a later CTE

* when creating 2 or more CTEs,

* * `WITH` is typed once

* * CTEs are separated by a comma

# Video 3

Use a CTE to generate:

* a set of all sales by each employee

```SQL
WITH all_sales AS (
  SELECT Orders.Id AS OrderId, Orders.EmployeeID,
  SUM(OrderDetails.UnitPrice * OrderDetails.Quantity) AS invoice_total
  FROM Orders
  JOIN OrderDetails ON Orders.id = OrderDetails.OrderId
  GROUP BY Orders.ID
),
revenue_by_employee AS (
  SELECT EmployeeId, SUM(invoice_total) AS total_revenue
  FROM all_sales
  GROUP BY EmployeeID
),
sales_by_employee AS (
  SELECT EmployeeID, COUNT(*) AS sales_count
  FROM all_sales
  GROUP BY EmployeeID
)
SELECT Employees.LastName, Employees.FirstName,
sales_by_employee.sales_count
FROM sales_by_employee
JOIN Employees
ON sales_by_employee.EmployeeID = Employees.id
```

# Video 2

Example: not a CTE
```SQL
WITH all_sales AS (
  SELECT Orders.Id AS OrderId, Orders.EmployeeID,
  SUM(OrderDetails.UnitPrice * OrderDetails.Quantity) AS invoice_total
  FROM Orders
  JOIN OrderDetails ON Orders.id = OrderDetails.OrderId
  GROUP BY Orders.ID
),
revenue_by_employee AS (
  SELECT EmployeeId, SUM(invoice_total) AS total_revenue
  FROM all_sales
  GROUP BY EmployeeID
),
sales_by_employee AS (
  SELECT EmployeeID, COUNT(*) AS sales_count
  FROM all_sales
  GROUP BY EmployeeID
)
-- revenue_by_employee.EmployeeID,
SELECT Employees.LastName, Employees.FirstName,
round(revenue_by_employee.total_revenue, 0) AS "Total Revenue",
sales_by_employee.sales_count AS "Sales Count",
round(revenue_by_employee.total_revenue/sales_by_employee.sales_count, 0) AS "Average Revenue Per Sale"
FROM revenue_by_employee
JOIN sales_by_employee ON revenue_by_employee.EmployeeID = sales_by_employee.EmployeeID
JOIN Employees ON sales_by_employee.EmployeeID = Employees.id
ORDER BY total_revenue DESC
```

Same example: as a CTE
```SQL
WITH all_orders AS (
  SELECT EmployeeID, COUNT(*) AS order_count
  FROM Orders
  GROUP BY EmployeeID
),
late_orders AS (
  SELECT EmployeeID, COUNT(*) AS order_count
  FROM Orders
  WHERE RequiredDate <= ShippedDate
  GROUP BY EmployeeID
)
SELECT Employees.ID, LastName,
all_orders.order_count AS total_order_count,
late_orders.order_count AS late_order_count  
FROM Employees
JOIN all_orders ON Employees.ID = all_orders.EmployeeID
JOIN late_orders ON Employees.ID = late_orders.EmployeeID
```

# Video 1

CTEs are supported by:
Oracle, SQL Server, PostgreSQL, Redshift, SQLite, MySQL v8+

```SQL
WITH product_details AS (
  SELECT ProductName, CategoryName, UnitPrice, UnitsInStock
  FROM Products
  JOIN Categories ON PRODUCTS.CategoryId = Categories.Id
  WHERE Products.Discontinued = 0;
)
SELECT * FROM product_details
ORDER BY CategoryName, ProductName

-- how many different products, and total stock count for each category, are there?
WITH product_details AS (
  SELECT ProductName, CategoryName, UnitPrice, UnitsInStock
  FROM Products
  JOIN Categories ON PRODUCTS.CategoryId = Categories.Id
  WHERE Products.Discontinued = 0
)
SELECT CategoryName, SUM(UnitsInStock) AS "total stock count" FROM product_details
GROUP BY CategoryName
```
