.mode column
.headers on

CREATE TABLE products (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  price_per_kilo NUMBER NOT NULL
);

CREATE TABLE receipts (
  id INTEGER PRIMARY KEY,
  salesperson TEXT NOT NULL,
  date TEXT NOT NULL
);

CREATE TABLE receipts_products (
  receipt_id INTEGER NOT NULL,
  product_id INTEGER NOT NULL,
  amount INTEGER NOT NULL,
  FOREIGN KEY (receipt_id) REFERENCES receipts(id),
  FOREIGN KEY (product_id) REFERENCES products(name)
);

INSERT INTO products VALUES (1,'Yumyums', 6);
INSERT INTO products VALUES (2,'Rifrafs', 7);
INSERT INTO products VALUES (3, 'Rumbles', 9.5);
INSERT INTO products VALUES (4,'Chunkies', 8);


INSERT INTO receipts VALUES (1, 'John', '2022-10-17T15:52');
INSERT INTO receipts VALUES (2, 'Jane', '2022-10-17T16:37');

INSERT INTO receipts_products VALUES (1, 'Yumyums', 2.5);
INSERT INTO receipts_products VALUES (1, 'Rifrafs', 1.2);
INSERT INTO receipts_products VALUES (2, 'Rumbles', 4.2);
INSERT INTO receipts_products VALUES (2, 'Chunkies', 2.4);

SELECT receipts.salesperson, receipts.date, products.name AS product, products.price_per_kilo
FROM receipts
JOIN receipts_products ON receipts.id = receipts_products.receipt_id
JOIN products ON receipts_products.product_id = products.name;