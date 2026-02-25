import pandas as pd
import numpy as np

# Load datasets
customers = pd.read_csv("Customers1.csv")
sales = pd.read_csv("Sales1.csv")
support = pd.read_csv("support1.csv")

# # Inspect basic info
# print(customers.shape)
# print(sales.shape)
# print(support.shape)

# print('\n')

# print(customers.columns)
# print(sales.columns)
# print(support.columns)

# print('\n')

# Checking info of sheets
print(customers.info())
print(sales.info())
print(support.info())

print('\n')
print(sales)
print('\n')

# Convert prices to numpy array
price_array = sales["Price"].to_numpy()

# Apply 10% discount
discounted_prices = price_array * 0.9

# Add discounted price column
sales["Discounted_Price"] = discounted_prices

sales["Revenue"] = sales["Quantity"] * sales["Price"]

print(sales)
print('\n')
print(customers)
#Filling  missing values with median
median_age = customers["Age"].median() 
customers["Age"] = customers["Age"].fillna(median_age,inplace=True)
print('\n')
print(customers)