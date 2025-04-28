#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

inp = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(inp, GPIO.IN)

t1 = 0
while(True):
    t2 = time.time()
    dt = t2-t1
    print(GPIO.input(inp), t2)
    t1 = t2
