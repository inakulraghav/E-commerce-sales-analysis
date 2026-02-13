-- STEP 0 DATA CREATION

CREATE DATABASE ecomprj;
USE  ecomprj;

CREATE TABLE customers
(customer_id INTEGER PRIMARY KEY AUTO_INCREMENT,
customer_name VARCHAR(30) NOT NULL,
email  VARCHAR(50) UNIQUE,
gender ENUM("Male","Female","Other") ,
age INTEGER CHECK (age BETWEEN 0 AND 120),
city VARCHAR(30),
country VARCHAR(20) DEFAULT "unknown",
signup_date DATE 
);


CREATE TABLE products
(product_id INTEGER PRIMARY KEY AUTO_INCREMENT,
product_name VARCHAR(30),
category VARCHAR(50),
sub_category VARCHAR(50),
cost_price DECIMAL(10,2) CHECK (cost_price >= 0),
selling_price DECIMAL(10,2)
); 



CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATE,
    order_status VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);


CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT,
    quantity INT CHECK (quantity>0),
    discount DECIMAL(5,2) CHECK (discount BETWEEN 0 AND 100),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE payments (
	payment_id INT PRIMARY KEY AUTO_INCREMENT,
	order_id INT NOT NULL,
    payment_method VARCHAR(30),
    payment_status VARCHAR(20),
    payment_date DATE,
    amount DECIMAL(10,2) CHECK (amount>0),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

CREATE TABLE shipments (
	shipment_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    shipped_date DATE,
    delivered_date DATE,
    delivery_status VARCHAR(30),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

CREATE TABLE returns (
	return_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    return_reason VARCHAR(100),
    return_date DATE,
    refund_amount DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

























