# Sprint 04 - SQL Data Modeling

This project is part of my Data Analytics bootcamp portfolio at IT Academy / Barcelona Activa.

The main goal of this sprint was to design and build a relational database using a star schema model, load data from CSV files, create staging tables, transform raw data into analytical tables and solve more advanced SQL modeling problems.

This sprint connects database creation, ETL logic, data modeling, fact and dimension tables, window functions and many-to-many relationship handling.

---

## Main Objectives

- Create a new database for the project
- Load CSV files using SQL
- Create staging tables for raw data import
- Design a star schema model
- Create dimension tables and a fact table
- Define primary keys and foreign keys
- Preserve referential integrity
- Use subqueries and aggregation queries
- Create a credit card status table using transaction history
- Apply window functions with `ROW_NUMBER()`
- Integrate product data into the model
- Resolve a many-to-many relationship using a bridge table
- Use `JSON_TABLE` to split multiple product IDs stored in one field
- Prepare the model for future analytical queries

---

## Database Design

The project creates a database called `sprint4_star`.

The design follows a star schema model, where a central fact table is connected to several dimension tables.

### Dimension Tables

The model includes dimension tables such as:

- `dim_user`
- `dim_company`
- `dim_credit_card`
- `dim_product`

These tables store descriptive information about users, companies, credit cards and products.

### Fact Table

The main fact table is:

- `fact_transaction`

This table stores transactional information such as:

- transaction ID
- card ID
- company ID
- user ID
- amount
- transaction status
- geographic information

---

## ETL and Staging Process

Before creating the final analytical model, raw CSV files are loaded into staging tables.

The staging layer is used to import data first and avoid applying complex transformations directly during the initial load.

This process helps to:

- Control the data import
- Detect loading warnings
- Prepare data before transformation
- Keep the final model cleaner
- Separate raw data from analytical tables

The data loading process is performed with `LOAD DATA`, following the exercise requirements.

---

## Tools & Technologies

- SQL
- MySQL
- MySQL Workbench
- Relational databases
- Star schema modeling
- Staging tables
- Fact tables
- Dimension tables
- Foreign keys
- Window functions
- `ROW_NUMBER()`
- `JSON_TABLE`
- Bridge tables
- CSV data loading
- ETL workflow

---

## Project Files

- `sprint04_sql_data_modeling.sql`: SQL script with the database creation, data loading, transformations and analytical queries
- `task_s4_sql_data_modeling.pdf`: final task report with explanations, screenshots, diagrams and query results
- `README.md`: project documentation

---

## Project Structure

### Level 1 - Database Creation and Star Schema

The first level focuses on creating the database and loading data from CSV files.

The workflow includes:

- Creating a new database
- Creating staging tables
- Loading raw CSV data with `LOAD DATA`
- Reviewing loading warnings
- Creating the final analytical tables
- Building a star schema with dimension and fact tables
- Defining relationships through foreign keys

The final model includes a central transaction fact table connected to descriptive dimension tables.

---

### Exercise 1 - Users with More Than 80 Transactions

A subquery is used to identify users with more than 80 transactions.

The query groups transactions by `user_id`, counts the number of transactions and filters users using `HAVING`.

This exercise demonstrates:

- Subqueries
- Aggregation
- `COUNT(*)`
- `GROUP BY`
- `HAVING`
- Joining aggregated results with user information

---

### Exercise 2 - Average Amount by IBAN for Donec Ltd

This query calculates the average transaction amount by credit card IBAN for the company `Donec Ltd`.

The query uses multiple tables from the star schema:

- `fact_transaction`
- `dim_company`
- `dim_credit_card`

The result is grouped by IBAN and ordered by average amount.

This exercise demonstrates:

- JOINs across fact and dimension tables
- Aggregation with `AVG()`
- Rounding monetary values
- Business-oriented SQL analysis

---

## Level 2 - Credit Card Status Table

In this level, a new table is created to classify credit cards as active or inactive.

The logic is based on the last three transactions of each card:

- If the last three transactions were declined, the card is classified as `inactive`
- If at least one of the last three transactions was not declined, the card is classified as `active`

To solve this correctly, the project uses the window function:

```sql
ROW_NUMBER()
