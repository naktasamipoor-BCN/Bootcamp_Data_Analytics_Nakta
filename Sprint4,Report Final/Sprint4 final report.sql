##SPRINT 4 
## Nivell 1
##Descàrrega els arxius CSV, estudia'ls i dissenya una base de dades amb un esquema d'estrella que contingui, almenys 4 taules de les 
##quals puguis realitzar les següents consultes:

-- 1) CONFIGURACIÓN DE LA BASE DE DATOS
DROP DATABASE IF EXISTS sprint4_star;
CREATE DATABASE sprint4_star;
USE sprint4_star;

-- 2) Creación de tablas Staging (solo para carga)
CREATE TABLE stg_american_users (
  id INT,
  name VARCHAR(100),
  surname VARCHAR(100),
  phone VARCHAR(50),
  email VARCHAR(150),
  birth_date VARCHAR(50),
  country VARCHAR(80),
  city VARCHAR(80),
  postal_code VARCHAR(20),
  address VARCHAR(200)
);

CREATE TABLE stg_european_users LIKE stg_american_users;

CREATE TABLE stg_companies (
  company_id VARCHAR(20),
  company_name VARCHAR(200),
  phone VARCHAR(50),
  email VARCHAR(150),
  country VARCHAR(80),
  website VARCHAR(200)
);

CREATE TABLE stg_credit_cards (
  id VARCHAR(30),
  user_id INT,
  iban VARCHAR(34),
  pan VARCHAR(25),
  pin INT,
  cvv INT,
  track1 VARCHAR(255),
  track2 VARCHAR(255),
  expiring_date VARCHAR(20)
);

CREATE TABLE stg_products (
  id INT,
  product_name VARCHAR(200),
  price VARCHAR(30),
  colour VARCHAR(20),
  weight DECIMAL(10,2),
  warehouse_id VARCHAR(20)
);

CREATE TABLE stg_transactions (
  id CHAR(36),
  card_id VARCHAR(30),
  business_id VARCHAR(20),
  `timestamp` VARCHAR(25),
  amount VARCHAR(30),
  declined TINYINT,
  product_ids VARCHAR(255),
  user_id INT,
  lat DECIMAL(18,15),
  longitude DECIMAL(18,15)
);

-- 3)Control y verificación de tablas
SHOW TABLES;
SHOW CREATE TABLE stg_american_users;

-- 4)CARGAR DATOS
SET GLOBAL local_infile = 1;

LOAD DATA LOCAL INFILE
'/Users/naktasamipoor/Documents/1-work/business/Start up/Orkeed/18-Data analysis/1-my sql/4-especizaliacion/sprint 4/american_users.csv'
INTO TABLE stg_american_users
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, name, surname, phone, email, birth_date, country, city, postal_code, address);

SELECT COUNT(*) 
FROM stg_american_users;

LOAD DATA LOCAL INFILE
'/Users/naktasamipoor/Documents/1-work/business/Start up/Orkeed/18-Data analysis/1-my sql/4-especizaliacion/sprint 4/european_users.csv'
INTO TABLE stg_european_users
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, name, surname, phone, email, birth_date, country, city, postal_code, address);

SELECT COUNT(*) 
FROM stg_european_users;

LOAD DATA LOCAL INFILE
'/Users/naktasamipoor/Documents/1-work/business/Start up/Orkeed/18-Data analysis/1-my sql/4-especizaliacion/sprint 4/companies.csv'
INTO TABLE stg_companies
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(company_id, company_name, phone, email, country, website);

SELECT COUNT(*) 
FROM stg_companies;

LOAD DATA LOCAL INFILE
'/Users/naktasamipoor/Documents/1-work/business/Start up/Orkeed/18-Data analysis/1-my sql/4-especizaliacion/sprint 4/credit_cards.csv'
INTO TABLE stg_credit_cards
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, user_id, iban, pan, pin, cvv, track1, track2, expiring_date);

SELECT COUNT(*) 
FROM stg_credit_cards;

LOAD DATA LOCAL INFILE
'/Users/naktasamipoor/Documents/1-work/business/Start up/Orkeed/18-Data analysis/1-my sql/4-especizaliacion/sprint 4/products.csv'
INTO TABLE stg_products
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, product_name, price, colour, weight, warehouse_id);

SELECT COUNT(*) 
FROM stg_products;

LOAD DATA LOCAL INFILE
'/Users/naktasamipoor/Documents/1-work/business/Start up/Orkeed/18-Data analysis/1-my sql/4-especizaliacion/sprint 4/transactions.csv'
INTO TABLE stg_transactions
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(id, card_id, business_id, `timestamp`, amount, declined, product_ids, user_id, lat, longitude);

SELECT COUNT(*) 
FROM stg_transactions;

SHOW WARNINGS LIMIT 50;

TRUNCATE TABLE stg_transactions;
ALTER TABLE stg_transactions
  MODIFY lat VARCHAR(50),
  MODIFY longitude VARCHAR(50);

-- 5)Creación de un esquema en estrella (al menos 4 tablas)
-- 5.1)dim_user
CREATE TABLE dim_user (
  user_id INT PRIMARY KEY,
  name VARCHAR(100),
  surname VARCHAR(100),
  email VARCHAR(150),
  country VARCHAR(80)
);

INSERT INTO dim_user
SELECT id, name, surname, email, country FROM stg_american_users
UNION ALL
SELECT id, name, surname, email, country FROM stg_european_users;

-- 5.2)dim_company
CREATE TABLE dim_company (
  company_id VARCHAR(20) PRIMARY KEY,
  company_name VARCHAR(200),
  country VARCHAR(80)
);

INSERT INTO dim_company
SELECT company_id, company_name, country
FROM stg_companies;

-- 5.3)dim_credit_card
CREATE TABLE dim_credit_card (
  card_id VARCHAR(30) PRIMARY KEY,
  user_id INT,
  iban VARCHAR(34),
  FOREIGN KEY (user_id) REFERENCES dim_user(user_id)
);

INSERT INTO dim_credit_card
SELECT id, user_id, iban
FROM stg_credit_cards;

-- 5.4)fact_transaction
CREATE TABLE fact_transaction (
  transaction_id CHAR(36) PRIMARY KEY,
  card_id VARCHAR(30),
  company_id VARCHAR(20),
  user_id INT,
  amount DECIMAL(10,2),
  declined TINYINT,
  FOREIGN KEY (card_id) REFERENCES dim_credit_card(card_id),
  FOREIGN KEY (company_id) REFERENCES dim_company(company_id),
  FOREIGN KEY (user_id) REFERENCES dim_user(user_id)
);

INSERT INTO fact_transaction
SELECT id, card_id, business_id, user_id,
       CAST(amount AS DECIMAL(10,2)), declined
FROM stg_transactions;

## Exercici 1
# Realitza una subconsulta que mostri tots els usuaris amb més de 80 transaccions utilitzant almenys 2 taules.
SELECT u.user_id, u.name, u.surname
FROM dim_user u
WHERE u.user_id IN (
  SELECT user_id
  FROM fact_transaction
  GROUP BY user_id
  HAVING COUNT(*) > 80
);

## Exercici 2
# Mostra la mitjana d'amount per IBAN de les targetes de crèdit a la companyia Donec Ltd, utilitza almenys 2 taules.
SELECT cc.iban,
       ROUND(AVG(ft.amount),2) AS avg_amount
FROM fact_transaction ft
JOIN dim_company c ON ft.company_id = c.company_id
JOIN dim_credit_card cc ON ft.card_id = cc.card_id
WHERE c.company_name = 'Donec Ltd'
AND ft.declined = 0
GROUP BY cc.iban
ORDER BY avg_amount desc;

## Nivell 2
#Crea una nova taula que reflecteixi l'estat de les targetes de crèdit basat en si les tres últimes transaccions han estat declinades 
#aleshores és inactiu, si almenys una no és rebutjada aleshores és actiu. Partint d’aquesta taula respon:
##Exercici 1
#Quantes targetes estan actives?
CREATE TABLE credit_card_status AS
SELECT card_id,
       CASE
         WHEN SUM(declined) = 3 THEN 'inactive'
         ELSE 'active'
       END AS status
FROM (
   SELECT card_id, declined
   FROM fact_transaction
   ORDER BY transaction_id DESC
) t
GROUP BY card_id;

SELECT COUNT(*) AS active_cards
FROM credit_card_status
WHERE status='active';

## Nivell 3
# Crea una taula amb la qual puguem unir les dades del nou arxiu products.csv amb la base de dades creada, tenint en compte que des de 
# transaction tens product_ids. Genera la següent consulta:
 -- 1)Crear dim_product
CREATE TABLE dim_product (
  product_id INT NOT NULL,
  product_name VARCHAR(255),
  price DECIMAL(10,2),
  colour VARCHAR(50),
  weight DECIMAL(10,2),
  warehouse_id INT,
  PRIMARY KEY (product_id)
) ENGINE=InnoDB;

ALTER TABLE dim_product
  MODIFY warehouse_id VARCHAR(20);

TRUNCATE TABLE dim_product;
INSERT INTO dim_product
SELECT
  id,
  product_name,
  REPLACE(price,'$',''),
  NULLIF(colour,''),
  weight,
  NULLIF(warehouse_id,'')
FROM stg_products;

SELECT COUNT(*) 
FROM dim_product;

-- 2) Construyendo un puente con FK + JSON_TABLE
CREATE TABLE bridge_transaction_product (
  transaction_id CHAR(36) NOT NULL,
  product_id INT NOT NULL,
  PRIMARY KEY (transaction_id, product_id),
  INDEX idx_btp_product (product_id),

  CONSTRAINT fk_btp_tx
    FOREIGN KEY (transaction_id)
    REFERENCES fact_transaction(transaction_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,

  CONSTRAINT fk_btp_product
    FOREIGN KEY (product_id)
    REFERENCES dim_product(product_id)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
) ENGINE=InnoDB;

-- 3)Importación de datos a Bridge con JSON_TABLE
INSERT INTO bridge_transaction_product (transaction_id, product_id)
SELECT ft.transaction_id,
       jt.product_id
FROM stg_transactions st
JOIN fact_transaction ft
  ON ft.transaction_id = st.id
JOIN JSON_TABLE(
    CONCAT('[', REPLACE(st.product_ids, ' ', ''), ']'),
    '$[*]' COLUMNS (
        product_id INT PATH '$'
    )
) jt;

SELECT COUNT(*) 
FROM bridge_transaction_product;

## Exercici 1
# Necessitem conèixer el nombre de vegades que s'ha venut cada producte.
SELECT p.product_id, 
       p.product_name,
       COUNT(*)        AS times_sold
FROM bridge_transaction_product b
JOIN fact_transaction  AS t ON t.transaction_id = b.transaction_id
JOIN dim_product       AS p ON p.product_id = b.product_id
WHERE t.declined = 0
GROUP BY p.product_id, p.product_name
ORDER BY times_sold DESC;
