from pyrocko import util, model
from pyrocko.client import catalog

tmin = util.str_to_time ('2017-01-02 13:00:00')
tmax = util.str_to_time ('2017-01-02 14:00:00')

# create an instance of the global CMT catalog
global_cmt_catalog = catalog.GlobalCMT()

# query the catalog
events = global_cmt_catalog.get_events(
    time_range=(tmin, tmax),
    magmin=4.0,
    latmin=-5.0,
    latmax=-4.0,
    lonmin=-77,
    lonmax=-76)
	
# dump events to catalog
model.dump_events(events, 'GCMT.EQ.txt')
