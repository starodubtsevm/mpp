
#---------------------------------------
class comparator(object):

	def __init__(self, threshold_min,threshold_max):
		"""initialization"""
		self.thres_min = threshold_min
		self.thres_max = threshold_max

	def proc(self, sample):
		"""comparing"""
		if sample >= self.thres_max:
			return 1
		if sample <= self.thres_min:
			return 0


