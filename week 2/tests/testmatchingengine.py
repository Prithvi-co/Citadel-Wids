from engine.order import Order
from engine.order_book import OrderBook
from engine.matching_engine import MatchingEngine

# initialize order book and matching engine
order_book = OrderBook()
engine = MatchingEngine(order_book)

# add SELL limit orders (ask side)
engine.process_order(Order(1, "SELL", 101, 10, 1, "LIMIT"))
engine.process_order(Order(2, "SELL", 102, 20, 2, "LIMIT"))
engine.process_order(Order(3, "SELL", 103, 30, 3, "LIMIT"))

# place MARKET BUY order to consume all asks
engine.process_order(Order(4, "BUY", None, 60, 4, "MARKET"))

print("Executed Trades:")
for t in engine.trade_history:
    print(t)

print("Remaining best ask:", order_book.get_best_ask())
