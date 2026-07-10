**Real Estate Price Prediction using Machine Learning**

## Project Overview

This project predicts residential property prices using Machine Learning.

The application analyzes property features such as:

- Location
- Total Square Feet
- Number of Bedrooms (BHK)
- Number of Bathrooms

and predicts the estimated market price.

## The project also includes a simple web application developed using **Streamlit**, allowing users to interactively predict house prices.

This project predicts residential property prices using Machine Learning techniques. The model analyzes various property features such as location, total square feet, number of bedrooms, and bathrooms to estimate the market price.

The project includes data preprocessing, exploratory data analysis (EDA), feature engineering, model training, evaluation, and comparison of multiple regression algorithms.

## Objectives
Predict house prices accurately.
Compare multiple regression algorithms.
Identify the most influential features affecting property prices.
Build a reusable machine learning model.
Dataset

Dataset Used: Bengaluru House Price Dataset from kaggle

## Features include:

Location
Total Square Feet
Number of Bedrooms (BHK)
Bathrooms
Property Price

## Target Variable:  Price

Technologies Used:
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-Learn
Jupyter Notebook

Machine Learning Models:
Linear Regression
Random Forest 
Gradient Boosting Regressor

## Evaluation Metrics:
Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)
R² Score

## Results:

Model	               MAE	         RMSE          R² Score
Linear Regression	  17.00         26.82	        0.8592
Random Forest	      15.11         27.03         	0.8569
Gradient Boosting	  17.15         26.24	        0.8652

Gradient Boosting achieved the best overall performance.

Feature Engineering:
Converted BHK from text to numeric values.
Converted square feet ranges into numeric values.
Applied One-Hot Encoding on location.
Removed outliers.
Created Price per Square Foot for outlier detection.
Exploratory Data Analysis

## Project Structure
house price prediction by Ishwari Gharat
Real_Estate_Price_Prediction/
│
├── app.py
├── house_price_model.pkl
├── Bengaluru_House_Data.csv
├── Real_Estate_Price_Prediction.ipynb
├── README.md
├── Internship_Report.pdf
└── requirements.txt


## Running the Project

Install dependencies:
pip install -r requirements.txt
Run the application:
streamlit run app.py

## Future Scope:
Add age of property.
Include amenities.
Build a web application using Flask or Django.
Deploy the model on the cloud.

## Developed By
**Ishwari Gharat**
Internship Project