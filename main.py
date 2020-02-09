from prepare_signal import *
from plot import *

#--------------------------------------
for i in range(sim_point):

	sample = input_signal_buf[i]
	new_sample = True

#-----main-cycle-------------------------------------------------------------
	if new_sample == True:
	
		temp1 = chan_fir.proc(sample)	# filtered signal
		filter_buf.append(temp1)

		temp2 = limiter_in.proc(temp1)	# signal after limiter
		limiter_buf.append(temp2)

		temp3 = det.proc(temp2)			# signal after fsk det
		fsk_det_buf.append(temp3)

		temp4 = det_iir.filter(temp3)	# signal after fsk det filter
		fsk_det_flt_buf.append(temp4)

		temp5 = comp_det.proc(temp4)	# signal after comparator
		comp_buf.append(temp5)

		sync,err,bit = sem_pll.proc(temp5)	#signal after pll
		sem_pll_buf.append(sync)
		sem_pll_err_buf.append(err)

		if sync == 1:
			temp12 = decoder1.proc(bit)		#signal after decoder
		else:
			pass

		new_sample = False

#-----plot-results-----------------------------------------------------------
plot (signal_buf,filter_buf,fsk_det_flt_buf,comp_buf,sem_pll_buf,sem_pll_err_buf)

plt.show()
#----------------------------------------------------------------------------
