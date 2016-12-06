from strategy.strategy_abc import AbsStrategy

class FedExStrategy(AbsStrategy):
    """ Implementation of FedEx calculate method """

    def calculate(self, order):
        return 3.00
