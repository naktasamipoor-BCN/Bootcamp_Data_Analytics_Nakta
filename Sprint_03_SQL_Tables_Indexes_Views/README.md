# Sprint 02 - SQL Fundamentals

This project is part of my Data Analytics bootcamp portfolio at IT Academy / Barcelona Activa.

The main goal of this sprint was to practice SQL fundamentals using a relational database related to companies and transactions.

The project focuses on database structure, table relationships, primary and foreign keys, JOIN queries, subqueries, aggregation functions and business-oriented SQL analysis.

---

## Main Objectives

- Import and inspect relational database tables
- Understand the structure of a relational schema
- Identify primary keys and foreign keys
- Analyze relationships between tables
- Use JOINs to combine company and transaction data
- Use subqueries without JOINs
- Apply aggregation functions such as `COUNT`, `AVG` and `SUM`
- Filter and sort business data
- Use date and amount conditions
- Apply `CASE` logic to classify companies based on transaction volume

---

## Database Structure

The project uses a relational database called `transactions`.

The database contains two main tables:

### `company`

This table stores company information.

Main fields include:

- `id`: unique company identifier and primary key
- `company_name`: company name
- `phone`: phone number
- `email`: email address
- `country`: company country
- `website`: company website

### `transaction`

This table stores transaction information.

Main fields include:

- `id`: unique transaction identifier and primary key
- `credit_card_id`: credit card identifier
- `company_id`: foreign key linked to the `company` table
- `user_id`: user identifier
- `lat`: latitude
- `longitude`: longitude
- `timestamp`: transaction date and time
- `amount`: transaction amount
- `declined`: transaction status

---

## Relationship Between Tables

The database follows a one-to-many relationship:

- One company can have many transactions.
- Each transaction belongs to one company.

The relationship is created through:

```sql
transaction.company_id → company.id
