import pandas as pd
import numpy as np

# # FIRST CLASS

# Creating a data frame:

# df_1 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(df_1)
# print(df_1.info())         #To see table's info
# print(df_1.describe())     #Gives values of basic operations
# print(df_1.shape)          #To get the shapes of the data frame
# print(df_1.size)           #To get the number of elements

# print(df_1.head())  #To see first five rows
# print(df_1.head(1)) #To see first row
# print(df_1.head(2)) #To see first two rows
# print(df_1.tail())  #To see last five rows
# print(df_1.tail(1)) #To see last row

# Adding custom columns and index values to our data frame:

# df_2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["A", "B", "C"], index=["x", "y", "z"])
# print(df_2)
# print(df_2.columns)        #To see the column names
# print(df_2.index)          #To see the index/row names
# print(df_2.index.tolist()) #To just see the values without extra info

# print(df_2.nunique())      #To see number of unique values in each column
# print(df_2["A"].unique())  #To see unique values by column name


# # LOADING DATA FROM FILES

# CSV:

# coffee = pd.read_csv("Pandas\Data\coffee.csv")
# print(coffee)
# print(coffee.sample(5)) #Get five random values

# EXCEL:

# olympics = pd.read_excel("Pandas\Data\olympics-data.xlsx") #Reads the default sheet 1
# print(olympics)

# olympics_result = pd.read_excel("Pandas\Data\olympics-data.xlsx", sheet_name="results")  # Reads the default sheet 1
# print(olympics_result)

# PARQUET:
# result = pd.read_parquet(r'Pandas\Data\results.parquet')
# print(result)


# # SECOND CLASS

# coffee = pd.read_csv("Pandas\Data\coffee.csv")

# loc & iloc
# loc filters data by rows and columns names:
# print(coffee.loc[0])
# print(coffee.loc[[0,1,5]])
# print(coffee.loc[5:12])
# print(coffee.loc[5:12, "Day"])
# print(coffee.loc[0:5, ["Day", "Units Sold"]])

# iloc filters data by rows and columns index values:
# print(coffee.iloc[0:5, [0,2]])


# at & iat: To get single values only
# print(coffee.at[0, "Units Sold"])
# print(coffee.iat[0,2])


# Change the index to something from the column name
# coffee.index = coffee["Day"]
# print(coffee)

# Now loc by numeric values wont work cause indexes are Day names
# print(coffee.loc["Monday"])
# print(coffee.loc["Monday":"Wednesday"])

# Changing values in data frames
# coffee.iloc[0, 2] = 10
# print(coffee)

# Just to get a column
# print(coffee["Day"])

# Sorting values
# print(coffee.sort_values("Units Sold"))
# print(coffee.sort_values("Units Sold", ascending=False))

# To loop over a dataframe
# for i in coffee.iterrows():
#     print(i)


# Filtering Data:

# bios = pd.read_csv(r"Pandas\Data\bios.csv")
# print(bios)
# print(bios.info())
# print(bios.loc[bios["height_cm"] > 215])
# print(bios.loc[bios["height_cm"] > 215, ["name", "height_cm"]])

# For multiple conditions
# print(bios.loc[(bios["height_cm"] > 215) & (bios["weight_kg"] < 100)])
# print(bios.loc[(bios["height_cm"] > 215) & (bios["born_country"]=="USA")])
# print(bios.loc[bios['name'].str.contains("Himanshu")])
# print(bios.loc[bios['name'].str.contains("Himanshu",case=False)])

# print(bios.loc[bios['born_country'].isin(["USA","IND","GBR"])])
# print(bios.loc[(bios['born_country'].isin(["USA","IND","GBR"]))& (bios['name'].str.startswith("Jack"))])

# # THIRD CLASS

# bios = pd.read_csv(r"Pandas\Data\bios.csv")

# But this is repeatitive so for only one condition we can also use:

# print(bios.query('born_country=="USA"'))
# print(bios.query('born_country=="USA" and name.str.contains("Jack")'))
# print(bios.query('born_country=="IND"'))


# Adding/Removing/Renaming in DataFrame:

# coffee = pd.read_csv("Pandas\Data\coffee.csv")

# To add something:
# coffee["Price"] = 4.99                      # Adds a column but this column have fixed value for all rows
# print(coffee)
# coffee.loc[14] = ["Sunday", "Espresso", 45] # Adds a row
# print(coffee)

# To add conditional values in a column
# coffee["New_Price"] = np.where(coffee["Coffee Type"] == "Espresso", 3.99, 5.99)
#                   Adds a column with condition that is if true then: x else: y
# print(coffee)

# To add a column with some formula

# coffee["New_Price"] = np.where(coffee["Coffee Type"] == "Espresso", 3.99, 5.99)
# print(coffee)
# coffee['Revenue'] = coffee['Units Sold'] * coffee['New_Price']
# print(coffee)

# To remove something:
# print(coffee.drop(0))                  # Removed the first row, Uses rows by default
# print(coffee.drop(columns=["Price"]))  # Removed the column Price

# coffee.drop(columns=["Price"])         # But the changes arent permanent in coffee so for that we do inplace=True
# print(coffee)

# coffee.drop(columns=["Price"], inplace=True)
# print(coffee)

# To rename a column:
# coffee.rename(columns={'New_Price':'Price'},inplace=True)
# print(coffee)


# View and Copy

# View:
# coffee_new = coffee
# coffee["Price"] = 4.99
# print(coffee_new)

# We see changes in coffee_new too cause its a view not copy

# Copy:
# coffee_new = coffee.copy()
# coffee["Price"] = 4.99
# print(coffee_new)


# Creating a column of only first names
# bios = pd.read_csv(r"Pandas\Data\bios.csv")
# bios["First_Name"] = bios["name"].str.split(" ").str[0]
# print(bios)

# To work with dates:

# print(bios.info())                                        # Date column is an object
# bios["Born_DateTime"] = pd.to_datetime(bios["born_date"]) # Creating a new column with converted data type
# print(bios.info())
# print(bios)
# bios['born_date'] = pd.to_datetime(bios['born_date'])     # Changing datatype of the same column
# print(bios.info())
# bios["Year"] = bios["Born_DateTime"].dt.year              # Adding the year column
# print(bios)


# To save a file:
# bios.to_csv(r"Pandas\Data\bios_new.csv", index=False)


# # FOURTH CLASS

# bios = pd.read_csv(r"Pandas\Data\bios.csv")

# Adding a custom column:

# def categorize_athlete(row):
#     if row['height_cm'] < 155:
#         return 'Short'
#     elif row['height_cm'] < 170:
#         return 'Average'
#     else:
#         return 'Tall'

# bios['Category'] = bios.apply(categorize_athlete, axis=1) # To use a function
# print(bios)

# To create other dataframes based on certain conditions:

# bios = pd.read_csv(r"Pandas\Data\bios.csv")
# usa = bios.loc[bios["born_country"] == "USA"].copy() # Ask them why we used copy?
# gbr = bios.loc[bios["born_country"] == "GBR"].copy()
# print(usa)
# print(gbr)

# Concating dataframes: Adding top to bottom

# new_df = pd.concat([usa, gbr])
# print(new_df)


# Merging data:

# nocs = pd.read_csv(r'Y:\CS\Pandas\Data\noc_regions.csv')
# print(nocs)
# Merging column with born country matched with NOC to get the full region name
# bios_new = pd.merge(bios, nocs, left_on='born_country', right_on='NOC')
# print(bios_new)


# Aggregating Functions:

# Counting values top to bottom
# print(bios['born_city'].value_counts())
# print(bios[bios['born_country']=='IND']['born_city'].value_counts())

# Group By
# coffee = pd.read_csv("Pandas\Data\coffee.csv")
# print(coffee.groupby(['Coffee Type'])['Units Sold'].sum())
# print(coffee.groupby(["Coffee Type"])["Units Sold"].mean())

# Aggregating Data
# coffee["Price"] = np.where(coffee["Coffee Type"] == "Espresso", 3.99, 5.99)
# print(coffee.groupby(["Day"]).agg({"Units Sold": "sum", "Price": "mean"}).reset_index()) # To add an additional index column
# print(coffee.groupby(["Coffee Type"]).agg({"Units Sold": "sum", "Price": "mean"}))
# print(coffee.groupby(["Coffee Type","Day"]).agg({"Units Sold": "sum", "Price": "mean"}))
# print(coffee.groupby(["Coffee Type","Day"]).agg({"Units Sold": "sum"}))


# # FIFTH CLASS

# Advanced topic:Using Pivot to do the last same thing:

# coffee_pivot = coffee.pivot(columns='Coffee Type',index='Day',values='Units Sold')
# print(coffee_pivot)
# print(coffee_pivot.sum())
# print(coffee_pivot.sum(axis=1))

# Counting by year, Diff from value_counts(), value_counts displays the values(only works on 1 column) while count(multiple columns) gives out a number
# bios = pd.read_csv(r"Pandas\Data\bios.csv")
# bios['born_date'] = pd.to_datetime(bios['born_date'])                               # Changing datatype of the same column
# print(bios.info())
# print(bios.groupby(bios['born_date'].dt.year).count())                              # Displays count of every column
# print(bios.groupby(bios['born_date'].dt.year)['name'].count().reset_index())        # Adds a index column at the beginning and only shows the name column
# print(bios.groupby(bios['born_date'].dt.year)['name'].value_count().reset_index())  # Shows value count of name column
# bios['born_year'] = bios['born_date'].dt.year                                       # To get the same result as count we have to add a column year
# print(bios.groupby(bios['born_year'])['born_year'].value_counts().reset_index())    # Now we can count the values of this column
# print(bios.groupby(bios["born_date"].dt.year)["name"].count().reset_index().sort_values('name', ascending=False))


# Handling Null Values:

# coffee = pd.read_csv("Pandas\Data\coffee.csv")
# coffee.loc[[2, 3], "Units Sold"] = np.nan
# print(coffee.head())
# print(coffee.info())

# Filling it with a value
# coffee.fillna(100,inplace=True)
# print(coffee.head())

# Filling it with a realistic value
# coffee.fillna(coffee['Units Sold'].mean(),inplace=True) #Fills it with an avg value
# print(coffee.head())

# Using interpolate: Fills it using a pattern
# coffee['Units Sold'] = coffee['Units Sold'].interpolate()
# print(coffee)

# To delete nan rows
# coffee.dropna(inplace=True)
# coffee.dropna(subset=['Units Sold'],inplace=True)
# print(coffee)

# To see the nan rows
# print(coffee['Units Sold'].isna())
# print(coffee[coffee["Units Sold"].isna()])

# opposite of it is notna
# print(coffee[coffee["Units Sold"].notna()])


# Optional to teach-Advanced Topics:

# 1.shift: Adds a column which shows the diff b/w prev and current value, can also shift back using negative values
# coffee = pd.read_csv(r"Y:\CS\Pandas\Data\coffee.csv")
# coffee["Price"] = np.where(coffee["Coffee Type"] == "Espresso", 3.99, 5.99)
# coffee["Revenue"] = coffee["Units Sold"] * coffee["Price"]
# coffee["Yesterday_Revenue"] = coffee["Revenue"].shift(2)
# print(coffee)
# coffee["Percent Change"] = coffee["Revenue"] * 100 / coffee["Yesterday_Revenue"]
# print(coffee)

# 2.rank: Adds a column which gives rank based on a certain column
# bios= pd.read_csv(r'Y:\CS\Pandas\Data\bios.csv')
# bios['Height Rank'] = bios['height_cm'].rank(ascending=False)
# print(bios.sort_values(['Height Rank']))

# 3.cumsum
# coffee = pd.read_csv(r'Y:\CS\Pandas\Data\coffee.csv')
# coffee["Price"] = np.where(coffee["Coffee Type"] == "Espresso", 3.99, 5.99)
# coffee["Revenue"] = coffee["Units Sold"] * coffee["Price"]
# coffee["Cumulative Revenue"] = coffee["Revenue"].cumsum()
# print(coffee)
