#!/usr/bin/env python

from pyrocko import io
import sys

for filename in sys.argv[1:]:
			traces = io.load(filename, format='sac')
			out_filename = filename
			io.save(traces, out_filename)
