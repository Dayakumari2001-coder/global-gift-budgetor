-- =========================================
-- SAMPLE DATA INSERTION
-- =========================================

-- insert user
INSERT INTO users (name) VALUES ('Daya Kumari');

-- insert exchange rates (latest values)
INSERT INTO exchange_rates (from_currency, to_currency, rate) VALUES ('USD','INR',83.00);
INSERT INTO exchange_rates (from_currency, to_currency, rate) VALUES ('EUR','INR',90.00);
INSERT INTO exchange_rates (from_currency, to_currency, rate) VALUES ('INR','USD',0.012);
INSERT INTO exchange_rates (from_currency, to_currency, rate) VALUES ('INR','EUR',0.011);
INSERT INTO exchange_rates (from_currency, to_currency, rate) VALUES ('USD','EUR',0.92);
INSERT INTO exchange_rates (from_currency, to_currency, rate) VALUES ('EUR','USD',1.08);

-- insert sample wishlist items
INSERT INTO wishlist (user_id, item_name, foreign_price, currency)
VALUES (1, 'Laptop', 1000.00, 'USD');

INSERT INTO wishlist (user_id, item_name, foreign_price, currency)
VALUES (1, 'Headphones', 200.00, 'EUR');
