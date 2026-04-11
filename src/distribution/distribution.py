import numpy as np

def buraunian_motion(dt, t) -> float:
    sample_size = int(t / dt)
    t_list = np.arange(0, t, dt)
    dW_list = np.sqrt(t_list) * np.random.randn(sample_size)
    W_list = np.cumsum(dW_list)

    return W_list[-1]
    