class ShippingCost(object):

    def __init__(self, strategy):
        # Strategy object in the constructor and saves that reference for later
        self._strategy = strategy

    def shipping_cost(self, order):
        # Here we use the reference of the strategy object and execute the calculate method on the order supplied
        return self._strategy.calculate(order)
