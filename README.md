<div class="rendered-markdown"><h1>Case Study - Whether Customer Accepts the Coupon</h1>
<h2>Use CRISP-DM model to find out Effectiveness of promoting coupons</h2>
<h3>1 Business Understanding</h3>
<h3>1.1 Background</h3>
<p>ABC company is providing their truck drivers with coupons as one of the employee incentive programs. They are analyzing the demographics and utility of this program,
<br  />based on usage of different categories of coupons. The objective of this analysis is to determine the factors that effects use of coupons. Based on the acceptance rate,
<br  />new categories of coupons can be included, increasing the effectiveness of the program or discontinue all or certain category of coupons.</p>
<p>Summary of business problem:
<br  />-Do not have correct metrics to analyze the fact that coupons are used efficiently across all the categories.</p>
<ul>
<li>Unable to identify factors influencing usage of coupons.</li>
</ul>
<h2>1.2 Business Goals and KPI</h2>
<p>The business goal is to determine the effectiveness of this program provided by ABC company and to make strategic decision to continue or discontinue this program</p>
<ul>
<li>Provide valuable insights into the effectiveness of the program in driving desired Behaviors among drivers. By understanding the correlation between coupon usage and customer behavior</li>
<li>Enhance employee engagement, motivation, and overall job satisfaction.</li>
<li>ABC Company will be better equipped to tailor future promotional efforts and incentives, ultimately fostering a more rewarding and productive work environment for its truck drivers</li>
</ul>
<h2>1.2 Data Mining Goals and KPI</h2>
<p>Build and analyze the data sets and build KPI’s that aligns with business goals.</p>
<ul>
<li>Identify patterns and trends in coupon usage data</li>
<li>Determine the factors influencing coupon acceptance.</li>
<li>Provide actionable insights to improve the effectiveness of the coupon program2 Data Understanding</li>
</ul>
<p>We have analyzed the data set using coupon.csv file and made sure the dataset contains data and metadata required for this analysis and achieve business goals</p>
<h2>2 Data Understanding</h2>
<p>‘Coupons.csv’ data file consists of 12684 rows and 26 columns. Data is collected in the form of .csv file and is in the tabular format.
<br  />I have used pandas library and DataFrame named df. Then, the .info() method is called on the DataFrame to display a summary of its structure and components,
<br  />including the number of rows and columns, column names, non-null counts, and data types of each column.</p>
<h2>2.1Gathering and Describing Data</h2>
<p>The data consists of various attributes, like destination, coupon, temperature, age, income etc and flag that shows if the coupons are accepted based on these attributes.
<br  />Following python libraries are used :</p>
<h2>use necessary libraries in the code</h2>
<p>import matplotlib.pyplot as plt
<br  />import seaborn as sns
<br  />import pandas as pd
<br  />import numpy as np
<br  />import plotly.express as px</p>
<h2>1. Read in the <code>coupons.csv</code> file</h2>
<p>df = pd.read_csv('data/coupons.csv')</p>
<h2>Summary of dataframe that shows the structure and components of the dataframe</h2>
<p>df.info()</p>
<p>The data consists of various attributes, like destination, coupon, temperature, age, income etc and flag that shows if the coupons are accepted based on these attributes.
<br  />Following python libraries are used :</p>
<h2>use necessary libraries in the code</h2>
<p>import matplotlib.pyplot as plt
<br  />import seaborn as sns
<br  />import pandas as pd
<br  />import numpy as np
<br  />import plotly.express as px</p>
<h2>1. Read in the <code>coupons.csv</code> file</h2>
<p>df = pd.read_csv('data/coupons.csv')</p>
<h2>Summary of dataframe that shows the structure and components of the dataframe</h2>
<p>df.info()</p>
<img width="782" src="https://raw.githubusercontent.com/Anudeshhub/anupamardeshmukh/6f3bf518087f17f00bf2af027a7b7893df194b14/Picture1.png" alt="Picture1">
<br  />•   The number of rows (each row represent a single customer data)  : 12684
<br  />•   The number of column :  26
<br  />•   The name of each column
<br  />•   The data type of each column</p>
<p>df.info()
<br  />Data columns (total 26 columns):</p>
<h1>Column                Non-Null Count  Dtype</h1>
<hr />
<p>    0        destination           12684      non-null       object
<br  />1        passanger             12684      non-null       object
<br  />2        weather               12684      non-null       object
<br  />3        temperature           12684      non-null       int64
<br  />4        time                  12684      non-null       object
<br  />5        coupon                12684      non-null       object
<br  />6        expiration            12684      non-null       object
<br  />7        gender                12684      non-null       object
<br  />8        age                   12684      non-null       object
<br  />9        maritalStatus         12684      non-null       object
<br  />10        has_children          12684     non-null       int64
<br  />11        education             12684     non-null       object
<br  />12        occupation            12684     non-null       object
<br  />13        income                12684     non-null       object
<br  />14        car                   108       non-null       object
<br  />15        Bar                   12577     non-null       object
<br  />16        CoffeeHouse           12467     non-null       object
<br  />17        CarryAway             12533     non-null       object
<br  />18        RestaurantLessThan20  12554     non-null       object
<br  />19        Restaurant20To50      12495     non-null       object
<br  />20        toCoupon_GEQ5min      12684     non-null       int64
<br  />21        toCoupon_GEQ15min     12684     non-null       int64
<br  />22        toCoupon_GEQ25min     12684     non-null       int64
<br  />23        direction_same        12684     non-null       int64
<br  />24        direction_opp         12684     non-null       int64
<br  />25        Y                     12684     non-null       int64</p>
<p>2.2 Data Preparation and Data Cleansing</p>
<h1>Get unique values from each column</h1>
<p>unique_values = {col: df[col].unique() for col in df.columns}
<br  />print(unique_values)</p>
<p>destination       :      'No Urgent Place', 'Home', 'Work'
<br  />passanger     :      'Alone', 'Friend(s)', 'Kid(s)', 'Partner'
<br  />weather       :      'Sunny', 'Rainy', 'Snowy'
<br  />temperature   :       55, 80, 30
<br  />time          :      '2PM', '10AM', '6PM', '7AM', '10PM'
<br  />coupon        :      'Restaurant(&lt;20)', 'Coffee House', 'Carry out &amp; Take away',</p>
<pre><code>                  'Bar','Restaurant(20-50)'
</code></pre>
<p>Expiration        :      '1d', '2h'
<br  />Gender        :      'Female', 'Male'
<br  />Age           :      '21', '46', '26', '31', '41', '50plus', '36', 'below21'
<br  />maritalStatus :      'Unmarried partner', 'Single', 'Married partner',</p>
<pre><code>                 'Divorced', 'Widowed'
</code></pre>
<p>has_children      :      1, 0
<br  />…etc</p>
<h2>2. Investigate the dataset for missing or problematic data</h2>
<h2>print(null_counts) from dataset</h2>
<p>total_counts = (df.isna().sum()).sum()
<br  />print(total_counts)</p>
<p>13219</p>
<h2>Identify nulls</h2>
<p>df[df['CarryAway'].isnull()].coupon.value_counts()
<br  />null_counts = df.isnull().sum()
<br  />total_percentage_null = (null_counts / df.size) * 100
<br  />total_percentage_null = total_percentage_null[total_percentage_null != 0]
<br  />print(total_percentage_null)</p>
<p>car                     3.813405
<br  />Bar                     0.032445
<br  />CoffeeHouse             0.065801
<br  />RestaurantLessThan20    0.039420
<br  />Restaurant20To50        0.057310
<br  />dtype: float64</p>
<h2>3. Replace NaN WITH 'Never'</h2>
<h2>Replaced NaN CarryAway values with 'Never'</h2>
<p>df['CarryAway'].fillna('Never', inplace=True)
<br  />df['Bar'] = df['Bar'].replace('',0)
<br  />df</p>
<img width="782" src="https://raw.githubusercontent.com/Anudeshhub/anupamardeshmukh/6f3bf518087f17f00bf2af027a7b7893df194b14/Picture2.png" alt="Picture2"><pre><code>  ## Investigate the dataset for missing or problematic data
     df[df['CarryAway'].isnull()].coupon.value_counts()

     Coffee House             57
   Restaurant(&lt;20)          34
   Bar                      24
   Carry out &amp; Take away    22
   Restaurant(20-50)        14
</code></pre>
<p>What proportion of bar coupons were accepted?  827
<br  />if (df_bar['Y'] == 1).any():</p>
<pre><code>sum_dfbar = df_bar['Y'].sum()
print(sum_dfbar)
</code></pre>
<p>7210</p>
<h6></h6>
<p>Decide what to do about your missing data –
<br  />replaced space with ‘Never’</p>
<pre><code>## Replaced NaN CarryAway values with 'Never'
df['CarryAway'].fillna('Never', inplace=True)
df['Bar'] = df['Bar'].replace('',0)
</code></pre>
<img width="782" src="https://raw.githubusercontent.com/Anudeshhub/anupamardeshmukh/6f3bf518087f17f00bf2af027a7b7893df194b14/Picture3.png" alt="Picture3"><ol>
<li>Exploratory data analysis and Visualizations
<br  />What proportion of the total observations chose to accept the coupon?
<br  />7210 total coupons were accepted by combining all the attributes</li>
</ol>
<h2>5. Use a bar plot to visualize the <code>coupon</code> column.</h2>
<p>couponcounts =  df['coupon'].value_counts()</p>
<p>plt.figure(figsize=(12, 8))
<br  />bars = plt.bar(couponcounts.index, couponcounts.values, color='blue')</p>
<h1>Add values on top of the bars</h1>
<p>for bar in bars:</p>
<pre><code>yval = bar.get_height()
plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')
</code></pre>
<h1>Add labels</h1>
<p>plt.xlabel(&ldquo;Coupon Category&rdquo;)
<br  />plt.ylabel(&ldquo;Count&rdquo;)
<br  />plt.title(&ldquo;Coupon Category Counts&rdquo;)
<br  />plt.show()</p>
<img width="782" src="https://raw.githubusercontent.com/Anudeshhub/anupamardeshmukh/6f3bf518087f17f00bf2af027a7b7893df194b14/Picture4.png" alt="Picture4"><p>Bar Plot is used to visualize Counts by Coupon Category</p>
<img width="782" src="https://raw.githubusercontent.com/Anudeshhub/anupamardeshmukh/6f3bf518087f17f00bf2af027a7b7893df194b14/Picture5.png" alt="Picture5"><p>Observation: The coupons for ‘Coffee house’ are mostly accepted</p>
<p>Use a histogram to visualize the temperature column.
<img width="782" src="https://raw.githubusercontent.com/Anudeshhub/anupamardeshmukh/6f3bf518087f17f00bf2af027a7b7893df194b14/Picture6.png" alt="Picture6"><p>Observation : Coupons are accepted more when temperature is high</p>
<p>Customer acceptances by overall coupon categories
<img width="782" src="https://raw.githubusercontent.com/Anudeshhub/anupamardeshmukh/6f3bf518087f17f00bf2af027a7b7893df194b14/Picture7.png" alt="Picture7"><br  />Observation :  Less priced coupons are more accepted, Coffee House and less expensive restaurants.
<br  />Compare the acceptance rate between those who went to a bar 3 or fewer times a month to those who went more.
<br  />BarCatgroup = df_bar.groupby('Bar')
<br  />BarCatgroup['Y'].sum()</p>
<p>Bar
<br  />1~3      257
<br  />4~8      117
<br  />gt8       36
<br  />less1    253
<br  />never    156</p>
<h1>Selecting rows where a condition is met</h1>
<h2>I can clean the data for 1~3, however, chose to use 'As Is'</h2>
<p>Acceptance sum for those who went to a bar 3 or fewer times a month: 666
<br  />Acceptance Rate for those who went to a bar 3 or fewer times a month: 9.237170596393897
<br  />Acceptance Rate for those who went to a bar 3 or fewer times a month rounded to 2 decimals : 9.24</p>
<p>Acceptance rate between drivers who go to bars more than once a month</p>
<h2>and had passengers that were not a kid and had occupations other than</h2>
<p>farming, fishing, or forestry source&rdquo;</p>
<p>Acceptance sum: 374
<br  />Acceptance Rate : 45.223700120918984
<br  />Acceptance Rate (rounded to 2 decimals) 45.23</p>
<p>acceptance rates between those drivers who go to bars more than once a month, had passengers that were not a kid, and were not widowed and are under the age of 30 and go to cheap restaurants more than 4 times a month and income is less than 50K</p>
<p>Acceptance sum[Several conditions']: 374
<br  />Acceptance Rate['Several conditions'] : 45.223700120918984
<br  />45.23</p>
<p>Coupon counts by Expiry Details</p>
<img width="782" src="https://raw.githubusercontent.com/Anudeshhub/anupamardeshmukh/6f3bf518087f17f00bf2af027a7b7893df194b14/Picture8.png" alt="Picture8"><br  />Observation:  Coffee House restraint coupons get more expired quickly, hence, utilized more by the customers</p>
<img width="782" src="https://raw.githubusercontent.com/Anudeshhub/anupamardeshmukh/6f3bf518087f17f00bf2af027a7b7893df194b14/Picture9.png" alt="Picture9"><h2>Conclusion:</h2>
<p>Based on the observations,</p>
<ul>
<li>More coupons expire in a day</li>
<li>Passengers go to Coffee House and Cheaper restaurants more than other categories</li>
<li>More coupons are used when temperature is low</li>
<li>More Females (50 Pus) buy coupons than Males</li>
<li>Passengers with no kids and having company tend to buy more Bar coupons</li>
<li>Passengers who are alone tend to go to work more and drive cars</li>
</ul>
<p>Recommendations
<br  />Based on demographics, Coffee House and Cheaper restaurant coupons are used, based on various demographics. These coupons can be continued to be given by the company.
<br  />Coupons for expensive restaurants can be discontinued, as the usage is low
<br  />Temperature has huge influence on the coupon usage. More coupons can be sent on days when the temperatures are low and that too for Coffee house.</p>
</div>
