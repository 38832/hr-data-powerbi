import pandas as pd
import json

# Read the Excel file
df = pd.read_excel('HR Data.xlsx', sheet_name='HR data')

print("=" * 80)
print("HR DATA ANALYSIS - PROJECT OVERVIEW")
print("=" * 80)

print(f"\nDataset Size: {len(df)} employee records with {len(df.columns)} attributes\n")

print("--- ATTRITION ANALYSIS ---")
attrition = df['Attrition'].value_counts()
print(f"Current Employees: {attrition.get('No', 0)} ({attrition.get('No', 0)/len(df)*100:.1f}%)")
print(f"Ex-Employees (Attrition): {attrition.get('Yes', 0)} ({attrition.get('Yes', 0)/len(df)*100:.1f}%)")

print("\n--- DEPARTMENT DISTRIBUTION ---")
print(df['Department'].value_counts().to_string())

print("\n--- TOP 10 JOB ROLES ---")
print(df['Job Role'].value_counts().head(10).to_string())

print("\n--- DEMOGRAPHICS ---")
print(f"Gender: {df['Gender'].value_counts().to_dict()}")
print(f"Marital Status: {df['Marital Status'].value_counts().to_dict()}")

print("\n--- KEY METRICS (Averages) ---")
print(f"Average Age: {df['Age'].mean():.1f} years")
print(f"Average Monthly Income: ${df['Monthly Income'].mean():,.0f}")
print(f"Average Years at Company: {df['Years At Company'].mean():.1f} years")
print(f"Average Daily Rate: ${df['Daily Rate'].mean():.0f}")
print(f"Average Distance from Home: {df['Distance From Home'].mean():.1f} km")
print(f"Average Job Satisfaction: {df['Job Satisfaction'].mean():.2f}/4.0")
print(f"Average Work-Life Balance: {df['Work Life Balance'].mean():.2f}/4.0")

print("\n--- COMPENSATION & BENEFITS ---")
print(f"Average Hourly Rate: ${df['Hourly Rate'].mean():.0f}")
print(f"Average Monthly Rate: ${df['Monthly Rate'].mean():,.0f}")
print(f"Employees with Stock Options: {(df['Stock Option Level'] > 0).sum()} ({(df['Stock Option Level'] > 0).sum()/len(df)*100:.1f}%)")
print(f"Average Performance Rating: {df['Performance Rating'].mean():.2f}/4.0")

print("\n--- EDUCATION ---")
print(df['Education Field'].value_counts().head(8).to_string())

print("\n--- BUSINESS TRAVEL ---")
print(df['Business Travel'].value_counts().to_string())

print("\n--- OVERTIME STATUS ---")
print(df['Over Time'].value_counts().to_string())
