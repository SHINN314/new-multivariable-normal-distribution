import numpy as np
import matplotlib.pyplot as plt

from environment import FIG_ROOT

def plot_ps(ps: np.ndarray, time: float, filename: str | None) -> list[np.ndarray]:
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

    plt.plot(time_steps, ps.T, color='lightgray', alpha=0.5, label='Sample Paths') # plot all sample paths
    plt.plot(time_steps, mean_path, color='black', label='Mean Path') # plot mean path
    plt.fill_between(time_steps, mean_path - std_path, mean_path + std_path, color='blue', alpha=0.2, label='Std Path') # plot std path
    plt.title(f'Sample Paths of Brownian Motion (t={time})')
    plt.xlabel('Time')
    plt.ylabel('Position')
    
    if filename is None:
        plt.show()
    else:
        plt.savefig(FIG_ROOT / filename)
        plt.clf()
        plt.close()

    return [mean_path, std_path]