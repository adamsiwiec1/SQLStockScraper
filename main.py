# Using yahoo finance api
import yfinance as yf
from stock import Stock
from dictionary import StockDictionary

def create_infoDict_list(stocks):
    dictList = []
    for stock in stocks:
        if stock.volume is not None:
            stokDict = get_info(str(stock.ticker))
        try:
            stock.ticker = stokDict["Ticker"]
            stock.name = stokDict["Name"]
            stock.price = stokDict["Price"]
            stock.ask = stokDict["Ask"]
            stock.bid = stokDict["Bid"]
            stock.daylow = stokDict["DayLow"]
            stock.dayhigh = stokDict["DayHigh"]
            stock.volume = stokDict["Volume"]
            stock.marketOpen = stokDict["MarketOpen"]
            stock.marketClose = 'MarketClose'
            dictList.append(stock.__dict__)
        except UnboundLocalError as e:
            print("Error" + str(e))
    for dict in dictList:
        print(dict)


def get_info(ticker):
    stock = yf.Ticker(ticker)

    infoDict = {

        # current
        "Ticker": stock.info['symbol'],
        "Name": stock.info['longName'],
        "Price": stock.info['regularMarketPrice'],
        "Ask": stock.info['ask'],
        "Bid": stock.info['bid'],
        "DayLow": stock.info['dayLow'],
        "DayHigh": stock.info['dayHigh'],
        "Volume": stock.info['regularMarketVolume'],
        "MarketOpen": stock.info['regularMarketOpen'],
        "MarketClose": stock.info['regularMarketPreviousClose'],

        # details
        "52WeekLow": stock.info['fiftyTwoWeekLow'],
        "52WeekHigh": stock.info['fiftyTwoWeekHigh'],
        "50DayAvg": stock.info['fiftyDayAverage'],
        "200DayAvg": stock.info['twoHundredDayAverage'],
        "AvgVolume": stock.info['averageVolume'],
        "10DayAvgVolume": stock.info['averageDailyVolume10Day'],

        # extra details
        "YtdReturn": stock.info['ytdReturn'],

        # short details
        "ShortShares": None,
        "SharesShortMonthAgo": None,
        "FloatShares": None,

        # extra extra details (might not be there)
        "Employees": None,
        "Sector": None,
        "BookValue": None,
        "LastDividendValue": None
    }

    # Try to populate short details
    try:
        infoDict['FloatShares'] = stock.info['floatShares']
        infoDict['ShortShares'] = stock.info['sharesShort']
        infoDict['SharesShortMonthAgo'] = stock.info['sharesShortPreviousMonthDate']
    except KeyError as e:
        print(f"Not able to pull short details for '{stock.info['symbol']}'\n\n Exception: {e}\n")

    # Try to populate extra details
    try:
        infoDict['Employees'] = stock.info['fullTimeEmployees']
        infoDict['Sector'] = stock.info['sector']
        infoDict['BookValue'] = stock.info['bookValue']
        infoDict['LastDividendValue'] = stock.info['lastDividendValue']
    except KeyError as e:
        print(f"Not able to pull extra extra details for '{stock.info['symbol']}'\n\n Exception: {e}")

    return infoDict


def get_short_perc():

    # Create an Array of
    stocks = [Stock]
    for stock in StockDictionary.NASDAQ:
        try:
            dict = get_info(str(stock))
        except ValueError as e:
            print(f'No tables found for {e}')
        if dict and dict['ShortShares']:
            stocks.append(dict)
            print(stock)
    for stock in stocks:
        if str(stock) != "<class 'stock.Stock'>":
            print(stock)
            if stock['ShortShares']:
                print(stock['ShortShares'])

get_short_perc()

# create_infoDict_list(stocksList)