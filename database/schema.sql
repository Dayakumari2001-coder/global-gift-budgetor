-- =========================================
-- CLEAN START (SAFE RE-RUN)
-- =========================================

DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS exchange_rates;
DROP TABLE IF EXISTS users;

DROP DATABASE IF EXISTS gift_db;
CREATE DATABASE gift_db;
USE gift_db;

-- =========================================
-- USERS TABLE
-- =========================================
-- stores user details

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- =========================================
-- WISHLIST TABLE
-- =========================================
-- stores user items with currency

CREATE TABLE wishlist (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    item_name VARCHAR(100) NOT NULL,
    foreign_price DECIMAL(10,2) NOT NULL,
    currency VARCHAR(10) NOT NULL,

    -- ensure price is positive
    CHECK (foreign_price > 0),

    -- link with user
    FOREIGN KEY (user_id) REFERENCES users(user_id)
    ON DELETE CASCADE
);

-- =========================================
-- EXCHANGE RATES TABLE (LATEST ONLY)
-- =========================================
-- stores latest currency rates with timestamps

CREATE TABLE exchange_rates (
    from_currency VARCHAR(10),
    to_currency VARCHAR(10),
    rate DECIMAL(10,4) NOT NULL,

    -- time when record created
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- auto update time when rate changes
    last_updated TIMESTAMP 
    DEFAULT CURRENT_TIMESTAMP 
    ON UPDATE CURRENT_TIMESTAMP,

    PRIMARY KEY (from_currency, to_currency)
);

-- =========================================
-- TEST QUERIES (OPTIONAL)
-- =========================================

-- view users
SELECT * FROM users;

-- view wishlist
SELECT * FROM wishlist;

-- view exchange rates with timestamps
SELECT * FROM exchange_rates;

-- calculate total in INR
SELECT SUM(w.foreign_price * e.rate) AS total_in_inr
FROM wishlist w
JOIN exchange_rates e
ON w.currency = e.from_currency
WHERE e.to_currency = 'INR';