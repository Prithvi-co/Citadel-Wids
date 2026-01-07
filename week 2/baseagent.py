from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, agent_id, cash=100000, inventory=0):
        self.uid = agent_id
        self.cash_balance = cash
        self.position = inventory

    @abstractmethod
    def decide_action(self, market_state):
        """
        Decide the next action based on the current market state.
        This method must be implemented in child classes.
        """
        pass

    def update_cash(self, value):
        self.cash_balance = self.cash_balance + value

    def update_position(self, qty):
        self.position = self.position + qty

    def __repr__(self):
        return (
            f"Agent(id={self.uid}, "
            f"cash_balance={self.cash_balance}, "
            f"position={self.position})"
        )
