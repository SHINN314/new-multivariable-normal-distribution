import numpy as np
import matplotlib.pyplot as plt

from bm import bm

def plot_ps(ps: np.ndarray, time: float, filename: str | None) -> list[float, float]:
    """Plot sample paths, mean and std path.
    Show or save the graph.
    Make sure to label the conditions in the graph.
    
    Parameters
    ----------
    ps: np.ndarray
        Sample paths.
    time: float
    filename: str | None
        If filename is None, show the graph, else save the graph to filename.
    """

    mean_path = np.mean(ps, axis=0)
    std_path = np.std(ps, axis=0)

    time_steps = np.linspace(0, time, ps.shape[1])

    plt.plot(time_steps, ps.T)
    plt.title(f'Sample Paths of Brownian Motion (t={time})')
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.legend()
    
    if filename is None:
        plt.show()
    else:
        plt.savefig(filename)
        plt.close()

    return [mean_path, std_path]