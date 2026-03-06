import pandas as pd



df = pd.read_csv("employee_attrition.csv")

print("Dataset Preview:")
print(df.head())

print("\nDataset Shape:", df.shape)
print("\nColumns:", df.columns)

print("\nMissing Values:")
print(df.isnull().sum())





df["Job_Satisfaction"].fillna(df["Job_Satisfaction"].median(), inplace=True)



attrition_yes = df[df["Attrition"] == "Yes"]

print("\nEmployees who left the company:")
print(attrition_yes)


overtime_employees = df[df["Overtime"] == "Yes"]

print("\nEmployees doing overtime:")
print(overtime_employees)


high_income = df[df["Monthly_Income"] > 60000]

print("\nHigh income employees:")
print(high_income)



sorted_income = df.sort_values(by="Monthly_Income", ascending=False)

print("\nEmployees sorted by Monthly Income:")
print(sorted_income)


dept_sorted = df.sort_values(by=["Department", "Monthly_Income"], ascending=[True, False])

print("\nDepartment wise salary ranking:")
print(dept_sorted)


avg_income_dept = df.groupby("Department")["Monthly_Income"].mean()

print("\nAverage Income per Department:")
print(avg_income_dept)


attrition_dept = df.groupby("Department")["Attrition"].value_counts()

print("\nAttrition by Department:")
print(attrition_dept)


avg_satisfaction = df.groupby("Department")["Job_Satisfaction"].mean()

print("\nAverage Job Satisfaction by Department:")
print(avg_satisfaction)


df["Income_Level"] = df["Monthly_Income"].apply(
    lambda x: "High" if x > 60000 else "Medium" if x > 50000 else "Low"
)

print("\nDataset with Income Level:")
print(df.head())




df.to_csv("Cleaned_Employee_Attrition.csv", index=False)

print("\nClean dataset saved as Cleaned_Employee_Attrition.csv")