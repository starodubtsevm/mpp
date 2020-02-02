import matplotlib.pyplot as plt
import numpy as np
from const import *

"""
Fsk generator
"""
class fsk_gen(object):
	def __init__(self, fc, A, data):
		"""initialization"""
		self.fc = fc
		self.fdev = fmod
		self.A = A
		self.byte = data
		self._y = []
		self._y_mod = []
		self.k = 0
		self.temp = 0
		self.data_in = []
		
		for j in range(7, -1, -1):
			self.data_in.append((self.byte & 1<<j)>>j)
		
		for i in range(len(t)):
			if self.data_in[self.k] == 1:
				self._y.append(self.A * np.cos(2 * np.pi * (self.fc-self.fdev) * t[i]))
				self._y_mod.append(1) 
				self.temp+=1.0/fs
				if self.temp >= 1.0/self.fdev:
					self.k+=1
					if self.k>7:self.k=0
					self.temp=0
			else:	
				self._y.append(self.A * np.cos(2 * np.pi * (self.fc+self.fdev) * t[i]))
				self._y_mod.append(0)
				self.temp+=1.0/fs
				if self.temp >= 1.0/self.fdev:
					self.k+=1
					if self.k>7:self.k=0
					self.temp=0
		
	def proc_signal(self,t):
		return self._y[t]
		
	def proc_data(self,t):
		return self._y_mod[t]

