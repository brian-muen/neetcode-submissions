-- Write your query below
SELECT name
FROM CUSTOMERS
WHERE id NOT IN (SELECT customer_id FROM orders)