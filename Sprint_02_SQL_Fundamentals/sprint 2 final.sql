## Sprint2:
##Nivell 1
##Exercici 1
##A partir dels documents adjunts (estructura_dades i dades_introduir), importa les dues 
##taules. Mostra les característiques principals de l'esquema creat i explica les 
##diferents taules i variables que existeixen. Assegura't d'incloure un diagrama que 
##il·lustri la relació entre les diferents taules i variables.

SHOW TABLES;

DESCRIBE company;

DESCRIBE transaction;

SHOW CREATE TABLE company;

SHOW CREATE TABLE transaction;

SELECT TABLE_NAME,COLUMN_NAME,CONSTRAINT_NAME,
  REFERENCED_TABLE_NAME,
  REFERENCED_COLUMN_NAME
FROM information_schema.KEY_COLUMN_USAGE
WHERE TABLE_SCHEMA = 'transactions'
  AND REFERENCED_TABLE_NAME IS NOT NULL
ORDER BY TABLE_NAME, COLUMN_NAME;

SELECT TABLE_NAME,COLUMN_NAME,DATA_TYPE,IS_NULLABLE,COLUMN_KEY
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'transactions'
ORDER BY TABLE_NAME, ORDINAL_POSITION;

SELECT * 
FROM company
LIMIT 10;

SELECT * 
FROM transaction 
LIMIT 10;

##Exercici 2 
##Utilitzant JOIN realitzaràs les següents consultes:

##2-1 Llistat dels països que estan generant vendes.
SELECT DISTINCT country
FROM company     AS c
JOIN transaction AS t ON t.company_id = c.id
ORDER BY country ASC;

##2-2 Des de quants països es generen les vendes.
SELECT COUNT(DISTINCT country) AS total_countries
FROM company                   AS c
JOIN transaction               AS t ON t.company_id = c.id;

##2-3 Identifica la companyia amb la mitjana més gran de vendes.
SELECT c.company_name, c.country, 
       ROUND(AVG(t.amount), 2) AS AVG_vendes
FROM company     AS c
JOIN transaction AS t ON t.company_id = c.id
Group BY c.company_name,c.country
ORDER BY AVG_vendes DESC
LIMIT 1;
                                 
## Exercici 3
## Utilitzant només subconsultes (sense utilitzar JOIN):
##3-1 Mostra totes les transaccions realitzades per empreses d'Alemanya.
SELECT *
FROM transaction
WHERE company_id IN (SELECT id
                     FROM company
                     WHERE country = 'Germany');

##3-2 Llista les empreses que han realitzat transaccions per un amount superior.
## a la mitjana de totes les transaccions.

 SELECT (SELECT c.company_name
         FROM company AS c
		 WHERE c.id = t.company_id) AS company_name, ROUND(t.amount, 2) AS amount
FROM transaction  AS t
WHERE t.amount > (SELECT AVG(t2.amount)
                  FROM transaction  AS t2)
ORDER By amount DESC; 

##3-3 Eliminaran del sistema les empreses que no tenen transaccions registrades, 
## entrega el llistat d'aquestes empreses.
SELECT *
FROM company AS c
WHERE NOT EXISTS (SELECT 1
                  FROM transaction AS t
				  WHERE t.company_id = c.id);

##check 
SELECT COUNT(*) AS companies_without_tx
FROM company    AS c
WHERE NOT EXISTS (SELECT 1
                  FROM transaction AS t
                  WHERE t.company_id = c.id);
				
##Nivell 2
##Exercici 1
##Identifica els cinc dies que es va generar la quantitat més gran d'ingressos a l'empresa 
##per vendes. Mostra la data de cada transacció juntament amb el total de les vendes.				
SELECT
   DATE(t.timestamp)        AS fecha_venta,
   c.company_name           AS nombre_empresa,
   ROUND(SUM(t.amount), 2)  AS total_ingresos
FROM transaction         AS t
JOIN company             AS c ON t.company_id = c.id
WHERE t.declined = 0
  AND amount IS NOT NULL
    AND timestamp IS NOT NULL
GROUP BY DATE(t.timestamp), c.company_name
ORDER BY total_ingresos DESC
LIMIT 5;

##2-2 Quina és la mitjana de vendes per país? Presenta els resultats ordenats de major a
## menor mitjà.
SELECT c.country,
	   ROUND(AVG(t.amount), 2) AS media_ventas
FROM company AS c
JOIN transaction AS t ON t.company_id = c.id
GROUP BY c.country
ORDER BY media_ventas DESC;

##Exercici 3
##En la teva empresa, es planteja un nou projecte per a llançar algunes campanyes 
##publicitàries per a fer competència a la companyia "Non Institute". Per a això, 
##et demanen la llista de totes les transaccions realitzades per empreses que estan 
##situades en el mateix país que aquesta companyia.
#3_1 Mostra el llistat aplicant JOIN i subconsultes.
SELECT company_name,company_id,t.*
FROM   transaction As t
Join   company     As c ON t.company_id=c.id
WHERE  c.country IN ( SELECT c2.country
                      FROM company AS c2
					  WHERE c2.company_name = 'Non Institute');
                      
##Mostra el llistat aplicant solament subconsultes.
SELECT (SELECT c.company_name
			 FROM company c
             WHERE c.id = t.company_id) AS company_name,
            (SELECT c.country
             FROM company c
             WHERE c.id = t.company_id) AS country , t.*
FROM transaction AS t
WHERE t.company_id IN (SELECT c1.id
                       FROM company c1
                        WHERE c1.country IN (SELECT c2.country
                                            FROM company AS c2
                                            WHERE c2.company_name = 'Non Institute')
                      );
                      
##Nivell 3
##Exercici 1
#3Presenta el nom, telèfon, país, data i amount, d'aquelles empreses que van realitzar 
##transaccions amb un valor comprès entre 350 i 400 euros i en alguna d'aquestes dates: 
##29 d'abril del 2015, 20 de juliol del 2018 i 13 de març del 2024. Ordena els resultats
## de major a menor quantitat.
SELECT c.company_name    AS nombre_empresa,
	   c.phone           AS telefono,
	   c.country         AS pais,
       DATE(t.timestamp) AS fecha_transaccion,
       t.amount          AS importe
FROM company             AS c
JOIN transaction         AS t  ON t.company_id = c.id
WHERE t.amount >= 350
  AND t.amount <= 400
  AND DATE(t.timestamp) IN ('2015-04-29',
                          '2018-07-20',
						  '2024-03-13')
ORDER BY t.amount DESC;

#Exercici 2
##Necessitem optimitzar l'assignació dels recursos i dependrà de la capacitat operativa 
#que es requereixi, per la qual cosa et demanen la informació sobre la quantitat de 
#transaccions que realitzen les empreses, però el departament de recursos humans és
# exigent i vol un llistat de les empreses on especifiquis si tenen més de 400 
#transaccions o menys.
SELECT c.company_name AS nombre_empresa,
       COUNT(t.id)    AS cantidad_transacciones,
CASE
    WHEN COUNT(t.id) > 400 THEN 'Mas de 400'
    ELSE '400 o menos'
    END AS categoria
FROM company c
LEFT JOIN transaction AS t ON t.company_id = c.id
						   AND t.declined = 0
GROUP BY c.id, c.company_name
ORDER BY cantidad_transacciones DESC;