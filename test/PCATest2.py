import numpy as np

### 主成分分析による次元削減
data = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
test = np.array(data)
X_bar = np.array([row - np.mean(row) for row in test.transpose()]).transpose()

print(test.transpose())
print(X_bar)