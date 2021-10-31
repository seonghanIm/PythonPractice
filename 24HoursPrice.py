import ccxt

binance = ccxt.binance()
ticker = binance.fetch_ticker(input("원하는 심볼을 입력하세요 : "))
print("open : ",ticker['open']) #open price
print("high : ",ticker['high']) #high price
print("low : ",ticker['low']) #low price
print("close : ",ticker['close']) #close price

