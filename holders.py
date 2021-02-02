from urllib.error import HTTPError

import yfinance as yf
from termcolor import colored
from db.config import sqlConnection
from stock import Stock
from dictionary import StockDictionary


def get_info(ticker):
    stock = yf.Ticker(ticker)

    print(f"{stock.major_holders[0][0]} {stock.major_holders[1][0]}")
    print(stock.institutional_holders)
    # print(stock.major_holders)
    # print(stock.major_holders)


def get_perc_holder(holders):

    for row in holders:
        for percent in holders[row]:
            print(percent)
            # for label in range(percent):
            #     print("\nlabel" + str(label))

# get_info("gme")
def print_holders(ticker):
    stock = yf.Ticker(ticker)
    try:
        if stock.major_holders[0][0]:
            if "Previous Close" not in stock.major_holders[0][0]:
                print(stock.major_holders)
            else:
                print(colored(f"Bid and ask were found for {ticker}", "red"))
        else:
            print(colored(f"No data for {ticker}", "red"))
    except TypeError:
        pass
        print(colored(f"Whatever a numpy float is, it's not iterable. {ticker} failed to add."))

    # get_perc_holder(stock.major_holders)


if __name__ == "__main__":

    try:
        for x in StockDictionary.STOCKS:
            try:
                print_holders(x)
            except ValueError as e:
                print("Error: VALUE ERROR:" + str(e))
                pass
    except HTTPError:
        print(colored('Error: HTTP ERROR'), "red")
        pass

