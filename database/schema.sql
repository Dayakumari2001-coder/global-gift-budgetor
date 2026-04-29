CREATE DATABASE gift_db;
USE gift_db;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE wishlist (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    item_name VARCHAR(100),
    foreign_price DECIMAL(10,2),
    currency VARCHAR(10),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE exchange_rates (
    currency VARCHAR(10) PRIMARY KEY,
    rate_to_inr DECIMAL(10,2)
);