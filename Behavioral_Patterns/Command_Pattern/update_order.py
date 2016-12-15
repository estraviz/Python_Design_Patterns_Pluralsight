from command_abc import AbsCommand
from order_command_abc import AbsOrderCommand

class UpdateOrder(AbsCommand, AbsOrderCommand):
    name = 'UpdateQuantity'
    description = 'UpdateQuantity number'

    def __init__(self, args):
        self.newqty = args[1]

    def execute(self):
        oldqty = 5
        # Simulate database UpdateOrder
        print('Updated Database')

        # Simmulate logging the update
        print('Logging: Updated quantity from %s to %s' %(oldqty, self.newqty))
