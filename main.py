import plotly . express as px
import pandas as pd
df = pd.read_csv("Superstore.csv",encoding="latin1")

print("Dataset shape:")
print(df.shape)

print("\n column names:")
print(df.columns.tolist())

print("\n Missing values:")
print(df.isna().sum())

print("\n Dataset information:")
df.info()

#convert date columns from text to real datetime values
df["Ordeer Date"]=pd.to_datetime(df["Order Date"])
df["Ship Date"]=pd.to_datetime(df["Ship Date"])

print(df[["Order Date","Ship Date"]].head())
print(df[["Order Date","Ship Date"]].dtypes)

#check for duplicate rows and invalid businessvalues
duplicate_rows=df.duplicated().sum()

print("\nDuplicate rows:")
print(duplicate_rows)

print("\n Invalid Quantity values:")
print((df["Quantity"]<=0).sum())

print("\n Invalid Sales values:")
print((df["Sales"]<0).sum())

print("\n Discount outside 0 to 1:")
print(((df["Discount"]<0) | (df["Discount"]>1)).sum())

#basic business KPI's
total_sales=df["Sales"].sum()
total_profit=df["Profit"].sum()
total_quantity=df["Quantity"].sum()
total_orders=df["Order ID"].nunique()

average_order_value=total_sales/total_orders

print("\nBusiness KPIs:")
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Quantity Sold:", total_quantity)
print("Total Orders:", total_orders)
print("Average Order Value:", average_order_value)
     
#regional business analysis
sales_by_region= (df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

profit_by_region=(df.groupby("Region")["Profit"].sum().sort_values(ascending=False))

print("\n Sales by Region:")
print(sales_by_region)

print("\n Profit by Region:")
print(profit_by_region)     
     
# first visualization - Sales by Region
region_sales_df = sales_by_region.reset_index()
fig = px.bar(region_sales_df,x="Region",y="Sales",title="Sales by Region")
fig.show()     
            
# second visualization - Profit by Region
region_profit_df = profit_by_region.reset_index()
profit_fig = px.bar(region_profit_df, x="Region",y="Profit",title="Profit by Region")
profit_fig.show()            