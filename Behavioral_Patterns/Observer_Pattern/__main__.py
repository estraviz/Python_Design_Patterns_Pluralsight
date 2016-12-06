from kpis import KPIs
from currentkpis import CurrentKPIs
from forecastkpis import ForecastKPIs

# Report on current KPI values. We instantiate the KPIs object, which is our subject object
kpis = KPIs()

# instantiate the two observer objects
currentKPIs = CurrentKPIs(kpis)
forecastKPIs = ForecastKPIs(kpis)

# We set the kpis to various values
kpis.set_kpis(open_tickets=23, closed_tickets=10, new_tickets=7)
kpis.set_kpis(100, 60, 20)
kpis.set_kpis(40, 20, 10)

# The first observer is detached and new values are set again
print("\nDetaching the currentKPIs observer...\n\n")
kpis.detach(currentKPIs)
kpis.set_kpis(open_tickets=111, closed_tickets=33, new_tickets=11)
