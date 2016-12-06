import abc

class MyABC(object):
    """ Abstract Base Class (aka Interface) Definition """

    # Make class abstract
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def do_something(self, value):
        """ Required method """

    @abc.abstractproperty
    def some_property(self):
        """ Required property """
