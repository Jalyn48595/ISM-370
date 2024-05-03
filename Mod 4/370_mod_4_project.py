# -*- coding: utf-8 -*-
"""370_Mod_4_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15MrEeSNkXBNsd95jxdNZc3ULeg2CS_9i

Credit Analysis Project
Jalyn Buthman
"""

#import pandas
import pandas as pd

#read in the .csv file
ca = pd.read_csv("/content/credit.csv")

#print the descriptive statistics
print('The descriptive statistics for this dataset is:')
print(ca.describe())
print()
print()

#the mean for BILL_AMT1 grouped by PAY_1
print ('The mean for Bill Amount 1, grouped by Pay 1:')
print(ca.groupby(['PAY_1'])['BILL_AMT1'].mean())
print()
print()

#the mean for AGE grouped by PAY_2
print('The mean for age, grouped by Pay 2:')
print(ca.groupby(['PAY_2'])['AGE'].mean())
print()
print()

#the number of unique ages in PAY_2
print('The number of unique ages in Pay 2:')
print(ca.groupby(['PAY_2'])['AGE'].nunique())
print()
print()

#analysis of a subset of data to only look at female data credit data
print('A subset of the data that only includes females:')
female = ca.loc[ca['SEX'] == 2]
print()
print('The mean of repayment statuses for PAY 1 within the female subset:')
print(female['PAY_1'].mean())
print()
print('The number of unique entries for Pay 1 within the female subset:')
print(female['PAY_1'].nunique())
print()
print('The number of unique entries for Pay 6 within the female subset:')
print(female['PAY_6'].nunique())
print()
print()

#analysis of a subset of data to only look at male data credit data
print('A subset of the data that only includes males:')
male = ca.loc[ca['SEX'] == 1]
print()
print('The mean of repayment statuses for PAY 1 within the male subset:')
print(male['PAY_1'].mean())
print()
print('The number of unique entries for Pay 1 within the male subset:')
print(male['PAY_1'].nunique())
print()
print('The number of unique entries for Pay 6 within the male subset:')
print(male['PAY_6'].nunique())