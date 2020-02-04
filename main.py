import matplotlib.pyplot as plt
import numpy as np
import math as m
from time import time
from fir_filter import *
from fsk_gen2 import *
from fsk_delay_det import *
from comparator import *
from limiter import *
from pll import *
from white_noise_gen import *
from const import *

#--------------------------------------
# main
#--------------------------------------
noise1 = white_noise(560)
fsk1 = fsk_gen(525,360,0x2c)	# source fsk signal
limiter_in = limiter (-2000,2000)	# input limiter
chan_fir = fir(h_bpf_525)	#.channel filter
det = fsk_det(33)		# fsk detector @ 525Hz
det_fir = fir(h_lpf_20)		#.fsk detector filter
comp_det = comparator(250,-250, 1)	# comparator after fsk detector filter
pll1 = pll(1)

noise_buf         =  []
signal_buf        =  []
filter_buf        =  []
limiter_buf       =  []
fsk_det_buf       =  []
fsk_det_flt_buf   =  []
comp_buf          =  []
pll_edge_buf      =  []

#tic = time()
for i in range(sim_point):

	temp00 = noise1.proc(i)		# noise
	noise_buf.append(temp00)

	temp0 = fsk1.proc_signal(i)	# fsk signal
	signal_buf.append(temp0)

	temp0 = temp0 +temp00		# signal + noise

	temp1 = chan_fir.proc(temp0)	# filtered signal
	filter_buf.append(temp1)

	temp2 = limiter_in.proc(temp1)	# signal after limiter
	limiter_buf.append(temp2)

	temp3 = det.proc(temp2)		# signal after fsk det
	fsk_det_buf.append(temp3)

	temp4 = det_fir.proc(temp3)	# signal after fsk det filter
	fsk_det_flt_buf.append(temp4)

	temp5 = comp_det.proc(temp4)	# signal after comparator
	comp_buf.append(temp5)
	
	temp6 = pll1.edge(temp5)	# signal after eage finder
	pll_edge_buf.append(temp6)

print('RMS noise value ' + str(np.sqrt(np.mean(noise_buf)**2)))	# RMS noise value

print('RMS signal value '+ str(np.sqrt(np.mean(signal_buf)**2)))	# RMS signal value



#toc = time()
#print(toc - tic)

fig, axs = plt.subplots(3, 2, sharex = True)
fig.subplots_adjust(hspace=0.1)

axs[0,0].plot(t, limiter_buf)
axs[0,0].set_xlabel('Limmiter output')

axs[1,0].plot(t, fsk_det_flt_buf)
axs[1,0].set_xlabel('FSK detector output (after the filter)')

axs[2,0].plot(t, comp_buf)
axs[2,0].set_ylim(-1, 2)
axs[2,0].set_xlabel('Comparator output')

#axs[0,1].plot(t, res4)
#axs[0,1].set_xlabel('Edge output')

axs[1,1].plot(t, pll_edge_buf)
axs[1,1].set_ylim(-1, 2)
axs[1,1].set_xlabel('Edge output')

axs[2,1].plot(t, noise_buf)
axs[2,1].set_xlabel('Noise output')

plt.show()

