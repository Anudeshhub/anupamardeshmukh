# Case Study – What drives Price of a car

## Use CRISP-DM model 
	
To understand what factors make a car more or less expensive.
Provide clear recommendations to your client, a used car dealership, as to what consumers value in a used car.

##  1.	Business Understanding
### 1.1.	Background
The dataset vehicles.csv is used to determine the prices of used car based on demographics (Region, States) and various other attributes like manufacturer, type of the car, cylinders, condition of used car etc.

The business problem can be defined as predicting the price of used cars based on various attributes provided in the dataset. 

This involves understanding the factors (or key drivers) that influence pricing of used cars in different regions and under different conditions.

### 1.2.	Business Goals and KPI’s
The business goal is to determine what factors make a car more or less expensive. At the end of analysis provide clear recommendations to a used car dealership, as to what consumers value in a used car.

### 1.3.	Data Mining Goals and KPI’s
Build and analyze the data sets and build KPI’s that aligns with business goals.

To address the business problem, a regression analysis could be employed where the dependent variable is the price of the used car, and the independent variables include those identified as key drivers. Techniques such as multiple linear regressions is used.

Feature engineering involves handling missing data, encoding categorical variables, and  scaling numerical features.

The ultimate goal is to that accurately predicts the price of a used car given its characteristics, which can help sellers optimize pricing
 
 In this application, condition of the car is used as the main characteristics to determine the price. Example : good cars can be priced high.

## 2.	Data Understanding 
     Raw data in the vehicle.csv file
     DataStructure

      Year                  : Generally, newer cars tend to
                              have higher prices.
      Manufacturer and Model: Some brands and models hold 
                              higher resale value due to
                              reputatiion, reliability, or  
                              desirability.
      Condition             : The state of the car (e.g.,
                              excellent, good, fair) affects 
                              its price.
      Odometer              : Lower mileage typically 
                              correlates with a higher price 
      Title Status		   :  Cars with a clean title often
                              fetch higher prices
      Transmission Type     : Automatic or manual 
                              transmission can affect price,
                              with automatic typically being 
                              more popular and thus higher
                              priced.
      Drive Type            : All-wheel drive or four-wheel  
                              drive vehicles often command 
                              higher prices, especially in 
                              certain regions.
      Size and Type          : Larger vehicles like SUVs or 
                               trucks usually have higher 
                               prices compared to smaller
                               cars like sedans.
      Fuel Type             :  Preferences for hybrid or 
                              electric vehicles might 
                              influence pricing trends in 
                              certain markets
     Location (Region/State): Local market conditions, 
                              economic factors, and 
                              demand can significantly impact 
                              prices.

## Observation
     o	The dataset had manu NaN values
     o	id, model,VIN,odometer reading has high cardinality 
     o	4 columns have numerical values and rest all are 
          text/strings
     o	Price is the dependent variables
     o	Key Drivers of the dataset by observation are
          manufacturer, condition, cylinders, transmission,
          type, paint_coor, state, year

## 3.	Data Preparation
     Dataset Before Cleanup

      <img width="782" src="https://raw.githubusercontent.com/Anudeshhub/anupamardeshmukh/images/datastructure.png" alt="datastructure">

    	The dataset had many NaN values
    	id, model,VIN,odometer reading has high 
          cardinality, so these can be removed
    	Identified and removed duplicates
    	Created standard format for the year
    	Cleaned up Values for Cylinder column
    	Removed non-numeric characters from 'cylinders'
          column and convert to numeric
    	Converted ‘type’ column to string
    	Replaced NaN values in 'cylinders' column with 0 
    	Converted 'cylinders' column to integer type  
    	Formatted year and created a new column year_new 
    	Dropped unnecessary columns
                'year', 'id', 'model', 'VIN', 'region',
                'odometer', 'title_status', 'drive', 'size' 
    	Dropped the columns that has high cardinality 

Only 4 columns are numeric. Id and Odometer has high cardinality and hence these are dropped and these do not give any valuable insights
 

# Dataset after cleanup
 

Data Exploration
Created Various Visualization to analyze data 

Not many outliers in the columns based on Condition and price of the Car

 

Pick up and SUV's are priced high and looks like high demand for these cars. 'Distribution of Car Prices by Type.

 








                      
4.	Calculated Mean Price by Manufacturer and Condition of the car and created a graph to show the correlation
 
Feature Engineering
	Separate features (X) and target (y)
	Defined categorical and numerical features
	Preprocessed pipeline for categorical features
	Created Training and Test datasets
	Defined numeric features (replace with your actual numeric feature names or indices)
	Complete preprocessing for numeric features
o	Created a ColumnTransformer to apply preprocessing steps to numeric features [manufacturer, condition]

 




## 4	Modeling
	Initialized models: Linear Regression, Ridge, and Lasso
	Defined pipelines for Linear, Ridge, and Lasso Regression
	Fitted and trained the models 
	Calculated Mean Squared Error for each Model
	Predict and evaluated the model using Linear Regression, 
     Ridge Regression and Lasso Regression.
     
     Output of Trained model : MSE
                   
     Linear Regression Mean Squared Error: 159170452.03
     Ridge Regression Mean Squared Error : 159170452.33
     Lasso Regression Mean Squared Error : 159170517.46 
     
     Lasso regression shows least Mean Squared Error. 
     
     Hence, this model can be deployed to find out price of 
     the cars based on various features. Predictions can be done using Lasso Regression model

## 5	Evaluation
Applied Cross-Validation logic to evaluate the model and
the final numbers showed same as predicted.

## 6	Deployment
     Decided to use Lasso Regression model for predictions, as this model  has least mean squared error
     
     Applied Lasso Regression model to predict the price of car based on   condition [Only one feature used]
                Condition = 1 - Excellent,   2  = Good '
                For a good car predicted price  = $17,325

# Recommendations to the Dealer
Based on our Analysis and Predictive model created and recommendations made based on 2 features and the price as dependable variable 

Brand Value (Manufacturer) : There is a demand for Brand value, as the sale for luxury cars was more, hence the dealer must keep more of these cars
                      
Condition of the Car :  Good condition cars though expensive, are preferred by customers and hence, they must increase the inventory of these cars

Prices of good cars will go up, as predicted, hence the dealer must have more good cars in their inventory	 
Summary: 

