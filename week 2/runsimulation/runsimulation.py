import random
from engine.order_book import OrderBook
from engine.matching_engine import MatchingEngine
from engine.event_loop import EventLoop
from agents.noise_agent import NoiseAgent
from analytics.tape import TradeTape
from analytics.snapshots import SnapshotRecorder
from analytics.metrics import vwap

# setting random seed
random.seed(42)

order_book = OrderBook()
matching_engine = MatchingEngine(order_book)
event_loop = EventLoop(matching_engine)

trade_tape = TradeTape()
snapshot_recorder = SnapshotRecorder()

agents = []
for i in range(10):
    agents.append(NoiseAgent(agent_id=i))

time_now = 0

for _ in range(50):
    time_now += 1
    chosen_agent = random.choice(agents)
    new_order = chosen_agent.decide_action(time_now)

    if new_order is not None:
        event_loop.push_event(time_now, new_order)

event_loop.execute()

for executed_trade in matching_engine.trade_history:
    trade_tape.add(executed_trade)

print("VWAP:", vwap(trade_tape.trades))
