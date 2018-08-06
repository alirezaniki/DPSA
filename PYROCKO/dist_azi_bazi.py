from pyrocko import orthodrome, model

e = model.Event(lat=-8.33, lon=116.48)
s = model.Event(lat=-21.57670, lon=119.83620)
dist = orthodrome.distance_accurate50m(e, s)
print(dist/1000)

# Azimuth and Back Azimuth
az = orthodrome.azibazi(e, s)
print (az)
