import numpy

# それぞれ独立な正規分布から Num * Dim 個のサンプルを得る。
# @return x[Num][Dim]
def normal(num: int, dim: int, mean: float=0, stdev: float=1) -> numpy.ndarray:
    return numpy.random.normal(mean, stdev, (num, dim))

# for example:
# print(normal(10, 2))
# [[-0.40329468 -0.22499157]
#  [-1.61006157  0.18545917]
#  [ 0.1289018  -1.6176506 ]
#  [-0.87373605 -0.57058567]
#  [ 0.98571375 -1.58999896]
#  [ 1.3732622  -0.14323583]
#  [ 2.03569148  0.70135341]
#  [-0.72993324  0.82095186]
#  [-0.05776733  1.4908088 ]
#  [ 0.22644174  0.83870648]]

def dimensionwise(num: int, dim: int, mses: list[tuple[float, float]]) -> numpy.ndarray:
    if len(mses) != dim:
        raise Exception("平均と標準偏差の列をあたえてください")
    res = numpy.zeros((num, dim))
    for d in range(dim):
        res[:, d] = numpy.random.normal(mses[d][0], mses[d][1], num)
    return res

# for example:
# print(dimensionwise(10, 2, [(0, 1), (50, 100)]))
# [[   0.60593129   84.62327516]
#  [   0.35279739   65.37902586]
#  [   2.05938237 -162.24626437]
#  [  -1.26383473   30.20891854]
#  [   0.50173075  128.62065984]
#  [  -0.33018213  113.49970895]
#  [   0.52690103 -193.33539546]
#  [   0.34770221  -64.49605414]
#  [   0.97034556   41.13796357]
#  [  -0.26131672   93.48581571]]
