#!/usr/bin/env python

#import RPi.GPIO as GPIO
import time
import sys
import numpy as np

inp = int(sys.argv[1])
outdir = 'evtfiles/'

GPIO.setmode(GPIO.BOARD)
GPIO.setup(inp, GPIO.IN)

edge_times = []
t1 = 0
prev_v = 0
starttime = time.time()
samp_t = time.time()
print("Starting run at ", starttime)
#One run is 900 seconds (15 min)
while(samp_t-starttime<900.): 
  try:
    samp_v = GPIO.input(inp)
#    samp_v = np.random.randint(0,2)
    if samp_v != prev_v and samp_v==1.0:
        samp_t = time.time()
        print(samp_t, samp_v)
        edge_times.append(samp_t)
    prev_v = samp_v
  except KeyboardInterrupt:
    print("Interrupted, writing file and exiting")
    endtime = time.time()
    np.save(outdir+'/eventfile_%s_%s_%s.npy'%(inp, starttime, endtime), edge_times)
    sys.exit()

endtime=time.time()
print("Reached end of run, writing file and exiting")
np.save(outdir+'/eventfile_%s_%s_%s.npy'%(inp, starttime, endtime), edge_times)
