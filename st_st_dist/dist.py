from pyrocko import orthodrome, model

e = model.Event(lat=10., lon=20.)
s = model.Station(lat=15., lon=120.)

# one possibility:
d = orthodrome.distance_accurate50m(e, s)
print (d/1000.)

