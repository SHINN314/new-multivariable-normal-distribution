import numpy as np
import matplotlib.pyplot as plt

from environment import FIG_ROOT

def plot_ps(ps: np.ndarray, time: np.ndarray, filename: str | None = None) -> list[np.ndarray]:
    """Plot sample paths, mean and std path.
    Show or save the graph.
    Make sure to label the conditions in the graph.
    
    Parameters
    ----------
    ps: np.ndarray
        Sample paths.
    time: np.ndarray
        Time steps.
    filename: str | None
        If filename is None, show the graph, else save the graph to filename.
    """

    mean_path = np.mean(ps, axis=0)
    std_path = np.std(ps, axis=0)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(
        time,
        ps.T,
        color="steelblue",
        alpha=0.75,
        linewidth=0.8,
    ) # plot sample paths
    ax.plot(
        time,
        mean_path,
        color="crimson",
        linewidth=2.5,
        label="Mean",
    ) # plot mean path
    ax.plot(
        time, 
        mean_path + std_path,
        color='crimson',
        alpha=0.5,
        linewidth=1.5,
    ) # plot mean + std path
    ax.plot(
        time,
        mean_path - std_path,
        color='crimson',
        alpha=0.5,
        linewidth=1.5,
    ) # plot mean - std path
    ax.set_title(f'Sample Paths (t={time[-1]})')
    ax.set_xlabel('Time')
    ax.set_ylabel('Position')
    fig.tight_layout()

    if filename is None:
        plt.show()
    else:
        FIG_ROOT.mkdir(parents=True, exist_ok=True)
        fig.savefig(FIG_ROOT / filename)

    plt.close(fig)

    return [mean_path, std_path]

if __name__ == "__main__":
    # Test the function with random data
    time = np.linspace(0, 1, 100)
    ps = np.random.randn(10, 100)  # 10 sample paths
    plot_ps(ps, time)