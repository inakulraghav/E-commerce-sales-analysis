USE ecomprj;
DROP VIEW full_dataset ; 
CREATE VIEW full_dataset AS 
SELECT 
-- orders details
 o.order_id,
 o.customer_id,
 o.order_date,
 o.order_status,

-- customers details
 c.customer_name,
 c.email,
 c.age,
 c.gender,
 c.city,
 c.country,
 c.signup_date,
 
 -- Order item details
 oi.quantity,
 oi.discount,
 
-- products details 
 p.product_name,
 p.category,
 p.sub_category,
 p.cost_price,
 p.selling_price,
 
 -- Shipment details
 s.shipped_date,
 s.delivered_date,
 s.delivery_status,
 
 -- payments details
 py.payment_method,
 py.payment_status,
 py.payment_date,
 py.amount as payment_amount_of_order,
 
 CASE 
 WHEN r.return_date IS NULL THEN "NO" 
 ELSE "YES"
 END AS item_returned,
 
 
 -- Return details
 r.return_date,
 r.return_reason,
 r.refund_amount
 
 
 
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.customer_id
LEFT JOIN order_items oi ON o.order_id = oi.order_id
LEFT JOIN products p ON oi.product_id = p.product_id
LEFT JOIN payments py ON o.order_id = py.order_id
LEFT JOIN shipments s ON o.order_id = s.order_id
LEFT JOIN returns r ON o.order_id = r.order_id
ORDER BY o.order_date ,o.order_id;

SELECT * FROM full_dataset;
 
























