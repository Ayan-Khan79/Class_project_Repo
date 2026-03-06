import pandas as pd
import numpy as np

# ---------------------------------
# 1. LOAD DATA
# ---------------------------------

customers = pd.read_csv("Customers1.csv")
sales = pd.read_csv("Sales1.csv")   # change to read_excel if your file is .xlsx
support = pd.read_csv("Support1.csv")

print("Customers Shape:", customers.shape)
print("Sales Shape:", sales.shape)
print("Support Shape:", support.shape)

print("\nCustomers Columns:", customers.columns)
print("Sales Columns:", sales.columns)
print("Support Columns:", support.columns)

print("\nMissing Values:")
print(customers.isnull().sum())
print(sales.isnull().sum())
print(support.isnull().sum())


# ---------------------------------
# 2. NUMPY ARRAY OPERATIONS
# ---------------------------------

prices = np.array(sales["Price"])

# Apply 10% discount
discounted_prices = prices * 0.9

sales["DiscountedPrice"] = discounted_prices

# Revenue calculation
sales["Revenue"] = sales["Quantity"] * sales["Price"]


# ---------------------------------
# 3. INDEXING & SLICING
# ---------------------------------

sales["OrderDate"] = pd.to_datetime(sales["OrderDate"])

# Orders in January 2025 (dataset may return empty but code is correct)
jan_orders = sales[
    (sales["OrderDate"].dt.month == 1) &
    (sales["OrderDate"].dt.year == 2025)
]

print("\nOrders in January 2025:")
print(jan_orders)

print("\nFirst 10 rows of Sales:")
print(sales.head(10))


# ---------------------------------
# 4. FILTERING
# ---------------------------------

north_customers = customers[customers["Region"] == "North"]
print("\nCustomers from North region:")
print(north_customers)

high_revenue_orders = sales[sales["Revenue"] > 10000]
print("\nOrders with revenue > 10000:")
print(high_revenue_orders)


# ---------------------------------
# 5. SORTING
# ---------------------------------

customers["SignupDate"] = pd.to_datetime(customers["SignupDate"])

customers_sorted = customers.sort_values(by="SignupDate")

sales_sorted = sales.sort_values(by="Revenue", ascending=False)

print("\nCustomers sorted by signup date:")
print(customers_sorted)

print("\nSales sorted by revenue:")
print(sales_sorted)


# ---------------------------------
# 6. GROUPING
# ---------------------------------

# merge region into sales
sales_region = pd.merge(sales, customers[["CustomerID", "Region"]], on="CustomerID")

avg_revenue_region = sales_region.groupby("Region")["Revenue"].mean()

print("\nAverage Revenue by Region:")
print(avg_revenue_region)

avg_resolution = support.groupby("IssueType")["ResolutionTime"].mean()

print("\nAverage Resolution Time by Issue Type:")
print(avg_resolution)


# ---------------------------------
# 7. DATA WRANGLING
# ---------------------------------

# Fill missing Age with median
customers["Age"].fillna(customers["Age"].median(), inplace=True)


# ---------------------------------
# MERGE DATASETS
# ---------------------------------

data = pd.merge(customers, sales, on="CustomerID")
data = pd.merge(data, support, on="CustomerID", how="left")


# ---------------------------------
# CUSTOMER LIFETIME VALUE
# ---------------------------------

clv = sales.groupby("CustomerID")["Revenue"].sum().reset_index()
clv.rename(columns={"Revenue": "CLV"}, inplace=True)

data = pd.merge(data, clv, on="CustomerID")


# ---------------------------------
# AVERAGE RESOLUTION TIME PER CUSTOMER
# ---------------------------------

avg_res_time = support.groupby("CustomerID")["ResolutionTime"].mean().reset_index()
avg_res_time.rename(columns={"ResolutionTime": "AvgResolutionTime"}, inplace=True)

data = pd.merge(data, avg_res_time, on="CustomerID", how="left")


# ---------------------------------
# EXPORT CLEAN DATA
# ---------------------------------

data.to_csv("Cleaned_Data.csv", index=False)

print("\nCleaned dataset saved as Cleaned_Data.csv")