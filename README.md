# Project Title: Industrial-Copper-Modelling
## ML Model Building and Evaluation

## Overview
This project involved building and evaluating machine learning models for both regression and classification tasks. The dataset contained features related to a sales or product scenario, and the goal was to predict the selling price for regression and the status (WON or LOST) for classification. The project also included creating a Streamlit web page for easy interaction with the models.

## Steps

### 1. Data Exploration
- Identified skewness and outliers in the dataset.
- Understood the distribution and relationships between variables.

### 2. Data Preprocessing
- Transformed the data into a suitable format.
- Handled any missing values, outliers, or skewness.
- Performed necessary cleaning and preprocessing steps.

### 3. Regression Modeling
- Trained regression models to predict the continuous variable 'Selling_Price'.
- Evaluated models using appropriate metrics such as Mean Squared Error (MSE), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and R-squared.

### 4. Classification Modeling
- Trained classification models to predict the status (WON or LOST).
- Utilized appropriate evaluation metrics such as accuracy, precision, recall, F1 score, and ROC AUC curve.

### 5. Model Optimization
- Optimized model hyperparameters using techniques such as cross-validation and grid search to find the best-performing models.

### 6. Interpretation and Assessment
- Interpreted the results of both regression and classification models.
- Assessed the performance of the models based on the defined problem statement.

### 7. Streamlit Web Application
- Developed a Streamlit web page where users could input values for each column.
- Implemented functionality to predict Selling_Price or Status (WON/LOST) based on the input values using the trained models.

## Models Used
### Regression Models
- RandomForestRegressor
- GradientBoostingRegressor
- DecisionTreeRegressor
- ExtraTreesRegressor
- AdaBoostRegressor
- LinearRegression
- Ridge
- Lasso
- KNeighborsRegressor

### Classification Models
- RandomForestClassifier
- GradientBoostingClassifier
- DecisionTreeClassifier
- ExtraTreesClassifier
- AdaBoostClassifier
- LogisticRegression
- RidgeClassifier
- KNeighborsClassifier
- LinearSVC

## Notes
- The dataset contained more noise and linearity between independent variables, so tree-based models were expected to perform well.
- Model performance was evaluated using cross-validation and appropriate evaluation metrics for both regression and classification tasks.
