import numpy as np
from bisect import bisect_left

def est(ps: np.ndarray, time: list[float], t_div: list[float], s_div: list[float]) -> tuple[ np.ndarray, np.ndarray ]:
    # noS は 点の数 = 区間数 + 1
    nop, noS = ps.shape
    assert type(nop) == int and type(noS) == int
    assert len(time) == noS

    ntd = len(t_div)
    s_div = [-np.inf] + s_div + [np.inf]
    nsd = len(s_div)
    assert ntd < noS

    mu = np.zeros((nsd, ntd))
    va = np.zeros((nsd, ntd))

    # tdiv の添え字を time の添え字に変換する配列
    tdiv_to_time = [0]*ntd
    # 現在は、tdiv 以上の最小の time を求めている
    # つまり、tdiv の左端での変化量だけ見る。
    last = 0
    for td in range(ntd):
        vtd = t_div[td]
        while last < noS and time[last] < vtd:
            last += 1
        tdiv_to_time[td] = last

    # まず、時間方向に区切る。
    for td in range(ntd):
        ti = tdiv_to_time[td]
        dt = time[ti + 1] - time[ti]

        freq = [0]*nsd
        # 見本経路ごとに変位を分類し、各 dx を収集する
        for p in range(nop):
            x = ps[p, ti]
            dx = ps[p, ti + 1] - x

            # s_div の中で、x 以下で最大のもののインデックス
            sd = bisect_left(s_div, x)
            freq[sd] += 1
            mu[sd, td] += dx / dt
            va[sd, td] += dx * dx / dt

        # mu = E[dx / dt], si = E[dx^2/dt] - mu^2 dt
        for sd in range(nsd):
            if freq[sd] != 0:
                mu[sd, td] /= freq[sd]
                va[sd, td] /= freq[sd]
        va[:, td] = va[:, td] - mu[:, td] * mu[:, td] * dt

    return mu, np.sqrt(va)

if __name__ == '__main__':
    print(np.zeros((0, 10)))
    print(bisect_left([], 0))