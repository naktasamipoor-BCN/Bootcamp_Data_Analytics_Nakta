# Sprint 03 - SQL Tables, Indexes and Views

This project is part of my Data Analytics bootcamp portfolio at IT Academy / Barcelona Activa.

The main goal of this sprint was to practice SQL table management, database modification, data integrity, foreign keys, indexes and views using a relational database related to companies, transactions, credit cards and users.

This sprint goes beyond basic queries and focuses on modifying the database structure, creating new tables, updating records, deleting data, creating views and validating relationships between tables.

---

## Main Objectives

- Create a new relational table
- Define primary keys and foreign keys
- Validate referential integrity before creating relationships
- Insert new records while respecting database constraints
- Update existing data
- Delete specific records safely
- Modify table structure using `ALTER TABLE`
- Remove unnecessary columns
- Create reusable SQL views
- Filter views for business analysis
- Detect and solve foreign key integrity errors
- Align the database model with a target entity-relationship diagram

---

## Database Context

This sprint continues working with the relational database used in the previous SQL exercises.

The project includes tables related to:

- Companies
- Transactions
- Credit cards
- Users

A new table called `credit_card` is created to store credit card information and connect it correctly with existing transaction data.

---

## Tools & Technologies

- SQL
- MySQL
- MySQL Workbench
- Relational databases
- Primary keys
- Foreign keys
- Indexes
- Views
- `ALTER TABLE`
- `UPDATE`
- `DELETE`
- `CREATE VIEW`
- Entity-relationship diagrams
- `information_schema`

---

## Project Files

- `sprint03_sql_tables_indexes_views.sql`: SQL script with the queries developed during the sprint
- `task_s3_sql_tables_indexes_views.pdf`: final task report with explanations, screenshots and results
- `README.md`: project documentation

---

## Exercises Included

### Level 1 - Creating and Modifying Tables

#### Exercise 1 - Create the `credit_card` Table

A new table called `credit_card` is created to store information about credit cards.

The table includes fields such as:

- `id`
- `iban`
- `pan`
- `pin`
- `cvv`
- `expiring_date`

The `id` field is defined as the primary key, allowing each credit card to be uniquely identified.

The relationship between `credit_card` and `transaction` is established through the field:

```sql
transaction.credit_card_id
