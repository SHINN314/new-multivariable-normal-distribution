import numpy as np
from bisect import bisect_right

# 時刻 t_div[i] から t_div[i+1]、変位 s_div[j] から s_div[j+1] の領域で、mu, sigma が一定であると仮定したとき、
# その値を mu[i, j-1], si[i, j-1] として出力する。
# t_div は time よりも粗く、time と端点を共有しなければならない。
# s_div は、さらに左右に (-infinity) と (+infinity) がついているとみなす。
# ちょうど時刻 t_div[i] のときの増分を採用して、計算をおこなう。
def est(ps: np.ndarray, time: list[float], t_div: list[float], s_div: list[float]) -> tuple[ np.ndarray, np.ndarray ]:
    # noS は 点の数 = 区間数 + 1
    nop, noS = ps.shape
    assert type(nop) == int and type(noS) == int, "ps が 2 次元配列でない"
    assert len(time) == noS, "ps の見本経路の長さと time の長さが一致していない"

    assert len(t_div) <= len(time), "t_div が time よりも粗くない"
    assert time[0] == t_div[0] and time[-1] == t_div[-1], "t_div が time と両端を共有していない"

    # t_div の最後は time の最後なので、情報を捨てる
    ntd = len(t_div) - 1
    SDiv = [-np.inf, *s_div ]
    # 空間の区切りは ( SD[0], SD[1] ), ..., [ SD[len(SD)-1], +inf ) の len(SDiv) 個
    nsd = len(SDiv)

    # 時間の区切りは [ td[0], td[1] ), ..., [ td[ntd-1], td[ntd = len(td)-1] ) の ntd 個
    mu = np.zeros((nsd, ntd))
    va = np.zeros((nsd, ntd))

    # tdiv の添え字を time の添え字に変換する配列
    tdiv_to_time = [0]*ntd
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
        assert dt > 0, "time に重複がある"

        freq = [0]*nsd
        # 見本経路ごとに変位を分類し、各 dx を収集する
        for p in range(nop):
            x = ps[p, ti]
            dx = ps[p, ti + 1] - x

            # s_div の中で、x 以下で最大のもののインデックスを探す。
            # bisect_right は x より大きい最小のもののインデックス
            sd = bisect_right(SDiv, x) - 1
            freq[sd] += 1
            mu[sd, td] += dx / dt
            va[sd, td] += dx * dx / dt

        # mu = E[dx / dt], va = E[dx^2/dt] - mu^2 dt
        for sd in range(nsd):
            if freq[sd] != 0:
                mu[sd, td] /= freq[sd]
                va[sd, td] /= freq[sd]
            else:
                mu[sd, td] = None
                va[sd, td] = None
        va[:, td] = va[:, td] - mu[:, td] * mu[:, td] * dt

    return mu, np.sqrt(va)
