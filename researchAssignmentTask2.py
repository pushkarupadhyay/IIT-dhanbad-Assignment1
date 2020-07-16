# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:01:21 2020

@author: pushkar
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#importing files
csv_file='researchsurvey-2019.csv'
df = pd.read_csv(csv_file)
df.head(10) #taking data from head

#plotting both seaborn and mathplotlib graphs

#Box Plot
sns.boxplot(x=df['Year'])
sns.boxplot(x=df['Value'])
sns.boxplot(x=df['Secondary_Breakdown'])
sns.boxplot(x=df['Breakdown'])

#Joint Plot
sns.jointplot(x=df['Year'], y= df['Value'],data=df,kind='reg') #plot in the right side
sns.jointplot(x=df['Value'], y= df['Year'],data=df,kind='hex') # plot in the left

#All type of graph plot
sns.pairplot(df)

#Scatter Plot
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['Value'], df['Year'])
ax.set_xlabel('Value')
ax.set_ylabel('Year')
plt.show()
 

df.dtypes   #knownig data types


#HeatMap
plt.figure(figsize=(20,10))
c= df.corr()
sns.heatmap(c,cmap='BrBG',annot=True)

#Histogram
df.head(10).plot(kind='bar', figsize=(10,5))
plt.title('Research Survey')
plt.ylabel('Value')
plt.xlabel('Year')

#Numpy Array
df = np.array(df[1:], dtype=np.float)

df = df.drop(['Table','Breakdown','Secondary_Breakdown','Year','Value'], axis=1)
df.shape
#Duplicate Rows
duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows:" , duplicate_rows_df.shape)

df.count()
df = df.drop_duplicates() #Duplicate files
df.shape #shows array dimension of CSV file
df.count() #count total objects,int,float in CSV file
print(df.isnull().sum())

df = df.dropna() #no null values present
df.count()
df.columns
df.describe()





#by mathploth
#course = data["num_reviews"]
#price = data["price"]

#x=[]
#y=[]

#x=list(price)
#y=list(course)

#plt.scatter(x,y) #for scattered graph
#plt.xlabel('price')
#plt.ylabel('num_reviews')
#plt.title('Price vs course_title')
#plt.pie(x,labels=y,autopct='%.2f%%') #for pie graph

#plt.show()
