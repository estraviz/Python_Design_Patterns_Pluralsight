from observer import AbsSubject

class KPIs(AbsSubject):
    """ Inherits from the Abstract Subject. It defines properties from the values to be tracked """

    _open_tickets = -1
    _closed_tickets = -1
    _new_tickets = -1

    @property
    def open_tickets(self):
        return self._open_tickets

    @property
    def closed_tickets(self):
        return self._closed_tickets

    @property
    def new_tickets(self):
        return self._new_tickets

    # Method used to set attributes to new values
    def set_kpis(self, open_tickets, closed_tickets, new_tickets):
        self._open_tickets = open_tickets
        self._closed_tickets = closed_tickets
        self._new_tickets = new_tickets

        # When new values are set, the notify method is called
        self.notify()
