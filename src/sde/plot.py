import numpy as np
import matplotlib.pyplot as plt

from environment import FIG_ROOT

def plot_ps(ps: np.ndarray, time: float, filename: str | None = None) -> list[np.ndarray]:
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
    ax.fill_between(
        time_steps,
        mean_path - std_path,
        mean_path + std_path,
        color='crimson',
        alpha=0.2,
        label='Mean ± Std',
    )  # plot std band
    ax.plot(
        time_steps,
        ps.T,
        color="steelblue",
        alpha=0.75,
        linewidth=0.8,
    ) # plot sample paths
    ax.plot(
        time_steps,
        mean_path,
        color="crimson",
        linewidth=2.5,
        label="Mean",
    ) # plot mean path
    ax.set_title(f'Sample Paths (t={time})')
    ax.set_xlabel('Time')
    ax.set_ylabel('Position')
    fig.tight_layout()

    if filename is None:
        fig.show()
    else:
        FIG_ROOT.mkdir(parents=True, exist_ok=True)
        fig.savefig(FIG_ROOT / filename)

    plt.close(fig)

    return [mean_path, std_path]

if __name__ == "__main__":
    # Test the plot_ps function with Brownian motion sample paths
    from bm import BrownianMotion

    bm = BrownianMotion(nos=100, nop=10)
    plot_ps(bm.ps, bm.eot)