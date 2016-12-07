import abc

class AbsObserver(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update(self, value):
        pass

    # The following two methods are required to take the class definition into a context manager
    def __enter__(self):
        return self

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        # Note that the exit method is abstract, so it must be implemented by the concrete observer
        pass
