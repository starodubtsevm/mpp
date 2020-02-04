from const import *
import numpy as np
import random

#---------------------------------------
class white_noise(object):

	def __init__(self, A):
		"""initialization"""
		self.ampl = A
		self.noise = self.ampl*np.random.randn(len(t))

	def proc(self,i):
		"""noise sample"""
		return self.noise[i]

