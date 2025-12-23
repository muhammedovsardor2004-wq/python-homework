import pandas as pd

sales = pd.read_csv('sales_data.csv')


category_stats = sales.groupby("Category").agg(
                                total_quantity_sold=("Quantity", "sum"),
                                average_price=("Price", "mean"),
                                max_quantity_single_sale=("Quantity", "max")
                            )

print(category_stats)


total_sold = (sales.groupby(['Category','Product'])
                    .agg(total_sold = ('Quantity','sum'))
                    .reset_index())

max_q = total_sold.loc[total_sold.groupby('Category')['total_sold'].idxmax()]
max_q


sales['total_price'] = sales.Quantity * sales.Price
total = sales

date = total.groupby('Date').agg({'total_price':'sum'})

best_day = date.idxmax()
max_val = date.total_price.max()

print(best_day,max_val)




import pandas as pd

df = pd.read_csv("customer_orders.csv")

order_counts = df.groupby("CustomerID")["OrderID"].nunique()

active_customers = order_counts[order_counts >= 20].index

filtered_customers = df[df["CustomerID"].isin(active_customers)]
filtered_customers


avg_price_per_customer = df.groupby("CustomerID")["Price"].mean()

premium_customers = avg_price_per_customer[avg_price_per_customer > 120]

print(premium_customers)


df["Total_Price"] = df["Quantity"] * df["Price"]

product_summary = df.groupby("Product").agg(
    total_quantity=("Quantity", "sum"),
    total_price=("Total_Price", "sum")
)

filtered_products = product_summary[product_summary["total_quantity"] <= 5]

print(filtered_products)


import sqlite3,pandas as pd

conn = sqlite3.connect("populations.db")

population = pd.read_sql(
    "SELECT * FROM population",
    conn
)

salary_bands = pd.read_excel("population_salary_analysis.xlsx")



def extract_min_max(band):
    band = band.replace("$", "").replace(",", "").lower()

    if "till" in band:
        max_val = int(band.split()[-1])
        return 0, max_val

    if "over" in band:
        min_val = int(band.split()[0])
        return min_val, np.inf

    min_val, max_val = band.split(" - ")
    return int(min_val), int(max_val)



import numpy as np

salary_bands[["Min", "Max"]] = salary_bands["Salary Band"].apply(
    lambda x: pd.Series(extract_min_max(x))
)



def get_salary_band(salary):
    row = salary_bands[
        (salary_bands["Min"] <= salary) &
        (salary_bands["Max"] >= salary)
    ]
    return row["Salary Band"].values[0] if not row.empty else "Unknown"
population["Salary_Category"] = population["salary"].apply(get_salary_band)


salary_summary = population.groupby("Salary_Category").agg(
    Number_of_population=("salary", "count"),
    Average_Salary=("salary", "mean"),
    Median_Salary=("salary", "median")
)
salary_summary
population



state_salary_summary = population.groupby(
    ["state", "Salary_Category"]
).agg(
    Number_of_population=("salary", "count"),
    Average_Salary=("salary", "mean"),
    Median_Salary=("salary", "median")
).reset_index()

state_salary_summary
