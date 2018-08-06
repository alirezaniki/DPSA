from pyrocko import orthodrome

# arguments: origin lat, origin lon, north [m], east [m]
lat, lon = orthodrome.ne_to_latlon(36.55, 54.23, 178500, -12000)

print(lat, lon)
