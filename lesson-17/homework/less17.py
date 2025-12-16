# TASK 1

# frame yartdim
import pandas as pd

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)

# column nomini uzgartirdim
df.rename(columns={
    'First Name' : "first_name",
    "Age" : "age"  
})

# top 3 tasi
df.head(3)

# urtacha yosh
df['Age'].mean()

# name va city columns
df[['First Name','City']]

# numpy bn random salary qiymati yaratdim
import numpy as np
df['Salary'] = np.random.randint(3000,10000,len(df))

# standart statestikasi
df.describe().round(2)


#TASK 2

#jadval yaratish
sales_and_expenses = {'Month':['Jan','Feb','Mar','Apr'], 'Sales':[5000,6000,7500,8000], 'Expenses':[3000,3500,4000,4500]}
df_sales = pd.DataFrame(sales_and_expenses)

# sales va expense max lari
df_sales[['Sales','Expenses']].max()

# sales va expense min lari
df_sales[['Sales','Expenses']].min()

# sales va expense avg lari
df_sales[['Sales','Expenses']].mean()


#TASK 3
# frame yaratdim
data1 = {'Category':['Rent','Utilities','Groceries','Entertainment'],
            'January' :[1200,200,300,150],
            'February':[1300,220,320,160],
            'March'   :[1400,240,330,170],
            'April'   :[1500,250,350,180]}

expenses = pd.DataFrame(data1)

# index qushish orqali kategiryalar buyicha max qiymatni topdim
expenses.set_index('Category')[['January','February','March','April']].max(axis=1)

# index qushish orqali kategiryalar buyicha min qiymatni topdim
expenses.set_index('Category')[['January','February','March','April']].min(axis=1)

# index qushish orqali kategiryalar buyicha o`ratcha  qiymatni topdim
expenses.set_index('Category')[['January','February','March','April']].mean(axis=1)

