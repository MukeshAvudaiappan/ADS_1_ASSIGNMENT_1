#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 12:16:04 2023

@author: mukeshavudaiappan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Functions
#Function to manipulate the dataframe to use into bar plot
def data_mal():
    for i in range(len(years)):
        victim_0_10.append(df_bar[(df_bar['Year'] == years[i]) &
        (df_bar['Subgroup'] == 'Total Rape Victims')]
                           ['Victims_Upto_10_Yrs'].sum())
        victim_10_14.append(df_bar[(df_bar['Year'] == years[i]) & 
        (df_bar['Subgroup'] == 'Total Rape Victims')]
                            ['Victims_Between_10-14_Yrs'].sum())
        victim_14_18.append(df_bar[(df_bar['Year'] == years[i]) & 
        (df_bar['Subgroup'] == 'Total Rape Victims')]
                            ['Victims_Between_14-18_Yrs'].sum())
        victim_18_30.append(df_bar[(df_bar['Year'] == years[i]) & 
        (df_bar['Subgroup'] == 'Total Rape Victims')]
                            ['Victims_Between_18-30_Yrs'].sum())
        victim_30_50.append(df_bar[(df_bar['Year'] == years[i]) & 
        (df_bar['Subgroup'] == 'Total Rape Victims')]
                            ['Victims_Between_30-50_Yrs'].sum())
        victim_50.append(df_bar[(df_bar['Year'] == years[i]) & 
        (df_bar['Subgroup'] == 'Total Rape Victims')]
                         ['Victims_Above_50_Yrs'].sum())

#Funtion to get the percentage% value for each element in the pie plot
def func(pct, allvalues):
    return '{:.1f}%'.format(pct)

#variables
#Converting all CSV files to dataframe

df_line = pd.read_csv('total_sales_world_annual.csv', index_col = 0)
df_bar = pd.read_csv('20_Victims_of_rape.csv')
df_pie = pd.read_csv('20_Victims_of_rape.csv')
df_line = df_line / 1000000
victim_0_10, victim_10_14, victim_14_18 = [], [], []
victim_18_30, victim_30_50, victim_50 = [], [], []
years = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]
data_mal()
x = np.arange(len(years))
width = .1
df_pie = df_pie[(df_pie['Year'] == 2010) & 
                (df_pie['Subgroup'] == 'Total Rape Victims')]
df_pie = df_pie.iloc[:,4:].sum()
df_pie = df_pie.drop('Victims_of_Rape_Total')
df_pie = df_pie.drop('Victims_Above_50_Yrs')
split = (0.1, 0.0, 0.1, 0.1, 0.1)
colors = ('orange', 'cyan', 'red', 'grey', 'yellow')
wp = {'linewidth' : 1, 'edgecolor' : 'white'}

# Plotting the total cars sold in three countries into line plot

plt.figure(figsize = (8, 5), layout = 'constrained')
plt.rcParams['font.size'] = 40
plt.style.use('default')
plt.plot(df_line.columns[:], df_line.loc['UNITED KINGDOM'].values,
         marker = 'o', label = 'UNITED KINGDOM')
plt.plot(df_line.columns[:], df_line.loc['EUROPE'].values,
         marker = 'o', label = 'EUROPE')
plt.plot(df_line.columns[:], df_line.loc['CHINA'].values,
         marker = 'o', label = 'CHINA')
plt.xlabel('Year', fontsize = 15)
plt.ylabel('Cars per million', fontsize = 15)
plt.title('Total Cars Sold', fontsize = 15)
plt.xticks(rotation = 35, fontsize = 12)
plt.yticks(fontsize = 12)
plt.grid('True')
plt.legend()
plt.show()
plt.close()

#plotting the 10 years of rape cases in India into bar plot

plt.figure(figsize = (10,6), layout = 'constrained')
plt.rcParams['font.size'] = 20
plt.style.use('default')
plt.bar(x - (width / 2) * 5, victim_0_10, width,
        label = 'Victim_Upto_10_Yrs')
plt.bar(x - width / 2, victim_10_14, width,
        label = 'Victim_Between_10_14_Yrs')
plt.bar(x + width / 2, victim_14_18, width,
        label = 'Victim_Between_14_18_Yrs')
plt.bar(x - (width / 2) * 3, victim_18_30, width,
        label = 'Victim_Between_18_30_Yrs')
plt.bar(x + (width / 2) * 3, victim_30_50, width,
        label = 'Victim_Between_30_50_Yrs')
plt.bar(x + (width / 2) * 5, victim_50, width, 
        label = 'Victims_Above_50_Yrs')
plt.xlabel('Year', fontsize = 16)
plt.ylabel('Total Rape cases reported', fontsize = 16)
plt.title('Total Rape cases in years - INDIA', fontsize = 18)
plt.xticks(x, labels = years, rotation = 35, fontsize = 13)
plt.yticks(fontsize = 13)
plt.legend()
plt.show()
plt.close()

#plotting the age wise rape cases into an pie chart 

fig, ax = plt.subplots(figsize = (10, 7))
wedges, texts, autotexts = ax.pie(df_pie,
                                  autopct = lambda pct: func(pct, df_pie),
                                  explode = split,
                                  labels = df_pie.index,
                                  shadow = True,
                                  colors = colors,
                                  startangle = 25,
                                  wedgeprops = wp,
                                  textprops = dict(color = "black"))
ax.legend(wedges, df_pie.index,
          title = 'Age Category',
          loc = 'center left',
          bbox_to_anchor = (1, 0, 0, 0))
plt.setp(autotexts, size = 11, weight = 'bold')
ax.set_title('Total Rape Cases in Years - INDIA')
plt.style.use('default')
plt.show()
plt.close()