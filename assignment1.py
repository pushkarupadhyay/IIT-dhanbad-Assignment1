# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:40:20 2020

@author: pushkar
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#importing files
csv_file='udemy_courses.csv'
df = pd.read_csv(csv_file)
df.head(10) #taking data from head

#plotting both seaborn and mathplotlib graphs

#Box Plot
sns.boxplot(x=df['price'])
sns.boxplot(x=df['num_lectures'])
sns.boxplot(x=df['num_reviews'])
sns.boxplot(x=df['num_subscribers'])

#Joint Plot
sns.jointplot(x=df['num_subscribers'], y= df['content_duration'],data=df,kind='reg') #plot in the right side
sns.jointplot(x=df['price'], y= df['num_lectures'],data=df,kind='hex') # plot in the left

#All type of graph plot
sns.pairplot(df)

#Scatter Plot
fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['num_subscribers'], df['price'])
ax.set_xlabel('num_subscribers')
ax.set_ylabel('price')
plt.show()
 

df.dtypes   #knownig data types


#HeatMap
plt.figure(figsize=(20,10))
c= df.corr()
sns.heatmap(c,cmap='BrBG',annot=True)

#Histogram
df.head(10).plot(kind='bar', figsize=(10,5))
plt.title('udemy courses')
plt.ylabel('price')
plt.xlabel('num_reviews')

#Numpy Array
df = np.array(df[1:], dtype=np.float)

df = df.drop(['course_id','url','level','content_duration','published_timestamp'], axis=1)
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


df['is_paid'].value_counts()
df_paid = df[df["is_paid"]]
df_paid
df_notpaid = df[df["is_paid"]]
df_notpaid
avg_subs_paid = round(df_paid["num_subscribers"].mean())
avg_subs_paid
avg_subs_notpaid = round(df_notpaid["num_subscribers"].mean())
avg_subs_notpaid
df['best-seller'] = df.apply(lambda row: 0, axis = 1)
for idx, row in df.iterrows():
    if  df.loc[idx,'is_paid'] == 1 and df.loc[idx,'num_subscribers'] > avg_subs_paid:  #aveage paid value
        df.loc[idx,'best-seller'] = 1
    if  df.loc[idx,'is_paid'] == 0 and df.loc[idx,'num_subscribers'] > avg_subs_notpaid: #avearge not paid value
        df.loc[idx,'best-seller'] = 1
df
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
