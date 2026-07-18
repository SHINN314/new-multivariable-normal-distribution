import numpy as np

class bm:
    def __init__(self):
        self.eot = 1.0
        self.nos = 10
        self.time = float(self.nos)
        self.nop = 1
        self.ps = np.zeros(self.nop,self.nos)
        self.dps = np.zeros(self.nop,self.nos)