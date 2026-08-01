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

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(time_steps, ps.T, color='lightgray', alpha=0.5, label='Sample Paths')  # plot all sample paths
    ax.plot(time_steps, mean_path, color='black', label='Mean Path')  # plot mean path
    ax.fill_between(
        time_steps,
        mean_path - std_path,
        mean_path + std_path,
        color='blue',
        alpha=0.2,
        label='Mean ± Std',
    )  # plot std band
    ax.set_title(f'Sample Paths (t={time})')
    ax.set_xlabel('Time')
    ax.set_ylabel('Position')
    ax.legend()
    fig.tight_layout()

    if filename is None:
        plt.show()
    else:
        FIG_ROOT.mkdir(parents=True, exist_ok=True)
        fig.savefig(FIG_ROOT / filename)

    plt.close(fig)

    return [mean_path, std_path]