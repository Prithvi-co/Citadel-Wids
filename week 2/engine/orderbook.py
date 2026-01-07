import heapq

class OrderBook:
    def __init__(self):
        self.bids = []
        self.asks = []

    def add_order(self, order):
        if order.side == "BUY":
            heapq.heappush(
                self.bids,
                (-order.price, order.timestamp, order)
            )
        elif order.side == "SELL":
            heapq.heappush(
                self.asks,
                (order.price, order.timestamp, order)
            )

    def get_best_bid(self):
        if len(self.bids) == 0:
            return None
        return self.bids[0][2]

    def get_best_ask(self):
        if len(self.asks) == 0:
            return None
        return self.asks[0][2]

    def remove_best_bid(self):
        if self.bids:
            heapq.heappop(self.bids)

    def remove_best_ask(self):
        if self.asks:
            heapq.heappop(self.asks)
