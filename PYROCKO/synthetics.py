import os

from pyrocko.gf import LocalEngine, Target, DCSource, ws
from pyrocko import trace, io
from pyrocko.marker import PhaseMarker

# The store we are going extract data from:
store_id = 'kazeroon'

# We need a pyrocko.gf.Engine object which provides us with the traces
# extracted from the store. In this case we are going to use a local
# engine since we are going to query a local store.
engine = LocalEngine(store_superdirs=['/home/alireza/Kiwi/GFDB'])

# Define a list of pyrocko.gf.Target objects, representing the recording
# devices. In this case one station with a three component sensor will
# serve fine for demonstation.
channel_codes = 'ENZ'
targets = [
    Target(
        lat=36.21,
        lon=48.22,
        store_id=store_id,
        codes=('', 'CVD', '', channel_code))
    for channel_code in channel_codes]

# Let's use a double couple source representation.
source_dc = DCSource(
    lat=34.00,
    lon=45.00,
    depth=10000,
    strike=170,
    dip=35,
    rake=50,
    magnitude=5.6)

# Processing that data will return a pyrocko.gf.Reponse object.
response = engine.process(source_dc, targets)

# This will return a list of the requested traces:
synthetic_traces = response.pyrocko_traces()
io.save(synthetic_traces, 'DISPL.CVD.mseed')
