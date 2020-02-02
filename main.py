import matplotlib.pyplot as plt
import numpy as np
from fir_filter import *
from fsk_gen2 import *
from fsk_delay_det import *
from const import *

#--------------------------------------
# main
#--------------------------------------

fsk1 = fsk_gen(525,16,0x2c)
chan_fir = fir(h)
det = fsk_det(31,fs)
#det_fir = fir(h)

res=[]
res2=[]

for i in range(sim_point):

	temp = fsk1.proc_signal(i)
	res2.append(fsk1.proc_data(i))
	temp2 = chan_fir.proc(temp)
	res.append(det.proc(temp2))
	
	
plt.plot(t, res)
plt.plot(t,res2)
plt.show()

