# -*- coding: utf-8 -*-
"""chi-xi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O3nhVSwg1ZycxIw8LoXzk1Pp6v6Mhzoq
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#from google.colab import drive
#drive.mount('/content/drive')

pip show sklearn

df = pd.read_csv('/content/loans_full_schema.csv',sep=',')
df

filtered_df = df[['earliest_credit_line', 'annual_income','interest_rate']].dropna()
filtered_df

#MODEL 1 - load data
m1_df = filtered_df[['annual_income','interest_rate']]
m1_x = m1_df.iloc[:,0].values.reshape(-1,1)
m1_y = m1_df.iloc[:,-1].values

m1_x_train, m1_x_test, m1_y_train, m1_y_test = train_test_split(m1_x, m1_y, test_size = 1/5, random_state = 0)

#Train

m1 = LinearRegression()
m1.fit(m1_x_train, m1_y_train)

plt.scatter(m1_x_train, m1_y_train, color = 'red')
plt.plot(m1_x_train, m1.predict(m1_x_train), color = 'blue')
plt.title('annual_income vs interest rate')
plt.xlabel('annual_income')
plt.ylabel('interest rate')
plt.show()

plt.scatter(m1_x_test, m1_y_test, color = 'red')
plt.plot(m1_x_test, m1.predict(m1_x_test), color = 'blue')
plt.title('annual_income vs interest rate')
plt.xlabel('annual_income')
plt.ylabel('interest rate')
plt.show()

#MODEL 2 - load data
m2_df = filtered_df[['earliest_credit_line','interest_rate']]
m2_x = m2_df.iloc[:,0].values.reshape(-1,1)
m2_y = m2_df.iloc[:,-1].values

m2_x_train, m2_x_test, m2_y_train, m2_y_test = train_test_split(m2_x, m2_y, test_size = 1/5, random_state = 0)

#Train
m2 = SVR()
m2.fit(m2_x_train, m2_y_train)

plt.scatter(m2_x_train, m2_y_train, color = 'red')
plt.plot(m2_x_train, m2.predict(m2_x_train), color = 'blue')
plt.title('earliest_credit_line vs interest rate')
plt.xlabel('earliest_credit_line')
plt.ylabel('interest rate')
plt.show()

plt.scatter(m2_x_test, m2_y_test, color = 'red')
plt.plot(m2_x_test, m2.predict(m2_x_test), color = 'blue')
plt.title('earliest_credit_line vs interest rate')
plt.xlabel('earliest_credit_line')
plt.ylabel('interest rate')
plt.show()

# Function to Predict interest rate based on both models
def predict(a:float, b:float):
    return (m1.predict([[a]]) + m2.predict([[b]]))[0]/2

predict(500,20)