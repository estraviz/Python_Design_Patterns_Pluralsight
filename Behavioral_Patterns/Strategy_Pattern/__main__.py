from strategy import Order, ShippingCost
from strategy import FedExStrategy, UPSStrategy, PostalStrategy

order = Order()

# Test FedeEx shipping
strategy_fedex = FedExStrategy()

# Another possibility, with a function:
#def fedex_strategy(order):
#    return 3.0
#
#strategy_fedex = fedex_strategy

cost_calculator_fedex = ShippingCost(strategy_fedex)

# A variation to this with a lambda expression:
# cost_calculator_fedex = ShippingCost(lambda order: 3.00)

cost_fedex = cost_calculator_fedex.shipping_cost(order)
assert cost_fedex == 3.0

# Test UPS Shipping
strategy_ups = UPSStrategy()
cost_calculator_ups = ShippingCost(strategy_ups)
cost_ups = cost_calculator_ups.shipping_cost(order)
assert cost_ups == 4.0

# Test Postal Shipping
strategy_postal = PostalStrategy()
cost_calculator_postal = ShippingCost(strategy_postal)
cost_postal = cost_calculator_postal.shipping_cost(order)
assert cost_postal == 5.0

# Everything OK if we reach this point
print("All tests passed!!")
