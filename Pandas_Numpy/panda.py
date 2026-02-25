import pandas as pd

df = pd.read_csv("Retail_sales.csv")

print(df)
print('\n')
print(df.groupby("Region")["Total_Spent"].sum())



