import numpy

# それぞれ独立な正規分布から Num * Dim 個のサンプルを得る。
# @return x[Num][Dim]
def normal(num: int, dim: int, mean: float=0, stdev: float=1) -> numpy.ndarray:
    return numpy.random.normal(mean, stdev, (dim, num))

# for example:
# print(normal(10, 2))
# [[-0.55090869 -0.99438105  0.4837106   2.05839369 -0.73151651  0.30172696 -1.03467287  0.4215287  -0.67413573  0.9797012 ]
#  [ 0.63483927 -0.09428223  1.50150113  0.07120784  1.02575574  1.25846207  0.83400668  0.05449522  0.51074329 -0.47793099]]
