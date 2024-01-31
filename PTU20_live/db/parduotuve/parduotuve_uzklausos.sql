-- Užklausos

-- daugiausiai parduodami produktai
SELECT product.id, product.name, SUM(bill_line.quantity) AS total_sold
FROM product
JOIN bill_line ON product.id = bill_line.product_id
GROUP BY product.id
ORDER BY total_sold DESC;

-- didžiausia produkto apyvarta
SELECT product.id, product.name, SUM(product.price * bill_line.quantity) AS total_revenue
FROM product
JOIN bill_line ON product.id = bill_line.product_id
GROUP BY product.id
ORDER BY total_revenue DESC;

-- geriausias klientas
SELECT customer.id, customer.first_name, customer.last_name, SUM(product.price * bill_line.quantity) AS total_spent
FROM customer
JOIN bill ON customer.id = bill.customer_id
JOIN bill_line ON bill.id = bill_line.bill_id
LEFT JOIN product ON bill_line.product_id = product.id
GROUP BY customer.id
ORDER BY total_spent DESC

-- didžiausia saskaita
SELECT bill.id, bill.purchase_date_time, customer.first_name AS customer_first_name, customer.last_name AS customer_last_name,
       SUM(product.price * bill_line.quantity) AS total_amount
FROM bill
JOIN customer ON bill.customer_id = customer.id
JOIN bill_line ON bill.id = bill_line.bill_id
JOIN product ON bill_line.product_id = product.id
GROUP BY bill.id
ORDER BY total_amount DESC