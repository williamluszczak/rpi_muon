#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import sys

infile = str(sys.argv[1])
data = np.loadtxt(infile)
wf = np.transpose(data)

vs = wf[0]
ts = wf[1]

edge_times = []
prev_v = 0
for i in range(0,len(ts)):
    samp_v = vs[i]
    samp_t = ts[i]
    if samp_v != prev_v and samp_v==1.0:
        print(samp_t, samp_v)
        edge_times.append(samp_t)
    prev_v = samp_v

min_t = edge_times[0]
max_t = edge_times[-1]
num = len(edge_times)

print("start_t, stop_t, n_ev, rate [Hz]")
print(min_t, max_t, num, num/(max_t-min_t))
