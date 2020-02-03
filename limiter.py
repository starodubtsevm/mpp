
#---------------------------------------
class limiter(object):

	def __init__(self, out_min, out_max):
		"""initialization"""
		self.out_min = out_min
		self.out_max = out_max

	def proc(self, sample):
		"""limiting"""
		if sample >= self.thres_max:
			return self.out_max
		if sample <= self.thres_min:
			return self.out_min
