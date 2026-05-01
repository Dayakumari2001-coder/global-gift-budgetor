-- =========================================
-- SAMPLE DATA INSERTION
-- =========================================

--insert user data
INSERT INTO users (home_currency) VALUES ('INR');
INSERT INTO users (home_currency) VALUES ('USD');


-- insert exchange rates (latest values)
INSERT INTO exchange_rates (from_currency, to_currency, rate) VALUES ('USD','INR',94.92);
INSERT INTO exchange_rates (from_currency, to_currency, rate) VALUES ('EUR','INR',110.92);
INSERT INTO exchange_rates (from_currency, to_currency, rate) VALUES ('INR','USD',0.0105);
INSERT INTO exchange_rates (from_currency, to_currency, rate) VALUES ('INR','EUR',0.0090);
INSERT INTO exchange_rates (from_currency, to_currency, rate) VALUES ('USD','EUR',0.8550);
INSERT INTO exchange_rates (from_currency, to_currency, rate) VALUES ('EUR','USD',1.1690);
INSERT INTO exchange_rates (from_currency, to_currency, rate) VALUES ('CAD','USD',0.73);
INSERT INTO exchange_rates (from_currency, to_currency, rate) VALUES ('CAD','INR',69.44);
INSERT INTO exchange_rates (from_currency, to_currency, rate) VALUES ('USD','CAD',1.37);
INSERT INTO exchange_rates (from_currency, to_currency, rate) VALUES ('USD','AED',3.67);
INSERT INTO exchange_rates (from_currency, to_currency, rate) VALUES ('CAD','AED',2.68);

-- insert sample wishlist items
INSERT INTO wishlist (item_name, foreign_price, currency,)
VALUES ('Laptop', 1000.00, 'USD');

INSERT INTO wishlist (item_name, foreign_price, currency)
VALUES ('Headphones', 200.00, 'EUR');
