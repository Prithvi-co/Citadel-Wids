import pandas as pd
import numpy as np

def vwap(trades):
    if trades is None or len(trades) == 0:
        return None

    trade_df = pd.DataFrame(trades)
    value = (trade_df["price"] * trade_df["quantity"]).sum()
    volume = trade_df["quantity"].sum()

    return value / volume


def average_spread(snapshots):
    spreads = []

    for snap in snapshots:
        if snap.get("spread") is not None:
            spreads.append(snap["spread"])

    if len(spreads) == 0:
        return None

    return sum(spreads) / len(spreads)


def volatility(snapshots, window=10):
    prices = []

    for snap in snapshots:
        if snap.get("mid_price") is not None:
            prices.append(snap["mid_price"])

    if len(prices) < window:
        return None

    returns = np.diff(np.log(prices))
    return np.std(returns)
