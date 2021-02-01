# Using yahoo finance api
import yfinance as yf
from termcolor import colored
from database.config import sqlConnection
from stock import Stock
from dictionary import StockDictionary


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
        "YtdReturn": stock.info['ytdReturn'],

        # exchange - sometimes not found (null)
        "Exchange": None,

        # short details
        "FloatShares": None,
        "ShortShares": None,
        "SharesShortMonthAgo": None,

        # # extra details (might not be there)
        # "Employees": None,
        # "Sector": None,
        # "BookValue": None,
        # "LastDividendValue": None
    }

    # Try to get exchange
    try:
        infoDict['Exchange'] = stock.info['exchange']
    except KeyError as e:
        print(f"Not able to pull exchange for '{stock.info['symbol']}'\n Exception: {e}\n")
        pass

    # Try to populate short details
    try:
        infoDict['FloatShares'] = stock.info['floatShares']
        infoDict['ShortShares'] = stock.info['sharesShort']
        infoDict['SharesShortMonthAgo'] = stock.info['sharesShortPreviousMonthDate']
    except KeyError as e:
        print(colored(f"Not able to pull short details for '{stock.info['symbol']}'\n Exception: {e}\n", "red"))
        pass

    # # Try to populate extra details
    # try:
    #     infoDict['Employees'] = stock.info['fullTimeEmployees']
    #     infoDict['Sector'] = stock.info['sector']
    #     infoDict['BookValue'] = stock.info['bookValue']
    #     infoDict['LastDividendValue'] = stock.info['lastDividendValue']
    # except KeyError as e:
    #     print(f"Not able to pull extra extra details for '{stock.info['symbol']}'\n\n Exception: {e}")

    return infoDict


def add_stock(stockDict):
    cursor = sqlConnection.cursor()

    try:
        # Execute SQL Command
        cursor.execute("INSERT INTO Stock VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (stockDict['Ticker'],
                    stockDict['Exchange'], stockDict['Name'], stockDict['Price'], stockDict['Ask'], stockDict['Bid'],
                    stockDict['DayLow'], stockDict['DayHigh'], stockDict['Volume'], stockDict['MarketOpen'],
                    stockDict['MarketClose'], stockDict['52WeekLow'], stockDict['52WeekHigh'], stockDict['50DayAvg'],
                    stockDict['200DayAvg'], stockDict['AvgVolume'], stockDict['10DayAvgVolume'], stockDict['YtdReturn'],
                    stockDict['FloatShares'], stockDict['ShortShares'], stockDict['SharesShortMonthAgo']))

        # Commit Changes to SQL Database
        sqlConnection.commit()
    except Exception as e:
        print(colored(f"Failed to add {stockDict['Ticker']} + {str(e)}?", "red"))
        # Roll back in case of error
        sqlConnection.rollback()


# def add_to_sql(stockDictList):
#     for stockDict in stockDictList:
#         try:
#             add_stock(stockDict)
#             print(colored(f"Successfully added {stockDict['Ticker']} to database!", "green"))
#         except Exception as e:
#             print(colored(f"Failed to add {stockDict['Ticker']}? + {str(e)}", "red"))

def add_to_sql(stockDict):
    try:
        add_stock(stockDict)
        print(colored(f"Successfully added {stockDict['Ticker']} to database!", "green"))
    except Exception as e:
        print(colored(f"Failed to add {stockDict['Ticker']}? + {str(e)}", "red"))


def create_stock_objects(tickers):
    stockList = []
    for ticker in tickers:
        try:
            stockDict = get_info(ticker)
            stockList.append(stockDict)
            print(colored(f"{ticker} was added to objects!", "green"))
            add_to_sql(stockDict)
        except Exception as e:
            print(colored(f"{ticker} was not added to objects\n Exception: {str(e)}", "red"))
            pass

    if stockList:
        return stockList


if __name__ == "__main__":
    stockList = create_stock_objects(StockDictionary.STOCKS)
    # add_to_sql(stockList)
