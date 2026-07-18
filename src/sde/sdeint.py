from bm import bm_class
import numpy as np
from typing import Callable

# X_(i+1) = mu(X_i, t_i) Dt + sigma(X_i, t_i) DB

def sdeint(bm: bm_class, mu: Callable[[float, float], float], sigma: Callable[[float, float], float], t: np.ndarray, y0: np.ndarray):
    assert y0.shape == (bm.nop)
    assert t.shape == (bm.nos)

    x = np.zeros((bm.nop, bm.nos))
    x[:, 0] = y0
    for i in range(bm.nos):
        for p in range(bm.nop):
            x[p, i+1] = mu(x[p, i], t[i]) * (t[i+1] - t[i]) + sigma(x[p, i], t[i]) * bm.dps[p, i]
    return x
