

# THIS CODE IS OLD AND NOT BEING USED CURRENTLY - LOOK IN MAIN

# DECIDED TO DO CALCULATIONS CLIENT SIDE VS SERVER

# def get_short_percentage():
#     # Create an Array of
#     stocks = [Stock]
#     for stock in StockDictionary.NASDAQ:
#         try:
#             dict = get_info(str(stock))
#         except ValueError as e:
#             print(f'No tables found for {e}')
#         if dict and dict['ShortShares']:
#             stocks.append(dict)
#             print(stock)
#     for stock in stocks:
#         if str(stock) != "<class 'stock.Stock'>":
#             print(stock)
#             if stock['ShortShares']:
#                 print(stock['ShortShares'])


# def create_infoDict_list(stocks):
#     dictList = []
#     for stock in stocks:
#         if stock.volume is not None:
#             stokDict = get_info(str(stock.ticker))
#         try:
#             stock.ticker = stokDict["Ticker"]
#             stock.name = stokDict["Name"]
#             stock.price = stokDict["Price"]
#             stock.ask = stokDict["Ask"]
#             stock.bid = stokDict["Bid"]
#             stock.daylow = stokDict["DayLow"]
#             stock.dayhigh = stokDict["DayHigh"]
#             stock.volume = stokDict["Volume"]
#             stock.marketOpen = stokDict["MarketOpen"]
#             stock.marketClose = 'MarketClose'
#             dictList.append(stock.__dict__)
#         except UnboundLocalError as e:
#             print("Error" + str(e))
#     for dict in dictList:
#         print(dict)


# create_infoDict_list(stocksList)
# get_short_perc()