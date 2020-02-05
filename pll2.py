from const import *

#---------------------------------------
class pll2(object):

	def __init__(self, delay):
		"""initialization"""

		self.delay = delay * 1e-3
		tick = 1.0/fs
		self.tick = 0
		self._buff_size = int(self.delay/tick)
		self._data = [0]*self._buff_size
		self.edge_val = 0
		
		self.syncCount = LEN_OF_BIT
		self.phErrCount = 0
		self.phErr = 0
		self.syncro = 0
		self.receiveFlag = 1
		self.edgeFlag = 0
		self.frontDet = 0

	def proc (self,sample):

		"""find edge """
		self.frontDet = self.frontDet << 1
		self.frontDet |= sample

		"""find @ check syncro """
		self.syncCount -= 1
		if (self.syncCount != 0):
			self.phErrCount += 1
			if (self.phErrCount >= LEN_OF_BIT) or (self.frontDet & 0x0003 == 0x0001):
				self.phErrCount = 0
			self.syncro = 0
			print ("first part  " + str(self.syncCount))
			return self.syncro, self.phErrCount

		else:
			self.phErr = self.phErrCount - LEN_OF_BIT/2

			if (abs(self.phErr) >= LEN_OF_BIT *3 / 200):
				if(abs(self.phErr) >= LEN_OF_BIT * 3 * 50):
					if(self.receiveFlag == 1):
						if(self.phErr < 0): 
							self.sincCount = LEN_OF_BIT+2
						else:
							self.syncCount = LEN_OF_BIT-2
					else:
						self.syncCount = LEN_OF_BIT-5-self.phErr*1/8
				else: 
					if (self.phErr < 0): 
						self.sincCount = LEN_OF_BIT +2
					else:
						self.syncCount = LEN_OF_BIT-2
			else:
				self.syncCount = LEN_OF_BIT
			self.syncro = 1
			print ("second part")
			return self.syncro,self.phErrCount


