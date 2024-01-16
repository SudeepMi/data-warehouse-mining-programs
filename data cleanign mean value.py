import pandas as pd
import numpy as np

data = pd.read_csv('employee2.csv')
print("Original Data")
print(data[0:25])
# Filling missing values with mean 
data['Salary']=data['Salary'].fillna(data['Salary'].mean())
print("Cleaned Data")
print(data[0:25])
"""
data = pd.read_csv('employee2.csv')
print("Original Data")
print(data[0:25])
# Filling missing values withi
data['Salary']=data['Salary'].interpolate(method="linear")
print("Cleaned Data")
print(data[0:25])
"""
