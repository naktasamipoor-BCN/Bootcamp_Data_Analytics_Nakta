# Sprint 11 - Data Visualization with Python and Power BI

This project is part of my Data Analytics bootcamp portfolio at IT Academy / Barcelona Activa.

The main goal of this sprint was to practice the complete data visualization workflow: connecting to a MySQL database, preparing data with Python, creating visualizations, interpreting results and transferring selected charts into Power BI using Python visuals.

This sprint connects database work, Python analysis, visual storytelling and business reporting.

---

## Main Objectives

- Connect Python to a MySQL database
- Load data from a relational star-schema database
- Create an analytical DataFrame for visualization
- Explore numerical and categorical variables
- Build charts with Python visualization libraries
- Analyze distributions, comparisons and relationships
- Transfer selected visualizations to Power BI
- Use Python scripts inside Power BI visuals
- Export the final Power BI report as PDF
- Communicate insights clearly through visual reporting

---

## Database Used

The project uses the `sprint4_star` database created in Sprint 4.

The database follows a star-schema model and includes information related to:

- Transactions
- Products
- Companies
- Users
- Card status
- Time-related data
- Geographic data

A main DataFrame called `df_analysis` is created by combining information from different tables.

The column `row_id` is kept as a unique identifier for each record because one transaction can include multiple products. This helps avoid duplicate-related issues and preserves the correct level of detail for the analysis.

---

## Power BI Approach

To keep the Python notebook and the Power BI report consistent, Power BI uses a SQL query that generates the same structure as the `df_analysis` DataFrame used in Python.

This avoids loading unnecessary tables into Power BI and keeps the report focused on a single prepared analytical dataset.

In Power BI, Python visuals use the automatic DataFrame called `dataset`. For that reason, the scripts are similar to the notebook code, but they use `dataset` instead of `df_analysis`.

---

## Tools & Technologies

- Python
- Jupyter Notebook
- Pandas
- Matplotlib
- Seaborn
- SQLAlchemy
- MySQL
- MySQL Workbench
- Power BI
- Power BI Python visuals
- PDF report export
- GitHub

---

## Project Files

- `sprint11_data_visualization_powerbi.ipynb`: main Jupyter Notebook with the MySQL connection, data preparation, visualizations and interpretations
- `sprint11_data_visualization_powerbi.pbix`: Power BI report with selected Python-based visualizations
- `sprint11_data_visualization_powerbi.pdf`: exported PDF version of the Power BI report
- `requirements.txt`: list of Python libraries required to run the notebook
- `.gitignore`: configuration file to avoid uploading unnecessary files
- `README.md`: project documentation

---

## Analysis Structure

The notebook is organized into three main levels.

### Level 1 - Basic Visualizations

This level focuses on creating visualizations based on different types of variables.

The analysis includes:

- One numerical variable
- Two numerical variables
- One categorical variable
- One categorical and one numerical variable
- Two categorical variables
- Three combined variables
- Pairplot of numerical variables
- Additional boxplot analysis

Examples of visualizations created:

- Distribution of transaction amount
- Relationship between product weight and price
- Number of records by company country
- Average transaction amount by company country
- Comparison between accepted and rejected transactions
- Pairplot of numerical variables

---

### Level 2 - Correlation Analysis

This level focuses on exploring relationships between numerical variables.

The analysis includes:

- Correlation analysis
- Heatmap interpretation
- Jointplot between `weight` and `price`
- Review of possible linear relationships

The goal was to identify whether the main numerical variables showed strong relationships or visible patterns.

---

### Level 3 - Power BI Integration

This level transfers selected Level 1 visualizations into Power BI using Python visuals.

The Power BI report includes visual comparisons and business-oriented charts based on the prepared analytical dataset.

---

## Key Visual Insights

Some of the main insights from the analysis were:

- Most transaction amounts are concentrated around medium values.
- Rejected transactions are much less frequent than non-rejected transactions.
- The average transaction amount varies depending on company country and transaction status.
- No strong linear relationship is observed between the main numerical variables in the pairplot.
- Visual comparisons help identify differences between accepted and rejected transactions.

---

## Key Skills Demonstrated

- Connecting Python to MySQL
- Loading data from a relational database
- Working with a star-schema data model
- Creating an analytical DataFrame
- Preparing data for visualization
- Building charts with Matplotlib and Seaborn
- Creating histograms, bar charts, scatter plots, boxplots and pairplots
- Interpreting visual patterns
- Creating Power BI reports
- Using Python visuals inside Power BI
- Exporting Power BI reports to PDF
- Writing clear analytical explanations

---

## Learning Outcome

This sprint helped me connect Python-based analysis with Power BI reporting.

I practiced the full workflow from database connection to visual analysis and final dashboard-style reporting.

This is highly relevant for a Data Analyst role because it shows how to transform database information into clear visual insights that can support business decisions.

---

## Relevance for Data Analytics

This project demonstrates practical skills needed in Data Analyst and Business Intelligence roles:

- Database-to-dashboard workflow
- SQL and Python integration
- Data visualization
- Power BI reporting
- Exploratory data analysis
- Business-oriented interpretation
- Communication of insights through visuals

---

## Connection with Kamport

The skills developed in this sprint are also relevant for Kamport’s future product vision.

Kamport will need dashboards and operational reports to monitor logistics data such as:

- Orders
- Shipments
- Routes
- Delivery performance
- Cost indicators
- CO₂ visibility
- Customer reporting
- Operational KPIs

This sprint helped me practice the same type of workflow needed to transform operational logistics data into clear dashboards and decision-support tools.
