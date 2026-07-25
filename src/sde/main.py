import bm
import sdeint

def mu(x, t):
    return 0

def si(x, t):
    return 0

xbm = bm.bm_class()
xps = sdeint.sdeint(xbm, mu, si, xbm.time, 0)
print('OK')