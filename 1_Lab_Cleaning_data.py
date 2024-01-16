import pandas as pd
import numpy as np

data = pd.read_csv('employee1.csv')
print("Original Data")
print(data[0:10])

# Removing missing values
data=data.dropna(axis=0)#axix=0 removes the row, if it is 1 it will remove column

# Removing duplicate rows
data.drop_duplicates(keep='first',inplace=True)

# Removing column Boonus %
del data['Bonus %']

# Correcting Inconsitencies among values
data['Team']=data['Team'].str.replace('Fin','Finance')
data['Team']=data['Team'].str.replace('Mkt','Marketing')
data['Team']=data['Team'].str.replace('Financeance','Finance')

print("Cleaned Data")
print(data[0:10])
data.to_csv('employees_cleaned.csv', index=False)
print("Successfully Cleaned...")
