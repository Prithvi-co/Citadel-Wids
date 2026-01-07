# Agent-Based Market Simulation (Week 2)

This project builds a simple agent-based market simulator.  
It demonstrates how different trading agents interact with a central exchange
through an order book and a matching engine.

## Components

### Agents
- **NoiseAgent**: Submits random buy and sell market orders.
- (Extensible) Additional agents can be added with custom decision logic.

### Engine
- **OrderBook**: Manages bid and ask queues using priority heaps.
- **MatchingEngine**: Processes incoming orders and logs executed trades.
- **EventLoop**: Handles order scheduling and execution based on time.

### Analytics
- **TradeTape**: Keeps a record of all executed trades.
- **SnapshotRecorder**: Captures market snapshots like best bid and ask prices.
- **Metrics**:
  - VWAP (Volume Weighted Average Price)
  - Average bid–ask spread
  - Volatility (based on log returns)

## Running the Simulation

Execute the simulation using:
```bash
python run_simulation.py

