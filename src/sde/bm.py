import numpy as np

class bm_class:
    def __init__(self):
        self.eot = 1.0
        self.nos = 10
        self.time = np.linspace(0, self.eot, self.nos+1)
        self.nop = 1
        self.ps = np.zeros((self.nop,self.nos))
        self.dps = np.zeros((self.nop,self.nos))