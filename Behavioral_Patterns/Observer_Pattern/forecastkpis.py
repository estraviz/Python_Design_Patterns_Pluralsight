from observer import AbsObserver

class ForecastKPIs(AbsObserver):
    # Quite similar to the CurrentKPIs module but for the display method

    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def update(self):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets

        self.display()

    def display(self):
        print("Forecast open tickets: {}".format(self.open_tickets))
        print("New tickets expected in one hour: {}".format(self.new_tickets))
        print("Tickets expected to be closed in next hour: {}\n".format(self.closed_tickets))

    def __exit__(self, exc_type, exc_value, traceback):
        self._kpis.detach(self)
