from strategy.strategy_abc import AbsStrategy

class PostalStrategy(AbsStrategy):
    """ Implementation of Postal calculate method """

    def calculate(self, order):
        return 5.00
