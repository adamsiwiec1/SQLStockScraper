# Using yahoo finance api
import textwrap

import yfinance as yf


def get_info():
    nok = yf.Ticker('NOK')

    # print("Info: " + str(nok.info) + "\n\n")
    #
    # print("Balance sheet: \n" + str(nok.balance_sheet) + "\n\n")
    # print("Cashflow:  \n" + str(nok.cashflow) + "\n\n")
    # print("Financials:  \n" + str(nok.financials) + "\n\n")
    # print("Splits  \n" + str(nok.splits) + "\n\n")

    print("Info: " + str(nok.info))



    # for i in ['Open', 'High', 'Close', 'Low']:
    #     nok[i] = nok[i].astype('float64')
get_info()