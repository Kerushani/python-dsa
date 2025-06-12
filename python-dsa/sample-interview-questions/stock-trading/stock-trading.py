"""
“We’d like you to design a simplified stock order matching engine. 
You’ll be given a list of stock transactions in the form of buy and sell orders. 
Each order includes a stock symbol, number of units, price per unit, and whether it's a buy or sell order.

Your job is to simulate an order matching system. 
A buy order should match with the most favorable sell order available — 
meaning, the lowest price that still satisfies the buyer’s price (i.e., sell_price <= buy_price). 
A match occurs only if the number of units also match. 
Once a transaction is matched, it is removed from the queue.

You’ll parse this from an input file and return a list of matched transactions along with any unmatched orders. 
Use object-oriented design.”

- sell_price <= buy_price
- units must match 
TOD0: Possible edge cases
"""

class Stock:
    # example of how this variable updates each time a new instance of a class appears
    count_stock=0
    def __init__(self, stock_symbol="unkown", units=0, price=0, order_type="unkown"):
        self.stock_symbol=stock_symbol
        self.units=units
        self.price=price
        self.order_type=order_type
        Stock.count_stock+=1

    def display_info(self):
        print(f"Stock: {self.stock_symbol}, Units: {self.units}, price: {self.price},order_type:{self.order_type}, number of stocks on market: {Stock.count_stock}")

class Buyer:
    def __init__(self, buy_price, units):
        self.buy_price=buy_price
        self.units=units
        self.matches=[]

class MatchingEngine:
    def __init__(self, stocks, buyers):
        self.stocks = stocks
        self.buyers = buyers
    def findMatches(self):
        match=[]
        for stock in self.stocks:
            for buyer in self.buyers:
                if stock.order_type == "sell" and stock.price <= buyer.buy_price and stock.units>=buyer.units:
                    match.append(stock.stock_symbol)
        print(match)

available_stocks = [Stock("TSLA", 56, 3, "sell"), Stock("APPL", 1092, 5, "sell"), Stock("AMZ", 54, 102, "sell")]

buyers = [Buyer(10, 56)]

matching_engine = MatchingEngine(available_stocks, buyers)

find_matches = matching_engine.findMatches()
    
# for stock in available_stocks:
#     stock.display_info()
# for buyer in buyers:
#     buyer.displayMatch()