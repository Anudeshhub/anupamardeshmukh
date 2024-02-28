import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import plotly.express as px
##1. Read in the `coupons.csv` file
df = pd.read_csv('data/coupons.csv')
df.head()
##2. Investigate the dataset for missing or problematic data
## CarryAway has missing values

df[df['CarryAway'].isnull()].coupon.value_counts()
##3. Decide what to do about your missing data -- drop, replace, other...
## Replaced NaN CarryAway values with 'Never'
df['CarryAway'].fillna('Never', inplace=True)
df['Bar'] = df['Bar'].replace('',0)
##4. What proportion of the total observations chose to accept the coupon? 
if (df['Y'] == 1).any():
    sumY = df['Y'].sum()
    print(sumY)
#7210 TOTAL observations chose to accept the coupon  Y = 1 "Coupon Accepted"  
##5. Use a bar plot to visualize the `coupon` column.
couponcounts =  df['coupon'].value_counts()
plt.figure(figsize=(12, 8))
plt.bar(couponcounts.index,couponcounts.values,color='blue')
# Add  labels
plt.xlabel("Coupon Category")
plt.ylabel("Count")

plt.show()
##6. Use a histogram to visualize the temperature column.
hist = px.histogram(df,x="temperature",title="Histogram of temperature",labels={"temperature": "temperature"},color_discrete_sequence = px.colors.qualitative.Dark24, color = "Y" )
hist.show()
##Investigating the Bar Coupons**
##Data Exploration
df_bar = df[df['coupon'] == 'Bar']
df_bar
##2. What proportion of bar coupons were accepted?
if (df_bar['Y'] == 1).any():
    sum_dfbar = df_bar['Y'].sum()
    print(sum_dfbar)
  ##3. Compare the acceptance rate between those who went to a bar 3 or fewer times a month to those who went more.
BarCatgroup = df_bar.groupby('Bar')
BarCatgroup['Y'].sum()

# Selecting rows where a condition is met


  
selected_rows_never = df_bar[df_bar['Bar'] == 'never'] 
selected_rows_less = df_bar[df_bar['Bar'] ==  'less1']
selected_rows_1to3 = df_bar[df_bar['Bar'] == '1~3']

# Grouping selected rows by 'Bar' and summing values in 'Y' column
BarCatgroupnever = selected_rows_never.groupby('Bar')
sum_of_never = BarCatgroupnever['Y'].sum()
BarCatgroupless = selected_rows_less.groupby('Bar')
sum_of_less = BarCatgroupless['Y'].sum()
BarCatgroup1to3 = selected_rows_1to3.groupby('Bar')
sum_of_1to3 = BarCatgroup1to3['Y'].sum()

print(sum_of_never)
print(sum_of_less.dtype)
print(sum_of_1to3.dtype)

Total = sum_of_never.dtype + sum_of_less.dtype + sum_of_1to3.dtype
print(Total)

