import numpy as np

def mymean(x):
    n = len(x)
    s = 0
    for i in range(n):
        s += x[i]
    s /= n
    return s

def mycov(x, y):
    mx = mymean(x)
    my = mymean(y)
    n = len(x)
    s = 0
    for i in range(n):
        s += (x[i] - mx) * (y[i] - my)
    s /= n
    return s

def mycovs(x):
    n = len(x)
    c = np.zeros([n, n])
    for i in range(n):
        c[i][i] = mycov(x[i], x[i])
        for j in range(n-i):
            c[i][j] = mycov(x[i], x[j])
            c[j][i] = c[i][j]
    return c

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