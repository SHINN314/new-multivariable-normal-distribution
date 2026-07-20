import numpy as np

def mymean(x):
    sample_num = len(x)
    sum = 0
    for i in range(sample_num):
        sum += x[i]
    return sum / sample_num

def mycov(x, y):
    mx = mymean(x)
    my = mymean(y)
    sample_num = len(x)
    sq_dev_sum = 0
    for i in range(sample_num):
        sq_dev_sum += (x[i] - mx) * (y[i] - my)
    return sq_dev_sum / sample_num

def mycovs(x: np.ndarray):
    dim = x.shape[1]
    cov = np.zeros([dim, dim])
    for i in range(dim):
        cov[i][i] = mycov(x[:,i], x[:,i])
        for j in range(dim-i):
            cov[i][j] = mycov(x[:,i], x[:,j])
            cov[j][i] = cov[i][j]
    return cov

def mysd(x):
    return np.sqrt(mycov(x, x))

if __name__ == "__main__":
    # print(len(np.array([1, 0])))
    x = [
        [0, 1, 2],
        [1, 2, 3],
        [0, 0, 9]
    ]
    print(mycovs(x))