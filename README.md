# Change Point Analysis of Brent Oil Prices

## Objective
Analyze historical Brent oil prices to detect structural changes using
statistical tests and Bayesian change point modeling.

## Methods
- Exploratory Data Analysis (EDA)
- Stationarity testing (ADF, KPSS)
- Log return transformation
- Bayesian MAP-based change point detection

## Structure
- `notebooks/`: Analysis notebooks
- `src/`: Reusable Python modules
- `reports/figures/`: Saved plots for reporting

## Notes
Due to computational constraints, Bayesian MAP estimation was used instead of
full MCMC sampling for change point detection.
