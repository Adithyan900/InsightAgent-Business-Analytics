import plotly.express as px
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="InsightAgent",
    layout="wide"
)

# load dataset
df = pd.read_csv("Superstore.csv", encoding="latin1")
df["Order Date"] = pd.to_datetime(df["Order Date"])

# sidebar filters
st.sidebar.header("Filters")

selected_region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

selected_category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

selected_segment = st.sidebar.multiselect(
    "Select Segment",
    options=df["Segment"].unique(),
    default=df["Segment"].unique()
)

filtered_df = df[
    (df["Region"].isin(selected_region)) &
    (df["Category"].isin(selected_category)) &
    (df["Segment"].isin(selected_segment))
]

# basic KPIs
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()

average_order_value = (
    total_sales / total_orders
    if total_orders > 0
    else 0
)

st.title("InsightAgent")
st.caption("AI-powered business analytics platform")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"{total_sales:,.2f}")
col2.metric("Total Profit", f"{total_profit:,.2f}")
col3.metric("Total Orders", f"{total_orders:,}")
col4.metric("Average Order Value", f"{average_order_value:,.2f}")

# regional analysis
sales_by_region = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
    .sort_values("Sales", ascending=False)
)

profit_by_region = (
    filtered_df.groupby("Region")["Profit"]
    .sum()
    .reset_index()
    .sort_values("Profit", ascending=False)
)

st.subheader("Regional Performance")

chart_col1, chart_col2 = st.columns(2)

sales_fig = px.bar(
    sales_by_region,
    x="Region",
    y="Sales",
    title="Sales by Region"
)

profit_fig = px.bar(
    profit_by_region,
    x="Region",
    y="Profit",
    title="Profit by Region"
)

chart_col1.plotly_chart(sales_fig, use_container_width=True)
chart_col2.plotly_chart(profit_fig, use_container_width=True)

# monthly sales trend
monthly_sales = (
    filtered_df.groupby(
        filtered_df["Order Date"].dt.to_period("M")
    )["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Order Date"] = monthly_sales["Order Date"].astype(str)

st.subheader("Monthly Sales Trend")

monthly_fig = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    title="Monthly Sales Trend",
    markers=True
)

st.plotly_chart(monthly_fig, use_container_width=True)

# first analysis tool

def get_top_region_by_sales(data):
    result = (
        data.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    top_region = result.index[0]
    top_sales = result.iloc[0]

    return top_region, top_sales

st.subheader("Ask InsightAgent")

question = st.text_input(
    "Ask a business question",
    placeholder="Example: Which region has the highest sales?"
)

if st.button("Analyze"):
    if question.lower().strip() == "which region has the highest sales?":
        region, sales = get_top_region_by_sales(filtered_df)

        st.success(
            f"{region} has the highest sales with {sales:,.2f}."
        )
    else:
        st.info(
            "For now, try: Which region has the highest sales?"
        )