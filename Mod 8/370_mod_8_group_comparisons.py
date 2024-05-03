# -*- coding: utf-8 -*-
"""370_Mod_8_Group_Comparisons.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RjqmtFRBP9h_xdePVLwDi_lMlTYnlnTd

\Title: MLB group comparisons
Description: Comparing samples of player heights using t-tests
Created by: Jalyn Buthman
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

mlb = pd.read_csv("/content/mlb.csv")

#a t-test that is more than 2 standard deviations away from the mean signifies that it is significant
#the data should be relativley normlly distributed to use t tests
print(mlb.head())
print()
print(mlb.describe())
print()

#a historgram to show the distrbution
plt.hist(mlb['height'], bins = 40)
plt.title('Disrtibution of MLB Heights')
plt.show()
print()

#create two random samples of players and one non random sample
#.sample (sample size, random_state (optional))
sample1 = mlb.sample(n= 30, random_state= 0)
sample2 = mlb.sample(n= 30)
sample3 = [71, 75, 77, 74, 74, 76, 77, 73, 78, 76, 75, 73, 75, 74, 73, 73, 75, 78, 74, 77]

#create box plots to visualize groups
#sample 3 needs to be specified as an array because it is a plain list rather than a dataframe
fig1, ax1= plt.subplots()
ax1.boxplot([mlb['height'], sample1['height'], sample2['height'], np.array(sample3)])
ax1.set_title('MLB Player Heights')
ax1.set_ylabel('Height (Inches)')
ax1.set_xticklabels(['Full Population', 'Sample1', 'Sample2', 'Sample3'])
plt.show()
print()

#print our hyptheses
#h0: what we accept with no data, h1: what we are trying to prove
print('H0: There is no difference bewteen the sample 2 mean height and the population mean height.')
print('H1: The mean height of sample 2 is greater than the population mean.')
print()

#use t-tests to compare groups
print('Pop vs. S1')
print(scipy.stats.ttest_ind(mlb['height'], sample1['height']))
print()
print('Pop vs. S2')
print(scipy.stats.ttest_ind(mlb['height'], sample2['height']))
print()
print('Pop vs. S3')
print(scipy.stats.ttest_ind(mlb['height'], np.array(sample3)))
print()