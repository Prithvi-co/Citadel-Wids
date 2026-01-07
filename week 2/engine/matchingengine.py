from engine.order_book import OrderBook

class MatchingEngine:
    def __init__(self, order_book):
        self.book = order_book
        self.trade_history = []

    def _record_trade(self, price, quantity, buy_order, sell_order, timestamp):
        trade = {
            "price": price,
            "quantity": quantity,
            "buy_order_id": buy_order.order_id,
            "sell_order_id": sell_order.order_id,
            "timestamp": timestamp
        }
        self.trade_history.append(trade)

    def process_order(self, order):
        if order.side == "BUY":
            self._process_buy(order)
        elif order.side == "SELL":
            self._process_sell(order)

    def _process_buy(self, buy_order):
        while buy_order.quantity > 0:
            ask = self.book.get_best_ask()
            if ask is None:
                break

            if buy_order.order_type == "LIMIT" and buy_order.price < ask.price:
                break

            traded_qty = min(buy_order.quantity, ask.quantity)
            traded_price = ask.price

            self._record_trade(
                traded_price,
                traded_qty,
                buy_order,
                ask,
                buy_order.timestamp
            )

            buy_order.quantity -= traded_qty
            ask.quantity -= traded_qty

            if ask.quantity == 0:
                self.book.remove_best_ask()

        if buy_order.quantity > 0 and buy_order.order_type == "LIMIT":
            self.book.add_order(buy_order)

    def _process_sell(self, sell_order):
        while sell_order.quantity > 0:
            bid = self.book.get_best_bid()
            if bid is None:
                break

            if sell_order.order_type == "LIMIT" and sell_order.price > bid.price:
                break

            traded_qty = min(sell_order.quantity, bid.quantity)
            traded_price = bid.price

            self._record_trade(
                traded_price,
                traded_qty,
                bid,
                sell_order,
                sell_order.timestamp
            )

            sell_order.quantity -= traded_qty
            bid.quantity -= traded_qty

            if bid.quantity == 0:
                self.book.remove_best_bid()

        if sell_order.quantity > 0 and sell_order.order_type == "LIMIT":
            self.book.add_order(sell_order)

