import numpy as np
import math

class BrownianMotion:
    def __init__(self, eot=1.0, nos=10, nop=1):
        self.eot = eot
        self.nos = nos
        self.time = np.linspace(0, eot, nos+1, endpoint=True)
        self.nop = nop
        self.ps = np.zeros((self.nop,self.nos+1))
        self.dps = np.zeros((self.nop,self.nos+1))
        for path_num in range(self.nop):
            self.dps[path_num,0] = 0
            for step_num in range(self.nos):
                x = np.random.uniform(0, 1)
                y = np.random.uniform(0, 1)
                dB = math.sqrt( -2 * math.log(x) * ( self.eot/self.nos ) ) * math.cos( 2 * math.pi * y )
                self.dps[path_num,step_num+1] = dB
                self.ps[path_num,step_num+1] = self.ps[path_num,step_num] + dB
        
