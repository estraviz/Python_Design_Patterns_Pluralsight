from observer import AbsObserver

class CurrentKPIs(AbsObserver):
    """ Inherits from Abstract Observer and takes a reference to the subject in the constructor """

    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def update(self):
        # It uses the reference of the subject in the constructor to retrieve the needed values from the subject's properties
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets

        # Display the results
        self.display()

    def display(self):
        print("Current open tickets: {}".format(self.open_tickets))
        print("New tickets in last hour: {}".format(self.new_tickets))
        print("Tickets closed in last hour: {}\n".format(self.closed_tickets))

    def __exit__(self, exc_type, exc_value, traceback):
        # Concrete observer that implements the __exit__ method. Python ensures that it will run when the context ends
        # Detach the Observer from the Subject
        self._kpis.detach(self)
