import matplotlib.pyplot as plt
import numpy as np

"""
Fsk generator
"""
class fsk_gen(object):
	def __init__(self, fc,fdev,A,data):
		"""initialization"""
		self.fc = fc
		self.fdev = fdev
		self.A = A
		self.data = data
		self.N = self.fdev * t_sim #how many bits to send
		self.sim_point = int(t_sim/(1.0/fs)) 
		t = np.linspace(0, t_sim, sim_point) 

	def proc(self)
		data_in = np.random.random_integers(0,1,N)
		data_out = []
		k = 0
		temp = 0
		y = []
		for i in range(len(t)):
			if data_in[k] == 1:
				y.append(A * np.cos(2 * np.pi * (fc+fdev) * t[i]))
				temp+=1.0/fs
				if temp >= 1.0/fdev:
					k+=1
					temp=0

			else:	
				y.append(A * np.cos(2 * np.pi * (fc-fdev) * t[i]))
				temp+=1.0/fs
				if temp >= 1.0/fdev:
					k+=1
					temp=0
		return y
