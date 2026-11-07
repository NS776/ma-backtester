from data import get_prices

prices = get_prices("AAPL")
print(prices.head())    
print(prices.tail())    
print(len(prices))      