import numpy as np
import matplotlib.pyplot as plt

def visualize_distribution(x):
    """
    データx (shape: [N, D]) の分布を可視化する関数
    D(次元数)は1または2を想定。
    """
    # データの次元数を取得
    num_samples = x.shape[0]
    dimension = x.shape[1]
    
    # 描画の準備
    plt.figure(figsize=(8, 6))
    
    if dimension == 1:
        print(f"{num_samples}個の1次元データをヒストグラムで可視化します。")
        # 1次元データの描画 (ヒストグラム)
        # x[:, 0] で (N, 1) を (N,) に変換して渡す
        plt.hist(x[:, 0], bins=50, density=True, alpha=0.7, color='blue', edgecolor='black')
        plt.title('1D Normal Distribution (Histogram)')
        plt.xlabel('Value')
        plt.ylabel('Density')
        
    elif dimension == 2:
        print(f"{num_samples}個の2次元データを可視化します。")
        # 2次元データの描画
        x_coords = x[:, 0]
        y_coords = x[:, 1]
        
        # パターン1: 散布図 (透明度alphaを下げて密集度を見やすくする)
        plt.scatter(x_coords, y_coords, alpha=0.3, s=10, color='red', label='Data points')
        
        # パターン2: 2次元ヒストグラム (データが多い場合はこちらが分布を見やすいです)
        # plt.hist2d(x_coords, y_coords, bins=50, cmap='Blues')
        # plt.colorbar(label='Frequency')
        
        plt.title('2D Normal Distribution (Scatter Plot)')
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        plt.grid(True)
        plt.legend()
        
    else:
        print("エラー: 1次元または2次元のデータのみ対応しています。")
        return

    # グラフを表示
    plt.tight_layout()
    plt.show()

# テスト用のデータ生成と関数の実行
if __name__ == "__main__":
    np.random.seed(42) # 再現性のためのシード固定
    num_data = 2000

    # 【テスト1】 1次元データの場合
    mean_1d = [5.0]
    cov_1d = [[2.0]] # 分散
    data_1d = np.random.multivariate_normal(mean_1d, cov_1d, num_data)
    visualize_distribution(data_1d)

    # 【テスト2】 2次元データの場合
    mean_2d = [2.0, 3.0]
    cov_2d = [[1.0, 0.8],   # 共分散行列 (XとYに正の相関を持たせる)
              [0.8, 1.0]]
    data_2d = np.random.multivariate_normal(mean_2d, cov_2d, num_data)
    visualize_distribution(data_2d)