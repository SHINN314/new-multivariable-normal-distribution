import distribution.t5ugu.main as dist_main
import feature_value.feature_value as feature_value
import visualize.visualize as visualize
import numpy as np

def run_pipeline(num: int = 2000, dim: int = 2, visualize_max_points: int = 200000):
	"""distribution の生成結果を feature_value に渡して統計量を計算する。"""
	samples = dist_main.normal(num=num, dim=dim)

	cov_matrix = feature_value.mycovs(samples)
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
	result = run_pipeline(num=2000, dim=1)
	print("means:", result["means"])
	print("stds:", result["stds"])
	print("cov_matrix:\n", result["cov_matrix"])