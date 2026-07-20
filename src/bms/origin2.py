import distribution.brownian_motion as brownian_motion
import feature_value.feature_value as feature_value
import visualize.visualize as visualize
import numpy as np


def run_brownian_pipeline(
	dt: float = 0.1,
	t: float = 1.0,
	dim: int = 2,
	num_samples: int = 2000,
	visualize_max_points: int = 200000,
):
	"""ブラウン運動データを生成し、feature_value で統計量を計算する。"""
	if dim < 1:
		raise ValueError("dim must be >= 1")
	if num_samples < 2:
		raise ValueError("num_samples must be >= 2")
	if dt <= 0 or t <= 0:
		raise ValueError("dt and t must be > 0")

	samples = brownian_motion.generate_brownian_motion_data(
		dt=dt,
		t=t,
		dim=dim,
		num_samples=num_samples,
	)

	# mycovs は [次元, サンプル数] を想定するため転置して渡す
	cov_matrix = feature_value.mycovs(samples.T)
	means = [feature_value.mymean(samples[:, d]) for d in range(dim)]
	stds = [feature_value.mysd(samples[:, d]) for d in range(dim)]

	plot_samples = samples
	if samples.shape[0] > visualize_max_points:
		indices = np.random.choice(samples.shape[0], size=visualize_max_points, replace=False)
		plot_samples = samples[indices]

	visualize.visualize_distribution(plot_samples)

	return {
		"samples": samples,
		"plot_samples": plot_samples,
		"means": means,
		"stds": stds,
		"cov_matrix": cov_matrix,
	}


if __name__ == "__main__":
	result = run_brownian_pipeline(dt=0.1, t=1.0, dim=2, num_samples=2000)
	print("means:", result["means"])
	print("stds:", result["stds"])
	print("cov_matrix:\n", result["cov_matrix"])
