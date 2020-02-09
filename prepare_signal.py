
from fir_filter import *
from fsk_gen2 import *
from fsk_delay_det import *
from comparator import *
from limiter import *
from pll2 import *
from white_noise_gen import *
from code import*
from IIR2Filter import *
from decode import *

noise1 = white_noise(0)
fsk1 = fsk_gen(525,235*1,0x2c)	# source fsk signal
fsk2 = fsk_gen(475,235*5,0x3c)	# interference fsk signal 1
fsk3 = fsk_gen(575,235*5,0x3c)	# interference fsk signal 2
limiter_in = limiter (-2,2)	# input limiter
chan_fir = fir(h_bpf_525)	#.channel filter
det = fsk_det(19.55)		# fsk detector #19.55@525
det_iir = IIR2Filter(4, [10], 'low',design='cheby1',rs = 2, fs=fs)
comp_det = comparator(-0.1,0.1, 1)# comparator after fsk detector filter
sem_pll = pll2()
decoder1 = decode()

noise_buf         =  []
signal_buf        =  []
signal2_buf       =  []
filter_buf        =  []
limiter_buf       =  []
fsk_det_buf       =  []
fsk_det_flt_buf   =  []
comp_buf          =  []
sem_pll_buf       =  []
sem_pll_err_buf   =  []
input_signal_buf  =  []


for i in range(sim_point):
#--Preparing input signal + noise------------------------------------
	fsk_signal = fsk1.proc_signal(i)
	signal_buf.append(fsk_signal)
	
	fsk_int_1  = fsk2.proc_signal(i)
	
	fsk_int_2  = fsk3.proc_signal(i)
	
	noise = noise1.proc(i)		# noise
	noise_buf.append(noise)

	input_signal = 1*fsk_signal + 1*fsk_int_1 + 1*fsk_int_2 + 1*noise
	input_signal_buf.append(input_signal)
