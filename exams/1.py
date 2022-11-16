import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class Perceptron(object):
    """
    eta: 学習率(0.0<eta<1.0)
    n_iter: トレーニング回数
    """

    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        """
        X: トレーニングデータ（pandas, 行にサンプル、列に特徴量）
        Y: 目的変数（pandas）
        """
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for ite in range(self.n_iter):
            # print('w:', self.w_)
            errors = 0
            for xi, target in zip(X, y):
                # print('xi:', xi)
                # 重みw1,...,wmの更新
                predict = self.predict(xi)
                update = self.eta * (target - predict)
                # print('target:', target, ' predict:', predict, ' update:', update)
                self.w_[1:] += update * xi
                # 重みw0の更新
                self.w_[0] += update
                # 重みの更新が0でない場合は誤分類としてカウント
                error = int(update != 0.0)
                # print('error:', error)
                errors += error
            # 反復回数ごとの誤差を格納
            print(ite, ": ", errors)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        """総入力を計算"""
        result = np.dot(X, self.w_[1:]) + self.w_[0]
        # print('w_', self.w_)
        # print('net_input_result:', result)
        return result

    def predict(self, X):
        """1ステップ後のクラスラベルを返す"""
        return np.where(self.net_input(X) >= 0.0, 1, -1)


s = os.path.join(
    "https://archive.ics.uci.edu",
    "ml",
    "machine-learning-databases",
    "iris",
    "iris.data",
)
df = pd.read_csv(s, header=None, encoding="utf-8")
y = df.iloc[0:100, 4].values
y = np.where(y == "Iris-setosa", -1, 1)
X = df.iloc[0:100, [0, 2]].values
plt.scatter(X[:50, 0], X[:50, 1], color="red", marker="o", label="setosa")
plt.scatter(X[50:100, 0], X[50:100, 1], color="blue", marker="x", label="versicolor")
plt.legend(loc="upper left")
ppn = Perceptron(eta=0.1, n_iter=10)
ppn.fit(X, y)
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker="o")
plt.xlabel("Epochs")
plt.ylabel("Number of update")
plt.show()
