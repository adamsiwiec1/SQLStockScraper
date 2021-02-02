# Takes a Ticker as an input and returns % Short, Short Shares, Float Shares, and Short Shares Month Ago
import yfinance as yf


def short_finder(ticker):

    stock = yf.Ticker(ticker)

    # print(stock.info['symbol'])
    # print(stock.info['sharesShort'])
    # print(stock.info['floatShares'])
    # print(stock.info['sharesShortPreviousMonthDate'])
    print(stock.info['TotalAssets'])


if __name__ == "__main__":

    while True:
        ticker = input("Enter a ticker: ")
        short_finder(ticker)

