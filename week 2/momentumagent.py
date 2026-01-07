from collections import deque
from engine.order import Order

class MomentumAgent:
    def __init__(self, agent_id, window=5, quantity=5):
        self.uid = agent_id
        self.lookback = window
        self.order_size = quantity
        self.price_history = deque(maxlen=window)

    def update_price(self, latest_price):
        if latest_price is not None:
            self.price_history.append(latest_price)

    def decide_action(self, time_stamp):
        if len(self.price_history) < self.lookback:
            return None

        average_price = sum(self.price_history) / len(self.price_history)
        current_price = self.price_history[-1]

        if current_price > average_price:
            return Order(self.uid, "BUY", None, self.order_size, time_stamp, "MARKET")
        else:
            return Order(self.uid, "SELL", None, self.order_size, time_stamp, "MARKET")
