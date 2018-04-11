# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 18:44:00 2018

@author: karthik
"""
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

salary_dataset = pd.read_csv("C:\\Users\\user\\Desktop\\salary.csv")
print(salary_dataset.head())

X = salary_dataset[['Worked Hours','Certification','Experience in years']]
Y = salary_dataset['Salary']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33)

linear_regression = LinearRegression()
linear_regression.fit(X_train,Y_train)
Y_pred = linear_regression.predict(X_test)

plt.figure(1)
plt.plot(list(range(len(Y_pred))),Y_pred,marker='o')
plt.plot(list(range(len(Y_test))),Y_test,marker='o')
plt.xlabel("Test Cases")
plt.ylabel("Salary")
plt.title("Salary Prediction")
plt.legend(('Predicted','Actual'))
plt.show()

print('Coefficients: \n', linear_regression.coef_)
print("Mean squared error: %.2f"% mean_squared_error(Y_test, Y_pred))
print('Variance score: %.2f' % r2_score(Y_test, Y_pred))
