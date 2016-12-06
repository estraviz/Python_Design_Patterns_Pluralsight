from abc import ABCMeta, abstractmethod

class AbsStrategy(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def calculate(self, order):
        # We define here an abstract method that will be implemented within concrete strategies that we define later
        """ Calculate shipping cost """
