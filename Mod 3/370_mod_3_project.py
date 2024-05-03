# -*- coding: utf-8 -*-
"""370_Mod_3_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KejdZb4mj7wJoGgvwiJaG9qhtSw9B7-D

Jalyn Buthman

Flagstaff Home Prices
"""

#import pandas as alais pd
import pandas as pd

#read the file into the project
data = pd.read_csv("/content/flagstaff_real_estate_data.csv")

#print the header of the dataset
print('\nThe following is the header of the dataset: ')
print(data.head)

#print the descriptive statistics and median of the dataset
print('\nThe following is the descriptive statistics of the dataset: ')
print(data.describe())
print('\nThe overall median of home value price is: ')
print(data['PRICE'].median())

#print the median home price for each year
print('\nThe median home price for each year was: ')
print(data.groupby(['YEAR'])['PRICE'].median())

#take a subset of the data that only includes years 2010-2019 and print the descriptive statistics
data_subset = data.loc[(data['YEAR'] >= 2010) & (data['YEAR']<=2019)]
print('\nThe following is the describtive statitics for a subset of the dataset that only includes years 2010-2019: ')
print(data_subset.describe())

#print the median home price for each year of the data subset
print('\nThe median home prices for the data subset grouped by year: ')
print(data_subset.groupby(['YEAR'])['PRICE'].median())

#print the median mone price for each month of the data subset
print('\nThe median home prices for the data subset grouped by month:')
print(data_subset.groupby(['MONTH'])['PRICE'].median())