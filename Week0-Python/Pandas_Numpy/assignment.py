import pandas as pd

df1 = pd.read_csv("employee_attrition.csv")
df2 = pd.read_csv("telecom_churn.csv")
df3 = pd.read_csv("sample_data1.csv")

# No of rows in each files
print("No of rows in Employee_attrition file is ", len(df1))
print("No of rows in Employee_Details file is ", len(df2))
print("No of rows in Telecom_churn file is ", len(df3))

# Columns which have missing values
print("No of missing values in Employee_attrition file is ", df1.isnull().sum())
print("No of misisng values in Employee_Details file is ", df2.isnull().sum())
print("No of missing values in Telecom_churn file is ", df3.isnull().sum())

# Average Salary
print("Average salary in Employee_attrition file is ", df1["Monthly_Income"].mean())
print("Average Salary  in Employee_Details file is ", df3["Salary"].mean())

# Max Employees
print("Max Employees in  Employee_attrition file is ", df1["Department"].max())
print("Max Employees in  Employee_Details file is ", df3["Department"].max())


