from kpis import KPIs
from currentkpis import CurrentKPIs
from forecastkpis import ForecastKPIs

# Report on current KPI values
with KPIs() as kpis:
    with CurrentKPIs(kpis), ForecastKPIs(kpis):
        kpis.set_kpis(open_tickets=25, closed_tickets=10, new_tickets=5)
        kpis.set_kpis(100, 50, 30)
        kpis.set_kpis(50, 10, 20)

# After the context managers have exited, the observers are no loger notified
print("\nExited content managers.........\n\n")

kpis.set_kpis(150, 110, 120)
