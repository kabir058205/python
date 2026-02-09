import pandas as pd
import numpy as np
from datetime import datetime
 


def main():

    
    
    # -------------------------------------------------
    # STEP 1: Create DataFrame
    # -------------------------------------------------
    print("\n=== STEP 1: CREATE DATAFRAME ===")

    data = {
        "EmpID": [101, 102, 103, 104, 105],
        "Name": ["Kabir", "Amit", "Sara", "John", "Ravi"],
        "Age": [35, 30, 28, 40, None],
        "Country": ["Sweden", "India", "USA", "UK", "India"],
        "Salary": [90000, 70000, 65000, 80000, 72000]
    }

    df = pd.DataFrame(data)
    print(df)
   
    # -------------------------------------------------
    # STEP 2: Inspect & Clean Data
    # -------------------------------------------------
    print("\n=== STEP 2: INSPECT & CLEAN DATA ===")

    print(df.info())
    print(df.isnull().sum())

    df["Age"] = df["Age"].fillna(df["Age"].mean())
    print(df)

    # -------------------------------------------------
    # STEP 3: Filter, Sort, Group
    # -------------------------------------------------
    print("\n=== STEP 3: FILTER, SORT, GROUP ===")

    print(df[df["Salary"] > 75000])
    print(df.sort_values(by="Salary", ascending=False))
    print(df.groupby("Country")["Salary"].mean())

    # -------------------------------------------------
    # STEP 4: Read & Write CSV
    # -------------------------------------------------
    print("\n=== STEP 4: READ & WRITE CSV ===")

    df.to_csv("employees.csv", index=False)
    df = pd.read_csv("employees.csv")
    print(df)

    # -------------------------------------------------
    # STEP 5: Bonus & Total Compensation
    # -------------------------------------------------
    print("\n=== STEP 5: BONUS & TOTAL COMP ===")

    df["Bonus"] = df["Salary"] * 0.10
    df["TotalComp"] = df["Salary"] + df["Bonus"]
    print(df)

    # -------------------------------------------------
    # STEP 6: Merge / Join
    # -------------------------------------------------
    print("\n=== STEP 6: MERGE / JOIN ===")

    dept_data = {
        "EmpID": [101, 102, 103, 104, 105],
        "Department": ["IT", "Finance", "HR", "IT", "Finance"]
    }

    df_dept = pd.DataFrame(dept_data)
    df = pd.merge(df, df_dept, on="EmpID")
    print(df)

    # -------------------------------------------------
    # STEP 7: Date & Time
    # -------------------------------------------------
    print("\n=== STEP 7: DATE & TIME ===")

    df["JoinDate"] = pd.to_datetime([
        "2020-01-10", "2019-03-15", "2021-07-01", "2018-11-20", "2022-06-05"
    ])

    df["YearsInCompany"] = (datetime.now() - df["JoinDate"]).dt.days // 365
    print(df[["Name", "JoinDate", "YearsInCompany"]])

    # -------------------------------------------------
    # STEP 8: Apply Function
    # -------------------------------------------------
    print("\n=== STEP 8: APPLY FUNCTION ===")

    def salary_band(salary):
        if salary >= 80000:
            return "High"
        elif salary >= 70000:
            return "Medium"
        else:
            return "Low"

    df["SalaryBand"] = df["Salary"].apply(salary_band)
    print(df[["Name", "Salary", "SalaryBand"]])

    # -------------------------------------------------
    # STEP 9: Statistics
    # -------------------------------------------------
    print("\n=== STEP 9: STATISTICS ===")

    print(df["Salary"].describe())
    print(df[["Age", "Salary"]].corr())

    # -------------------------------------------------
    # STEP 10: Value Counts
    # -------------------------------------------------
    print("\n=== STEP 10: VALUE COUNTS ===")

    print(df["Country"].value_counts())

    # -------------------------------------------------
    # STEP 11: Duplicates
    # -------------------------------------------------
    print("\n=== STEP 11: DUPLICATES ===")

    print(df.duplicated())
    df = df.drop_duplicates()

    # -------------------------------------------------
    # STEP 12: Rename Columns
    # -------------------------------------------------
    print("\n=== STEP 12: RENAME COLUMNS ===")

    df = df.rename(columns={"EmpID": "EmployeeID"})
    print(df.columns)

    # -------------------------------------------------
    # STEP 13: Lambda Function
    # -------------------------------------------------
    print("\n=== STEP 13: LAMBDA FUNCTION ===")

    df["Tax"] = df["Salary"].apply(lambda x: x * 0.2)
    print(df[["Name", "Salary", "Tax"]])

    # -------------------------------------------------
    # STEP 14: Ranking
    # -------------------------------------------------
    print("\n=== STEP 14: RANKING ===")

    df["SalaryRank"] = df["Salary"].rank(ascending=False)
    print(df[["Name", "Salary", "SalaryRank"]])

    # -------------------------------------------------
    # STEP 15: Multi Column Sort
    # -------------------------------------------------
    print("\n=== STEP 15: MULTI COLUMN SORT ===")

    print(df.sort_values(by=["Country", "Salary"], ascending=[True, False]))

    # -------------------------------------------------
    # STEP 16: String Operations
    # -------------------------------------------------
    print("\n=== STEP 16: STRING OPS ===")

    df["NameUpper"] = df["Name"].str.upper()
    print(df[["Name", "NameUpper"]])

    # -------------------------------------------------
    # STEP 17: Conditional Column
    # -------------------------------------------------
    print("\n=== STEP 17: CONDITIONAL COLUMN ===")

    df["SeniorFlag"] = np.where(df["Age"] >= 35, "Senior", "Junior")
    print(df[["Name", "Age", "SeniorFlag"]])

    # -------------------------------------------------
    # STEP 18: Pivot Table
    # -------------------------------------------------
    print("\n=== STEP 18: PIVOT TABLE ===")

    pivot = pd.pivot_table(
        df,
        values="Salary",
        index="Department",
        columns="Country",
        aggfunc="mean"
    )
    print(pivot)
    
    # -------------------------------------------------
    # STEP 19: Export Excel
    # -------------------------------------------------
    print("\n=== STEP 19: EXPORT EXCEL ===")
    try:
        df.to_excel("employees_final.xlsx", index=False)
        print("employees_final.xlsx created")
    except ModuleNotFoundError:
        print("openpyxl is not installed — cannot write Excel files with pandas.")
        print("Installing openpyxl and re-running will enable Excel export.")
        print("Falling back to CSV export instead.")
        df.to_csv("employees_final.csv", index=False)
        print("employees_final.csv created")
        

if __name__ == "__main__":
    main()
