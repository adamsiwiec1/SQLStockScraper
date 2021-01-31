class Stock(object):

    def __init__(self, ticker, name, price, ask, bid, daylow, dayhigh, volume, marketOpen, marketClose, floor, ceiling):
        self.ticker = ticker
        self.tickerString = str(self.ticker)
        self.name = name
        self.price = price
        self.ask = ask
        self.bid = bid
        self.daylow = daylow
        self.dayhigh = dayhigh
        self.volume = volume
        self.marketOpen = marketOpen
        self.marketClose = marketClose
        self.floor = floor
        self.ceiling = ceiling
        self.count = 0
        self.limitCount = 0

