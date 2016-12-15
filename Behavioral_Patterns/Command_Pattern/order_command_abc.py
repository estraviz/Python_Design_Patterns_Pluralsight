import abc

class AbsOrderCommand(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractproperty
    def description(self):
        pass
