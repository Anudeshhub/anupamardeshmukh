##Practical Application Assignment 5.1: Will the Customer Accept the Coupon?
##Execute below code
##Output for this code would give various imported libraries and visualizations

## Python libraries used in the code
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import plotly.express as px
import math


##1. Read in the `coupons.csv` file
df = pd.read_csv('data/coupons.csv')

##Gathering and Describing data
##Summary of dataframe that shows the structure and components of the dataframe
df.info()
df.head()

##Data Preparation and Data Cleansing
# Get unique values from each column
unique_values = {col: df[col].unique() for col in df.columns}
print(unique_values)

##2. Investigate the dataset for missing or problematic data

##print(null_counts) from dataset
total_counts = (df.isna().sum()).sum()
print(total_counts)

## Identify nulls 
df[df['CarryAway'].isnull()].coupon.value_counts()
null_counts = df.isnull().sum()
total_percentage_null = (null_counts / df.size) * 100
total_percentage_null = total_percentage_null[total_percentage_null != 0]
print(total_percentage_null)

# Count the occurrences of each destination for each passenger
destination_counts = df.groupby('passanger')['destination'].value_counts().unstack()
barplot = destination_counts.plot(kind='bar', figsize=(15, 8))
plt.xlabel('passanger')
plt.ylabel('Destination Count')
plt.title('Destination Count for Each Passanger')
plt.legend(title='Destination')
plt.savefig('passanger_destination_barplot.pdf')
##plt.text(-1.2, 1.8, 'Note: Passangers with no company are more likely to go to work more', fontsize=12, ha='top')
plt.show()

##3. Replace NaN WITH 'Never'
## Replaced NaN CarryAway values with 'Never'
df['CarryAway'].fillna('Never', inplace=True)
df['Bar'] = df['Bar'].replace('',0)
df

##4. What proportion of the total observations chose to accept the coupon? 
if (df['Y'] == 1).any():
    sumY = df['Y'].sum()
    print(sumY)

##5. Use a bar plot to visualize the `coupon` column.
couponcounts =  df['coupon'].value_counts()

plt.figure(figsize=(12, 8))
bars = plt.bar(couponcounts.index, couponcounts.values, color='blue')

# Add values on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')

# Add labels
plt.xlabel("Coupon Category")
plt.ylabel("Count")
plt.title("Coupon Category Counts")
plt.show()


##6. Use a histogram to visualize the temperature column.
# Create a histogram using Plotly Express
hist = px.histogram(df, x="temperature", title="Histogram of Temperature",
                    labels={"temperature": "Temperature"}, color="Y",
                    color_discrete_sequence=px.colors.qualitative.Dark24)

# Show the histogram
hist.show()

##Customer acceptances by overall coupon categories 

# Grouping selected rows by 'coupon' and summing values in 'Y' column
couponsaccepted = df.groupby('coupon')['Y'].sum().reset_index()

## Show total count for each coupon group, which accepts coupon
print('couponaccepted')

# Adjusting the size of the plot
plt.figure(figsize=(10, 8))

# Create line plot with switched x and y variables
sns.lineplot(data=couponsaccepted, x='coupon', y='Y', marker='o')

# Add labels to data points
for index, row in couponsaccepted.iterrows():
    plt.text(row['coupon'], row['Y'], str(row['Y']), ha='center', va='bottom')

plt.xlabel('Coupon Type')
plt.ylabel('Number of Coupons Accepted')
plt.title('Overall Coupon acceptances by Coupon categories')

plt.show()

##---------------------------------------------------------------

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
##I can clean the data for 1~3, however, chose to use 'As Is'
 
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
print(sum_of_less)
print(sum_of_1to3)

acceptance_sum = sum_of_never.sum() + sum_of_less.sum() + sum_of_1to3.sum()
print("Acceptance sum for those who went to a bar 3 or fewer times a month:",acceptance_sum )

SumBar = df['Y'].sum()
acceptance_rate = ( acceptance_sum / SumBar ) * 100
print("Acceptance Rate for those who went to a bar 3 or fewer times a month:",acceptance_rate )

# Round up the decimal number to 2 decimal places
import math
acceptance_rate_dec = math.ceil(acceptance_rate * 100) / 100
print(acceptance_rate_dec)  # Output: 2 decimals

##print("Acceptance Rate for those who went to a bar more than 3 times a month:", acceptance_rate_more_than_3)

selected_rows_gr8 = df_bar[df_bar['Bar'] == 'gr8'] 
selected_rows_4to8 = df_bar[df_bar['Bar'] == '4~8']

# Grouping selected rows by 'Bar' and summing values in 'Y' column
BarCatgroupgr8 = selected_rows_gr8.groupby('Bar')
sum_of_gr8 = BarCatgroupgr8['Y'].sum()

BarCatgroup4to8 = selected_rows_4to8.groupby('Bar')
sum_of_4to8 = BarCatgroup4to8['Y'].sum()

print(sum_of_gr8)
print(sum_of_4to8)


acceptance_sum_gr3 = sum_of_gr8.sum() +  sum_of_4to8.sum()
print("Acceptance Sum for those who went to a bar more than 3 times a month:",acceptance_sum_gr3 )

SumBar = df_bar['Y'].sum()
      
acceptance_rate_gr3 = ( acceptance_sum_gr3 / SumBar ) * 100
print("Acceptance Rate  for those who went to a bar more than 3 times a month:",acceptance_rate_gr3 )

# Round up the decimal number to 2 decimal places
acceptance_rate_decgr3 = math.ceil(acceptance_rate_gr3 * 100) / 100
print(acceptance_rate_decgr3)  # Output: 2 decimals
##---------------------------------------------------

##4. Compare the acceptance rate between drivers who go to a bar more than once a month and are over the age of 25 to the all others.  Is there a difference?
 
df_bar25 = df_bar[df_bar['age'] > '25']
    
selected_rows_1to3 = df_bar25[df_bar25['Bar'] == '1~3']
BarCatgroup1to3 = selected_rows_1to3.groupby('Bar')
sum_of_1to3 = BarCatgroup1to3['Y'].sum()

selected_rows_gr8 = df_bar25[df_bar25['Bar'] == 'gr8'] 
selected_rows_4to8 = df_bar25[df_bar25['Bar'] == '4~8']

# Grouping selected rows by 'Bar' and summing values in 'Y' column
BarCatgroupgr8 = selected_rows_gr8.groupby('Bar')
sum_of_gr8 = BarCatgroupgr8['Y'].sum()

BarCatgroup4to8 = selected_rows_4to8.groupby('Bar')
sum_of_4to8 = BarCatgroup4to8['Y'].sum()


acceptance_sum_g25 = sum_of_1to3.sum() + sum_of_gr8.sum() + sum_of_4to8.sum()
print("Acceptance sum for those who went to a bar at least once a month and are over the age of 25:",acceptance_sum_g25 )

SumBar25 = df_bar25['Y'].sum()
acceptance_rate_g25 = ( acceptance_sum_g25 / SumBar25 ) * 100
print("Acceptance Rate for those who went to a bar more than once a month and are over the age of 25:",acceptance_rate )

# Round up the decimal number to 2 decimal places
acceptance_rate_dec = math.ceil(acceptance_rate_g25 * 100) / 100
print(acceptance_rate_dec)  # Output: 2 decimals


##5. Use the same process to compare the acceptance rate between drivers who go to bars more than once a month
##and had passengers that were not a kid and had occupations other than farming, fishing, or forestry ource"

df_barnokid = df_bar[(df_bar['passanger'] != 'Kid(s)') & ((df_bar['occupation'] != 'Farming Fishing & Forestry'))]
    
selected_rows_1to3 = df_barnokid[df_barnokid['Bar'] == '1~3']
BarCatgroup1to3 = selected_rows_1to3.groupby('Bar')
sum_of_1to3 = BarCatgroup1to3['Y'].sum()

selected_rows_gr8 = df_barnokid[df_barnokid['Bar']  == 'gr8'] 
selected_rows_4to8 = df_barnokid[df_barnokid['Bar'] == '4~8']

# Grouping selected rows by 'Bar' and summing values in 'Y' column
BarCatgroupgr8 = selected_rows_gr8.groupby('Bar')
sum_of_gr8 = BarCatgroupgr8['Y'].sum()

BarCatgroup4to8 = selected_rows_4to8.groupby('Bar')
sum_of_4to8 = BarCatgroup4to8['Y'].sum()


acceptance_sum_nokid = sum_of_1to3.sum() + sum_of_gr8.sum() + sum_of_4to8.sum()
print("Acceptance sum for those who went to a bar at least once a month and are not widower:",acceptance_sum_g25 )

SumBar25 = df_bar25['Y'].sum()
acceptance_rate_nokid = ( acceptance_sum_nokid / SumBar25 ) * 100
print("Acceptance Rate for those who went to a bar more than once a month and are not widower:",acceptance_rate )

# Round up the decimal number to 2 decimal places
acceptance_rate_dec = math.ceil(acceptance_rate_g25 * 100) / 100
print(acceptance_rate_dec)  # Output: 2 decimals

##6. Compare the acceptance rates between those drivers who:\n",
##go to bars more than once a month, had passengers that were not a kid, and were not widowed 
df_barnowidow = df_bar[(df_bar['passanger'] != 'Kid(s)') & ((df_bar['maritalStatus'] != 'Widower'))]
    
selected_rows_1to3 = df_barnowidow[df_barnowidow['Bar'] == '1~3']
BarCatgroup1to3 = selected_rows_1to3.groupby('Bar')
sum_of_1to3 = BarCatgroup1to3['Y'].sum()

selected_rows_gr8 = df_barnowidow[df_barnowidow['Bar']  == 'gr8'] 
selected_rows_4to8 = df_barnowidow[df_barnowidow['Bar'] == '4~8']

# Grouping selected rows by 'Bar' and summing values in 'Y' column
BarCatgroupgr8 = selected_rows_gr8.groupby('Bar')
sum_of_gr8 = BarCatgroupgr8['Y'].sum()

BarCatgroup4to8 = selected_rows_4to8.groupby('Bar')
sum_of_4to8 = BarCatgroup4to8['Y'].sum()


acceptance_sum_nowidower = sum_of_1to3.sum() + sum_of_gr8.sum() + sum_of_4to8.sum()
print("Acceptance sum for those who went to a bar at least once a month,  and are no kids and not widower:",acceptance_sum_nowidower )


##go to bars more than once a month and are under the age of 30 

df_barageless30 = df_bar[(df_bar['age'] < '30') | (df_bar['age'] == 'below21')]
    
selected_rows_1to3 = df_barageless30[df_barageless30['Bar'] == '1~3' ]
BarCatgroup1to3 = selected_rows_1to3.groupby('Bar')
sum_of_1to3 = BarCatgroup1to3['Y'].sum()

selected_rows_gr8 = df_barageless30[df_barageless30['Bar']  == 'gr8'] 
selected_rows_4to8 = df_barageless30[df_barageless30['Bar'] == '4~8']

# Grouping selected rows by 'Bar' and summing values in 'Y' column
BarCatgroupgr8 = selected_rows_gr8.groupby('Bar')
sum_of_gr8 = BarCatgroupgr8['Y'].sum()

BarCatgroup4to8 = selected_rows_4to8.groupby('Bar')
sum_of_4to8 = BarCatgroup4to8['Y'].sum()


acceptance_sum_less30 = sum_of_1to3.sum() + sum_of_gr8.sum() + sum_of_4to8.sum()
print("Acceptance sum for those who went to a bar at least once a month and age below 30:",acceptance_sum_less30 )

##go to cheap restaurants more than 4 times a month and income is less than 50K
df_barincome = df_bar[((df_bar['RestaurantLessThan20'].isin(['1~3', '4~8', 'gt8'])) &
                       (df_bar['income'].isin(['$37500 - $49999', '$12500 - $24999', '$25000 - $37499'])))]

selected_rows_1to3 = df_barincome[df_barincome['Bar'] == '1~3' ]
BarCatgroup1to3 = selected_rows_1to3.groupby('Bar')
sum_of_1to3 = BarCatgroup1to3['Y'].sum()

selected_rows_gr8 = df_barincome[df_barincome['Bar']  == 'gr8'] 
selected_rows_4to8 = df_barincome[df_barincome['Bar'] == '4~8']

# Grouping selected rows by 'Bar' and summing values in 'Y' column
BarCatgroupgr8 = selected_rows_gr8.groupby('Bar')
sum_of_gr8 = BarCatgroupgr8['Y'].sum()

BarCatgroup4to8 = selected_rows_4to8.groupby('Bar')
sum_of_4to8 = BarCatgroup4to8['Y'].sum()


acceptance_sum_df_barincome = sum_of_1to3.sum() + sum_of_gr8.sum() + sum_of_4to8.sum()
print("Acceptance sum for those who went to a bar at least once a month and income < 50k:",acceptance_sum_df_barincome )

## Define the categories and their corresponding sums
categories = ['Nokid_NoWidower', 'Age<30', 'Income < 50K']
sums = (acceptance_sum_nowidower, acceptance_sum_less30, acceptance_sum_df_barincome)

# Create the bar plot
plt.figure(figsize=(10, 6))
plt.bar(categories, sums, color=['blue', 'orange', 'green'])

# Add labels and title
plt.xlabel('Bar Category')
plt.ylabel('Acceptance Sum')
plt.title('Acceptance Sum for Cheap Restaurant Visitors with Income <$50k')


# Show the plot
plt.show()


##7.  Based on these observations, what do you hypothesize about drivers who accepted the bar coupons?
### Independent Investigation\n",
##"Using the bar coupon example as motivation, you are to explore one of the other coupon groups and 
##try to determine the characteristics of passengers who accept the coupons.  "
import seaborn as sns

# Filter DataFrame to include only rows where 'coupon' is not 'Bar'
df_nobar = df[df['coupon'] != 'Bar']

# Calculate the sum of 'Y' for the filtered DataFrame
sum_dfnobar = df_nobar['Y'].sum()


# Adjusting the size of the plot
plt.figure(figsize=(10, 8))

# Visualize the proportion of accepted coupons using a histogram
sns.histplot(data=df_nobar, x='coupon', hue='Y', multiple='stack')

# Add labels and legend
plt.xlabel('Coupon Categories')
plt.ylabel('Count')
plt.title('Coupon accepted by counts')

plt.show()


###Additional details
expiration2h = df[(df['expiration'] == '2h') & (df['Y'] == 1)]
expiration1d = df[(df['expiration'] == '1d') & (df['Y'] == 1)]

counts_2h = expiration2h['expiration'].value_counts()
counts_1d = expiration1d['expiration'].value_counts()

# Plot the counts as a bar plot
bar_2h = plt.bar(counts_2h.index, counts_2h.values, color='blue', label='2h')
bar_1d = plt.bar(counts_1d.index, counts_1d.values, color='red', label='1d')

# Add values on the bars
for bar in bar_1d:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, yval, va='bottom', ha='center')

# Add values on the bars
for bar in bar_2h:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, yval, va='bottom', ha='center')

# Add labels and legend
plt.xlabel('Expiration')
plt.ylabel('Count')
plt.title('Coupon counts by Expiry Details')
plt.legend()

# Show the plot
plt.show()



