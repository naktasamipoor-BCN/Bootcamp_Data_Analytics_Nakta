##Sprint 3
## Nivell 1
## Exercici 1
#La teva tasca és dissenyar i crear una taula anomenada "credit_card" que emmagatzemi detalls crucials sobre les targetes de crèdit. 
#La nova taula ha de ser capaç d'identificar de manera única cada targeta i establir una relació adequada amb les altres dues taules 
#("transaction" i "company"). Després de crear la taula serà necessari que ingressis la informació del document denominat 
#"dades_introduir_credit". Recorda mostrar el diagrama i realitzar una breu descripció d'aquest.

CREATE TABLE IF NOT EXISTS credit_card (
  id            VARCHAR(20)  NOT NULL,
  iban          VARCHAR(34)  NOT NULL,
  pan           CHAR(19)     NOT NULL,
  pin           CHAR(4)      NOT NULL,
  cvv           CHAR(4)      NOT NULL,
  expiring_date VARCHAR(10)  NOT NULL,
  PRIMARY KEY (id)
);

SHOW CREATE TABLE transaction;

DESCRIBE credit_card;

SELECT COUNT(*) AS total_credit_cards
FROM credit_card;

SELECT COUNT(*)       AS  invalid_refs
FROM transaction      AS t
LEFT JOIN credit_card AS c ON c.id = t.credit_card_id
WHERE t.credit_card_id IS NOT NULL
  AND c.id IS NULL;
  
  
-- Se crea la clave foránea entre transaction y credit_card una vez verificada
-- la integridad de los datos, garantizando la coherencia del modelo relacional.
ALTER TABLE transaction
  ADD CONSTRAINT fk_transaction_credit_card
  FOREIGN KEY (credit_card_id) REFERENCES credit_card(id);

SHOW CREATE TABLE transaction;

ALTER TABLE transaction
  MODIFY credit_card_id VARCHAR(20);

##Exercici 2
#3El departament de Recursos Humans ha identificat un error en el número de compte associat a la targeta de crèdit amb ID CcU-2938. 
## La informació que ha de mostrar-se per a aquest registre és: TR323456312213576817699999. Recorda mostrar que el canvi es va realitzar.
UPDATE credit_card
SET iban = 'TR323456312213576817699999'
WHERE id = 'CcU-2938';

SELECT id, iban
FROM credit_card
WHERE id = 'CcU-2938';

##Exercici 3
##En la taula "transaction" ingressa una nova transacció amb la següent informació:

INSERT INTO transaction
(id, credit_card_id, company_id, user_id, lat, longitude, amount, declined)
VALUES
('108B1D1D-5B23-A76C-55EF-C568E49A99DD', 'CcU-9999', 'b-9999', 
  9999, 829.999, -117.999, 111.11, 0);

SELECT *
FROM company
WHERE id = 'b-9999';

INSERT INTO company (id, company_name)
VALUES ('b-9999', 'Test Company');

-- check
SELECT * FROM company 
WHERE id = 'b-9999';

-- check
SELECT id
FROM credit_card
WHERE id = 'CcU-9999';

INSERT INTO credit_card (id, iban, pan, pin, cvv, expiring_date)
VALUES ('CcU-9999', 'TR323456312213576817699999', '1111222233334444',
         '1234', '123', '2030-12-31');

-- check
SELECT id, iban
FROM credit_card
WHERE id = 'CcU-9999';

-- control
SELECT 
id, credit_card_id, company_id, user_id, lat, longitude, amount, declined
FROM transaction
WHERE id = '108B1D1D-5B23-A76C-55EF-C568E49A99DD';

##Exercici 4
#Des de recursos humans et sol·liciten eliminar la columna "pan" de la taula credit_card. Recorda mostrar el canvi realitzat.
ALTER TABLE credit_card
DROP COLUMN pan;

DESCRIBE credit_card;

##Nivell 2
##Exercici 1
#Elimina de la taula transaction el registre amb ID 000447FE-B650-4DCF-85DE-C7ED0EE1CAAD de la base de dades.
SELECT *
FROM transaction
WHERE id = '000447FE-B650-4DCF-85DE-C7ED0EE1CAAD';

DELETE
FROM transaction
WHERE id = '000447FE-B650-4DCF-85DE-C7ED0EE1CAAD';

##Exercici 2
#La secció de màrqueting desitja tenir accés a informació específica per a realitzar anàlisi i estratègies efectives. S'ha sol·licitat 
#crear una vista que proporcioni detalls clau sobre les companyies i les seves transaccions. Serà necessària que creïs una vista 
#anomenada VistaMarketing que contingui la següent informació: Nom de la companyia. Telèfon de contacte. País de residència.
#Mitjana de compra realitzat per cada companyia. Presenta la vista creada, ordenant les dades de major a menor mitjana de compra.
CREATE VIEW VistaMarketing AS
 SELECT c.company_name     AS nombre_compania,
       c.phone             AS telefono,
       c.country           AS pais,
       AVG(t.amount)       AS media_compra
 FROM company              AS c
 JOIN transaction          AS t ON t.company_id = c.id
 WHERE t.declined = 0
 GROUP BY c.id, c.company_name,c.phone,c.country;

SELECT *
FROM VistaMarketing
ORDER BY media_compra DESC;

##Exercici 3
#Filtra la vista VistaMarketing per a mostrar només les companyies que tenen el seu país de residència en "Germany"
SELECT *
FROM VistaMarketing
WHERE pais = 'Germany'
ORDER BY media_compra DESC;

##Nivell 3
##Exercici 1
#La setmana vinent tindràs una nova reunió amb els gerents de màrqueting. Un company del teu equip va realitzar modificacions en la base 
#de dades, però no recorda com les va realitzar. 
SHOW TABLES;

SELECT kcu.CONSTRAINT_NAME, kcu.COLUMN_NAME,
       kcu.REFERENCED_TABLE_NAME, kcu.REFERENCED_COLUMN_NAME
FROM information_schema.KEY_COLUMN_USAGE AS kcu
WHERE kcu.TABLE_SCHEMA = DATABASE()
  AND kcu.TABLE_NAME = 'transaction'
  AND kcu.REFERENCED_TABLE_NAME IS NOT NULL;

ALTER TABLE user
RENAME TO data_user;

#check
SHOW TABLES LIKE 'data_user';
SELECT COUNT(*) 
FROM data_user;

-- check Comprobación de la consistencia de los datos y tipos de columnas
DESCRIBE transaction;
DESCRIBE data_user;

-- Consistencia de los datos y tipos de columnas
ALTER TABLE data_user
MODIFY id INT NOT NULL;

ALTER TABLE transaction
MODIFY user_id INT;

ALTER TABLE transaction
ADD CONSTRAINT fk_transaction_user
FOREIGN KEY (user_id)
REFERENCES data_user(id);

-- Buscar Orphan user_id
SELECT COUNT(*)     AS orphan_user_ids
FROM transaction    AS t
LEFT JOIN data_user AS du ON du.id = t.user_id
WHERE t.user_id IS NOT NULL
  AND du.id IS NULL;

SELECT t.id, t.user_id
FROM transaction    AS t
LEFT JOIN data_user AS du ON du.id = t.user_id
WHERE t.user_id IS NOT NULL
  AND du.id IS NULL;

INSERT INTO data_user (id)
VALUES ('9999');

-- Verificar cambios a realizar en Tabla Company
DESCRIBE company;
ALTER TABLE company DROP website;

-- Verificar cambios a realizar en Tabla data user
DESCRIBE data_user;
ALTER TABLE data_user
  RENAME COLUMN email TO personal_email,
  MODIFY COLUMN id INT;

-- Verificar cambios a realizar en Tabla Credit_card
DESCRIBE Credit_card;
ALTER TABLE credit_card
  MODIFY COLUMN iban VARCHAR(50),
  MODIFY COLUMN pin VARCHAR(4),
  MODIFY COLUMN cvv INT,
  MODIFY COLUMN expiring_date VARCHAR(20),
  ADD COLUMN fecha_actual DATE;
  
  -- Mostrar cambios en la tabla
SHOW CREATE TABLE data_user;
SHOW CREATE TABLE company;
SHOW CREATE TABLE credit_card;
SHOW CREATE TABLE transaction;

##Exercici 2
#L'empresa també us demana crear una vista anomenada "InformeTecnico" que contingui la següent informació:
#ID de la transacció,Nom de l'usuari/ària,Cognom de l'usuari/ària,IBAN de la targeta de crèdit usada.Nom de la companyia de la transacció 
#realitzada.
#Assegureu-vos d'incloure informació rellevant de les taules que coneixereu i utilitzeu àlies per canviar de nom columnes segons calgui.

CREATE OR REPLACE VIEW InformeTecnico AS
SELECT t.id            AS transaction_id,
       du.name         AS user_name,
       du.surname      AS user_surname,
       cc.iban         AS credit_card_iban,
       c.company_name  AS company_name
FROM transaction       AS t
JOIN data_user         AS du ON du.id = t.user_id
JOIN credit_card       AS cc ON cc.id = t.credit_card_id
JOIN company           AS c  ON c.id = t.company_id;

SELECT *
FROM InformeTecnico
ORDER BY transaction_id DESC;


