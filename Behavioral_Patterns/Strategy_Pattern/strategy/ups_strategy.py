from strategy.strategy_abc import AbsStrategy

class UPSStrategy(AbsStrategy):
    """ Implementation of UPS calculate method """

    def calculate(self, order):
        return 4.00
