import distribution.t5ugu.main as dist_main
import feature_value.feature_value as feature_value


def run_pipeline(num: int = 2000, dim: int = 2):
	"""distribution の生成結果を feature_value に渡して統計量を計算する。"""
	samples = dist_main.normal(num=num, dim=dim)

	# feature_value.mycovs は「行=特徴量, 列=サンプル」を想定しているため転置する
	cov_matrix = feature_value.mycovs(samples.T)
	means = [feature_value.mymean(samples[:, d]) for d in range(dim)]
	stds = [feature_value.mysd(samples[:, d]) for d in range(dim)]

	return {
		"samples": samples,
		"means": means,
		"stds": stds,
		"cov_matrix": cov_matrix,
	}


if __name__ == "__main__":
	result = run_pipeline(num=2000, dim=2)
	print("means:", result["means"])
	print("stds:", result["stds"])
	print("cov_matrix:\n", result["cov_matrix"])