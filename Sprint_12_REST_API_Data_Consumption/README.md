# Sprint 12 - REST API Data Consumption

This project is part of my Data Analytics bootcamp portfolio at IT Academy / Barcelona Activa.

The main goal of this sprint was to practice how to consume data from REST APIs using Python, interpret HTTP status codes, work with JSON responses and transform API data into structured pandas DataFrames.

The project is developed in a Jupyter Notebook and is organized into three levels: REST API fundamentals, interaction with a real public API, and public data extraction from Open Data Barcelona.

---

## Main Objectives

- Send HTTP requests using the `requests` library
- Query public APIs using the `GET` method
- Interpret HTTP status codes such as `200`, `201` and `404`
- Send `POST`, `PATCH` and `DELETE` requests
- Read and process JSON responses
- Transform JSON data into pandas DataFrames
- Query public datasets through the Open Data Barcelona API
- Export final data into a `.csv` file
- Prepare external API data for future analysis and visualization

---

## Tools & Technologies

- Python
- Jupyter Notebook
- requests
- pandas
- JSON
- REST APIs
- HTTP methods
- Open Data Barcelona API
- CSV export
- GitHub

---

## Project Files

- `sprint12_rest_api_data_consumption.ipynb`: main notebook with API requests, JSON processing, DataFrame creation and CSV export
- `zonas_carga_descarga_barcelona.csv`: exported dataset created from Open Data Barcelona API results
- `README.md`: English project documentation
- `README_ES.md`: Spanish project documentation

---

## Notebook Structure

### Level 1 - REST API Fundamentals with JSONPlaceholder

In the first level, the public JSONPlaceholder API is used to practice basic REST API methods.

The work includes:

- Querying resources with `GET`
  - `/posts`
  - `/users`
  - `/todos`
- Checking status codes
- Reviewing the number of records returned
- Querying a non-existing post to receive a `404` error
- Creating a fictional post using `POST`
- Partially updating a post using `PATCH`
- Simulating a delete operation using `DELETE`

JSONPlaceholder is used as a practice API. It returns responses for creation, update and deletion requests, but it does not actually modify the server data.

---

### Level 2 - Working with a Real Public API

In the second level, the project works with the REST Countries API.

Before selecting this API, other options related to sustainability and carbon footprint were reviewed. REST Countries API was selected because it provides clear endpoints, does not require authentication, returns JSON data and allows easy transformation into a pandas DataFrame.

The work includes:

- Reviewing available endpoints
- Reviewing useful parameters such as `fields`
- Sending a `GET` request to the `/v3.1/region/europe` endpoint
- Extracting fields such as:
  - Country name
  - Capital
  - Region
  - Population
  - Languages
  - Currencies
- Transforming nested JSON fields into a cleaner tabular structure
- Creating a pandas DataFrame from the API response

---

### Level 3 - Open Data Barcelona API

In the third level, the Open Data Barcelona API is used to search and retrieve public urban data from Barcelona.

The search focuses on topics connected with Kamport and the final Data Analytics project, such as:

- Urban logistics
- Last-mile delivery
- Loading and unloading zones
- Traffic
- Urban restrictions
- Air quality
- Sustainability

Different keywords are tested using `package_search`. The selected dataset is:

`zones-carrega-descarrega`

This dataset contains information about loading and unloading zones in Barcelona. It does not contain direct shipment or parcel delivery data, but it provides useful urban infrastructure information related to last-mile logistics.

The work includes:

- Using `package_search` to find relevant datasets
- Using `package_show` to review dataset details
- Selecting a CSV resource with `datastore_active = True`
- Using `datastore_search` to retrieve records
- Converting records into a pandas DataFrame
- Exporting the final DataFrame to CSV

The generated file is:

`zonas_carga_descarga_barcelona.csv`

---

## Generated Output

The notebook generates a CSV file with records retrieved from Open Data Barcelona:

`zonas_carga_descarga_barcelona.csv`

This file can be reused in future analysis, dashboards or other data analytics tools.

---

## Key Skills Demonstrated

- REST API data consumption
- HTTP request handling
- Status code interpretation
- JSON response processing
- Working with nested JSON structures
- pandas DataFrame creation
- Data extraction from public APIs
- Open Data exploration
- CSV export
- Preparing external data for analysis
- Clear notebook documentation

---

## Learning Outcome

This sprint helped me practice the complete workflow of consuming data from APIs.

First, I worked with a practice API to understand the main HTTP methods. Then, I queried a real public API and transformed its JSON response into a DataFrame. Finally, I used the Open Data Barcelona API to search for a dataset, select a useful resource, retrieve real records and export the result to CSV.

This workflow is important for Data Analyst roles because many real-world data sources are accessed through APIs and need to be transformed into tabular formats before analysis, visualization or reporting.

---

## Relevance for Data Analytics

This project is especially relevant for Data Analyst and Business Intelligence roles because it demonstrates:

- Ability to work with external data sources
- Basic API literacy
- JSON-to-DataFrame transformation
- Public data exploration
- Data preparation for reporting
- Reproducible data extraction workflow
- Connection between raw API data and analytical outputs

---

## Connection with Kamport

This sprint is directly connected to Kamport’s future product vision.

Kamport is focused on urban logistics and last-mile delivery. The dataset selected in Level 3 is related to loading and unloading zones in Barcelona, which can be relevant for understanding urban logistics infrastructure.

This type of data could support future analysis related to:

- Urban route planning
- Loading and unloading zone identification
- Last-mile delivery optimization
- Urban logistics infrastructure
- Sustainability and mobility analysis
- API-based integrations with logistics partners
- Operational dashboards and reporting

The skills developed in this sprint are useful for future logistics-tech product development, especially for connecting Kamport with external APIs, public datasets, carrier systems and operational data sources.
