class SnapshotRecorder:
    def __init__(self):
        self.records = []

    def capture(self, time_stamp, best_bid, best_ask):
        if best_bid is not None and best_ask is not None:
            mid_price = (best_bid.price + best_ask.price) / 2
            spread = best_ask.price - best_bid.price
        else:
            mid_price = None
            spread = None

        snapshot = {
            "timestamp": time_stamp,
            "best_bid": best_bid.price if best_bid else None,
            "best_ask": best_ask.price if best_ask else None,
            "mid_price": mid_price,
            "spread": spread
        }

        self.records.append(snapshot)
