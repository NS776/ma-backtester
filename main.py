from data import get_prices
from data import get_prices
from strat import add_signals, run_backtest

prices = get_prices("AAPL")
print(prices.head())
print(prices.tail())
print(len(prices))

prices = get_prices("AAPL")
df = add_signals(prices)
df = run_backtest(df)

print(df[["Close", "short_ma", "long_ma", "position"]].tail(10))
print("Buy and hold final value:", df["market_cumulative"].iloc[-1])
print("Strategy final value:    ", df["strategy_cumulative"].iloc[-1])