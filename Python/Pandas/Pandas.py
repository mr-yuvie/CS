import pandas as pd

# df_1 = pd.DataFrame([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
# print(df_1)
# print(df_1.head()) #Starting 5 lines
# print(df_1.tail()) #Last 5 lines
# print(df_1.head(10))
# print(df_1.tail(1))

# print(df_1.info())
# print(df_1.describe())

# df_2 = pd.DataFrame([[1, 2], [3, 4], [3, 6]], columns=["A", "B"], index=["x", "y", "z"])
# print(df_2)

# print(df_2.index)
# print(df_2.columns.tolist())
# print(df_2.info())
# print(df_2.describe()) #Basic Information

# print(df_2.nunique())
# print(df_2["B"].unique())

# print(df_2.shape)
# print(df_2.size)

# print(coffee)

# olympics_bios = pd.read_excel("Y:\CS\Python\Pandas\Data\olympics-data.xlsx", sheet_name="bios")
# olympics_results = pd.read_excel("Y:\CS\Python\Pandas\Data\olympics-data.xlsx", sheet_name="results")
# print(olympics_bios)

# results = pd.read_feather(r"Y:\CS\Python\Pandas\Data\results.feather")
# print(results)

# results_2 = pd.read_parquet(r"Data\data\results.parquet")
# print(results_2)


## Loc and Iloc
# coffee = pd.read_csv("Y:\CS\Python\Pandas\Data\coffee.csv")
# print(coffee)
# print(coffee.loc[5:12, ["Day"]])
# print(coffee.iloc[5:12,[0]])

# print(coffee.loc[0:5, ["Day", "Units Sold"]])
# print(coffee.iloc[0:5, [0,2]])

# coffee.index = coffee["Day"]
# print(coffee)
# print(coffee.loc[["Monday", "Tuesday"],["Units Sold"]])

# print(coffee.loc["Monday"])
# coffee.iloc[0,2] = 10
# print(coffee)
# print(coffee["Day"])
# print(coffee.iloc[:,0])
# print(coffee)
# print(coffee.sort_values("Units Sold"))
# print(coffee.sort_values("Units Sold", ascending=False))

# print(coffee.at["Monday", "Units Sold"])
# print(coffee.iat[0,2])

# print(coffee.iterrows())

# for i in coffee.iterrows():
#     print(i)

# bios = pd.read_csv(r"Y:\CS\Python\Pandas\Data\bios.csv")
# print(bios)
# print(bios.info())

# print(bios.loc[bios["height_cm"] > 215, ["height_cm","name"]])
# print(bios.loc[(bios["height_cm"] > 215) & (bios["weight_kg"] <100)])
# print(bios.loc[(bios["height_cm"] > 215) & (bios["born_country"]=="AUS")])

# print(bios.loc[bios['name'].str.contains("Riya",case=False)])
# print(bios.loc[bios['name'].str.startswith("Riya")])
# print(bios.loc[bios['name'].str.endswith("Williams")])
# print(bios["born_country"])
# print(bios.loc[bios["born_country"].isin(["IND","FRA"])])
# print(bios.loc[bios["born_country"] == "IND"])
# print(bios.loc[(bios['born_country'].isin(["USA","IND","GBR"]))& (bios['name'].str.startswith("Jack"))])

# print(bios.query('born_country=="IND" and name.str.startswith("Anand")'))

# Add or Remove Columns
# coffee = pd.read_csv("Y:\CS\Python\Pandas\Data\coffee.csv")
# print(coffee)

# Conditional Statments
# import numpy as np

# coffee.loc[14] = ["Sunday", "Espresso", 45]
# coffee["New_Price"] = np.where(coffee["Coffee Type"] == "Espresso", 3.99, 5.99)
# coffee["Price"] = 4.99
# if true then: x, else: y
# coffee["Revenue"] = coffee["Units Sold"] * coffee["New_Price"]
# coffee.loc[2,'Units Sold'] = 45
# print(coffee)

# print(coffee.drop(0))
# print(coffee.drop(columns=["Price"]))
# coffee.drop(0, inplace=True)
# coffee.drop(columns=["Price"], inplace=True)
# coffee.rename(columns={"New_Price": "Price"}, inplace=True)
# print(coffee)

# coffee.to_csv(r"Y:\CS\Python\Pandas\Data\coffe_new.csv",index=False)

# view and Copy

# View
# coffee_new = coffee
# coffee["Price"] = 4.99
# print(coffee_new)

# Copy
# coffee_new_2 = coffee.copy()
# coffee["Data"] = 1
# print(coffee)
# print(coffee_new_2)

# print(coffee)
# coffee['Revenue'] = coffee['Units Sold'] * coffee['New_Price']
# # print(coffee)
# coffee.rename(columns={"New_Price":"Price"},inplace=True)
# print(coffee)

# bios = pd.read_csv(r"Y:\CS\Python\Pandas\Data\bios.csv")

# First name sorting

# bios['First Name'] = bios['name'].str.split(" ").str[0]
# print(bios)

# print(bios.info())

# bios["DateTime"]= pd.to_datetime(bios['born_date'])
# print(bios.info())

# bios['Year']= bios['DateTime'].dt.year
# print(bios)

# bios = pd.read_csv(r"Y:\CS\Python\Pandas\Data\bios.csv")

# def categorize_athlete(row):
#     if row['height_cm'] < 155:
#         return 'Short'
#     elif row['height_cm'] < 170:
#         return 'Average'
#     else:
#         return 'Tall'

# bios['height_category'] = bios.apply(categorize_athlete, axis=1)
# print(bios)

# bios.to_csv(r"Y:\CS\Pandas\Data\data\bios1.csv")

# ind = bios.loc[bios['born_country']=='IND'].copy()
# usa = bios.loc[bios["born_country"] == "USA"].copy()
# print(ind,usa)

# new_df = pd.concat([ind,usa])
# print(new_df)
# new_df.to_csv(r'Y:\CS\Pandas\Data\new_df.csv')

# Merging Data
# nocs = pd.read_csv(r'Y:\CS\Python\Pandas\Data\noc_regions.csv')
# print(bios)
# print(nocs)
# bios_new = pd.merge(bios, nocs, left_on='born_country', right_on='NOC')
# print(bios_new)

# Aggregate functions

# Counting
# print(bios[bios["born_country"] == "IND"]["born_city"].value_counts())

# coffee = pd.read_csv("Y:\CS\Pandas\Data\coffee.csv")

# print(coffee.head())
# print(coffee.groupby(["Coffee Type"])["Units Sold"].sum())
# print(coffee.groupby(["Coffee Type"])["Units Sold"].mean())

# import numpy as np
# coffee["Price"] = np.where(coffee["Coffee Type"] == "Espresso", 3.99, 5.99)
# print(coffee)
# print(coffee.groupby(['Coffee Type']).agg({'Units Sold':'sum'}))
# print(coffee.groupby(['Day']).agg({'Units Sold':'sum'})) #{'Column name':'Agg function'}
# print(coffee.groupby(['Coffee Type','Day']).agg({'Units Sold':'sum'}))

# coffee_pivot = coffee.pivot(columns="Coffee Type",index="Day",values="Units Sold")
# print(coffee_pivot.sum())


# bios= pd.read_csv(r"Y:\CS\Pandas\Data\bios.csv")
# print(bios)
# print(bios.info())
# bios['born_date'] = pd.to_datetime(bios['born_date'])
# print(bios.info())
# print(bios)
# print(bios.groupby(bios['born_date'].dt.year)['name'].count().reset_index())
# print(bios.groupby(bios['born_date'].dt.year)['born_city'].value_counts().reset_index())

# Handling NUll Values
# import numpy as np
# coffee = pd.read_csv("Y:\CS\Pandas\Data\coffee.csv")
# print(coffee)
# coffee.loc[[2,3],'Units Sold'] = np.nan
# print(coffee.info())
# print(coffee.fillna(1000))
# coffee.fillna(1000,inplace=True)
# print(coffee)
# coffee.fillna(coffee['Units Sold'].mean(),inplace=True)
# print(coffee)

# print(coffee)
# coffee['Units Sold'] = coffee['Units Sold'].interpolate() #Fills using a pattern
# print(coffee)

# yyyy-mm-dd

# print(coffee.dropna())
# coffee.dropna()
# print(coffee)

# print(coffee.notna())
# print(coffee[coffee["Units Sold"].notna()])

# print(coffee.isna())
# print(coffee[coffee['Units Sold'].isna()])

# coffee = pd.read_csv("Y:\CS\Pandas\Data\coffee.csv")

# import numpy as np
# coffee["Price"] = np.where(coffee["Coffee Type"] == "Espresso", 3.99, 5.99)
# coffee['Revenue'] = coffee["Units Sold"] * coffee["Price"]
# coffee['Cum Revenue'] = coffee["Revenue"].cumsum()
# print(coffee)
# coffee["Yesterday_Revenue"] = coffee["Revenue"].shift(2)
# print(coffee)
# coffee["Percent"] = (coffee["Revenue"] - coffee["Yesterday_Revenue"])/100
# print(coffee)

# coffee["Rank"] = coffee["Revenue"].rank(ascending=False).sort_values()
# print(coffee)
