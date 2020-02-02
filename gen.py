#from scipy import signal
import numpy as np


def gen_sin(fsignal,t,Ampl):

	samples = Ampl*np.sin(2 * np.pi * fsignal * t + 0.001)
	return samples
