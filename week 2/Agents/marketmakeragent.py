from engine.order import Order

class MarketMakerAgent:
    def __init__(self, agent_id, spread=1, quantity=5):
        self.uid = agent_id
        self.spread_width = spread
        self.order_size = quantity

    def generate_orders(self, ref_price, time_stamp):
        if ref_price is None:
            return []

        buy_price = ref_price - self.spread_width
        sell_price = ref_price + self.spread_width

        buy_order = Order(
            self.uid,
            "BUY",
            buy_price,
            self.order_size,
            time_stamp,
            "LIMIT"
        )

        sell_order = Order(
            self.uid,
            "SELL",
            sell_price,
            self.order_size,
            time_stamp,
            "LIMIT"
        )

        return [buy_order, sell_order]
