import pandas as pd

df = pd.read_csv("Dataset.csv")

print(df)
print('\n')

exceptional = df[df["Score"] > 90]
print(exceptional)
print('\n')

sales = df[df["Department"] == "Sales"]
print(sales)
print('\n')

sorted_score = df.sort_values(by="Score", ascending=False)
print(sorted_score)
print('\n')

dept_sorted = df.sort_values(
    by=["Department", "Score"],
    ascending=[True, False]
)
print(dept_sorted)
print('\n')