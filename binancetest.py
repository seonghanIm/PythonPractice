import ccxt

binance = ccxt.binance()
markets = binance.fetch_tickers()
print(markets.keys())

# 코인 심볼 가져오기


