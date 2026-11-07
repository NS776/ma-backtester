import pandas as pd


def add_signals(prices, short_window=50, long_window=200):
    """Add moving averages and a 'position' column (1 = hold stock, 0 = cash)."""
    df = prices.copy()  

    df["short_ma"] = df["Close"].rolling(short_window).mean()
    df["long_ma"] = df["Close"].rolling(long_window).mean()

    # Signal is 1 if short_ma > long_ma, else 0
    df["signal"] = (df["short_ma"] > df["long_ma"]).astype(int)

    # Shifting 1 day
    df["position"] = df["signal"].shift(1)

    return df

def run_backtest(df):
    """Calculate daily and cumulative returns for the strategy and buy-and-hold."""
    df = df.copy()

    # Daily % change in price
    df["market_return"] = df["Close"].pct_change()

    df["strategy_return"] = df["position"] * df["market_return"]

    # Cumulative growth of £1 invested
    df["market_cumulative"] = (1 + df["market_return"]).cumprod()
    df["strategy_cumulative"] = (1 + df["strategy_return"]).cumprod()

    return df