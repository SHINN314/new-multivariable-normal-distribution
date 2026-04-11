import numpy as np

def brownian_motion(dt: float, t: float) -> float:
    """1次元ブラウン運動をシミュレーションする関数
    
    Parameters
    ----------
    dt: float
        時間の刻み幅
    t: float
        シミュレーションする時間の長さ
    
    Returns
    -------
    float
        ブラウン運動の最終的な位置
    """
    sample_size = int(t / dt)
    dW_list = np.sqrt(dt) * np.random.randn(sample_size)
    B_t = np.sum(dW_list)

    return B_t

def multivariable_brownian_motion(dt: float, t: float, dim: int) -> np.ndarray:
    """多次元ブラウン運動をシミュレーションする関数
    
    Parameters
    ----------
    dt: float
        時間の刻み幅
    t: float
        シミュレーションする時間の長さ
    dim: int
        ブラウン運動の次元数

    Returns
    -------
    np.ndarray
        ブラウン運動の最終的な位置"""
    coordinate = np.empty(dim)
    for i in range(dim):
        coordinate[i] = brownian_motion(dt, t)

    return coordinate

def generate_brownian_motion_data(dt: float, t: float, dim: int, num_samples: int) -> np.ndarray:
    """ブラウン運動のデータセットを生成する関数

    Parameters
    ----------
    dt: float
        時間の刻み幅
    t: float
        シミュレーションする時間の長さ
    dim: int
        ブラウン運動の次元数
    num_samples: int
        生成するサンプル数

    Returns
    -------
    np.ndarray
        ブラウン運動のデータセット
    """
    data = np.empty((num_samples, dim))
    for i in range(num_samples):
        data[i] = multivariable_brownian_motion(dt, t, dim)

    return data

if __name__ == "__main__":
    # 例
    dt = 0.1
    t = 1.0
    dim = 3
    num_samples = 5
    data = generate_brownian_motion_data(dt, t, dim, num_samples)
    print(data)
