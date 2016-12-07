import abc
from observer import AbsObserver

class AbsSubject(object):
    """ Abstract Subject base class. It is also now a context manager """

    __metaclass__ = abc.ABCMeta
    _observers = set()

    # These are the three required methods. In this case, these are not abstract but implementations
    def attach(self, observer):
        # Attach checks the type of the observer argument
        if not isinstance(observer, AbsObserver):
            raise TypeError('Observer not derived from AbsObserver')

        # Add the new observer to the set
        self._observers |= {observer}
        # Note to self: |= a.k.a. pipe equal operator is the bit-wise OR equal operator

    def detach(self, observer):
        # Removes the observer from the set
        self._observers -= {observer}

    def notify(self, value=None):
        # Loops through the observers in the set and invokes the update method in each one
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Here we implement the __exit__ method and clear the set of observers, thus removing any dangling references
        self._observers.clear()
