import matplotlib.pyplot as plt
import numpy as np
from time import time
from fir_filter import *
from fsk_gen2 import *
from fsk_delay_det import *
from comparator import *
from limiter import *
from const import *

#--------------------------------------
# main
#--------------------------------------

fsk1 = fsk_gen(525,36,0x2c)	# source fsk signal
chan_fir = fir(h_bpf_525)	#.channel filter
det = fsk_det(31,fs)		# fsk detector @ 525Hz
det_fir = fir(h_lpf_20)		#.fsk detector filter
comp_det = comparator(50,-50)	# comparator after fsk detector filter
limiter_in = limiter (200,-200)	# input limiter

res0 =[]
res1 =[]
res2 =[]
res3 =[]
res4 =[]
res5 =[]

#tic = time()
for i in range(sim_point):
	
	temp0 = fsk1.proc_signal(i)

	temp1 = limiter.proc(temp0)
	res0.append(temp1)

	temp2 = chan_fir.proc(temp1)
	res1.append(temp2)

	temp3 = det.proc(temp2)
	res2.append(temp3)

	temp4 = det_fir.proc(temp3)
	res3.append(temp4)

#toc = time()
#print(toc - tic)

fig, axs = plt.subplots(3, 2, sharex = True)
fig.subplots_adjust(hspace=0.1)

axs[0,0].plot(t, res1)
axs[0,0].set_xlabel('Channel filter output')

axs[1,0].plot(t, res2)
axs[1,0].set_xlabel('FSK detector output (after the filter)')

axs[2,0].plot(t, res3)
axs[2,0].set_ylim(-1, 2)
axs[2,0].set_xlabel('Comparator output')

#axs[0,1].plot(t, res4)
#axs[0,1].set_xlabel('PLL output')

#axs[1,1].plot(t, res5)
#axs[1,1].set_xlabel('???? output')

#axs[2,1].plot(t, res6)
#axs[2,1].set_xlabel('???? output')

plt.show()

