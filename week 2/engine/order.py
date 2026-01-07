class Order:
    def __init__(self, order_id, side, price, quantity, time_stamp, order_kind):
        self.order_id = order_id
        self.side = side
        self.price = price
        self.quantity = quantity
        self.timestamp = time_stamp
        self.order_type = order_kind

    def __repr__(self):
        return (
            f"Order("
            f"id={self.order_id}, "
            f"side={self.side}, "
            f"price={self.price}, "
            f"quantity={self.quantity}, "
            f"timestamp={self.timestamp}, "
            f"type={self.order_type}"
            f")"
        )
