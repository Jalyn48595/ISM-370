# -*- coding: utf-8 -*-
"""370_Mod_10_Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Do-X6zb0JLfRm0yODOzSDPEhgFpucYQb
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#modify pandas display options to show all columns and not wrap
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

#read in the dataset and print the descriptive statistics
lv = pd.read_csv("/content/lv_hotel_reviews.csv", sep= ';')
print(lv.describe())
print()
print('Within this dataset the mean number of reviews is 48 while the mean number of helpful votes is 31.')
print()


#save all num_reviews and helpful_votes into two lists
reviews = lv['num_reviews'].tolist()
votes = lv['helpful_votes'].tolist()

reviews_num = 300
x= np.array(reviews)
y = np.array(votes)

#linear regression
from sklearn.linear_model import LinearRegression
x = lv['num_reviews'].values.reshape(-1, 1)
y = lv['helpful_votes'].values.reshape(-1, 1)
regressor = LinearRegression()
regressor.fit(x, y)

#plot the linear regression line
regline = regressor.predict(x)
plt.scatter(lv['num_reviews'], lv['helpful_votes'], color = 'blue')
plt.plot(sorted(lv['num_reviews']), regline, 'r')
plt.title('Helpful Votes By Number of Reviews')
plt.xlabel('Number of Helpful Votes')
plt.ylabel('Number of Reviews By User')
plt.show()
print()

#nearest neighbor
k = 15
from sklearn.neighbors import KNeighborsRegressor
knnregressor = KNeighborsRegressor(n_neighbors = k)
knnregressor.fit (x, y)
print('Mean helpful votes of the 15 nearest neighbors: ')
print(knnregressor.predict(np.array(reviews_num).reshape(-1, 1)))
print()

#decision tree
from sklearn.tree import DecisionTreeRegressor
dtregressor = DecisionTreeRegressor (max_depth = 3)
dtregressor.fit (np.array(reviews).reshape(-1, 1), np.array(votes))
print('My decision tree prediction of number of helpful votes: ')
print(dtregressor.predict(np.array(reviews_num).reshape(1, -1)))
print()

#random forest
from sklearn.ensemble import RandomForestRegressor
rfregressor = RandomForestRegressor()
rfregressor.fit(np.array(reviews).reshape(-1, 1), np.array(votes))
print('Random forest prediction of number of helpful votes: ')
print(rfregressor.predict(np.array(reviews_num).reshape(1, -1)))
print()


#neural network
from sklearn.neural_network import MLPRegressor
nnregressor = MLPRegressor()
nnregressor.fit(np.array(reviews).reshape(-1, 1), np.array(votes))
print('Neural network prediction of number of helpful votes: ')
print(nnregressor.predict(np.array(reviews_num).reshape(1, -1)))
print()

#print a comment on what you learned from the above analysis (with 300 reviews)
print('From the linear regression, nearest neighbor, decision tree, random forest and neural network analyses')
print('I learned that the Random Forest model had the highest prediction of helpful votes and the Neural Network')
print('model had the lowest prediction for number of helpful votes. Without looking at the error rate I would guess')
print('that the Decision Tree model would be the best for this situation because its prediction was the closest to')
print('the average of the 4 models predictions, however you cannot truly see which model is best without their error rates.')
print()

#print a comment on what you learned from changing reviews from 300 to 10
print('When I changed the number of reviews from 300 to 10 the predicted number of helpful votes significantly decreased.')
print('A larger number of reviews likely gives a more accurate prediction due to having a larger sample size to pull from.')
print('When the number of reviews was decreased to 10, a convergence warning appeared on the Neural Network model prediction.')
print()

#create a 75%/25% train-test split of the data, print the prediction scores for each model
from sklearn.model_selection import train_test_split
x = np.array(reviews).reshape(-1, 1)
y= np.array(votes)
trainingx, testx, trainingy, testy = train_test_split(x, y, random_state = 1)

#linear regression error prediction
regressor = LinearRegression()
regressor.fit (trainingx, trainingy)
predicted = regressor.predict(testx)
predictionerror = abs(predicted - testy)
print('Linear regression prediction score: ')
print(np.mean(predictionerror))
print()

#K nearest neighbor error prediction
knnregressor = KNeighborsRegressor(n_neighbors = 15)
knnregressor.fit (trainingx, trainingy)
predicted = knnregressor.predict(testx)
predictionerror = abs(predicted - testy)
print('Nearest neighbor prediction score: ')
print(np.mean(predictionerror))
print()

#decision trees error prediction
dtregressor = DecisionTreeRegressor(max_depth = 3)
dtregressor.fit (trainingx, trainingy)
predicted = dtregressor.predict(testx)
predictionerror = abs(predicted - testy)
print('Decision Tree prediction score: ')
print(np.mean(predictionerror))
print()

#random forest error prediction
rfregressor = RandomForestRegressor(random_state = 1)
rfregressor.fit (trainingx, trainingy)
predicted = rfregressor.predict(testx)
predictionerror = abs(predicted - testy)
print('Random forest prediction score: ')
print(np.mean(predictionerror))
print()

#neural network error prediction
nnregressor = MLPRegressor()
nnregressor.fit (trainingx, trainingy)
predicted = rfregressor.predict(testx)
predictionerror = abs(predicted - testy)
print('Neural network prediction score: ')
print(np.mean(predictionerror))
print()


#print a comment on what you learned from comparing the prediction scores, what analysis is best for this data/situation
print('When comparing the error prediction scores I can see that the Linear Regression model had the lowest error')
print('prediction score. Therefore, the linear prediction model would be the best analysis model for this dataset.')
print()