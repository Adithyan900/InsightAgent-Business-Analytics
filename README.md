# InsightAgent

InsightAgent is an AI-powered business analytics platform that turns business CSV data into interactive KPIs, visualizations, and data-driven insights.

The project is being built as an agentic analytics system where Python performs the actual calculations while the AI layer will later interpret user questions, choose analytical tools, verify results, and explain business insights.

## Current Features

- CSV-based business analytics
- Data inspection and validation
- KPI calculation
- Interactive Streamlit dashboard
- Region, Category, and Segment filters
- Sales by Region visualization
- Profit by Region visualization
- Monthly Sales Trend
- Natural-language analysis foundation
- Pandas-based verified calculations

## Business KPIs

The current dashboard calculates:

- Total Sales
- Total Profit
- Total Quantity Sold
- Total Orders
- Average Order Value

## Tech Stack

- Python
- Pandas
- Plotly
- Streamlit

## Project Architecture

```text
CSV Dataset
    ↓
Data Profiling
    ↓
Business Analysis
    ↓
Pandas Calculations
    ↓
Interactive Charts
    ↓
Streamlit Dashboard
