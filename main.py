import matplotlib.pyplot as plt
import numpy as np
from time import time
from fir_filter import *
from fsk_gen2 import *
from fsk_delay_det import *
from comparator import *
from const import *

#--------------------------------------
# main
#--------------------------------------

fsk1 = fsk_gen(525,36,0x2c)
chan_fir = fir(h_bpf_525)
det = fsk_det(31,fs)
det_fir = fir(h_lpf_20)
comp_det = comparator(50,-50)


res1=[]
res2=[]
res3=[]

#tic = time()
for i in range(sim_point):
	
	temp = fsk1.proc_signal(i)

	temp2 = chan_fir.proc(temp)
	res1.append(temp2)

	temp3 = det.proc(temp2)
	res2.append(temp3)

	temp4 = det_fir.proc(temp3)
	res3.append(temp4)

#toc = time()
#print(toc - tic)
	
fig, axs = plt.subplots(3, 2, sharex=True)
fig.subplots_adjust(hspace=0.1)

axs[0,0].plot(t, res1)
axs[0,0].set_xlabel('Channel filter output')

axs[1,0].plot(t, res2)
axs[1,0].set_xlabel('FSK detector output (after the filter)')

axs[2,0].plot(t, res3)
axs[2,0].set_ylim(-1, 2)
axs[2,0].set_xlabel('Comparator output')

plt.show()

