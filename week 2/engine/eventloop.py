import heapq

class EventLoop:
    def __init__(self, engine):
        self.engine = engine
        self.current_time = 0
        self.events = []
        self.counter = 0

    def push_event(self, time_stamp, order):
        heapq.heappush(
            self.events,
            (time_stamp, self.counter, order)
        )
        self.counter += 1

    def execute(self):
        while self.events:
            ts, _, order = heapq.heappop(self.events)
            self.current_time = ts
            self.engine.process_order(order)
