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
  <a href="#exploratory-data-analysis">EDA</a> •
  <a href="#ml-insights">ML Insights</a> •
  <a href="#results">Results</a> •
  <a href="#future-work">Future Work</a> 
</p>


## How To Use

To clone and run this repository, you'll need to install the packages found under the **requirements.txt** file. From your command line:

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

The Nutella Sales Prediction Concept aims to forecast the daily sales volume of Nutella across various supermarkets based on several factors such as promotions, discount rates, store traffic, and location type. This project is a conceptualization of an isolated scenario focused on incorporating discounts into products and predicting the optimal stock to order. The use case is scalable to a wide range of products, not only restricted to Nutella. This analysis helps to optimize stock management and promotional strategies

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

## Exploratory Data Analysis

### Discount Rate vs Sales Volume
<img src="img/discount_rate_sales.png" alt="Discount Rate vs Sales Volume" width="600">

- **Higher discount rates generally result in higher sales volumes, as expected customers tend to look for the products with a high discount associated to them.**

### Correlation Matrix
<img src="img/correlation_matrix.png" alt="Correlation Matrix" width="600">

- **Higher discounts and longer promotions result in higher sales, suggesting promotions play an important role when trying to boost sales.**
- **Negative correlations can be found with the features "Planned_Promotions_30_Days" and "Planned_Promotions_7_Days". Future planned promotions might discourage immediate purchases.**

### Sales Volume Over Time
<img src="img/sales_volume_over_time.png" alt="Sales Volume Over Time" width="600">

- **Sales volume fluctuates throughout the years, with noticeable peaks around specific months (likely holiday seasons as December).**
- **Spikes in sales volume can be found likely due to promotional events or special sales.**

## ML Insights

### Feature Importance Analysis
- **XGBoost Feature Importance**  
  <img src="img/xgboost_feature_importance.png" alt="XGBoost Feature Importance" width="700">
  - The most important features are `Location_Type_Rural`, `Supermarket_Type_Small`, `Month`, and `Promotion_Duration`.

- **CatBoost Feature Importance**  
  <img src="img/catboost_feature_importance.png" alt="CatBoost Feature Importance" width="700">
  - `Month` is the most significant feature, followed by `Supermarket_Type_Small` and `Location_Type_Rural`.

### Learning Curve Analysis
<p align="center">
  <img src="img/xgboost_lc.png" alt="XGBoost Learning Curve" width="450">
  <img src="img/catboost_lc.png" alt="CatBoost Learning Curve" width="450">
</p>

- **XGBoost Learning Curve:** The training error is consistently low, while the validation error improves with larger training sizes, indicating a reduction of overfitting.
- **CatBoost Learning Curve:** The training error remains low throughout, while validation error decreases significantly when more data is used, showing good generalization.

Plots generated during model evaluation:
- Feature Importance (Random Forest, XGBoost, CatBoost)
- Learning Curves (Random Forest, XGBoost, CatBoost)
- Ensemble Model Comparison

These graphs provide insights into feature relevance, model training dynamics, and overall model performance.



## Results

The results demonstrate that **CatBoost** achieved the lowest RMSE on both the validation and test sets, suggesting it has the best predictive performance among the individual models. The **Ensemble Model**, which combines predictions from XGBoost and CatBoost using a weighted average, shows an improved performance compared to XGBoost but slightly worse than CatBoost alone. This indicates that the ensemble strategy effectively captures diverse patterns from different models but could benefit from additional tuning or a better meta-learner.

Key Insights:
- **CatBoost** outperformed the other models with a test RMSE of **5.64**, indicating good generalization capability.
- **XGBoost** performed reasonably well with a test RMSE of **6.99**, which suggests that its performance could be enhanced by further hyperparameter tuning.
- The **Ensemble Model** provides a promising approach but requires further refinement to improve over the best single model.

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
- Include Hyperparameter Tuning.
- Another algorithm/approach can be also considered in further analysis.

---

> [josemanugtz@live.com](josemanugtz@live.com) &nbsp;&middot;&nbsp;
> GitHub [@JoseManuelGtz](https://github.com/JoseManuelGtz/) &nbsp;&middot;&nbsp;
> LinkedIn [Jose Manuel Gutierrez](www.linkedin.com/in/josemanuelgutierrez17)
