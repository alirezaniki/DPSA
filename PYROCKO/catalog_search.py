from pyrocko import util
from pyrocko.client import catalog

tmin = util.ctimegm ('2018-06-11 01:18:00')
tmax = util.ctimegm ('2018-06-11 01:19:00')
mag = 4.5

# download event information from GEOFON web page

geofon = catalog.Geofon()
event_names = geofon.get_event_names(
    time_range=(tmin, tmax),
    magmin=mag)

for event_name in event_names:
    event = geofon.get_event(event_name)
    print(event)
