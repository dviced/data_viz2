import yfinance as yf
import pandas as pd
import plotly.express as px
import streamlit as st

# Define the SMI companies and their tickers
smi_companies = {
    "Zurich Insurance Group AG": "ZURN.SW",
    "Lonza Group AG": "LONN.SW",
    "Givaudan SA": "GIVN.SW",
    "Swiss Life Holding AG": "SLHN.SW",
    "Geberit AG": "GEBN.SW",
}

# Fetch historical data for the companies
start_date = "2024-01-01"
end_date = "2025-01-01"

price_data = {}
for company, ticker in smi_companies.items():
    stock_data = yf.download(ticker, start=start_date, end=end_date, progress=False)["Adj Close"]
    price_data[company] = stock_data

# Combine data into a DataFrame
df = pd.DataFrame(price_data)

# Reshape for Plotly (long format)
df_reset = df.reset_index().melt(id_vars="Date", var_name="Company", value_name="Stock Price")

# Create the interactive line chart
fig = px.line(
    df_reset, 
    x="Date", 
    y="Stock Price", 
    color="Company", 
    title="SMI Components Stock Prices (2024)",
    labels={"Date": "Date", "Stock Price": "Price (CHF)", "Company": "Company"},
    color_discrete_sequence=px.colors.qualitative.Set2  # Custom color palette
)
fig.update_layout(template="plotly_white", hovermode="x unified")

st.plotly_chart(fig)
