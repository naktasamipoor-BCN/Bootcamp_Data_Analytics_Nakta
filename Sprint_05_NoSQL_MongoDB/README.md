# Sprint 05 - NoSQL and MongoDB

This project is part of my Data Analytics bootcamp portfolio at IT Academy / Barcelona Activa.

The main goal of this sprint was to practice NoSQL database concepts using MongoDB and MongoDB Compass.

The project focuses on creating a MongoDB database, importing JSON files as collections, exploring document-based data, writing MongoDB queries and performing basic analytical operations on a cinema-related dataset.

---

## Main Objectives

- Create a MongoDB database
- Import JSON files into MongoDB collections
- Understand the structure of a document-based database
- Work with collections instead of relational tables
- Query documents using MongoDB syntax
- Filter data using simple and compound conditions
- Work with arrays and nested fields
- Use regular expressions for text filtering
- Use aggregation pipelines
- Count documents by condition
- Explore geospatial data in MongoDB Compass
- Compare NoSQL flexibility with relational database models

---

## Database Context

The project uses a MongoDB database called:

`sprint5_cinema`

The database includes several collections related to a cinema/movie dataset:

- `users`
- `comments`
- `movies`
- `theaters`
- `sessions`

Each collection stores JSON-like documents with flexible structures.

The `comments` collection contains user interactions, while `movies` includes rich descriptive attributes such as genres, year, IMDb information and awards.

The `theaters` collection includes geospatial information that can be visualized through MongoDB Compass.

---

## Tools & Technologies

- MongoDB
- MongoDB Compass
- NoSQL databases
- JSON documents
- MongoDB queries
- Aggregation pipelines
- Regular expressions
- Nested fields
- Geospatial data
- Document-based data modeling

---

## Project Files

- `task_s5_nosql_mongodb.pdf`: final task report with explanations, screenshots and query results
- `README.md`: project documentation

---

## Exercises Included

### Level 1 - Database Creation and Basic Queries

The first level focuses on creating the MongoDB database and importing the provided JSON files into collections.

Tasks include:

- Creating the `sprint5_cinema` database
- Creating collections from JSON files
- Validating the imported data
- Reviewing the number of documents in each collection
- Exploring the structure of the main collections

Basic queries include:

- Showing the first two comments in the database
- Counting the number of registered users
- Counting theaters located in California
- Identifying the first registered user
- Counting movies classified as comedy

This level helped me understand how data is stored and queried in MongoDB collections.

---

### Level 1 - Compound Queries

The project also includes more specific document queries, such as:

- Finding movies produced in 1932 that are either drama movies or in French
- Finding American movies produced between 2012 and 2014 with 5 to 9 awards

These queries demonstrate the use of:

- `$or`
- `$gte`
- `$lte`
- Array filtering
- Nested fields such as `awards.wins`
- Multiple query conditions

---

## Level 2 - Regex and Aggregation

### Email Domain Filtering

One exercise counts how many comments were written by users with an email domain matching `gameofthron.es`.

This was solved using a regular expression.

This demonstrates how MongoDB can filter text values based on flexible patterns.

### Aggregation by Zip Code

Another exercise counts how many theaters exist in each zip code within Washington D.C.

This was solved using an aggregation pipeline with:

- `$match`
- `$group`
- `$sum`

This demonstrates how MongoDB can be used not only for document retrieval but also for grouped analytical queries.

---

## Level 3 - Advanced Filtering and Geospatial Exploration

### IMDb Rating Query

The project includes a query to find movies directed by John Landis with an IMDb rating between 7.5 and 8.

This query combines:

- Filtering on array fields
- Filtering on nested fields
- Range conditions

### Theater Location Map

The final exercise uses MongoDB Compass to visualize the location of theaters on a map.

The analysis uses the geospatial field:

`location.geo`

This demonstrates how MongoDB can store and explore location-based data.

---

## Key Skills Demonstrated

- Creating a MongoDB database
- Importing JSON data
- Understanding document-based data structures
- Querying collections
- Filtering arrays
- Filtering nested fields
- Using comparison operators
- Using `$or`
- Using regular expressions
- Counting documents
- Aggregating data with `$match` and `$group`
- Working with geospatial fields
- Using MongoDB Compass for schema exploration
- Understanding NoSQL flexibility and scalability

---

## Learning Outcome

This sprint helped me understand the differences between relational and non-relational databases.

I practiced working with flexible document structures, nested fields, arrays and JSON-based data.

I also learned how MongoDB can be used for analytical queries, text filtering, aggregation and geospatial exploration.

These skills are useful for a Data Analyst role because real-world data is not always stored in relational tables. Many systems use document-based databases, APIs or semi-structured data formats that require NoSQL knowledge.

---

## Relevance for Data Analytics

This project is relevant for Data Analyst and Business Intelligence roles because it demonstrates:

- NoSQL database literacy
- Ability to work with semi-structured data
- JSON-based data understanding
- Querying nested and flexible data structures
- Basic aggregation in MongoDB
- Geospatial data exploration
- Analytical thinking beyond traditional SQL databases

---

## Connection with Kamport

The skills developed in this sprint are also relevant to Kamport’s future product vision.

Kamport may need to work with flexible operational data from different sources, such as:

- Shipment events
- Tracking updates
- API responses
- Carrier data
- Driver activity
- Route checkpoints
- Customer interactions
- Location-based delivery information

MongoDB and NoSQL concepts can be useful when dealing with semi-structured logistics data, especially when the structure of incoming data may vary between partners, carriers or API providers.

The geospatial part of this sprint is also relevant for urban logistics, route planning and last-mile delivery analysis.
