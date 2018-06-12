from pyrocko import io, util

trace = io.load('DISPL.GRMI.BHZ')
tr = trace[0]
tr.shift (15)
io.save (tr, 'SH.DISPL.GRMI.BHZ')
