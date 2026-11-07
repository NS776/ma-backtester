import os
import yfinance as yf
import pandas as pd

# Defining function to get prices
def get_prices(ticker, start="2015-01-01", end="2025-01-01"):
    """Download daily prices for a ticker, using a saved CSV if we have one."""
    os.makedirs("cache", exist_ok=True)
    filename = f"cache/{ticker}_{start}_{end}.csv"

    if os.path.exists(filename):
        return pd.read_csv(filename, index_col=0, parse_dates=True)

    data = yf.download(ticker, start=start, end=end, auto_adjust=True)

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data.to_csv(filename)
    return data