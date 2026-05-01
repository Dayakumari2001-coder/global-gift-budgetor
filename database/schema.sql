-- =========================================
-- CLEAN START 
-- =========================================

DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS exchange_rates;
DROP TABLE IF EXISTS users;

DROP DATABASE IF EXISTS gift_db;
CREATE DATABASE gift_db;
USE gift_db;

-- =========================================
--  USER TABLE
-- =========================================

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    home_currency VARCHAR(10) NOT NULL,
);

-- =========================================
-- WISHLIST TABLE
-- =========================================
-- stores user items with currency

CREATE TABLE wishlist (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    foreign_price DECIMAL(16,4) NOT NULL,
    currency VARCHAR(10) NOT NULL,

    -- ensure price is positive
    CHECK (foreign_price > 0),

    -- link with user
    --FOREIGN KEY (user_id) REFERENCES users(user_id)
    --ON DELETE CASCADE
);

-- =========================================
-- EXCHANGE RATES TABLE 
-- =========================================
-- stores latest currency rates with timestamps

CREATE TABLE exchange_rates (
    from_currency VARCHAR(10),
    to_currency VARCHAR(10),
    rate DECIMAL(19,6) NOT NULL,

    -- time when record created
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- auto update time when rate changes
    last_updated TIMESTAMP 
    DEFAULT CURRENT_TIMESTAMP 
    ON UPDATE CURRENT_TIMESTAMP,

    PRIMARY KEY (from_currency, to_currency)
);
