import matplotlib.pyplot as plt
import numpy as np
from const import *

def plot (signal_buf,filter_buf,fsk_det_flt_buf,comp_buf,sem_pll_buf,sem_pll_err_buf):

	fig, axs = plt.subplots(3, 2)
	fig.subplots_adjust(hspace=0.1)

	axs[0,0].plot(t, signal_buf)
	axs[0,0].set_xlabel('Input signal')

	axs[1,0].plot(t, filter_buf)
	#axs[1,0].plot(t, limiter_buf)
	axs[1,0].set_xlabel('After channel filter output')

	axs[2,0].plot(t, fsk_det_flt_buf)
	#axs[2,0].plot(t, fsk_det_buf)
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
