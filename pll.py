from const import *

#---------------------------------------
class pll(object):

	def __init__(self, delay):
		"""initialization"""
		self.delay = delay * 1e-3
		tick = 1.0/fs
		self._buff_size = int(self.delay/tick)
		self._data = [0]*self._buff_size
		self.tick = 100

	def edge(self, sample):
		"""demodulation"""
		self._data.insert(0,sample)
		self._data.pop()
		y = self._data[self._buff_size - 1] != sample
		#if y == 1: self.tick = 0
		return y

	def local_gen(self):
		"""Local generator"""

		if 0 <= self.tick < int(0.5*(1.0/fmod)/(1.0/fs)):
			self.tick+=1
			return 1
			
		if self.tick == int(0.5*(1.0/fmod)/(1.0/fs)):
			self.tick+=1
			return 0

		if int(0.5*(1.0/fmod)/(1.0/fs)) < self.tick < int(1.0/fmod/(1.0/fs)):
			self.tick+=1
			return 0

		if self.tick == int((1.0/fmod)/(1.0/fs)):
			self.tick = 0
			return 0

