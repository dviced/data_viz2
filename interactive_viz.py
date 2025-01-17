import pandas as pd
import plotly.express as px
import streamlit as st

#load data from csv_file "smi_price_data.csv"
df = pd.read_csv("smi_price_data.csv", index_col=0)

# Reshape for Plotly (long format)
df_reset = df.reset_index().melt(id_vars="Date", var_name="Company", value_name="Stock Price")

# Create the interactive line chart
fig = px.line(
    df_reset, 
    x="Date", 
    y="Stock Price", 
    color="Company", 
    title="The magnificent 7 Stock Prices",
    labels={"Date": "Date", "Stock Price": "Price (CHF)", "Company": "Company"},
    color_discrete_sequence=px.colors.qualitative.Set2  # Custom color palette
)
fig.update_layout(template="plotly_white", hovermode="x unified")

st.plotly_chart(fig)
