# You may modify the code as you like

import numpy as np
from bm import BrownianMotion
from sdeint import sdeint

def mu(x, t):
    return 0

def si(x, t):
    return 1

bm = BrownianMotion(nos=100, nop=1000)
ps = sdeint(bm, mu, si, bm.time, np.zeros(bm.nop))
print('OK')