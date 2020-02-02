
#---------------------------------------
class fsk_det(object):

	def __init__(self, delay,fs):
		"""initialization"""
		self.delay = delay * 1e-3
		tick = 1.0/fs
		self._buff_size = int(self.delay/tick)
		self._data = [0]*self._buff_size
		self._index = 0

	def proc(self, sample):
		"""demodulation"""
		self._data.insert(0,sample)
		self._data.pop()
		y = self._data[self._buff_size - 1] * sample
		self._index += 1
		#print(sample,y,self._index)
		return y
			
