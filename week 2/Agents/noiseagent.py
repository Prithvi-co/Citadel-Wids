import random
from engine.order import Order

class NoiseAgent:
    def __init__(self, agent_id, max_qty=10):
        self.uid = agent_id
        self.max_size = max_qty

    def decide_action(self, time_stamp):
        side = random.choice(["BUY", "SELL"])
        quantity = random.randint(1, self.max_size)

        order = Order(
            self.uid,
            side,
            None,
            quantity,
            time_stamp,
            "MARKET"
        )

        return order
