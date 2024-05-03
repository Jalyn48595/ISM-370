# -*- coding: utf-8 -*-
"""370_Mod_5_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EtZ0DEirA5SB7lr-z_5pPTI6UMsefXvi

Exploratory Data Analysis with Plotting Bike Share Data
Jalyn Buthman
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import median

#read in the bike share data
df = pd.read_csv("/content/bike_share_data.csv")
print(df.head())
print ()

#a histogram to show the distribution of the number of registered bike users
plt.hist(df['registered'], bins= 30, rwidth=.9)
plt.title('Distribution of Registered Bike Users')
plt.ylabel('Frequency')
plt.xlabel('Number of Registered Users')
plt.show()

"""The histogram plot showing the distribution of registered bike users above is right skewed. This shows us that instances with low counts of registered bike users are far more frequent than instances with high counts of registered bike users. This could show that we need to work on getting more of our users registered. It could also indicate that our users are not always logging into their account, which would list them as a casual user."""

#a bar plot to show the median number of registered riders grouped by month for 2011
p = sns.barplot(data = df[df['yr'] == 0], x = 'mnth', y = 'registered', estimator = median)
p.set(title = 'Median Number of Registered Riders in 2011')
p.set(xlabel= 'Month')
p.set (ylabel= 'Number of Registered Riders')
p.set_ylim (top= 230)
plt.show()

#a bar plot to show the median number of registed riders grouped by month for 2012
p = sns.barplot(data = df[df['yr'] == 1], x = 'mnth', y = 'registered', estimator = median)
p.set(title = 'Median Number of Registered Riders in 2012')
p.set(xlabel= 'Month')
p.set (ylabel= 'Number of Registered Riders')
p.set_ylim (top= 230)
plt.show()

"""The bar plots showing the median number of registered riders by month in 2011 and 2012 show that:


1.   The overall median number of registered riders increased from 2011 to 2012
2.   The month with the lowest median number of registered riders was January for both years
3.   The month with the highest median number of registered riders was June in 2011
4.   The month with the highest median number of registered riders was September in 2012
5.   December had the smallest increase in the median number of registered riders from 2011 to 2012

"""

#a bar plot showing the median number of registered rideres grouped by hour for the month of july in 2011 and 2012
p = sns.barplot(data = df, x = 'hr', y = 'registered', estimator = median)
p.set(title = 'Median Number of Registered Riders for July 2011 & July 2012')
p.set(xlabel= 'Hour of The Day')
p.set (ylabel= 'Number of Registered Riders')
plt.show()

"""The bar plot showing the median number of registered riders by hour for July 2011 & 2012 shows that:

1.   Overnight hours (12am - 5am) have the lowest median number of registered riders
2.   The highest median number of registered riders happen during the hours of 8am, 5pm, and 6pm. These hours seem to corrospond to regular work communting hours
3.   During normal working hours (for this purpose 8am - 6pm to include communte times), 10am has the lowest median number of registered riders
"""

#a bar plot showing the median number of registered riders grouped by day for 2011 and 2012
p = sns.barplot(data = df, x = 'weekday', y = 'registered', estimator = median)
p.set(title = 'Median Registered Riders by Day for 2011 and 2012')
p.set(xlabel= 'Day')
p.set (ylabel= 'Number of Registered Riders')
plt.show()

"""The bar plot showing the median number of registered riders by day for 2011 & 2012 shows that:

1.   Sunday has the lowest median number of registered riders, and Saturday has the second lowest
2.   Friday has the highest median number of registered riders
3.   There is a slight general trend of an increasing median number of registered riders from Sunday to Friday


**Please note that for this insight I assumed that 0 = Sunday and 6 = Saturday as I could not find a .txt file explaining the dataset in canvas under this module or previous modules  
"""

#a scatter plot showing the relationship between windspeed and the number of registered riders for March of 2011
subset = df.loc[(df['yr'] == 0) & (df['mnth'] == 3)]
#print(subset)
p = sns.scatterplot(data = subset, x = 'windspeed', y = 'registered')
p.set(title = 'Relationship Between Windspeed and Number of Registered Riders for March 2011')
p.set(xlabel= 'Windspeed')
p.set(ylabel= 'Number of Registered Riders')
plt.show()
print()

"""The scatter plot showing the relationship between windspeed and number of registered riders in March of 2011 shows that:



1.   Generally, there is a trend where the number of registered riders decreases with the windspeed until a windspeed of 0.4, afterwhich the count of registered riders decreases at a faster rate

Reccomendations

 Based on the exploratory analysis above I would reccomend that we (the bike company):


1.   Increase the incentives that we offer to riders when they sign in before a ride
2.   Offer additional incentives, such as points towards a small physical reward, to registered riders who ride on the weekends or outside of regular working hours (8am - 6pm)
"""