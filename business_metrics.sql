SELECT
ROUND(SUM(payment_value),2) AS total_revenue
FROM ecommerce_dw.fact_sales;

SELECT
COUNT(DISTINCT order_id) AS total_orders
FROM ecommerce_dw.fact_sales;

SELECT
product_id,
COUNT(*) AS total_sales
FROM ecommerce_dw.fact_sales
GROUP BY product_id
ORDER BY total_sales DESC
LIMIT 10;

SELECT
customer_id,
SUM(payment_value) AS revenue
FROM ecommerce_dw.fact_sales
GROUP BY customer_id
ORDER BY revenue DESC
LIMIT 10;

SELECT
customer_state,
ROUND(SUM(payment_value),2) AS revenue
FROM ecommerce_dw.fact_sales
GROUP BY customer_state
ORDER BY revenue DESC;

SELECT
FORMAT_DATE('%Y-%m', DATE(order_purchase_timestamp))
AS month,
ROUND(SUM(payment_value),2)
AS revenue
FROM ecommerce_dw.fact_sales
GROUP BY month
ORDER BY month;

