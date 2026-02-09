# Interim Report: Change Point Analysis of Brent Oil Prices
## 1. Introduction

This interim report outlines the planned analysis of Brent oil prices to detect structural breaks and understand how major geopolitical, economic, and OPEC-related events impact price movements. 
The goal is to prepare a reproducible workflow and compile supporting data for future Bayesian change point modeling.
 ## 2. Data Analysis Workflow

The analysis will follow a structured workflow:

1. **Data Ingestion and Preprocessing**
   - Load historical Brent oil price data (`brentoilprices.csv`).
   - Convert date fields to datetime format.
   - Handle missing values if any.

2. **Exploratory Data Analysis (EDA)**
   - Visualize raw prices to identify trends and volatility.
   - Compute log returns to stabilize variance.
   - Identify periods of high volatility or structural changes.

3. **Event Data Compilation**
   - Research and curate major events affecting oil prices.
   - Construct a structured dataset (`oil_market_events.csv`) including:
     - Event date
     - Event description
     - Category (OPEC policy, geopolitical conflict, economic shock, sanctions)
   - This dataset will later support interpretation of detected change points.

4. **Bayesian Change Point Modeling (Planned)**
   - Detect structural breaks using PyMC Bayesian change point models.
   - Estimate mean shifts before and after each change point.

5. **Interpretation and Communication**
   - Associate detected change points with historical events.
   - Generate insights for investors, policymakers, and energy stakeholders.
## 3. Event Data Summary

The event dataset includes 10 major events over the last two decades, selected based on their likely impact on Brent oil prices:

| Date       | Event                                         | Category                  |
|------------|-----------------------------------------------|---------------------------|
| 2003-03-20 | Iraq War begins                               | Geopolitical Conflict     |
| 2008-09-15 | Global Financial Crisis escalation            | Economic Shock            |
| 2011-02-15 | Arab Spring unrest in oil-producing regions  | Geopolitical Conflict     |
| 2014-11-27 | OPEC decision not to cut production          | OPEC Policy               |
| 2016-01-16 | International sanctions on Iran lifted       | Sanctions                 |
| 2018-05-08 | US withdraws from Iran nuclear deal          | Sanctions                 |
| 2020-03-11 | COVID-19 declared global pandemic            | Economic Shock            |
| 2020-04-12 | OPEC+ agrees historic production cuts        | OPEC Policy               |
| 2021-10-01 | Global energy supply chain disruption        | Economic Shock            |
| 2022-02-24 | Russia invades Ukraine                        | Geopolitical Conflict     |

> Note: These events are selected based on documented global impact. This dataset supports later association with statistical change points but does **not imply causality**.
  ## 4. Time Series Understanding

Exploratory analysis of Brent oil prices revealed:

- **Trends:** Long-term trends exist in the price series.  
- **Volatility Clustering:** Periods of high and low volatility alternate, often aligning with major events.  
- **Non-stationarity:** Raw prices are non-stationary; log returns improve stationarity for modeling.  
- **Structural Breaks:** Sudden spikes and drops suggest potential change points.  

**Conclusion:**  
The observed properties justify applying Bayesian change point detection to identify statistically significant shifts in the underlying price behavior.
-  ## 6. Next Steps

1. Finalize EDA and generate visualizations for interim review.  
2. Implement Bayesian change point model in PyMC.  
3. Map detected change points to curated events for hypothesis generation.  
4. Prepare interim GitHub repository for submission with structured folders, data files, and notebook.
