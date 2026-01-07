# Citadel × WiDS – Agent-Based Market Simulation Project

This repository presents a three-week learning and implementation project focused on
financial markets, randomness, and market microstructure.  
The project gradually moves from core concepts to a complete agent-based exchange
simulation with analytics support.

---

## Week 0: Foundations – Python, Randomness, and Risk

### Work Done
- Revised Python basics required for quantitative finance applications
- Implemented **Geometric Brownian Motion (GBM)** to model asset price dynamics
- Simulated multiple GBM price paths using the same parameters
- Created visualizations:
  - Asset price paths over time
  - Distribution of final prices using histograms
- Wrote a short reflection on the role of randomness in financial risk

### Key Concepts Learned
- Randomness is a fundamental component of financial markets
- Even with fixed drift and volatility, price paths can differ widely
- Risk should be viewed as a **range of possible outcomes**, not a single prediction
- Volatility determines uncertainty and spread of outcomes
- Losses are natural outcomes of randomness, not rare events

---

## Week 1: Market Microstructure & System Design

### Work Done
- Studied the structure of modern electronic trading markets
- Designed a modular **market simulator architecture**
- Defined responsibilities and interactions between:
  - Trading agents
  - Market environment
  - Order book
  - Trade recording and analytics

### Architecture Overview
- **Agents**
  - Observe market information
  - Make trading decisions
  - Submit orders to the exchange
- **Market Environment**
  - Maintains the simulation clock
  - Routes incoming orders
  - Tracks overall market state
- **Order Book**
  - Stores bids and asks
  - Uses price–time (FIFO) priority
  - Handles order matching
- **Trade Logging & Analytics**
  - Records executed trades
  - Enables spread, depth, and tape analysis

### Key Concepts Learned
- Core ideas of market microstructure
- Price–time priority and FIFO execution
- Difference between liquidity providers and liquidity takers
- Impact of randomness on order flow
- Importance of modular system design

---

## Week 2: Agent-Based Exchange Implementation

### Work Done
Implemented a complete agent-based exchange simulator in Python:

#### Agents
- **NoiseAgent**
  - Places random market buy and sell orders
- **MomentumAgent**
  - Trades based on recent price movements
- **MarketMakerAgent**
  - Posts two-sided limit orders around the mid-price
- **Base Agent Interface**
  - Defined using abstraction to support extensibility

#### Engine
- **Order**
  - Represents buy/sell and market/limit orders
- **OrderBook**
  - Maintains bid and ask priority heaps
  - Provides best bid and best ask access
- **MatchingEngine**
  - Matches orders using price–time priority
  - Logs executed trades
- **EventLoop**
  - Schedules and processes orders in timestamp order

#### Analytics
- **TradeTape**
  - Stores all executed trades
- **SnapshotRecorder**
  - Records best bid, best ask, mid-price, and spread
- **Metrics**
  - VWAP (Volume Weighted Average Price)
  - Average bid–ask spread
  - Volatility based on log returns

#### Testing & Simulation
- Unit-style tests to verify matching engine correctness
- Full simulation runner featuring:
  - Multiple interacting agents
  - Random order arrivals
  - Trade execution
  - VWAP calculation

---

## Key Learning Outcomes

By the end of this project, the following concepts were understood and implemented:

- Agent-based modeling of financial markets
- Order-driven exchange mechanics
- Order books and matching engines
- Market orders versus limit orders
- Liquidity provision and consumption
- Event-driven simulation design
- Probabilistic interpretation of financial risk
- Modular and extensible software architecture

---
