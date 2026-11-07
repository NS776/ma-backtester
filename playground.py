import pandas as pd
prices = pd.DataFrame({
    "Close": [10, 11, 12, 11, 13]
})
print(prices)
print (prices["Close"])
print(prices["Close"].mean())
print(prices["Close"].rolling(3).mean())