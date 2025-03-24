<h1 align="center">
  <br>
  <a href="https://www.rewe-group.com/en/"> <img src="https://upload.wikimedia.org/wikipedia/commons/8/8a/Logo_Nutella.svg" alt="REWE Group" width="400"></a>
  <br>
  Nutella Sales Prediction
  <br>
</h1>

<p align="center">
  <a href="#how-to-use">How To Use</a> •
  <a href="#introduction">Introduction</a> •
  <a href="#experimental-set-up">Experimental Set-Up</a> •
  <a href="#results">Results</a> •
  <a href="#future-work">Future Work</a> 
</p>


## How To Use

To clone and run this challenge, you'll need to install the packages found under the **requirements.txt** file. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/JoseManuelGtz/nutella-forecasting.git

# Go into the repository
$ cd nutella-forecasting

# Create a virtual environment
$ conda create --name ml-workplace python=3.9.18

# Activate the environment
$ conda activate ml-workplace

# Install dependencies
$ pip install -r requirements.txt
```

## Introduction

The Nutella Sales Prediction Concept aims to forecast the daily sales volume of Nutella across various supermarkets based on several factors such as promotions, discount rates, store traffic, and location type. This analysis helps to optimize stock management and promotional strategies.

The dataset is stored as `nutella_sales.csv` and includes various numerical and categorical features to enhance the prediction.

### Features Used:

| **Feature**              | **Description**                                                                   | **Type**           |
|--------------------------|----------------------------------------------------------------------------------|--------------------|
| `Date`                   | The specific date of the sales record (YYYY-MM-DD format).                      | Categorical (DateTime) |
| `Regular_Price`          | Original price of Nutella before any discount is applied.                       | Numerical          |
| `Discounted_Price`       | The price of Nutella after the discount is applied.                             | Numerical          |
| `Discount_Rate`          | The percentage discount applied to the regular price.                          | Numerical          |
| `Promotion_Type`         | Type of promotion applied (Flash Sale, Percentage, BOGO).                 | Categorical        |
| `Promotion_Duration`     | Duration of the promotion in days.                                               | Numerical          |
| `Month`                  | Month of the year extracted from the `Date` feature (1-12).                     | Numerical          |
| `Month_Sin`              | Sine encoding of the month.                                                      | Numerical          |
| `Month_Cos`              | Cosine encoding of the month.                                                    | Numerical          |
| `Day_of_Week`            | Day of the week extracted from the `Date` feature (0=Monday, ..., 6=Sunday).     | Categorical        |
| `Is_Holiday`             | Whether the date corresponds to a holiday (0 = No, 1 = Yes).                   | Categorical (Binary) |
| `Supermarket_Type`       | Type of supermarket (Big, Medium, Small).                                 | Categorical        |
| `Location_Type`          | Location of the supermarket (Urban, Suburban, Rural).                    | Categorical        |
| `Store_Traffic`          | Estimated foot traffic in the store.                                            | Numerical          |
| `Planned_Promotions_7_Days`  | Number of planned promotions within the next 7 days.                          | Numerical          |
| `Planned_Promotions_30_Days` | Number of planned promotions within the next 30 days.                        | Numerical          |
| `Sales_Volume`           | Number of Nutella jars sold per day. **(Target Variable)**                         | Numerical          |


## Experimental Set-Up

The following models have been implemented and evaluated:
- **Random Forest Regressor**
- **XGBoost Regressor**
- **CatBoost Regressor**
- **Ensemble Model (Weighted Average)**

### Additional Settings:
- Data Split: Train (80%), Validation (10%), Test (10%)
- Evaluation Metrics: RMSE, MAE


## Results

Performance comparison of models:

| Model           | Validation RMSE | Test RMSE |
|-----------------|-----------------|-----------|
| Random Forest   | 9.93            | 10.09      |
| XGBoost         | 6.99            | 6.99       |
| CatBoost        | 5.64            | 5.64       |
| Ensemble        | 5.99            | 5.99       |


## Future Work

### Model Improvement
- Apply advanced feature selection techniques.
- Improve ensemble strategy by trying **stacking and boosting techniques**.
- Experiment with different learning rates, regularization techniques, and feature engineering.
- Include Hyperparameter Tuning

---

> [josemanugtz@live.com](josemanugtz@live.com) &nbsp;&middot;&nbsp;
> GitHub [@JoseManuelGtz](https://github.com/JoseManuelGtz/) &nbsp;&middot;&nbsp;
> LinkedIn [Jose Manuel Gutierrez](www.linkedin.com/in/josemanuelgutierrez17)
