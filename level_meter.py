from const import *
from prepare_signal import*
from IIR2Filter import *
from FIR2Filter import *

class level_meter(object):

    def __init__(self):
        """initialization"""
        self.Fcar = 525 # несущая КРЛ
        self.fs = fs
        self.A = 1
        self.k = 2 * np.cos(2 * np.pi * self.Fcar / self.fs)
        self.X0_0 = 0
        self.X1_0 = 0
        self.X2_0 = self.A * np.sin(2 * np.pi * self.Fcar / self.fs)
        self.cycle_count = 0
        self.filt2 = IIR2Filter(16, [5], 'low',design='cheby1',rs = 2, fs=fs)
        self.filt = FIR2Filter(256, 1,15, fs=fs)

    def local_gen(self,t):
        '''Локальный генератор sin'''
        self.cycle_count = self.cycle_count + 1
        self.X0_0 = self.k*self.X1_0-self.X2_0
        y_0 = self.X0_0
        self.X2_0 = self.X1_0
        self.X1_0 = self.X0_0

        return y_0

    def proc(self, sample):
        """ Измерение уровня входного сигнала"""

        sig = sample*self.local_gen(t)

        temp = self.filt2.filter(sig)
        f = abs(temp)
        f_out = self.filt2.filter(f)

        return f_out


