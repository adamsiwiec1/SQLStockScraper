# Using yahoo finance api
import yfinance as yf
from termcolor import colored
from db.config import sqlConnection
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

        # extra details - may not be found
        'Country': None,
        'Sector': None,
        'Industry': None,
        'TotalAssets': None,
        '52WeekChange': None,
        'LastDividendValue': None,
        'PayoutRatio': None,
        'ProfitMargins': None,

        # short details
        "FloatShares": None,
        "ShortShares": None,
        "SharesShortMonthAgo": None,

        # # extra extra details
        "Employees": None,
        "BookValue": None,
        'MorningStarRiskRating': None,
        'EarningsQuarterlyGrowth': None,
        'NetIncomeToCommon': None,
        'SharesOutstanding': None,
        "ShortRatio": None,
        'Market': None,
        'LongBusinessSummary': None
    }

    # Try to get exchange
    try:
        infoDict['Exchange'] = stock.info['exchange']
    except KeyError as e:
        print(f"Not able to pull exchange for '{stock.info['symbol']}'\n Exception: {e}\n")
        pass

    # Try to get extra details
    try:
        infoDict['Country'] = stock.info['country']
        infoDict['Sector'] = stock.info['sector']
        infoDict['Industry'] = stock.info['industry']
        infoDict['TotalAssets'] = stock.info['totalAssets']
        infoDict['FiftyTwoWeekChange'] = stock.info['52WeekChange']
        infoDict['LastDividendValue'] = stock.info['lastDividendValue']
        infoDict['PayoutRatio'] = stock.info['payoutRatio']
        infoDict['ProfitMargins'] = stock.info['profitMargins']

    except KeyError as e:
        print(f"Not able to extra details for '{stock.info['symbol']}'\n Exception: {e}\n")
        pass

    # Try to populate short details
    try:
        infoDict['FloatShares'] = stock.info['floatShares']
        infoDict['ShortShares'] = stock.info['sharesShort']
        infoDict['SharesShortMonthAgo'] = stock.info['sharesShortPreviousMonthDate']
    except KeyError as e:
        print(colored(f"Not able to pull short details for '{stock.info['symbol']}'\n Exception: {e}\n", "red"))
        pass

    # Try to populate extra details
    try:
        infoDict['Employees'] = stock.info['fullTimeEmployees']
        infoDict['BookValue'] = stock.info['bookValue']
        infoDict['MorningStarRiskRating'] = stock.info['morningStarRiskRating']
        infoDict['EarningsQuarterlyGrowth'] = stock.info['earningsQuarterlyGrowth']
        infoDict['NetIncomeToCommon'] = stock.info['netIncomeToCommon']
        infoDict['SharesOutstanding'] = stock.info['sharesOutstanding']
        infoDict['ShortRatio'] = stock.info['shortRatio']
        infoDict['Market'] = stock.info['market']
        infoDict['LongBusinessSummary'] = stock.info['longBusinessSummary']
    except KeyError as e:
        print(f"Not able to pull extra extra details for '{stock.info['symbol']}'\n\n Exception: {e}")

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
