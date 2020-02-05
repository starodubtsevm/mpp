import matplotlib.pyplot as plt
import numpy as np
import math as m
from time import time
from fir_filter import *
from fsk_gen2 import *
from fsk_delay_det import *
from comparator import *
from limiter import *
from pll2 import *
from white_noise_gen import *
from const import *

#--------------------------------------
# main
#--------------------------------------
noise1 = white_noise(360)
fsk1 = fsk_gen(525,360,0x2c)	# source fsk signal
limiter_in = limiter (-2000,2000)	# input limiter
chan_fir = fir(h_bpf_525)	#.channel filter
det = fsk_det(33)		# fsk detector @ 525Hz
det_fir = fir(h_lpf_20)		#.fsk detector filter
comp_det = comparator(350,-350, 1)	# comparator after fsk detector filter
sem_pll = pll2(1)

noise_buf         =  []
signal_buf        =  []
filter_buf        =  []
limiter_buf       =  []
fsk_det_buf       =  []
fsk_det_flt_buf   =  []
comp_buf          =  []
pll_edge_buf      =  []
pll_local_gen_buf =  []
pll_phase_det_buf =  []
sem_pll_buf       =  []
sem_pll_err_buf   =  []

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

#	temp6 = pll1.edge(temp5)	# signal after edge finder
#	pll_edge_buf.append(temp6)

#	temp7 = pll1.local_gen()
#	pll_local_gen_buf.append(temp7)

	temp8,temp9 = sem_pll.proc(temp5)
	sem_pll_buf.append(temp8)
	sem_pll_err_buf.append(temp9)
#rms_sig = np.sqrt(np.mean(np.square(signal_buf)))
#print ("RMS signal "+ str(rms_sig))

#rms_noise = np.sqrt(np.mean(np.square(noise_buf)))
#print ("RMS noise "+ str(rms_noise))

#rms_noise_filt = np.sqrt(np.mean(np.square(filter_buf)))
#print ("RMS noise after channel filer "+ str(rms_noise_filt))

fig, axs = plt.subplots(3, 2, sharex = True)
fig.subplots_adjust(hspace=0.1)

axs[0,0].plot(t, signal_buf)
axs[0,0].set_xlabel('Input signal')

axs[1,0].plot(t, filter_buf)
axs[1,0].set_xlabel('After channel filter output')

axs[2,0].plot(t, fsk_det_flt_buf)
axs[2,0].set_xlabel('After fsk det and filter output')

axs[0,1].plot(t, comp_buf)
axs[0,1].set_ylim(-0.5, 2)
axs[0,1].set_xlabel('Comp output')

axs[1,1].plot(t, sem_pll_buf)
axs[1,1].set_ylim(-0.5, 2)
axs[1,1].set_xlabel('Sync Pll sem output')

axs[2,1].plot(t, sem_pll_err_buf)
#axs[2,1].set_ylim(-0.5, 2)
axs[2,1].set_xlabel('Error Pll sem output')

plt.show()

