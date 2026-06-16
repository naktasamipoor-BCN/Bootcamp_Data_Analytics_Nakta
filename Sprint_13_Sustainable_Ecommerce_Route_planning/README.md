# Sustainable E-commerce Route Planning

## A Data-Driven Analysis of Time, Traffic, Cost and CO₂

This repository contains a final Data Analytics project focused on sustainable e-commerce logistics and last-mile delivery decision-making.

The main idea of the project is simple: a delivery option should not be evaluated only by speed or cost. A better delivery decision should balance operational performance and environmental impact, including delivery time, route cost, traffic conditions, route reliability, delivery efficiency and estimated CO₂ emissions.

The project uses public datasets to explore these factors and builds a simplified **Delivery Option Score** as an educational decision-support model.

> This is an educational data analytics project. The scoring model is intentionally simple, transparent and explainable. It is not a production routing algorithm.

---

## Project Objectives

The main objectives of this project are:

- Analyze e-commerce delivery route performance.
- Study the relationship between delivery time, distance, cost and traffic.
- Analyze CO₂ emissions across vehicle types, route types and traffic conditions.
- Explore delivery reliability, congestion impact and on-time delivery behavior.
- Add a real urban traffic context using Barcelona open traffic data.
- Build a simple and explainable Delivery Option Score.
- Create final CSV outputs that support a GitHub repository and final presentation.
- Communicate insights clearly using simple Python code, Markdown explanations and visualizations.

---

## Final Deliverables

The final project deliverables are organized as follows:

- Main analysis notebook: `notebooks/sustainable_ecommerce_route_planning.ipynb`
- Optional Streamlit dashboard app: `app.py`
- Generated CSV outputs: `data/outputs/`
- Final presentation PDF: `presentation/sustainable_ecommerce_route_planning_presentation_EN_final.pdf`
- Final reports: `reports/`

> The editable PowerPoint version is kept separately to avoid increasing the repository size. The official presentation deliverable in this repository is the PDF version.

---

## Project Files

The main analysis notebook is located in the `notebooks/` folder:

```text
notebooks/sustainable_ecommerce_route_planning.ipynb
```

The optional Streamlit dashboard app is located at the root of the repository:

```text
app.py
```

The final presentation is included as a PDF in the `presentation/` folder, and the final reports are stored in the `reports/` folder.

The notebook follows this structure:

```text
1. Project Overview and Data Loading
2. Data Cleaning and Preparation
3. Exploratory Data Analysis (EDA)
4. KPI Calculation and KPI Dashboard
5. Delivery Option Score
6. Final Improvements, Conclusions and Future Work
7. Final Project Output Check
```

The notebook was designed to be readable and easy to explain. The code is kept simple on purpose, with Markdown explanations before and after the main analysis steps.

> Note: In the GitHub version, the notebook is stored inside `notebooks/`. The file paths are defined with `Path("..")`, so the notebook reads raw data from `../data/raw/` and writes output files to `../data/outputs/`. No absolute local computer paths are required.


---

## Repository Structure

The repository is organized using a clean project structure. Raw datasets are stored in `data/raw/`, generated CSV outputs are stored in `data/outputs/`, and the final notebook is stored in `notebooks/`.

```text
sustainable-ecommerce-route-planning/
│
├── README.md
├── requirements.txt
├── app.py
│
├── notebooks/
│   └── sustainable_ecommerce_route_planning.ipynb
│
├── data/
│   ├── raw/
│   │   ├── ecommerce_logistics_route_planning_dataset.csv
│   │   ├── green ecommerce_logistics_carbon_emissions_v1.csv
│   │   ├── Transportation and Logistics Tracking Dataset. 2.xlsx
│   │   ├── 2026_01_Gener_TRAMS_TRAMS.csv
│   │   ├── 2026_02_Febrer_TRAMS_TRAMS.csv
│   │   ├── 2026_03_Marc_TRAMS_TRAMS.csv
│   │   ├── 2026_04_Abril_TRAMS_TRAMS.csv
│   │   ├── 2026_05_Maig_TRAMS_TRAMS.csv
│   │   └── 2026_06_Juny_TRAMS_TRAMS.csv
│   │
│   └── outputs/
│       ├── delivery_option_score_results.csv
│       ├── top_delivery_options.csv
│       ├── route_decision_matrix.csv
│       ├── route_examples.csv
│       ├── kpi_summary.csv
│       ├── presentation_kpi_summary.csv
│       ├── emission_intensity_by_vehicle.csv
│       ├── green_fleet_transition_scenario.csv
│       ├── barcelona_trams_valid_status_summary.csv
│       ├── barcelona_trams_monthly_valid_summary.csv
│       ├── congestion_impact_summary.csv
│       ├── co2_by_vehicle_traffic.csv
│       ├── iqr_outlier_summary.csv
│       ├── kruskal_test_summary.csv
│       ├── on_time_rate_by_distance_group.csv
│       ├── score_category_component_profile.csv
│       └── statistical_relationship_checks.csv
│
├── presentation/
│   └── sustainable_ecommerce_route_planning_presentation_EN_final.pdf
│
└── reports/
    ├── report_Sprint_13_Sustainable_Ecommerce_Route_planning.pdf
    └── informe_Sprint_13_Sustainable_Ecommerce_Route_planning.pdf
```

The notebook uses `pathlib` to define the project folders. It is expected to be executed from inside the `notebooks/` folder, with the raw datasets placed inside `data/raw/` and generated outputs saved inside `data/outputs/`.

---

## Datasets Used

### 1. E-commerce Logistics Route Planning Dataset

This is the main operational dataset of the project.

It contains **1,000 delivery route records** and **18 variables** related to:

- Delivery location
- Delivery distance
- Delivery time window
- Order priority
- Vehicle capacity and utilization
- Traffic density
- Average speed
- Weather impact
- Fuel and driver costs
- Optimized route time
- Optimized route cost
- Delivery efficiency
- Route reliability

This dataset is used to analyze route planning, cost behavior, traffic impact, delivery efficiency and operational reliability.

---

### 2. Green Logistics: Carbon Footprint for E-Commerce

This dataset contains **12,000 delivery records** focused on carbon footprint estimation in e-commerce logistics.

It includes:

- Vehicle type
- Route type
- Delivery distance
- Package weight
- Traffic conditions
- Carbon emissions in kgCO₂e
- Eco-friendly delivery flag

This dataset is used to analyze sustainability, CO₂ emissions, vehicle comparison, emission intensity and green delivery opportunities.

---

### 3. Transportation and Logistics Tracking Dataset

This dataset is used as a supporting source for reliability and congestion analysis.

It includes multiple logistics-related tables such as:

- On-time delivery impact
- Customer ratings
- Route ratings
- Delivery time with and without congestion
- Weather conditions
- Regional delivery time differences

In this project, only the most relevant sheets were selected to keep the analysis focused and manageable.

---

### 4. Barcelona TRAMS Traffic Dataset

This dataset is used as a real urban traffic context layer.

It contains traffic status information by road section in Barcelona for the first six months of 2026.

The traffic status codes were interpreted as:

| Code | Meaning |
|---:|---|
| 0 | No data |
| 1 | Very fluid |
| 2 | Fluid |
| 3 | Dense |
| 4 | Very dense |
| 5 | Congestion |
| 6 | Section closed |

Since `0` represents missing traffic status, the main Barcelona traffic insights are based on valid traffic records only.

---

## Methodology

The project follows a simple and explainable data analysis workflow:

1. Load datasets.
2. Inspect data structure.
3. Clean column names and data types.
4. Check missing values and duplicates.
5. Perform exploratory data analysis.
6. Calculate key performance indicators.
7. Create visualizations.
8. Build a simplified Delivery Option Score.
9. Add additional validation and scenario analysis.
10. Export final CSV outputs.
11. Summarize conclusions, limitations and future work.
12. Run a final technical output check.

The analysis is modular because the datasets come from different sources and do not share a common transaction ID.

---

## Key Performance Indicators

The main KPIs are grouped into four areas.

### Route Planning KPIs

- Total route options
- Average delivery distance
- Average optimized route time
- Minimum optimized route time
- Average optimized route cost
- Minimum optimized route cost
- Average traffic density index
- Average delivery efficiency score
- Average route reliability index

### CO₂ and Sustainability KPIs

- Total carbon records
- Average CO₂ emissions per delivery
- Total CO₂ emissions
- Eco-friendly delivery rate
- Average emission intensity per km
- CO₂ by vehicle type
- CO₂ by route type
- CO₂ by traffic condition

### Tracking and Reliability KPIs

- Clean on-time delivery rate
- Clean delayed delivery rate
- Average customer rating
- Delivery time with and without congestion
- Congestion delay
- Congestion delay percentage
- On-time delivery rate by distance group

### Barcelona Traffic Context KPIs

- Valid traffic record share
- Most common valid traffic status
- High congestion share
- Monthly congestion trend
- Valid actual vs predicted traffic match rate

---

## Main KPI Summary

The final presentation-ready KPI summary includes the following messages:

| Project area | Main KPI message |
|---|---|
| Route Planning | Average optimized route time is **74.25 minutes**, with an average cost of **565.86 cost units**. |
| CO₂ and Sustainability | Average CO₂ emissions are **71.99 kgCO₂e**, and the eco-friendly rate is **42.70%**. |
| Tracking and Reliability | Clean on-time delivery rate is **36.91%**, while clean delayed delivery rate is **63.09%**. |
| Barcelona Traffic Context | After excluding `No data`, the most common valid Barcelona TRAMS traffic status is **Fluid**, with a valid prediction match rate of **77.21%**. |

---

## Delivery Option Score

A simplified **Delivery Option Score** was created to compare route options across multiple criteria.

The score combines:

- Time score
- Cost score
- Estimated CO₂ score
- Reliability score
- Traffic score
- Efficiency score

For time, cost, estimated CO₂ and traffic, lower values receive higher scores.  
For reliability and efficiency, higher values receive higher scores.

Each component is converted to a 0-100 scale and then combined using project-defined weights:

| Component | Weight | Direction |
|---|---:|---|
| Time | 20% | Lower is better |
| Cost | 20% | Lower is better |
| Estimated CO₂ | 25% | Lower is better |
| Reliability | 20% | Higher is better |
| Traffic | 10% | Lower is better |
| Efficiency | 5% | Higher is better |

The final formula is:

```text
Delivery Option Score =
    time_score × 0.20
  + cost_score × 0.20
  + co2_score × 0.25
  + reliability_score × 0.20
  + traffic_score × 0.10
  + efficiency_score × 0.05
```

The best overall route in the final results is:

| Route option | Delivery Option Score | Time | Cost | Estimated CO₂ | Reliability |
|---|---:|---:|---:|---:|---:|
| Route option 418 | 92.62 | 15.33 min | 85.07 cost units | 2.04 kgCO₂e | 0.863 |

---

## Why This Score Is Used

The Delivery Option Score follows a simplified **Multi-Criteria Decision Analysis (MCDA)** logic.

In logistics and sustainable transport, decisions usually require trade-offs between several criteria, such as:

- Delivery time
- Cost
- CO₂ emissions
- Reliability
- Traffic conditions
- Operational efficiency

The weights used in this project are **not an industry standard**. They are educational assumptions selected to reflect the project focus on balancing operational performance and environmental impact.

In a real business environment, the weights could be tuned according to the needs of a platform, customer segment or operational strategy. For example:

- A same-day delivery platform may give more weight to time and reliability.
- A low-emission delivery platform may give more weight to CO₂ and vehicle type.
- A cost-sensitive operation may give more weight to cost.
- A premium B2B service may give more weight to reliability and service level.

In real-world projects, the scoring model could be validated or improved using:

- Historical delivery performance data
- Customer preferences
- SLA requirements
- Stakeholder interviews
- AHP, BWM, TOPSIS or other MCDA methods
- Pareto-based multi-objective optimization
- Machine learning models for delivery time, cost or reliability prediction

For this project, the goal is not to build a production algorithm. The goal is to demonstrate how different logistics indicators can be combined into a transparent and explainable decision-support model.

---

## Additional Analysis Added in the Final Version

The final notebook includes several improvements beyond the initial EDA and KPI analysis.

### 1. Improved Barcelona TRAMS Interpretation

`Status 0` was correctly treated as `No data`.  
The main traffic insights use only valid traffic records.

### 2. Emission Intensity

A new metric was calculated:

```text
emission_intensity_kgco2e_per_km = Carbon_Emission_kgCO2e / Distance_KM
```

This makes it easier to compare vehicles fairly, because total CO₂ can be strongly influenced by route distance.

### 3. Green Fleet Transition Scenario

A simple scenario was added:

> What if 50% of Diesel Van trips were replaced by Electric Van trips?

The scenario estimates:

- Total diesel trips
- Replacement share
- Current emissions for replaced trips
- Estimated EV emissions
- Estimated CO₂ saved
- Estimated saving percentage

In the final output, replacing 50% of Diesel Van trips with Electric Van trips estimates a saving of approximately **30,167 kgCO₂e**, or **80.67%** for the replaced trips.

### 4. Congestion Impact

A supporting congestion analysis compares delivery time with and without congestion.

For the cities included in the supporting sheet, congestion increased delivery time by more than 100% on average.

### 5. Statistical and Visual Validation

The final notebook also includes:

- Spearman correlation checks
- Kruskal-Wallis tests
- IQR outlier checks
- Score category component profile
- CO₂ interaction by vehicle type and traffic condition
- On-time rate by distance group
- Presentation-ready comparative visuals

These checks are not meant to overcomplicate the project. They are used to support the main conclusions and make the analysis more reliable.

---

## Main Insights

### 1. Route performance is multi-dimensional

The fastest route is not always the best overall option. A balanced delivery decision should consider time, cost, traffic, estimated CO₂ and reliability together.

### 2. CO₂ emissions vary strongly by vehicle type

Heavy trucks and diesel vans have much higher emissions than electric vans, cargo bicycles and drones. Emission intensity per kilometer is useful for comparing vehicles fairly.

### 3. Traffic affects both time and sustainability

Traffic congestion increases delivery time and can also increase emissions, especially for combustion vehicles affected by idling and stop-and-go driving.

### 4. Reliability is important for decision-making

Route reliability and on-time delivery are important operational indicators. They connect logistics performance with customer experience.

### 5. Urban context matters

Barcelona traffic data confirms that delivery analysis should consider city-level traffic behavior. Even when the project uses simulated or public logistics datasets, adding a real urban traffic context improves the interpretation.

### 6. A simple score can help compare trade-offs

The Delivery Option Score shows how multiple indicators can be combined into one decision-support view. However, the final score should always be interpreted together with its components.

---

## Presentation and Reports

The final presentation is provided as a PDF in the `presentation/` folder.  
The editable PowerPoint version is not included in the repository in order to keep the repository lighter and avoid adding large binary files to the Git history.

The `reports/` folder contains the final written report versions. The English version is the main public reference, and the Spanish version can be included as a complementary deliverable for local academic review.

---

## Output Files

The project generates several CSV outputs that support the analysis, README and presentation.

| File | Description |
|---|---|
| `kpi_summary.csv` | Main KPI summary generated in the KPI section |
| `presentation_kpi_summary.csv` | Presentation-ready KPI summary generated in the KPI section |
| `route_examples.csv` | Selected route examples for storytelling and presentation |
| `delivery_option_score_results.csv` | Final route-level scoring results |
| `top_delivery_options.csv` | Top-ranked delivery options |
| `route_decision_matrix.csv` | Best route examples by decision need |
| `barcelona_trams_valid_status_summary.csv` | Valid Barcelona traffic status summary |
| `barcelona_trams_monthly_valid_summary.csv` | Monthly Barcelona traffic summary |
| `emission_intensity_by_vehicle.csv` | CO₂ intensity by vehicle type |
| `green_fleet_transition_scenario.csv` | Green fleet transition scenario results |
| `congestion_impact_summary.csv` | Delivery time with and without congestion |
| `statistical_relationship_checks.csv` | Spearman correlation checks between main variables |
| `kruskal_test_summary.csv` | Non-parametric statistical test summary |
| `iqr_outlier_summary.csv` | Outlier summary using IQR |
| `score_category_component_profile.csv` | Average score components by score category |
| `co2_by_vehicle_traffic.csv` | CO₂ analysis by vehicle type and traffic condition |
| `on_time_rate_by_distance_group.csv` | On-time delivery rate by distance group |

The notebook includes a final output check to verify that these files were created successfully and do not contain unwanted `Unnamed` columns.

---

## Limitations

This project is based on public and simulated datasets. The datasets come from different sources and do not share a common transaction ID, so the analysis is modular rather than based on a full row-by-row merge.

Other limitations include:

- The Delivery Option Score is a simplified educational model.
- The score weights are project-defined assumptions, not validated industry weights.
- Estimated CO₂ in the score is calculated using an average emission factor per kilometer.
- The carbon reduction scenario is an estimate, not a full operational simulation.
- The Barcelona TRAMS dataset is used as city-level context, not as a direct route-level delivery input.
- The tracking congestion comparison is based on a small supporting sheet, so it should be interpreted carefully.
- Real carrier prices, real vehicle assignments and real delivery routes are not included.
- Real-time operational constraints such as driver availability, exact vehicle capacity and live routing are not included.
- Machine learning models are not part of the main scope of this version.

---

## Future Work

Future versions of this project could include:

- Using Barcelona ITINERARIS data for current and predicted travel time.
- Building machine learning models to predict delivery time, route cost or route reliability.
- Adding real carrier data and real delivery performance records.
- Improving CO₂ estimation with more detailed vehicle, fuel and load data.
- Extending the analysis with real-time traffic and routing APIs.
- Creating a more advanced recommendation model for sustainable delivery options.
- Building an interactive decision-support dashboard for route comparison.
- Testing different score weight scenarios for different logistics strategies.
- Creating a route-level merge between traffic, delivery and emissions data if compatible data becomes available.

---

## Final Conclusion

This project shows how public logistics, sustainability and traffic datasets can be combined to support data-driven delivery decisions.

The analysis demonstrates that sustainable e-commerce route planning requires a balance between operational efficiency and environmental impact. By combining time, cost, traffic, reliability and estimated CO₂ indicators, the Delivery Option Score provides a simple and explainable way to compare delivery options.

The project is designed as an educational data analytics case study, but the workflow can be extended in future versions with real-time data, predictive models, more advanced optimization methods and interactive decision-support tools.
