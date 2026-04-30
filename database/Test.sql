USE gift_db;

-- =========================================
-- VIEW ALL TABLES
-- =========================================

SHOW TABLES;

-- =========================================
-- VIEW USERS
-- =========================================

SELECT * FROM users;

-- =========================================
-- VIEW WISHLIST ITEMS
-- =========================================

SELECT * FROM wishlist;

-- =========================================
-- VIEW EXCHANGE RATES
-- =========================================

SELECT * FROM exchange_rates;

-- =========================================
-- CHECK TOTAL (INR)
-- =========================================

SELECT SUM(w.foreign_price * e.rate) AS total_in_inr
FROM wishlist w
JOIN exchange_rates e
ON w.currency = e.from_currency
WHERE e.to_currency = 'INR';

-- =========================================
-- CHECK TOTAL (USD)
-- =========================================

SELECT SUM(w.foreign_price * e.rate) AS total_in_usd
FROM wishlist w
JOIN exchange_rates e
ON w.currency = e.from_currency
WHERE e.to_currency = 'USD';

-- =========================================
-- CHECK LAST UPDATED TIME
-- =========================================

SELECT from_currency, to_currency, rate, last_updated
FROM exchange_rates;

-- =========================================
-- TEST UPDATE RATE
-- =========================================

UPDATE exchange_rates
SET rate = 85
WHERE from_currency='USD' AND to_currency='INR';

-- verify update
SELECT rate, last_updated FROM exchange_rates
WHERE from_currency='USD' AND to_currency='INR';