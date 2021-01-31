# Using yahoo finance api
import yfinance as yf
from stock import Stock


# Mock Stocks
stocksList = [Stock(str('NOK'), "", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00, 6.00)]
stocksList.append(Stock(str('AZN'), "", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 45.00, 50.00))
stocksList.append(Stock(str('AAPL'), "", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 99.00, 500.00))
stocksList.append(Stock(str('TSLA'), "", 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 500.00, 900.00))


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
        "Sector": stock.info['sector'],
        "BookValue": stock.info['bookValue'],
        "YtdReturn": stock.info['ytdReturn'],
        "LastDividendValue": stock.info['lastDividendValue'],
        "ShareShort": stock.info['sharesShort'],
        "FloatShares": stock.info['floatShares'],
        "Employees": stock.info['fullTimeEmployees']


    }

    return infoDict


create_infoDict_list(stocksList)