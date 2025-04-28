#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('test.txt')
data = data[:-1]
dts = np.diff(data)
badevs = np.where(dts<25e-6)
print(len(badevs[0]))

firstev = data[0]
lastev = data[-1]
livetime = lastev-firstev
N = len(data)-len(badevs[0])
print(N, livetime, N/livetime, len(data)/livetime, len(badevs))

diffhist, diffbins = np.histogram(dts, bins = np.linspace(0, 0.1, 50))
diffhist = np.append(diffhist, 0)
plt.plot(diffbins, diffhist, drawstyle='steps-post')
plt.semilogy()
plt.xlabel('dt')
plt.ylabel('N')
plt.title('Time measured between consecutive pulses')
plt.xlim(0,0.1)
plt.ylim(0,)
#plt.show()
