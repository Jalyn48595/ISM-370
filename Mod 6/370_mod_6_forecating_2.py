# -*- coding: utf-8 -*-
"""370_Mod_6_Forecating_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-rGCO89Pw3s11faKSLyQoV7r3Eca1ZSz

Title: Forecasting and regression analysis
Description: This project covers forecasting and regression analysis that may affect the cash price of wheat
"""

import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

#read in the dataset, print the header and info
wheat = pd.read_csv("/content/wheat_cash_1963.csv")
print(wheat.head())
print()
print(wheat.info())
print()

#print the descriptive statistics
print(wheat.describe())
print()

#

#create a histogram of wheat prices
plt.hist(wheat['price'], bins=10)
plt.title('Distribution of wheat prices')
plt.ylabel('Frequency')
plt.xlabel('Price')
plt.show
print()

#create a scatterplot showing the relationship between economic growth and wheat price
plt.scatter(wheat['economic_growth'], wheat['price'])
plt.title('Relationship between economic growth and wheat price')
plt.ylabel('Price of wheat')
plt.xlabel('Economic Growth')
plt.show()

#Perform linear regression to help with forecasting using a library called statsmodels
#create the model with the dependant or outcome variable on the left and the independat/predictor variable on the right

#ols is a type of regression
#model = smf.ols(formula='outcome ~ predictor', data =dataframe).fit()
model = smf.ols(formula='price ~ economic_growth', data =wheat).fit()

#print the summary stats to view the results
print(model.summary())
print()

#f-statistic is the p value for the entire model
#p value is the possibility of the finding being due to error or randomness
#a p value less than 0.05 is statistically meaningful, may need to convert from scientific notation
#if meaningful you have a signifigant relationship between at least one independant variable and the dependant one

#intercept is always listed, under this are independant variables
#P>|t| is the independant variable for each variable, if there is one variable this is the same as above

#if coef is positive it indicates a positive relationship and vise versa
#the coef number means that when the independent variable (economic_growth) increases by 1 (in this case $1)
#price will increase by the number listed (.5016, or $0.50)

#R-squared, how much variance in price can be statistically attributed to economic growth, consider this as a percentage



#retrive coefficients and intercept
#params = paramaters which gives info about the model
intercept = model.params[0] #intercept is the first parameter in the list
coefficients = model.params

#print the intercept and coeffcients
print('Intercept', intercept)
print('Coefficients', coefficients[1])
print()
#print(model.params)

#forecast the cash price of wheat given an economic growth rate

#print the last 10 rows of economic growth to determine a test value
print(wheat['economic_growth'][-10:])
print()

#try a test value of 4.5
#calculate regression equation for this model (general: y=mx +b)
#y= the dependant value/outcome
#m= the coefficient
#x= test value
#b= intercept

#initialize variables to use in the equation
m = coefficients[1]
x = 4 #the test/input value
b = intercept

#create the specific equation for forecasting
predicted_wheat_price = m * x + b
print(f'Predicted wheat price when economic growth is {x}: ${predicted_wheat_price:,.2f}')
print()

#since we have a small dataset, we can print entire data to check our tets values
print(wheat)
print()

#check your predicted value against values in the dataset
#change your test(x) value to make different forecasts

"""Insights and Conclusions:


*   Economic growth is positivley correlated with the cash price of wheat, when growth increases, prices increase.
*   We should watch the economic growth indicator to determine what wheat pr


"""

#create a new regression model with multiple independant variables
model2 = smf.ols(formula= 'price ~ economic_growth + population_growth + meat_consumption', data= wheat).fit()
print(model2.summary())


#check prob(f-statistic), then p>|t| of each variable, then coefficient of each variable, then the rquare)
#e-10 is that the decimal point will move left 10 times
#the coefficient of a variable depends on how many variables you are looking at
#its an issue if your independant variables are too correlated with each other

#when each variable increases by 1, price will increase by the coefficient
#rsquared is how much variation in the data can be explained by the variable

#save the coeffiecients to variables
print(model2.params)
print()
intercept = model2.params[0]
econ_coef = model2.params[1]
pop_coef = model2.params[2]
meat_coef = model2.params[3]

#save the test values to variables
econ_x = 3.8
pop_x = 1.40
meat_x = 152.95

#generate a regression equation and print the forecast
price2 = econ_coef * econ_x + pop_coef * pop_x + meat_coef *meat_x + intercept
print('The forecasted cash price of wheat given the test values: ')
print(f'${price2:,.2f}')

#check if the prediction with one variable (above) is closer to the actual price than the one with multiple variables (test multiple times)
#if you get a negative value rerun the code cells