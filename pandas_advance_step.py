import pandas as pd
import numpy as np
from datetime import datetime
from hello import say_hello


def create_dataframe():
    return pd.DataFrame({
        "EmpID": [101, 102, 103, 104, 105],
        "Name": ["Kabir", "Amit", "Sara", "John", "Ravi"],
        "Age": [35, 30, 28, 40, None],
        "Country": ["Sweden", "India", "USA", "UK", "India"],
        "Salary": [90000, 70000, 65000, 80000, 72000],
    })


def clean_data(df):
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    return df


def enrich_compensation(df):
    df["Bonus"] = df["Salary"] * 0.1
    df["TotalComp"] = df["Salary"] + df["Bonus"]
    return df


def add_dates(df):
    df["JoinDate"] = pd.to_datetime([
        "2020-01-10", "2019-03-15", "2021-07-01", "2018-11-20", "2022-06-05"
    ])
    df["YearsInCompany"] = (datetime.now() - df["JoinDate"]).dt.days // 365
    return df


def add_flags(df):
    df["SalaryBand"] = pd.cut(
        df["Salary"],
        bins=[0, 70000, 80000, float("inf")],
        labels=["Low", "Medium", "High"]
    )
    df["SeniorFlag"] = np.where(df["Age"] >= 35, "Senior", "Junior")
    return df


def export(df):
    df.to_csv("employees_final.csv", index=False)


def main():
    say_hello()

    df = (
        create_dataframe()
        .pipe(clean_data)
        .pipe(enrich_compensation)
        .pipe(add_dates)
        .pipe(add_flags)
    )

    print(df)
    export(df)


if __name__ == "__main__":
    main()
