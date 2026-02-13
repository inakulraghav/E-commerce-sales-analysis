-- STEP 1 DATA EXTRACTION
USE ecomprj;


INSERT INTO customers (customer_name, email, gender, age, city, country, signup_date) VALUES
('Rajesh Kumar', 'rajesh.kumar@gmail.com', 'Male', 28, 'Delhi', 'India', '2023-01-15'),
('Priya Sharma', 'priya.sharma@yahoo.com', 'Female', 32, 'Mumbai', 'India', '2023-02-20'),
('Amit Patel', 'amit.patel@gmail.com', 'Male', 25, 'Ahmedabad', 'India', '2023-03-10'),
('Sneha Reddy', 'sneha.reddy@gmail.com', 'Female', 29, 'Hyderabad', 'India', '2023-04-05'),
('Vikram Singh', 'vikram.singh@hotmail.com', 'Male', 35, 'Bangalore', 'India', '2023-05-12'),
('Anjali Gupta', 'anjali.gupta@gmail.com', 'Female', 27, 'Pune', 'India', '2023-06-18'),
('Rahul Verma', 'rahul.verma@gmail.com', 'Male', 31, 'Chennai', 'India', '2023-07-22'),
('Pooja Mehta', 'pooja.mehta@yahoo.com', 'Female', 26, 'Kolkata', 'India', '2023-08-30'),
('Sanjay Joshi', 'sanjay.joshi@gmail.com', 'Male', 40, 'Jaipur', 'India', '2023-09-14'),
('Neha Desai', 'neha.desai@gmail.com', 'Female', 33, 'Surat', 'India', '2023-10-25');


INSERT INTO products (product_name, category, sub_category, cost_price, selling_price) VALUES
('iPhone 14', 'Electronics', 'Mobile Phones', 65000.00, 79999.00),
('Samsung Galaxy S23', 'Electronics', 'Mobile Phones', 55000.00, 69999.00),
('OnePlus Nord 3', 'Electronics', 'Mobile Phones', 28000.00, 32999.00),
('Boat Airdopes 141', 'Electronics', 'Earphones', 1200.00, 1499.00),
('Mi TV 4A 32-inch', 'Electronics', 'Televisions', 18000.00, 21999.00),
('Samsung Refrigerator', 'Appliances', 'Refrigerators', 32000.00, 38999.00),
('Whirlpool Washing Machine', 'Appliances', 'Washing Machines', 22000.00, 25999.00),
('Nike Air Max', 'Fashion', 'Shoes', 3500.00, 4999.00),
('Levi''s Jeans', 'Fashion', 'Clothing', 1800.00, 2499.00),
('Amazon Echo Dot', 'Electronics', 'Smart Speakers', 3500.00, 4499.00),
('Dell Inspiron Laptop', 'Electronics', 'Laptops', 55000.00, 64999.00),
('HP LaserJet Printer', 'Electronics', 'Printers', 12000.00, 14999.00),
('Puma T-Shirt', 'Fashion', 'Clothing', 800.00, 1199.00),
('Tupperware Set', 'Home & Kitchen', 'Containers', 1500.00, 1999.00),
('Philips Trimmer', 'Grooming', 'Trimmers', 1200.00, 1699.00);


INSERT INTO orders (customer_id, order_date, order_status) VALUES
(1, '2024-01-10', 'Delivered'),
(2, '2024-01-12', 'Shipped'),
(3, '2024-01-15', 'Pending'),
(4, '2024-01-18', 'Delivered'),
(5, '2024-01-20', 'Processing'),
(6, '2024-01-22', 'Delivered'),
(1, '2024-01-25', 'Shipped'),
(7, '2024-01-28', 'Pending'),
(8, '2024-02-01', 'Delivered'),
(9, '2024-02-05', 'Cancelled');


INSERT INTO order_items (order_id, product_id, quantity, discount) VALUES
(1, 1, 1, 5.00),   -- iPhone 14 with 5% discount
(1, 4, 1, 10.00),  -- Boat Earphones with 10% discount
(2, 2, 1, 0.00),   -- Samsung Phone
(2, 9, 2, 15.00),  -- 2 Levi's Jeans with 15% discount
(3, 3, 1, 8.00),   -- OnePlus Phone
(4, 5, 1, 12.00),  -- Mi TV
(4, 7, 1, 7.50),   -- Washing Machine
(5, 10, 1, 5.00),  -- Echo Dot
(6, 6, 1, 0.00),   -- Refrigerator
(7, 11, 1, 3.00),  -- Dell Laptop
(8, 13, 3, 20.00), -- 3 Puma T-Shirts
(9, 15, 1, 10.00), -- Philips Trimmer
(10, 8, 1, 0.00);  -- Nike Shoes (cancelled order)



INSERT INTO payments (order_id, payment_method, payment_status, payment_date, amount) VALUES
(1, 'Credit Card', 'Completed', '2024-01-10', 81499.00),
(2, 'UPI', 'Completed', '2024-01-12', 78998.00),
(3, 'Debit Card', 'Pending', '2024-01-15', 30358.00),
(4, 'Net Banking', 'Completed', '2024-01-18', 56398.00),
(5, 'Credit Card', 'Completed', '2024-01-20', 4274.00),
(6, 'COD', 'Pending', '2024-01-22', 38999.00),
(7, 'UPI', 'Completed', '2024-01-25', 63049.00),
(8, 'Debit Card', 'Completed', '2024-01-28', 2877.00),
(9, 'Credit Card', 'Completed', '2024-02-01', 1529.00),
(10, 'UPI', 'Refunded', '2024-02-05', 4999.00);



INSERT INTO shipments (order_id, shipped_date, delivered_date, delivery_status) VALUES
(1, '2024-01-11', '2024-01-13', 'Delivered'),
(2, '2024-01-13', NULL, 'In Transit'),
(3, NULL, NULL, 'Processing'),
(4, '2024-01-19', '2024-01-21', 'Delivered'),
(5, '2024-01-21', NULL, 'Shipped'),
(6, '2024-01-23', '2024-01-25', 'Delivered'),
(7, '2024-01-26', NULL, 'In Transit'),
(8, NULL, NULL, 'Pending'),
(9, '2024-02-02', '2024-02-04', 'Delivered'),
(10, NULL, NULL, 'Cancelled');

INSERT INTO returns (order_id, return_reason, return_date, refund_amount) VALUES
(1, 'Product damaged', '2024-01-20', 79999.00),
(4, 'Wrong item delivered', '2024-01-25', 21999.00),
(6, 'Not satisfied with product', '2024-01-30', 38999.00);



















